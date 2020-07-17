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
                  std::atomic<bool>& run_flag, std::atomic<bool>& sleeping_flag,
                  std::atomic<bool>& done_flag, unsigned int empty_queue_wait_time,
                  std::exception_ptr& exception_ptr)
        : m_queue_mutex(queue_mutex), m_queue(queue), m_run_flag(run_flag),
          m_sleeping_flag(sleeping_flag), m_done_flag(done_flag),
          m_empty_queue_wait_time(empty_queue_wait_time),
          m_exception_ptr(exception_ptr) {
  }

  void operator()() {
    while (m_run_flag.get() && m_exception_ptr == nullptr) {
      // Check if there is anything it the queue to be done and get it
      std::unique_ptr<ThreadPool::Task> task_ptr = nullptr;
      std::unique_lock<std::mutex> lock {m_queue_mutex.get()};
      if (!m_queue.get().empty()) {
        task_ptr = Euclid::make_unique<ThreadPool::Task>(m_queue.get().front());
        m_queue.get().pop_front();
      }
      lock.unlock();

      // If we have some work to do, do it. Otherwise sleep for some time.
      if (task_ptr) {
        try {
          (*task_ptr)();
        } catch(...) {
          m_exception_ptr.get() = std::current_exception();
        }
      } else {
        m_sleeping_flag.get() = true;
        std::this_thread::sleep_for(std::chrono::milliseconds(m_empty_queue_wait_time));
        m_sleeping_flag.get() = false;
      }
    }
    // Indicate that the worker is done
    m_sleeping_flag.get() = true;
    m_done_flag.get() = true;
  }

private:

  std::reference_wrapper<std::mutex> m_queue_mutex;
  std::reference_wrapper<std::deque<ThreadPool::Task>> m_queue;
  std::reference_wrapper<std::atomic<bool>> m_run_flag;
  std::reference_wrapper<std::atomic<bool>> m_sleeping_flag;
  std::reference_wrapper<std::atomic<bool>> m_done_flag;
  unsigned int m_empty_queue_wait_time;
  std::reference_wrapper<std::exception_ptr> m_exception_ptr;

};

} // end of anonymous namespace

ThreadPool::ThreadPool(unsigned int thread_count, unsigned int empty_queue_wait_time)
        : m_worker_run_flags(thread_count), m_worker_sleeping_flags(thread_count),
          m_worker_done_flags(thread_count), m_empty_queue_wait_time(empty_queue_wait_time) {
  for (unsigned int i = 0; i < thread_count; ++i) {
    m_worker_run_flags.at(i) = true;
    m_worker_sleeping_flags.at(i) = false;
    m_worker_done_flags.at(i) = false;
    std::thread(Worker{m_queue_mutex, m_queue, m_worker_run_flags.at(i), m_worker_sleeping_flags.at(i),
                       m_worker_done_flags.at(i), m_empty_queue_wait_time, m_exception_ptr}).detach();
  }
}

namespace {

void waitWorkers(std::vector<std::atomic<bool>>& worker_flags, unsigned int wait_time) {
  // Now wait until all the workers have finish any current tasks
  for (auto& flag : worker_flags) {
    while (!flag) {
      std::this_thread::sleep_for(std::chrono::milliseconds(wait_time));
    }
  }
}

}

bool ThreadPool::checkForException(bool rethrow) {
  if (m_exception_ptr) {
    if (rethrow) {
      std::rethrow_exception(m_exception_ptr);
    } else {
      return true;
    }
  }
  return false;
}

void ThreadPool::block() {
  // Wait for the queue to be empty
  bool queue_is_empty = false;
  while (!queue_is_empty && m_exception_ptr == nullptr) {
    std::unique_lock<std::mutex> lock {m_queue_mutex};
    queue_is_empty = m_queue.empty();
    lock.unlock();
    if (!queue_is_empty) {
      std::this_thread::sleep_for(std::chrono::milliseconds(m_empty_queue_wait_time));
    }
  }
  // Wait for the workers to finish the currently executing tasks
  waitWorkers(m_worker_sleeping_flags, m_empty_queue_wait_time);
  // Check if any worker finished with an exception
  checkForException(true);
}


ThreadPool::~ThreadPool() {
  // Stop all the workers. They will stop right after they finish the task
  // they already run.
  std::fill(m_worker_run_flags.begin(), m_worker_run_flags.end(), false);
  // Now wait until all the workers have finish any current tasks
  waitWorkers(m_worker_done_flags, m_empty_queue_wait_time);
}

void ThreadPool::submit(Task task) {
  std::lock_guard<std::mutex> lock {m_queue_mutex};
  m_queue.emplace_back(std::move(task));
}

} // Euclid namespace



