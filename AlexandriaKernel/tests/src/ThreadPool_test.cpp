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

/**
 * @file tests/src/ThreadPool_test.cpp
 * @date 01/06/17
 * @author nikoapos
 */

#include <chrono>
#include <mutex>
#include <thread>
#include <vector>

#include <boost/test/unit_test.hpp>

#include "AlexandriaKernel/ThreadPool.h"
#include "ElementsKernel/Exception.h"

using namespace Euclid;

class SleepTask {

public:
  SleepTask(int sleep, std::mutex& mutex, std::vector<int>& output) : m_sleep(sleep), m_mutex(mutex), m_output(output) {}

  void operator()() {
    std::this_thread::sleep_for(std::chrono::milliseconds(m_sleep));
    std::lock_guard<std::mutex> lock{m_mutex.get()};
    m_output.get().push_back(m_sleep);
  }

private:
  int                                      m_sleep;
  std::reference_wrapper<std::mutex>       m_mutex;
  std::reference_wrapper<std::vector<int>> m_output;
};

class ExceptionTask {

public:
  void operator()() {
    throw Elements::Exception();
  }
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(ThreadPool_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(block_test) {

  // Given
  std::mutex       mutex;
  std::vector<int> output{};
  ThreadPool       pool{4, 10};

  // When
  pool.submit(SleepTask(1000, mutex, output));
  pool.submit(SleepTask(700, mutex, output));
  pool.submit(SleepTask(900, mutex, output));
  pool.submit(SleepTask(500, mutex, output));
  pool.submit(SleepTask(350, mutex, output));
  pool.submit(SleepTask(100, mutex, output));
  BOOST_CHECK_GT(pool.activeThreads(), 0);
  pool.block();

  // Then
  std::lock_guard<std::mutex> lock{mutex};
  BOOST_CHECK(!pool.checkForException());
  BOOST_CHECK_EQUAL(output.size(), 6);
  BOOST_CHECK_EQUAL(output[0], 500);
  BOOST_CHECK_EQUAL(output[1], 700);
  BOOST_CHECK_EQUAL(output[2], 100);
  BOOST_CHECK_EQUAL(output[3], 350);
  BOOST_CHECK_EQUAL(output[4], 900);
  BOOST_CHECK_EQUAL(output[5], 1000);

  BOOST_CHECK_GT(pool.activeThreads(), 0);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(destructor_test) {

  // Given
  std::mutex       mutex;
  std::vector<int> output{};

  // When
  {
    ThreadPool pool{4, 10};
    pool.submit(SleepTask(1000, mutex, output));
    pool.submit(SleepTask(700, mutex, output));
    pool.submit(SleepTask(900, mutex, output));
    pool.submit(SleepTask(500, mutex, output));
    pool.submit(SleepTask(300, mutex, output));
    pool.submit(SleepTask(100, mutex, output));
    std::this_thread::sleep_for(std::chrono::milliseconds(600));
  }

  // Then
  std::lock_guard<std::mutex> lock{mutex};
  BOOST_CHECK_EQUAL(output.size(), 5);
  BOOST_CHECK_EQUAL(output[0], 500);
  BOOST_CHECK_EQUAL(output[1], 700);
  BOOST_CHECK_EQUAL(output[2], 300);
  BOOST_CHECK_EQUAL(output[3], 900);
  BOOST_CHECK_EQUAL(output[4], 1000);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(block_exception_test) {

  // Given
  ThreadPool pool{4};

  // When
  pool.submit(ExceptionTask());

  // Then
  BOOST_CHECK_THROW(pool.block(), Elements::Exception);
  BOOST_CHECK(pool.checkForException());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(checkForException_test) {

  // Given
  ThreadPool pool{4};

  // When
  pool.submit(ExceptionTask());
  std::this_thread::sleep_for(std::chrono::milliseconds(100));

  // Then
  BOOST_CHECK(pool.checkForException());
  BOOST_CHECK_THROW(pool.checkForException(true), Elements::Exception);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
