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

#include "AlexandriaKernel/Semaphore.h"
#include "SemaphorePosix.icpp"

namespace Euclid {

Semaphore::Semaphore(unsigned int i) : m_impl(new SemaphoreImpl(i)) {}

Semaphore::~Semaphore() {}

void Semaphore::release() {
  m_impl->post();
}

void Semaphore::acquire() {
  m_impl->wait();
}

bool Semaphore::try_acquire() {
  return m_impl->try_acquire();
}

bool Semaphore::try_acquire_until(const std::chrono::system_clock::time_point& abs_time) {
  return m_impl->try_acquire_until(abs_time);
}

}  // namespace Euclid