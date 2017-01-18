/*
 * Copyright (C) 2012-2020 Euclid Science Ground Segment
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

/**
 * @file AlexandriaKernel/ThreadPool.h
 * @date 01/06/17
 * @author nikoapos
 */

#ifndef _ALEXANDRIAKERNEL_THREADPOOL_H
#define _ALEXANDRIAKERNEL_THREADPOOL_H

#include <vector>
#include <thread>
#include <mutex>
#include <atomic>
#include <deque>
#include <functional>

namespace Euclid {

/**
 * @class ThreadPool
 * @brief
 *
 */
class ThreadPool {

public:
  
  using Task = std::function<void(void)>;

  ThreadPool(unsigned int thread_count=std::thread::hardware_concurrency(), unsigned int empty_queue_wait_time=50);
  
  /**
   * @brief Destructor
   */
  virtual ~ThreadPool();
  
  void submit(Task task);
  
  void block();

private:
  
  std::mutex m_queue_mutex {};
  std::vector<std::atomic<bool>> m_worker_run_flags;
  std::vector<std::atomic<bool>> m_worker_done_flags;
  std::deque<Task> m_queue {};
  unsigned int m_empty_queue_wait_time;

}; /* End of ThreadPool class */

} /* namespace Euclid */


#endif
