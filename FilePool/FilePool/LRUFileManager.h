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

#ifndef POOLTESTS_LRUFILEMANAGER_H
#define POOLTESTS_LRUFILEMANAGER_H

#include "FileManager.h"

namespace Euclid {
namespace FilePool {

/**
 * Least Recently Used strategy for the FileManager
 */
class LRUFileManager final : public FileManager {
public:
  /**
   * Constructor
   * @param limit
   *    Limit on the number of open files. If 0, it will query the system to obtain the configured limit.
   */
  explicit LRUFileManager(unsigned limit = 500);
  virtual ~LRUFileManager();

  void notifyUsed(FileId id) override;

  unsigned getLimit() const;
  unsigned getUsed() const;
  unsigned getAvailable() const;

protected:
  void notifyIntentToOpen(bool write) override;
  void notifyOpenedFile(FileId id) override;
  void notifyClosedFile(FileId id) override;

private:
  unsigned   m_limit;
  std::mutex m_close_fd_mutex;
  /// Sorted from less to more recent
  std::list<FileId>                             m_sorted_ids;
  std::map<FileId, std::list<FileId>::iterator> m_current_pos;
};

}  // namespace FilePool
}  // namespace Euclid

#endif  // POOLTESTS_LRUFILEMANAGER_H
