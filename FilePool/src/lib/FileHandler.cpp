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

#include "FilePool/FileHandler.h"

namespace Euclid {
namespace FilePool {

FileHandler::FileHandler(const boost::filesystem::path& path, std::weak_ptr<FileManager> file_manager)
    : m_path(path), m_file_manager(file_manager), m_is_readonly(true) {}

FileHandler::~FileHandler() {
  for (auto& avail : m_available_fd) {
    avail.second->close();
  }
}

bool FileHandler::isReadOnly() const {
  return m_is_readonly;
}

bool FileHandler::close(FileManager::FileId id) {
  std::unique_ptr<FdWrapper> fd_ptr;
  {
    std::lock_guard<std::mutex> this_lock(m_handler_mutex);
    auto                        iter = m_available_fd.find(id);
    if (iter == m_available_fd.end())
      return false;
    fd_ptr = std::move(iter->second);
    m_available_fd.erase(iter);
  }
  fd_ptr->close();
  return true;
}

}  // namespace FilePool
}  // namespace Euclid
