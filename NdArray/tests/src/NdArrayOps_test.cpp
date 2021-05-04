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

#include "NdArray/Operations.h"
#include <boost/test/unit_test.hpp>

using namespace Euclid::NdArray;

struct OpsFixture {
  NdArray<int>    one_axis{{3}, {1, 2, 3}};
  NdArray<float>  two_axes{{3, 4}, {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}};
  NdArray<double> three_axes{{3, 4, 5}, {0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                         20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
                                         40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59}};
};

BOOST_AUTO_TEST_SUITE(NdArrayOps_test)

BOOST_AUTO_TEST_CASE(UnravelIndex_test) {
  // These are easy to verify with numpy.unravel_index
  auto coords = unravel_index(0, {3, 4});
  BOOST_CHECK_EQUAL(coords.size(), 2);
  BOOST_CHECK_EQUAL(coords[0], 0);
  BOOST_CHECK_EQUAL(coords[1], 0);

  coords = unravel_index(4, {3, 4});
  BOOST_CHECK_EQUAL(coords[0], 1);
  BOOST_CHECK_EQUAL(coords[1], 0);

  coords = unravel_index(9, {3, 4});
  BOOST_CHECK_EQUAL(coords[0], 2);
  BOOST_CHECK_EQUAL(coords[1], 1);

  coords = unravel_index(55, {3, 4, 8});
  BOOST_CHECK_EQUAL(coords.size(), 3);
  BOOST_CHECK_EQUAL(coords[0], 1);
  BOOST_CHECK_EQUAL(coords[1], 2);
  BOOST_CHECK_EQUAL(coords[2], 7);
}

BOOST_AUTO_TEST_CASE(UnravelIndexOutOfBounds_test) {
  BOOST_CHECK_THROW(unravel_index(555, {3, 4, 8}), std::out_of_range);
}

BOOST_FIXTURE_TEST_CASE(Sum2_test, OpsFixture) {
  BOOST_CHECK_EQUAL(sum(two_axes), 78.);

  std::vector<float> expected0{15, 18, 21, 24};
  auto               sum0 = sum(two_axes, 0);
  BOOST_REQUIRE_EQUAL(sum0.shape().size(), 1);
  BOOST_REQUIRE_EQUAL(sum0.shape()[0], 4);
  BOOST_CHECK_EQUAL_COLLECTIONS(sum0.begin(), sum0.end(), expected0.begin(), expected0.end());

  std::vector<float> expected1{10, 26, 42};
  auto               sum1 = sum(two_axes, 1);
  BOOST_REQUIRE_EQUAL(sum1.shape().size(), 1);
  BOOST_REQUIRE_EQUAL(sum1.shape()[0], 3);
  BOOST_CHECK_EQUAL_COLLECTIONS(sum1.begin(), sum1.end(), expected1.begin(), expected1.end());

  BOOST_CHECK_THROW(sum(two_axes, 2), std::out_of_range);
}

BOOST_FIXTURE_TEST_CASE(Sum3_test, OpsFixture) {
  BOOST_CHECK_EQUAL(sum(three_axes), 1770.);

  std::vector<double> expected0{60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117};
  auto                sum0 = sum(three_axes, 0);
  BOOST_REQUIRE_EQUAL(sum0.shape().size(), 2);
  BOOST_REQUIRE_EQUAL(sum0.shape()[0], 4);
  BOOST_REQUIRE_EQUAL(sum0.shape()[1], 5);
  BOOST_CHECK_EQUAL_COLLECTIONS(sum0.begin(), sum0.end(), expected0.begin(), expected0.end());

  std::vector<double> expected1{30, 34, 38, 42, 46, 110, 114, 118, 122, 126, 190, 194, 198, 202, 206};
  auto                sum1 = sum(three_axes, 1);
  BOOST_REQUIRE_EQUAL(sum1.shape().size(), 2);
  BOOST_REQUIRE_EQUAL(sum1.shape()[0], 3);
  BOOST_REQUIRE_EQUAL(sum1.shape()[1], 5);
  BOOST_CHECK_EQUAL_COLLECTIONS(sum1.begin(), sum1.end(), expected1.begin(), expected1.end());

  std::vector<double> expected2{10, 35, 60, 85, 110, 135, 160, 185, 210, 235, 260, 285};
  auto                sum2 = sum(three_axes, 2);
  BOOST_REQUIRE_EQUAL(sum2.shape().size(), 2);
  BOOST_REQUIRE_EQUAL(sum2.shape()[0], 3);
  BOOST_REQUIRE_EQUAL(sum2.shape()[1], 4);
  BOOST_CHECK_EQUAL_COLLECTIONS(sum2.begin(), sum2.end(), expected2.begin(), expected2.end());

  BOOST_CHECK_THROW(sum(two_axes, 3), std::out_of_range);
}

BOOST_FIXTURE_TEST_CASE(Sum1_test, OpsFixture) {
  auto sum0 = sum(one_axis, 0);
  BOOST_REQUIRE_EQUAL(sum0.shape().size(), 1);
  BOOST_REQUIRE_EQUAL(sum0.shape()[0], 1);
  BOOST_CHECK_EQUAL(sum0.at(0), 6);
}

BOOST_AUTO_TEST_SUITE_END()
