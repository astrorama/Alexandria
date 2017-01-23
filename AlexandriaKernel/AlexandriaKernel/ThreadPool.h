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
 * 
 * @brief Basic thread pool implementation
 * 
 * @details
 * This class provides a basic thread pool implementation, to be used when the
 * boost thread pool is not available (boost versions earlier than 1.56). If
 * your boost version contains the thread pool (boost/thread/thread_pool.hpp) use
 * this one instead.
 * 
 * Using the pool is quite simple. The constructor of the ThreadPool gets as
 * parameter the number of threads that will be spawned (defaults to the number
 * of threads available). The ThreadPool::submit() method can be used to submit
 * tasks to the thread pool queue. Tasks can be anything that can be assigned
 * to a std::function object which does not get any parameters and returns void.
 * The thread pool will assign all tasks to the threads to be executed at the
 * same order as they are submitted. To block until all the tasks in the pool
 * have been executed, one can all the ThreadPool::block() method.
 * 
 * Note that when the ThreadPool object goes out of scope and its destructor is
 * called it will not process any tasks that are not already started, but it will
 * block until all threads finish with the currently executing tasks.
 *
 */
class ThreadPool {

public:
  
  /// The type of tasks the pool can execute
  using Task = std::function<void(void)>;

  /**
   * @brief Constructs a new ThreadPool
   * @param thread_count
   *    The number of threads in the pool (defaults to the number of available cores)
   * @param empty_queue_wait_time
   *    The time (in milliseconds) the pool threads sleep after they try to get
   *    a task from an empty queue before they retry
   */
  ThreadPool(unsigned int thread_count=std::thread::hardware_concurrency(), unsigned int empty_queue_wait_time=50);
  
  /// All tasks not yet started are discarded and it blocks until all already
  /// executing tasks are finished
  virtual ~ThreadPool();
  
  /// Submit a task to be executed
  void submit(Task task);
  
  /// Blocks the calling thread until all the tasks in the pool queue are finished.
  /// Note that submitting tasks until this method returns is not allowed.
  void block();

private:
  
  std::mutex m_queue_mutex {};
  std::vector<std::atomic<bool>> m_worker_run_flags;
  std::vector<std::atomic<bool>> m_worker_sleeping_flags;
  std::vector<std::atomic<bool>> m_worker_done_flags;
  std::deque<Task> m_queue {};
  unsigned int m_empty_queue_wait_time;

}; /* End of ThreadPool class */

} /* namespace Euclid */


#endif
