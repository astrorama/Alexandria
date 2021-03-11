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

#ifndef POOLTESTS_FILEMANAGER_H
#define POOLTESTS_FILEMANAGER_H

#include <boost/filesystem/path.hpp>
#include <list>
#include <map>
#include <mutex>

namespace Euclid {
namespace FilePool {

// Forward declaration
class FileHandler;

/**
 * This trait has to be implemented for all supported file descriptor types.
 * @tparam TFD
 *  File descriptor type
 */
template <typename TFD>
struct OpenCloseTrait {
  static TFD open(const boost::filesystem::path& path, bool write) {
    static_assert(std::is_constructible<TFD, const boost::filesystem::path&, bool>::value && std::is_move_constructible<TFD>::value,
                  "Specialization of OpenCloseTrait or a constructible(path,bool) and movable");
    return TFD(path, write);
  }
  static void close(TFD& /*fd*/) {
    static_assert(std::is_constructible<TFD, const boost::filesystem::path&, bool>::value && std::is_move_constructible<TFD>::value,
                  "Specialization of OpenCloseTrait or a constructible(path,bool) and movable");
    // NOOP
  }
};

/**
 * Provide an open/close interface to FileHandler. Concrete policies must inherit
 * this interface and implement the notify* methods.
 */
class FileManager {
public:
  /// Opaque structure, its members can only be used by FileManager and derived classes
  struct FileMetadata;

  /// Opaque FileId, its concrete type should only be assumed to be copyable and hashable
  using FileId = FileMetadata*;

  /// Constructor
  FileManager();

  /// Destructor
  virtual ~FileManager();

  /**
   * Get a file handler
   * @tparam TFD
   *    File descriptor type
   * @param path
   *    File path
   * @return
   *    A FileHandler for the given file and with the requested file descriptor type
   * @details
   *    If there is already a FileHandler<TFD> for the given path, this will return the same
   *    shared pointer as already in use. The FileHandler is thread-safe, so this is OK.
   *    The path is normalized (no symlinks and no '.' or '..'), so this holds true even if
   *    the same file is specified in different manners.
   * @warning
   *    The above is *not* true for hardlinks. If the same file is referenced by different paths that
   *    are hardlinks to the same file, it will return different handlers, so there will be no read/write
   *    protection in place.
   * @throws Elements::Exception
   *    If there is already a FileHandler with a *different* file descriptor type.
   */
  std::shared_ptr<FileHandler> getFileHandler(const boost::filesystem::path& path);

  /**
   * Open a file
   * @tparam TFD
   *    File descriptor type.
   * @param path
   *    File path
   * @param write
   *    True if the file is to be opened in write mode
   * @param request_close
   *    The manager will call this function when it needs to close the file descriptor,
   *    so whoever called open can put everything in order. The callback can return "false" if the given
   *    FileId can not be closed (i.e. it is still in use). The callback is responsible for calling close.
   * @return
   *    A pair FileId, FileDescriptor
   * @note
   *    An specialization of OpenCloseTrait must exists for TFD.
   * @warning
   *    Files will be closed when the FileManager is destroyed. Make sure that the information required by the
   *    callback lives longer than the FileManager.
   *    You do not need to care about this when using FileHandlers
   * @details
   *    Why the callback? The FilePool is designed to have single ownership of the file descriptors, so it can
   *    work with non-copyable file types. Files are either owned by the FileHandler (if not in use) or by the FileAccessor
   *    (if in use). Therefore, it can only let the owner know the file should be closed.
   *    Again, this caveat is unimportant if the access is done via FileHandlers.
   */
  template <typename TFD>
  std::pair<FileId, TFD> open(const boost::filesystem::path& path, bool write, std::function<bool(FileId)> request_close);

  /**
   * Close a file
   * @param id
   *    The id returned by open
   */
  template <typename TFD>
  void close(FileId id, TFD& fd);

  /**
   * Notify that the given file has been/is going to be used. This will update
   * the book-keeping data used to decide what to close when.
   */
  virtual void notifyUsed(FileId id);

  /**
   * @return
   *    True if the path has an associated handler
   */
  bool hasHandler(const boost::filesystem::path& path) const;

  /**
   * @return
   *    A default FileManager implementation
   */
  static std::shared_ptr<FileManager> getDefault();

protected:
  using Clock     = std::chrono::steady_clock;
  using Timestamp = Clock::time_point;

  mutable std::mutex m_mutex;

  /**
   * Map path / handler
   * @details
   *    The value is a std::weak_ptr because we are not really interested on keeping a handler
   *    alive if no one is using it. However, if someone has a handler pointing to a file alive,
   *    and someone else wants a handler to the same file, it should get the same handler.
   */
  std::map<boost::filesystem::path, std::weak_ptr<FileHandler>> m_handlers;

  /**
   * Map a file id to its metadata
   */
  std::map<FileId, std::unique_ptr<FileMetadata>> m_files;

  /** @warning
   *     Concrete implementations *must* call this on their destructors.
   */
  void closeAll();

  virtual void notifyIntentToOpen(bool write) = 0;
  virtual void notifyOpenedFile(FileId)       = 0;
  virtual void notifyClosedFile(FileId)       = 0;
};

}  // end of namespace FilePool
}  // namespace Euclid

#define FILEMANAGER_IMPL
#include "_impl/FileManager.icpp"
#undef FILEMANAGER_IMPL

#endif  // POOLTESTS_FILEMANAGER_H
