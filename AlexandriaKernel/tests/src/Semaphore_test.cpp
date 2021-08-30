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
#include <boost/test/unit_test.hpp>

using Euclid::Semaphore;

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(Semaphore_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(AcquireRelease_test) {
  Semaphore sem(10);
  for (int i = 0; i < 9; ++i) {
    sem.acquire();
  }
  sem.release();
  sem.acquire();
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(TryAcquire_test) {
  Semaphore sem(10);
  for (int i = 0; i < 10; ++i) {
    sem.acquire();
  }
  BOOST_CHECK(!sem.try_acquire());
  sem.release();
  BOOST_CHECK(sem.try_acquire());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(TimedAcquire_test) {
  Semaphore sem(10);
  for (int i = 0; i < 10; ++i) {
    sem.acquire();
  }

  // No slot available
  auto before = std::chrono::steady_clock::now();
  BOOST_CHECK(!sem.try_acquire_for(std::chrono::seconds(2)));
  auto after      = std::chrono::steady_clock::now();
  auto waited_for = after - before;
  BOOST_CHECK_GE(std::chrono::duration_cast<std::chrono::seconds>(waited_for).count(), 2);

  // One available
  sem.release();
  before = std::chrono::steady_clock::now();
  BOOST_CHECK(sem.try_acquire_for(std::chrono::seconds(2)));
  after      = std::chrono::steady_clock::now();
  waited_for = after - before;
  BOOST_CHECK_LT(std::chrono::duration_cast<std::chrono::seconds>(waited_for).count(), 2);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
