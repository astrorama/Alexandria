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
 * @file src/lib/ThreadPool.cpp
 * @date 01/06/17
 * @author nikoapos
 */

#include "AlexandriaKernel/ThreadPool.h"
#include "AlexandriaKernel/memory_tools.h"

namespace Euclid {

namespace {

class Worker {
  
public:
  
  Worker(std::mutex& queue_mutex, std::deque<ThreadPool::Task>& queue,
                  std::atomic<bool>& run_flag, std::atomic<bool>& done_flag,
                  uint empty_queue_wait_time)
        : m_queue_mutex(queue_mutex), m_queue(queue), m_run_flag(run_flag),
          m_done_flag(done_flag), m_empty_queue_wait_time(empty_queue_wait_time) {
  }
        
  void operator()() {
    while (m_run_flag.get()) {
      // Check if there is anything it the queue to be done and get it
      std::unique_ptr<ThreadPool::Task> task_ptr = nullptr;
      std::unique_lock<std::mutex> lock {m_queue_mutex.get()};
      if (!m_queue.get().empty()) {
        task_ptr = make_unique<ThreadPool::Task>(m_queue.get().front());
        m_queue.get().pop_front();
      }
      lock.unlock();
      
      // If we have some work to do, do it. Otherwise sleep for some time.
      if (task_ptr) {
        (*task_ptr)();
      } else {
        std::this_thread::sleep_for(std::chrono::milliseconds(m_empty_queue_wait_time));
      }
    }
    // Indicate that the worker is done
    m_done_flag.get() = true;
  }
  
private:

  std::reference_wrapper<std::mutex> m_queue_mutex;
  std::reference_wrapper<std::deque<ThreadPool::Task>> m_queue;
  std::reference_wrapper<std::atomic<bool>> m_run_flag;
  std::reference_wrapper<std::atomic<bool>> m_done_flag;
  uint m_empty_queue_wait_time;
  
};
  
} // end of anonymous namespace

ThreadPool::ThreadPool(uint thread_count, uint empty_queue_wait_time)
        : m_worker_run_flags(thread_count), m_worker_done_flags(thread_count),
          m_empty_queue_wait_time(empty_queue_wait_time) {
  for (uint i = 0; i < thread_count; ++i) {
    m_worker_run_flags.at(i) = true;
    m_worker_done_flags.at(i) = false;
    std::thread(Worker{m_queue_mutex, m_queue, m_worker_run_flags.at(i),
                       m_worker_done_flags.at(i), m_empty_queue_wait_time}).detach();
  }
}

void ThreadPool::block() {
  bool queue_is_empty = false;
  while (!queue_is_empty) {
    std::unique_lock<std::mutex> lock {m_queue_mutex};
    queue_is_empty = m_queue.empty();
    lock.unlock();
    if (!queue_is_empty) {
      std::this_thread::sleep_for(std::chrono::milliseconds(m_empty_queue_wait_time));
    }
  }
}


ThreadPool::~ThreadPool() {
  // Stop all the workers. They will stop right after they finish the task
  // they already run.
  for (auto& flag : m_worker_run_flags) {
    flag = false;
  }
  // Now wait until all the workers have finish any current tasks
  for (auto& flag : m_worker_done_flags) {
    while (!flag) {
      std::this_thread::sleep_for(std::chrono::milliseconds(m_empty_queue_wait_time));
    }
  }
}

void ThreadPool::submit(Task task) {
  std::lock_guard<std::mutex> lock {m_queue_mutex};
  m_queue.emplace_back(std::move(task));
}

} // Euclid namespace



