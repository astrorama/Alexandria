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
 * @file tests/src/ThreadPool_test.cpp
 * @date 01/06/17
 * @author nikoapos
 */

#include <mutex>
#include <vector>
#include <thread>
#include <chrono>

#include <boost/test/unit_test.hpp>

#include "AlexandriaKernel/ThreadPool.h"


#include <iostream>

using namespace Euclid;

class SleepTask {

public:
  
  SleepTask(int sleep, std::mutex& mutex, std::vector<int>& output) :
  m_sleep(sleep), m_mutex(mutex), m_output(output) {
  }

  void operator()() {
    std::this_thread::sleep_for(std::chrono::milliseconds(m_sleep));
    std::lock_guard<std::mutex> lock {m_mutex.get()};
    m_output.get().push_back(m_sleep);
  }
  
private:
  
  int m_sleep;
  std::reference_wrapper<std::mutex> m_mutex;
  std::reference_wrapper<std::vector<int>> m_output;
  
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (ThreadPool_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE( block_test ) {

  // Given
  std::mutex mutex;
  std::vector<int> output {};
  ThreadPool pool {4};
  
  // When
  pool.submit(SleepTask(300, mutex, output));
  pool.submit(SleepTask(100, mutex, output));
  pool.submit(SleepTask(200, mutex, output));
  pool.submit(SleepTask(50, mutex, output));
  pool.submit(SleepTask(155, mutex, output));
  pool.submit(SleepTask(75, mutex, output));
  pool.block();
  
  // Then
  std::lock_guard<std::mutex> lock {mutex};
  BOOST_CHECK_EQUAL(output.size(), 6);
  BOOST_CHECK_EQUAL(output[0], 50);
  BOOST_CHECK_EQUAL(output[1], 100);
  BOOST_CHECK_EQUAL(output[2], 75);
  BOOST_CHECK_EQUAL(output[3], 200);
  BOOST_CHECK_EQUAL(output[4], 155);
  BOOST_CHECK_EQUAL(output[5], 300);

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE( destructor_test ) {

  // Given
  std::mutex mutex;
  std::vector<int> output {};
  
  // When
  {
    ThreadPool pool {4};
    pool.submit(SleepTask(300, mutex, output));
    pool.submit(SleepTask(100, mutex, output));
    pool.submit(SleepTask(200, mutex, output));
    pool.submit(SleepTask(50, mutex, output));
    pool.submit(SleepTask(155, mutex, output));
    pool.submit(SleepTask(75, mutex, output));
    std::this_thread::sleep_for(std::chrono::milliseconds(60));
  }
  
  
  // Then
  std::lock_guard<std::mutex> lock {mutex};
  BOOST_CHECK_EQUAL(output.size(), 5);
  BOOST_CHECK_EQUAL(output[0], 50);
  BOOST_CHECK_EQUAL(output[1], 100);
  BOOST_CHECK_EQUAL(output[2], 75);
  BOOST_CHECK_EQUAL(output[3], 200);
  BOOST_CHECK_EQUAL(output[4], 300);

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


