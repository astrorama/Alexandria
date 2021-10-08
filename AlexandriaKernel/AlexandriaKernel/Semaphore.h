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

#ifndef _ALEXANDRIAKERNEL_SEMAPHORE_H
#define _ALEXANDRIAKERNEL_SEMAPHORE_H

#include <chrono>
#include <memory>

namespace Euclid {

/**
 * @class Semaphore
 * Counting semaphore, based on the C++20 API, so it can be eventually swapped
 */
class Semaphore {
public:
  /**
   * Constructor
   * @param i
   *    The internal counter will be initialized to i
   */
  explicit Semaphore(unsigned int i);

  /**
   * Destructor
   */
  ~Semaphore();

  /**
   * Increment the counter. Does not block.
   */
  void release();

  /**
   * Decrement the counter. Blocks if it was already 0 until some other thread calls release()
   */
  void acquire();

  /**
   * Try decrementing the counter.
   * @return false if the counter can not be decremented (already at 0)
   */
  bool try_acquire();

  /**
   * Try decrementing the counter with an *absolute timeout*
   * @param abs_time
   *    If the counter can not be decremented, the call will block until this time point
   *    is reached. If it was in the past, it will return immediately.
   * @return
   *    false if the counter can not be decremented within the time window
   */
  bool try_acquire_until(const std::chrono::system_clock::time_point& abs_time);

  /**
   * @copybrief try_acquire_until
   * @tparam Clock
   * @tparam Duration
   * @param abs_time
   * @return
   *    false if the counter can not be decremented within the time window
   */
  template <class Clock, class Duration>
  bool try_acquire_until(const std::chrono::time_point<Clock, Duration>& abs_time) {
    return try_acquire_until(std::chrono::system_clock::now() + (Clock::now() - abs_time));
  }

  /**
   * Try decrementing the counter with a *relative timeout*
   * @tparam Rep
   * @tparam Ratio
   * @param rel_time
   *    If the counter can not be decremented, the call will block for this duration.
   * @return
   *    false if the counter can not be decremented within the time window
   */
  template <class Rep, class Ratio>
  bool try_acquire_for(const std::chrono::duration<Rep, Ratio>& rel_time) {
    return try_acquire_until(std::chrono::system_clock::now() + rel_time);
  }

private:
  class SemaphoreImpl;
  std::unique_ptr<SemaphoreImpl> m_impl;
};

}  // namespace Euclid

#endif  // _ALEXANDRIAKERNEL_SEMAPHORE_H
