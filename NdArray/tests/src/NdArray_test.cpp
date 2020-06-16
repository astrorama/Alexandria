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
* @file tests/src/Matrix_test.cpp
* @date November 21, 2018
* @author Alejandro Alvarez Ayllon
*/

#include <boost/test/unit_test.hpp>
#include "NdArray/NdArray.h"

using namespace Euclid::NdArray;

BOOST_AUTO_TEST_SUITE(Matrix_test)

BOOST_AUTO_TEST_CASE(OneDimension_test) {
  NdArray<int> m{5};
  m.at(0) = 10;

  BOOST_CHECK_EQUAL(m.shape().size(), 1);
  BOOST_CHECK_EQUAL(m.shape()[0], 5);
  BOOST_CHECK_EQUAL(m.at(0), 10);
}

BOOST_AUTO_TEST_CASE(TwoDimension_test) {
  NdArray<int> m{2, 3};
  m.at(0, 0) = 10;
  m.at(1, 0) = 15;
  m.at(0, 1) = 50;
  m.at(1, 1) = 20;

  BOOST_CHECK_EQUAL(m.shape().size(), 2);
  BOOST_CHECK_EQUAL(m.shape()[0], 2);
  BOOST_CHECK_EQUAL(m.shape()[1], 3);
  BOOST_CHECK_EQUAL((m.at(0, 0)), 10);
  BOOST_CHECK_EQUAL((m.at(std::vector<size_t>{0, 0})), 10);
  BOOST_CHECK_EQUAL((m.at(1, 1)), 20);

  const NdArray<int> &cm = m;
  BOOST_CHECK_EQUAL((cm.at(1, 1)), 20);

  std::vector<int> expected{
    10, 50, 0,
    15, 20, 0
  };
  BOOST_CHECK_EQUAL_COLLECTIONS(cm.begin(), cm.end(), expected.begin(), expected.end());
}

BOOST_AUTO_TEST_CASE(InitFromVector_test) {
  NdArray<int> m{std::vector<size_t>{2, 3}, {10, 50, 0, 15, 20, 0}};

  BOOST_CHECK_EQUAL(m.shape()[0], 2);
  BOOST_CHECK_EQUAL(m.shape()[1], 3);
  BOOST_CHECK_EQUAL((m.at(0, 0)), 10);
  BOOST_CHECK_EQUAL((m.at(1, 1)), 20);
}

BOOST_AUTO_TEST_CASE(BadInitFromVector_test) {
  try {
    NdArray<int> m{std::vector<size_t>{2, 3}, {10, 50, 0, 15}};
    BOOST_ERROR("The construction should have failed");
  }
  catch (...) {
  }
}

BOOST_AUTO_TEST_CASE(BadCoordinates_test) {
  NdArray<int> m{std::vector<size_t>{2, 3}, {10, 50, 0, 15, 20, 0}};

  BOOST_CHECK_THROW(m.at(1), std::out_of_range);
  BOOST_CHECK_THROW(m.at(1, 2, 3), std::out_of_range);
  BOOST_CHECK_THROW(m.at(4, 2), std::out_of_range);
}

BOOST_AUTO_TEST_CASE(Fill_test) {
  NdArray<int> m{2, 3};
  std::fill(m.begin(), m.end(), 42);

  std::vector<int> expected{42, 42, 42, 42, 42, 42};
  BOOST_CHECK_EQUAL_COLLECTIONS(m.begin(), m.end(), expected.begin(), expected.end());
  BOOST_CHECK_EQUAL(m.at(1, 1), 42);
}

BOOST_AUTO_TEST_CASE(Copy_test) {
  std::vector<int> original{1, 1, 2, 3, 5, 8};
  std::vector<int> expected(original.begin(), original.end());
  NdArray<int> m(std::vector<size_t>{2, 3}, original);

  BOOST_CHECK_EQUAL(original.size(), 6);
  BOOST_CHECK_EQUAL_COLLECTIONS(m.begin(), m.end(), expected.begin(), expected.end());
}

BOOST_AUTO_TEST_CASE(Move_test) {
  std::vector<int> original{1, 1, 2, 3, 5, 8};
  std::vector<int> expected(original.begin(), original.end());
  NdArray<int> m(std::vector<size_t>{2, 3}, std::move(original));

  BOOST_CHECK_EQUAL(original.size(), 0);
  BOOST_CHECK_EQUAL_COLLECTIONS(m.begin(), m.end(), expected.begin(), expected.end());
}

BOOST_AUTO_TEST_CASE(Ostream_test) {
  std::vector<int> original{1, 1, 2, 3, 5, 8};
  NdArray<int> m(std::vector<size_t>{2, 3}, std::move(original));

  std::stringstream stream;
  stream << m;

  BOOST_CHECK_EQUAL(stream.str(), std::string("<2,3>1,1,2,3,5,8"));
}

BOOST_AUTO_TEST_CASE(FromIterator_test) {
  std::list<int> original{1, 7, 6, 9, 5, 3};
  NdArray<int> m(std::vector<size_t>{2, 3}, std::begin(original), std::end(original));
  BOOST_CHECK_EQUAL(original.size(), 6);
  BOOST_CHECK_EQUAL_COLLECTIONS(m.begin(), m.end(), original.begin(), original.end());
}

BOOST_AUTO_TEST_SUITE_END()
