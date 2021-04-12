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

#include "FilePool/FileAccessor.h"
#include <boost/test/unit_test.hpp>

using namespace Euclid::FilePool;

// This struct can not be copied or assigned, only moved
// The code can only compile if it works properly with movable-only types
// Normally you would not expect file descriptors to be copyable
struct NonCopyableFd {
  int m_fd;

  explicit NonCopyableFd(int fd) : m_fd(fd) {}
  NonCopyableFd(const NonCopyableFd&) = delete;
  NonCopyableFd& operator=(const NonCopyableFd&) = delete;

  NonCopyableFd(NonCopyableFd&& other) {
    m_fd       = other.m_fd;
    other.m_fd = -1;
  }
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(FileAccessorTest)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(OnlyReadTest) {
  boost::shared_mutex mutex;
  int                 release_flags = 0;
  auto                callback      = [&release_flags](NonCopyableFd&& fd) { release_flags |= fd.m_fd; };

  {
    // We can have multiple readers
    NonCopyableFd f1(1), f2(2), f3(4);

    FileReadAccessor<NonCopyableFd> a1(std::move(f1), callback, boost::shared_lock<boost::shared_mutex>(mutex));
    FileReadAccessor<NonCopyableFd> a2(std::move(f2), callback, boost::shared_lock<boost::shared_mutex>(mutex));
    FileReadAccessor<NonCopyableFd> a3(std::move(f3), callback, boost::shared_lock<boost::shared_mutex>(mutex));

    BOOST_CHECK_EQUAL(a1.m_fd.m_fd, 1);
    BOOST_CHECK_EQUAL(a2.m_fd.m_fd, 2);
    BOOST_CHECK_EQUAL(a3.m_fd.m_fd, 4);
    BOOST_CHECK(a1.isReadOnly());
    BOOST_CHECK_EQUAL(release_flags, 0);
  }

  BOOST_CHECK_EQUAL(release_flags, 7);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(WriteTest) {
  boost::shared_mutex mutex;
  int                 release_flags = 0;
  auto                callback      = [&release_flags](NonCopyableFd&& fd) { release_flags |= fd.m_fd; };

  {
    // Only one writer
    NonCopyableFd f1(1);
    FileWriteAccessor<NonCopyableFd> a1(std::move(f1), callback, boost::unique_lock<boost::shared_mutex>(mutex));

    BOOST_CHECK_EQUAL(a1.m_fd.m_fd, 1);
    BOOST_CHECK(!a1.isReadOnly());
    BOOST_CHECK_EQUAL(release_flags, 0);
    // The mutex must be acquired
    BOOST_CHECK(!mutex.try_lock());
  }

  BOOST_CHECK(mutex.try_lock());
  BOOST_CHECK_EQUAL(release_flags, 1);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
