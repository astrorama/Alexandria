/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
 *
 * This library is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free
 * Software Foundation; either version 3.0 of the License, or (at your option)
 * any later version.
 *
 * This library is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
 * details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this library; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 */

#ifndef POOLTESTS_FILEACCESSOR_H
#define POOLTESTS_FILEACCESSOR_H

#include <boost/thread/shared_mutex.hpp>

namespace Euclid {
namespace FilePool {

/**
 * Template-free base for all FileAccessors
 */
class FileAccessorBase {
public:
  using SharedMutex         = boost::shared_mutex;
  using SharedLock          = boost::shared_lock<SharedMutex>;
  using UniqueLock          = boost::unique_lock<SharedMutex>;
  using UpgradeLock         = boost::upgrade_lock<SharedMutex>;
  using UpgradeToUniqueLock = boost::upgrade_to_unique_lock<SharedMutex>;

  virtual ~FileAccessorBase() = default;

  /// @return true if the wrapped file descriptor is read-only
  virtual bool isReadOnly() const = 0;
};

/**
 * Wraps a file descriptor, so when the instance is destroyed, the callback is
 * called with the wrapped descriptor moved-in
 * @tparam TFD
 *  File descriptor type
 * @details
 *  This is a base class that hides away if the accessor is read-only or write-only,
 *  as the locking mechanisms in each case should not bother the calling code
 */
template <typename TFD>
class FileAccessor : public FileAccessorBase {
public:
  using ReleaseDescriptorCallback = std::function<void(TFD&&)>;

  /// The wrapped file descriptor
  TFD m_fd;

  /// Destructor
  virtual ~FileAccessor() = default;

  /// @return true if the wrapped file descriptor is read-only
  virtual bool isReadOnly() const = 0;

protected:
  FileAccessor(TFD&& fd, ReleaseDescriptorCallback release_callback);

  ReleaseDescriptorCallback m_release_callback;
};

/**
 * Wraps a file descriptor together with a shared lock, so multiple read accessors pointing
 * to the same **physical file** can exist at the same time.
 * @tparam TFD
 *  File descriptor type
 * @note
 *  The file descriptor is still unique, since normally file descriptors can not be shared
 *  between threads (shared buffers, offsets, etc.)
 *  What is shared is the *file* itself.
 */
template <typename TFD>
class FileReadAccessor : public FileAccessor<TFD> {
public:
  typedef FileAccessor<TFD> Base_;
  using ReleaseDescriptorCallback = typename Base_::ReleaseDescriptorCallback;
  using SharedLock                = typename Base_::SharedLock;

  /**
   * Constructor
   * @param fd
   *    File descriptor
   * @param release_callback
   *    Callback to be called at destruction
   * @param lock
   *    Shared lock
   */
  FileReadAccessor(TFD&& fd, ReleaseDescriptorCallback release_callback, SharedLock lock);

  /// It can not be copied
  FileReadAccessor(const FileReadAccessor&) = delete;

  /// But it can be moved
  FileReadAccessor(FileReadAccessor&&) = default;

  /// Destructor
  virtual ~FileReadAccessor();

  /// @return Always true
  bool isReadOnly() const final;

private:
  SharedLock m_shared_lock;
};

/**
 * Wraps a file descriptor together with an exclusive lock, so there can only be one
 * accessor (no simultaneous reads!)
 * @tparam TFD
 *  File descriptor type
 */
template <typename TFD>
class FileWriteAccessor : public FileAccessor<TFD> {
public:
  typedef FileAccessor<TFD> Base_;
  using ReleaseDescriptorCallback = typename Base_::ReleaseDescriptorCallback;
  using SharedLock                = typename Base_::SharedLock;
  using UniqueLock                = typename Base_::UniqueLock;

  /**
   * Constructor
   * @param fd
   *    File descriptor
   * @param release_callback
   *    Callback to be called at destruction
   * @param lock
   *    Unique lock to the underlying file
   */
  FileWriteAccessor(TFD&& fd, ReleaseDescriptorCallback release_callback, UniqueLock lock);

  /// Destructor
  virtual ~FileWriteAccessor();

  /// @return Always true
  bool isReadOnly() const final;

private:
  UniqueLock m_unique_lock;
};

}  // namespace FilePool
}  // namespace Euclid

#define FILEACCESSOR_IMPL
#include "_impl/FileAccessor.icpp"
#undef FILEACCESSOR_IMPL

#endif  // POOLTESTS_FILEACCESSOR_H
