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
  NdArray<float>  one_axis_float{{3}, {1, 2, 3}};
  NdArray<float>  two_axes{{3, 4}, {7, 8, 3, 4, 5, 2, 1, 12, 11, 6, 10, 9}};
  NdArray<double> three_axes{{3, 4, 5}, {//
                                         42, 32, 41, 47, 11, 33, 59, 58, 54, 2, 45, 4,  17, 23, 7,  49, 57, 40, 19, 18,
                                         6,  39, 24, 36, 50, 52, 12, 38, 37, 8, 15, 30, 5,  20, 26, 43, 28, 10, 27, 44,
                                         35, 14, 25, 1,  31, 21, 29, 48, 9,  0, 51, 34, 16, 55, 53, 46, 13, 3,  22, 56}};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(NdArrayOps_test)

//-----------------------------------------------------------------------------

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

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(UnravelIndexOutOfBounds_test) {
  BOOST_CHECK_THROW(unravel_index(555, {3, 4, 8}), std::out_of_range);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Sum2_test, OpsFixture) {
  BOOST_CHECK_EQUAL(sum(two_axes), 78.);

  std::vector<float> expected0{23, 16, 14, 25};
  auto               sum0 = sum(two_axes, 0);
  BOOST_REQUIRE_EQUAL(sum0.shape().size(), 1);
  BOOST_REQUIRE_EQUAL(sum0.shape()[0], 4);
  BOOST_CHECK_EQUAL_COLLECTIONS(sum0.begin(), sum0.end(), expected0.begin(), expected0.end());

  std::vector<float> expected1{22, 20, 36};
  auto               sum1 = sum(two_axes, 1);
  BOOST_REQUIRE_EQUAL(sum1.shape().size(), 1);
  BOOST_REQUIRE_EQUAL(sum1.shape()[0], 3);
  BOOST_CHECK_EQUAL_COLLECTIONS(sum1.begin(), sum1.end(), expected1.begin(), expected1.end());

  auto sum_1 = sum(two_axes, -1);
  BOOST_REQUIRE_EQUAL(sum_1.shape().size(), 1);
  BOOST_REQUIRE_EQUAL(sum_1.shape()[0], 3);
  BOOST_CHECK_EQUAL_COLLECTIONS(sum_1.begin(), sum_1.end(), expected1.begin(), expected1.end());

  BOOST_CHECK_THROW(sum(two_axes, 2), std::out_of_range);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Sum3_test, OpsFixture) {
  BOOST_CHECK_EQUAL(sum(three_axes), 1770.);

  std::vector<double> expected0{83, 85, 90, 84, 92, 106, 100, 144, 100, 10, 111, 68, 38, 98, 86, 138, 98, 53, 68, 118};
  auto                sum0 = sum(three_axes, 0);
  BOOST_REQUIRE_EQUAL(sum0.shape().size(), 2);
  BOOST_REQUIRE_EQUAL(sum0.shape()[0], 4);
  BOOST_REQUIRE_EQUAL(sum0.shape()[1], 5);
  BOOST_CHECK_EQUAL_COLLECTIONS(sum0.begin(), sum0.end(), expected0.begin(), expected0.end());

  std::vector<double> expected1{169, 152, 156, 143, 38, 116, 109, 77, 120, 128, 153, 90, 92, 87, 140};
  auto                sum1 = sum(three_axes, 1);
  BOOST_REQUIRE_EQUAL(sum1.shape().size(), 2);
  BOOST_REQUIRE_EQUAL(sum1.shape()[0], 3);
  BOOST_REQUIRE_EQUAL(sum1.shape()[1], 5);
  BOOST_CHECK_EQUAL_COLLECTIONS(sum1.begin(), sum1.end(), expected1.begin(), expected1.end());

  std::vector<double> expected2{173, 206, 96, 183, 155, 147, 96, 152, 106, 107, 209, 140};
  auto                sum2 = sum(three_axes, 2);
  BOOST_REQUIRE_EQUAL(sum2.shape().size(), 2);
  BOOST_REQUIRE_EQUAL(sum2.shape()[0], 3);
  BOOST_REQUIRE_EQUAL(sum2.shape()[1], 4);
  BOOST_CHECK_EQUAL_COLLECTIONS(sum2.begin(), sum2.end(), expected2.begin(), expected2.end());

  auto sum_1 = sum(three_axes, -1);
  BOOST_REQUIRE_EQUAL(sum_1.shape().size(), 2);
  BOOST_REQUIRE_EQUAL(sum_1.shape()[0], 3);
  BOOST_REQUIRE_EQUAL(sum_1.shape()[1], 4);
  BOOST_CHECK_EQUAL_COLLECTIONS(sum_1.begin(), sum_1.end(), expected2.begin(), expected2.end());

  BOOST_CHECK_THROW(sum(two_axes, 3), std::out_of_range);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Sum1_test, OpsFixture) {
  auto sum0 = sum(one_axis, 0);
  BOOST_REQUIRE_EQUAL(sum0.shape().size(), 1);
  BOOST_REQUIRE_EQUAL(sum0.shape()[0], 1);
  BOOST_CHECK_EQUAL(sum0.at(0), 6);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ArgMax_test, OpsFixture) {
  auto argmax1 = argmax(one_axis);
  BOOST_CHECK_EQUAL(argmax1[0], 2);

  auto argmax2 = argmax(two_axes);
  BOOST_CHECK_EQUAL(argmax2[0], 1);
  BOOST_CHECK_EQUAL(argmax2[1], 3);

  auto argmax3 = argmax(three_axes);
  BOOST_CHECK_EQUAL(argmax3[0], 0);
  BOOST_CHECK_EQUAL(argmax3[1], 1);
  BOOST_CHECK_EQUAL(argmax3[2], 1);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ArgMin_test, OpsFixture) {
  auto argmin1 = argmin(one_axis);
  BOOST_CHECK_EQUAL(argmin1[0], 0);

  auto argmin2 = argmin(two_axes);
  BOOST_CHECK_EQUAL(argmin2[0], 1);
  BOOST_CHECK_EQUAL(argmin2[1], 2);

  auto argmin3 = argmin(three_axes);
  BOOST_CHECK_EQUAL(argmin3[0], 2);
  BOOST_CHECK_EQUAL(argmin3[1], 1);
  BOOST_CHECK_EQUAL(argmin3[2], 4);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Trapz1d_test, OpsFixture) {
  std::vector<float> knots_regular{1, 2, 3};
  auto               integrated = trapz(one_axis_float, knots_regular.begin(), knots_regular.end(), 0);
  BOOST_CHECK_EQUAL(integrated.size(), 1);
  BOOST_CHECK_CLOSE(integrated.at(0), 4, 1e-8);

  std::vector<float> knots_irregular{1, 2.5, 10};
  integrated = trapz(one_axis_float, knots_irregular.begin(), knots_irregular.end(), 0);
  BOOST_CHECK_CLOSE(integrated.at(0), 21, 1e-8);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Trapz2d_test, OpsFixture) {
  std::vector<float> knots_regular{1, 2, 3, 4};

  auto integrated = trapz(two_axes, knots_regular.begin(), knots_regular.end() - 1, 0);
  BOOST_REQUIRE_EQUAL(integrated.size(), 4);
  BOOST_CHECK_CLOSE(integrated.at(0), 14., 1e-8);
  BOOST_CHECK_CLOSE(integrated.at(1), 9., 1e-8);
  BOOST_CHECK_CLOSE(integrated.at(2), 7.5, 1e-8);
  BOOST_CHECK_CLOSE(integrated.at(3), 18.5, 1e-8);

  integrated = trapz(two_axes, knots_regular.begin(), knots_regular.end(), -1);
  BOOST_REQUIRE_EQUAL(integrated.size(), 3);
  BOOST_CHECK_CLOSE(integrated.at(0), 16.5, 1e-8);
  BOOST_CHECK_CLOSE(integrated.at(1), 11.5, 1e-8);
  BOOST_CHECK_CLOSE(integrated.at(2), 26., 1e-8);

  std::vector<float> knots_irregular{1, 2.5, 10., 10.5};
  integrated = trapz(two_axes, knots_irregular.begin(), knots_irregular.end() - 1, 0);
  BOOST_CHECK_CLOSE(integrated.at(0), 69., 1e-8);
  BOOST_CHECK_CLOSE(integrated.at(1), 37.5, 1e-8);
  BOOST_CHECK_CLOSE(integrated.at(2), 44.25, 1e-8);
  BOOST_CHECK_CLOSE(integrated.at(3), 90.75, 1e-8);

  integrated = trapz(two_axes, knots_irregular.begin(), knots_irregular.end(), -1);
  BOOST_REQUIRE_EQUAL(integrated.size(), 3);
  BOOST_CHECK_CLOSE(integrated.at(0), 54.25, 1e-8);
  BOOST_CHECK_CLOSE(integrated.at(1), 19.75, 1e-8);
  BOOST_CHECK_CLOSE(integrated.at(2), 77.5, 1e-8);

  BOOST_CHECK_THROW(trapz(two_axes, knots_irregular.begin(), knots_irregular.end(), 6), std::out_of_range);
  BOOST_CHECK_THROW(trapz(two_axes, knots_irregular.begin(), knots_irregular.end(), 0), std::length_error);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Trapz3d_test, OpsFixture) {
  std::vector<float> knots_irregular{1., 2.8, 3.9, 4.1, 5.};

  auto integrated = trapz(three_axes, knots_irregular.begin(), knots_irregular.end(), -1);
  BOOST_REQUIRE_EQUAL(integrated.size(), 12);
  BOOST_REQUIRE_EQUAL(integrated.shape()[0], 3);
  BOOST_REQUIRE_EQUAL(integrated.shape()[1], 4);

  std::vector<float> expected2{141.65, 183.55, 73.15, 171.3, 119.85, 112.85, 82.95, 120.45, 82.55, 97.1, 159.7, 99.5};
  for (size_t i = 0; i < expected2.size(); ++i) {
    BOOST_CHECK_CLOSE(expected2[i], *(integrated.begin() + i), 1e-4);
  }

  integrated = trapz(three_axes, knots_irregular.begin(), knots_irregular.end() - 1, 1);
  BOOST_REQUIRE_EQUAL(integrated.size(), 15);
  BOOST_REQUIRE_EQUAL(integrated.shape()[0], 3);
  BOOST_REQUIRE_EQUAL(integrated.shape()[1], 5);

  std::vector<float> expected1{119.8,  122.65, 136.05, 137.45, 19.15, 94.85, 74.8, 80.95,
                               101.75, 77.9,   99.7,   78.05,  102.8, 51.9,  67.95};
  for (size_t i = 0; i < expected1.size(); ++i) {
    BOOST_CHECK_CLOSE(expected1[i], *(integrated.begin() + i), 1e-4);
  }

  integrated = trapz(three_axes, knots_irregular.begin(), knots_irregular.end() - 2, 0);
  BOOST_REQUIRE_EQUAL(integrated.size(), 20);
  BOOST_REQUIRE_EQUAL(integrated.shape()[0], 4);
  BOOST_REQUIRE_EQUAL(integrated.shape()[1], 5);

  std::vector<float> expected0{65.75, 93.05, 85.45, 95.05, 99.45, 116.65, 86.45, 133.7, 107.2, 13.4,
                               90.3,  65.8,  31.35, 79.95, 73.15, 131.75, 99.05, 52.15, 68.35, 110.8};
  for (size_t i = 0; i < expected0.size(); ++i) {
    BOOST_CHECK_CLOSE(expected0[i], *(integrated.begin() + i), 1e-4);
  }
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
