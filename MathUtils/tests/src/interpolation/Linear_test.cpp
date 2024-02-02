/*
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
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
 * @file tests/src/interpolation/Linear_test.cpp
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#include "MathUtils/function/function_tools.h"
#include "MathUtils/interpolation/interpolation.h"
#include <boost/test/unit_test.hpp>
#include <memory>

struct Linear_Fixture {
  double close_tolerance{1E-10};
  double small_tolerance{1E-20};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(Linear_test)

//-----------------------------------------------------------------------------
// Test the linear interpolation
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Linear, Linear_Fixture) {

  // Given
  std::vector<double> x{-1., 0., 1., 2., 8., 10.};
  std::vector<double> y{4., 3., 1., 2., 2., 20.};

  // When
  auto   linear = Euclid::MathUtils::interpolate(x, y, Euclid::MathUtils::InterpolationType::LINEAR, false);
  double value1 = (*linear)(-2.);
  double value2 = (*linear)(-1.);
  double value3 = (*linear)(-.5);
  double value4 = (*linear)(0.);
  double value5 = (*linear)(1.);
  double value6 = (*linear)(1.7);
  double value7 = (*linear)(5.);
  double value8 = (*linear)(9.);
  double value9 = (*linear)(10.1);

  // Then
  BOOST_CHECK_SMALL(value1, small_tolerance);
  BOOST_CHECK_CLOSE(value2, 4., close_tolerance);
  BOOST_CHECK_CLOSE(value3, 3.5, close_tolerance);
  BOOST_CHECK_CLOSE(value4, 3., close_tolerance);
  BOOST_CHECK_CLOSE(value5, 1., close_tolerance);
  BOOST_CHECK_CLOSE(value6, 1.7, close_tolerance);
  BOOST_CHECK_CLOSE(value7, 2., close_tolerance);
  BOOST_CHECK_CLOSE(value8, 11., close_tolerance);
  BOOST_CHECK_SMALL(value9, small_tolerance);
}

BOOST_FIXTURE_TEST_CASE(LinearXYDataset, Linear_Fixture) {

  // Given
  auto dataset = Euclid::XYDataset::XYDataset::factory({-1., 0., 1., 2., 8., 10.}, {4., 3., 1., 2., 2., 20.});

  // When
  auto   linear = Euclid::MathUtils::interpolate(dataset, Euclid::MathUtils::InterpolationType::LINEAR, false);
  double value1 = (*linear)(-2.);
  double value2 = (*linear)(-1.);
  double value3 = (*linear)(-.5);
  double value4 = (*linear)(0.);
  double value5 = (*linear)(1.);
  double value6 = (*linear)(1.7);
  double value7 = (*linear)(5.);
  double value8 = (*linear)(9.);
  double value9 = (*linear)(10.1);

  // Then
  BOOST_CHECK_SMALL(value1, small_tolerance);
  BOOST_CHECK_CLOSE(value2, 4., close_tolerance);
  BOOST_CHECK_CLOSE(value3, 3.5, close_tolerance);
  BOOST_CHECK_CLOSE(value4, 3., close_tolerance);
  BOOST_CHECK_CLOSE(value5, 1., close_tolerance);
  BOOST_CHECK_CLOSE(value6, 1.7, close_tolerance);
  BOOST_CHECK_CLOSE(value7, 2., close_tolerance);
  BOOST_CHECK_CLOSE(value8, 11., close_tolerance);
  BOOST_CHECK_SMALL(value9, small_tolerance);
}

//-----------------------------------------------------------------------------
// Test the linear interpolation, with extrapolation on the edges
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(LinearExtrapolation, Linear_Fixture) {

  // Given
  std::vector<double> x{-1., 0., 1., 2., 8., 10.};
  std::vector<double> y{4., 3., 1., 2., 2., 20.};

  // When
  auto   linear = Euclid::MathUtils::interpolate(x, y, Euclid::MathUtils::InterpolationType::LINEAR, true);
  double value1 = (*linear)(-2.);
  double value2 = (*linear)(-1.);
  double value3 = (*linear)(-.5);
  double value4 = (*linear)(0.);
  double value5 = (*linear)(1.);
  double value6 = (*linear)(1.7);
  double value7 = (*linear)(5.);
  double value8 = (*linear)(9.);
  double value9 = (*linear)(10.1);

  // Then
  BOOST_CHECK_CLOSE(value1, 5., close_tolerance);
  BOOST_CHECK_CLOSE(value2, 4., close_tolerance);
  BOOST_CHECK_CLOSE(value3, 3.5, close_tolerance);
  BOOST_CHECK_CLOSE(value4, 3., close_tolerance);
  BOOST_CHECK_CLOSE(value5, 1., close_tolerance);
  BOOST_CHECK_CLOSE(value6, 1.7, close_tolerance);
  BOOST_CHECK_CLOSE(value7, 2., close_tolerance);
  BOOST_CHECK_CLOSE(value8, 11., close_tolerance);
  BOOST_CHECK_CLOSE(value9, 20.9, close_tolerance);
}

BOOST_FIXTURE_TEST_CASE(LinearExtrapolationXYDataset, Linear_Fixture) {

  // Given
  auto dataset = Euclid::XYDataset::XYDataset::factory({-1., 0., 1., 2., 8., 10.}, {4., 3., 1., 2., 2., 20.});

  // When
  auto   linear = Euclid::MathUtils::interpolate(dataset, Euclid::MathUtils::InterpolationType::LINEAR, true);
  double value1 = (*linear)(-2.);
  double value2 = (*linear)(-1.);
  double value3 = (*linear)(-.5);
  double value4 = (*linear)(0.);
  double value5 = (*linear)(1.);
  double value6 = (*linear)(1.7);
  double value7 = (*linear)(5.);
  double value8 = (*linear)(9.);
  double value9 = (*linear)(10.1);

  // Then
  BOOST_CHECK_CLOSE(value1, 5., close_tolerance);
  BOOST_CHECK_CLOSE(value2, 4., close_tolerance);
  BOOST_CHECK_CLOSE(value3, 3.5, close_tolerance);
  BOOST_CHECK_CLOSE(value4, 3., close_tolerance);
  BOOST_CHECK_CLOSE(value5, 1., close_tolerance);
  BOOST_CHECK_CLOSE(value6, 1.7, close_tolerance);
  BOOST_CHECK_CLOSE(value7, 2., close_tolerance);
  BOOST_CHECK_CLOSE(value8, 11., close_tolerance);
  BOOST_CHECK_CLOSE(value9, 20.9, close_tolerance);
}

//-----------------------------------------------------------------------------
// Extrapolate a single point
//-----------------------------------------------------------------------------
BOOST_FIXTURE_TEST_CASE(Linear1DataPoint, Linear_Fixture) {

  // Given
  std::vector<double> x{2.};
  std::vector<double> y{42.};

  // When
  auto   linear = Euclid::MathUtils::interpolate(x, y, Euclid::MathUtils::InterpolationType::LINEAR, true);
  double value1 = (*linear)(-2.);
  double value2 = (*linear)(-1.);
  double value3 = (*linear)(-.5);
  double value4 = (*linear)(2.);
  double value5 = (*linear)(100.);

  // Then
  BOOST_CHECK_CLOSE(value1, 42., close_tolerance);
  BOOST_CHECK_CLOSE(value2, 42., close_tolerance);
  BOOST_CHECK_CLOSE(value3, 42., close_tolerance);
  BOOST_CHECK_CLOSE(value4, 42., close_tolerance);
  BOOST_CHECK_CLOSE(value5, 42., close_tolerance);
}

BOOST_FIXTURE_TEST_CASE(Linear1DataPointXYDataset, Linear_Fixture) {

  // Given
  auto dataset = Euclid::XYDataset::XYDataset::factory({2.}, {42.});

  // When
  auto   linear = Euclid::MathUtils::interpolate(dataset, Euclid::MathUtils::InterpolationType::LINEAR, true);
  double value1 = (*linear)(-2.);
  double value2 = (*linear)(-1.);
  double value3 = (*linear)(-.5);
  double value4 = (*linear)(2.);
  double value5 = (*linear)(100.);

  // Then
  BOOST_CHECK_CLOSE(value1, 42., close_tolerance);
  BOOST_CHECK_CLOSE(value2, 42., close_tolerance);
  BOOST_CHECK_CLOSE(value3, 42., close_tolerance);
  BOOST_CHECK_CLOSE(value4, 42., close_tolerance);
  BOOST_CHECK_CLOSE(value5, 42., close_tolerance);
}

//-----------------------------------------------------------------------------
// Do not extrapolate a single point
//-----------------------------------------------------------------------------
BOOST_FIXTURE_TEST_CASE(Linear1DataPointNoExtrapolate, Linear_Fixture) {

  // Given
  std::vector<double> x{2.};
  std::vector<double> y{42.};

  // When
  auto   linear = Euclid::MathUtils::interpolate(x, y, Euclid::MathUtils::InterpolationType::LINEAR, false);
  double value1 = (*linear)(-2.);
  double value2 = (*linear)(2.);
  double value3 = (*linear)(5.);

  // Then
  BOOST_CHECK_EQUAL(value1, 0.);
  BOOST_CHECK_CLOSE(value2, 42., close_tolerance);
  BOOST_CHECK_EQUAL(value3, 0.);
}

BOOST_FIXTURE_TEST_CASE(Linear1DataPointNoExtrapolateXYDataset, Linear_Fixture) {

  // Given
  auto dataset = Euclid::XYDataset::XYDataset::factory({2.}, {42.});

  // When
  auto   linear = Euclid::MathUtils::interpolate(dataset, Euclid::MathUtils::InterpolationType::LINEAR, false);
  double value1 = (*linear)(-2.);
  double value2 = (*linear)(2.);
  double value3 = (*linear)(5.);

  // Then
  BOOST_CHECK_EQUAL(value1, 0.);
  BOOST_CHECK_CLOSE(value2, 42., close_tolerance);
  BOOST_CHECK_EQUAL(value3, 0.);
}

//-----------------------------------------------------------------------------
// Step function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(LinearStep, Linear_Fixture) {
  // Given
  std::vector<double> x{1., 2., 2., 4.};
  std::vector<double> y{1., 2., 3., 4.};

  // When
  auto   linear = Euclid::MathUtils::interpolate(x, y, Euclid::MathUtils::InterpolationType::LINEAR, true);
  double value1 = (*linear)(1);
  double value2 = (*linear)(2);
  double value3 = (*linear)(3);
  double value4 = (*linear)(4);

  // Then
  BOOST_CHECK_CLOSE(value1, 1., close_tolerance);
  BOOST_CHECK_CLOSE(value2, 2., close_tolerance);
  BOOST_CHECK_CLOSE(value3, 3.5, close_tolerance);
  BOOST_CHECK_CLOSE(value4, 4., close_tolerance);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Linear_Integration, Linear_Fixture) {
  // Given
  std::vector<double> x{-1., 0., 1., 2., 8., 10.};
  std::vector<double> y{4., 3., 1., 2., 2., 20.};

  // When
  auto linear = Euclid::MathUtils::interpolate(x, y, Euclid::MathUtils::InterpolationType::LINEAR, true);

  // Then
  BOOST_CHECK_CLOSE(Euclid::MathUtils::integrate(*linear, -1., 10.), 41., close_tolerance);
  BOOST_CHECK_CLOSE(Euclid::MathUtils::integrate(*linear, 0.5, 4.), 6.25, close_tolerance);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Linear_Vector, Linear_Fixture) {
  // Given
  std::vector<double> x{-1., 0., 1., 2., 8., 10.};
  std::vector<double> y{4., 3., 1., 2., 2., 20.};
  std::vector<double> x2{-2., -1., -0.5, 0., 1., 1.7, 5., 9., 10.1};

  // When
  auto linear = Euclid::MathUtils::interpolate(x, y, Euclid::MathUtils::InterpolationType::LINEAR, false);

  std::vector<double> output;
  (*linear)(x2, output);

  // Then
  std::vector<double> expected{0., 4., 3.5, 3., 1., 1.7, 2., 11., 0.};
  BOOST_REQUIRE_EQUAL(output.size(), x2.size());
  for (size_t i = 0; i < output.size(); ++i) {
    BOOST_CHECK_CLOSE(output[i], expected[i], close_tolerance);
  }
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(LinearExtrapolate_Vector, Linear_Fixture) {
  // Given
  std::vector<double> x{-1., 0., 1., 2., 8., 10.};
  std::vector<double> y{4., 3., 1., 2., 2., 20.};
  std::vector<double> x2{-2., -1., -0.5, 0., 1., 1.7, 5., 9., 10.1};

  // When
  auto linear = Euclid::MathUtils::interpolate(x, y, Euclid::MathUtils::InterpolationType::LINEAR, true);

  std::vector<double> output;
  (*linear)(x2, output);

  // Then
  std::vector<double> expected{5., 4., 3.5, 3., 1., 1.7, 2., 11., 20.9};
  BOOST_REQUIRE_EQUAL(output.size(), x2.size());
  for (size_t i = 0; i < output.size(); ++i) {
    BOOST_CHECK_CLOSE(output[i], expected[i], close_tolerance);
  }
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(LinearInterpolateAllOutside, Linear_Fixture) {
  // Given
  std::vector<double> x{-1., 0., 1., 2., 8., 10.};
  std::vector<double> y{4., 3., 1., 2., 2., 20.};
  std::vector<double> x2{-20., -10., -5};
  std::vector<double> x3{40., 50., 60, 70., 80.};

  // When
  auto linear = Euclid::MathUtils::interpolate(x, y, Euclid::MathUtils::InterpolationType::LINEAR, false);

  // Then
  std::vector<double> output;
  (*linear)(x2, output);
  BOOST_CHECK_EQUAL(output.size(), x2.size());

  for (auto& v : output) {
    BOOST_CHECK_EQUAL(v, 0.);
  }

  (*linear)(x3, output);
  BOOST_CHECK_EQUAL(output.size(), x3.size());
  for (auto& v : output) {
    BOOST_CHECK_EQUAL(v, 0.);
  }
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(LinearInterpolateStepIntegrate, Linear_Fixture) {
  // Given
  std::vector<double> x{0., 1., 1., 2., 3., 4.};
  std::vector<double> y{0., 0., 1., 1., 1., 0.};

  // When
  auto linear = Euclid::MathUtils::interpolate(x, y, Euclid::MathUtils::InterpolationType::LINEAR, false);

  // Then
  auto integral = Euclid::MathUtils::integrate(*linear, 0., 4.);
  BOOST_CHECK_CLOSE(integral, 2.5, close_tolerance);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
