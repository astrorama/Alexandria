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

#include "FilePool/FileManager.h"
#include "FilePool/FileHandler.h"
#include "FilePool/LRUFileManager.h"
#include <boost/filesystem/operations.hpp>

#if BOOST_VERSION < 106000
/**
 * weakly_canonical was introduced in 1.60.00
 * Loosely based on boost implementation, but without optimizations
 */
boost::filesystem::path weakly_canonical(const boost::filesystem::path& path) {
  auto                    iter = path.end();
  boost::filesystem::path head = path;

  for (; !head.empty(); --iter) {
    if (boost::filesystem::exists(head)) {
      break;
    }
    head.remove_filename();
  }

  if (head.empty())
    return boost::filesystem::absolute(path);
  head = boost::filesystem::canonical(head);

  boost::filesystem::path tail;
  for (; iter != path.end(); ++iter) {
    tail /= *iter;
  }

  if (tail.empty())
    return head;

  return boost::filesystem::absolute(head / tail);
}
#endif

namespace Euclid {
namespace FilePool {

std::shared_ptr<FileManager> FileManager::getDefault() {
  static auto default_manager = std::make_shared<LRUFileManager>();
  return default_manager;
}

FileManager::FileManager() {}

FileManager::~FileManager() {}

void FileManager::notifyUsed(FileId id) {
  // In principle a FileId should only be hold by a single thread, so no need to lock here
  id->m_last_used = Clock::now();
  ++id->m_used_count;
}

void FileManager::closeAll() {
  std::vector<FileMetadata*> to_be_closed;

  // To avoid deadlocks on the callback, we get the pointers first
  {
    std::unique_lock<std::mutex> lock(m_mutex);
    std::transform(m_files.begin(), m_files.end(), std::back_inserter(to_be_closed),
                   [](std::pair<FileId const, std::unique_ptr<FileMetadata>>& entry) { return entry.second.get(); });
  }

  // And request the closing after
  for (auto& fd : to_be_closed) {
    fd->m_request_close();
  }
}

std::shared_ptr<FileHandler> FileManager::getFileHandler(const boost::filesystem::path& path) {
  auto canonical = weakly_canonical(path);

  std::lock_guard<std::mutex>  lock(m_mutex);
  auto                         i = m_handlers.find(canonical);
  std::shared_ptr<FileHandler> handler_ptr;

  if (i != m_handlers.end()) {
    handler_ptr = i->second.lock();
  }
  // Either didn't exist or it is gone
  if (!handler_ptr) {
    std::weak_ptr<FileManager> this_weak       = shared_from_this();
    auto                       handler_destroy = [this_weak, canonical](FileHandler* obj) {
      auto this_shared = this_weak.lock();
      if (this_shared) {
        std::lock_guard<std::mutex> manager_lock(this_shared->m_mutex);
        this_shared->m_handlers.erase(canonical);
      }
      delete obj;
    };
    handler_ptr           = std::shared_ptr<FileHandler>(new FileHandler(canonical, this_weak), handler_destroy);
    m_handlers[canonical] = handler_ptr;
  }
  return handler_ptr;
}

bool FileManager::hasHandler(const boost::filesystem::path& path) const {
  std::lock_guard<std::mutex> this_lock(m_mutex);
  auto                        canonical = weakly_canonical(path);
  auto                        iter      = m_handlers.find(canonical);
  return iter != m_handlers.end();
}

}  // namespace FilePool
}  // namespace Euclid
