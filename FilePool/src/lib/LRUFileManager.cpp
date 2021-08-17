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

#include "FilePool/LRUFileManager.h"
#include "ElementsKernel/Exception.h"
#include <sys/resource.h>

namespace Euclid {
namespace FilePool {

LRUFileManager::LRUFileManager(unsigned limit) : m_limit(limit) {
  if (m_limit == 0) {
    struct rlimit rlim;
    getrlimit(RLIMIT_NOFILE, &rlim);
    assert(rlim.rlim_cur > 3);
    m_limit = rlim.rlim_cur - 3;  // Account for stdout, stderr and stdin
  }
}

LRUFileManager::~LRUFileManager() {
  closeAll();
}

void LRUFileManager::notifyIntentToOpen(bool /*write*/) {
  // Only one thread can be making space
  std::lock_guard<std::mutex> close_lock(m_close_fd_mutex);
  std::unique_lock<std::mutex> lock(m_mutex);

  while (m_files.size() >= m_limit) {
    bool closed = false;
    for (auto& id : m_sorted_ids) {
      auto& meta       = m_files[id];
      auto  close_call = meta->m_request_close;
      lock.unlock();
      closed = close_call();
      lock.lock();
      // If the file was closed, the iterator on m_sorted_ids has been invalidated!
      if (closed)
        break;
    }
    if (!closed) {
      throw Elements::Exception() << "Limit reached and failed to close any existing file descriptor";
    }
  }
}

void LRUFileManager::notifyOpenedFile(FileManager::FileId id) {
  std::lock_guard<std::mutex> lock(m_mutex);
  m_sorted_ids.emplace_back(id);
  m_current_pos[id] = m_sorted_ids.end();
  --m_current_pos[id];
}

void LRUFileManager::notifyClosedFile(FileManager::FileId id) {
  std::lock_guard<std::mutex> lock(m_mutex);
  auto                        iter = m_current_pos[id];
  m_current_pos.erase(id);
  m_sorted_ids.erase(iter);
}

void LRUFileManager::notifyUsed(FileManager::FileId id) {
  // Update count
  id->m_last_used = Clock::now();
  ++id->m_used_count;

  // Bring it to the back, since it is the last used
  std::lock_guard<std::mutex> lock(m_mutex);
  auto                        iter = m_current_pos[id];
  auto                        ptr  = std::move(*iter);
  m_sorted_ids.erase(iter);
  m_sorted_ids.emplace_back(std::move(ptr));
  m_current_pos[id] = m_sorted_ids.end();
  --m_current_pos[id];
}

unsigned int LRUFileManager::getLimit() const {
  return m_limit;
}

unsigned int LRUFileManager::getUsed() const {
  return m_sorted_ids.size();
}

unsigned int LRUFileManager::getAvailable() const {
  return m_limit - m_sorted_ids.size();
}

}  // namespace FilePool
}  // namespace Euclid
