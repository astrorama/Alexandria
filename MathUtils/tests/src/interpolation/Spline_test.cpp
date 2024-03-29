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
 * @file tests/src/interpolation/Spline_test.cpp
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#include "MathUtils/function/function_tools.h"
#include "MathUtils/interpolation/interpolation.h"
#include "MathUtils/numericalDifferentiation/FiniteDifference.h"
#include <boost/test/unit_test.hpp>
#include <cmath>

using namespace Euclid::MathUtils;

struct Spline_Fixture {
  const double eps = std::sqrt(std::numeric_limits<double>::epsilon());
  const double close_tolerance{1.2E-2};
  const double small_tolerance{1E-10};

  std::vector<double> x = std::vector<double>(200);
  std::vector<double> y = std::vector<double>(200);

  Spline_Fixture() {
    std::generate(x.begin(), x.end(), [xvalue = -10.1]() mutable {
      xvalue += 0.1;
      return xvalue;
    });
    std::transform(x.begin(), x.end(), y.begin(), &sin);
  }
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(Spline_test)

//-----------------------------------------------------------------------------
// The interpolated function value at x must match the same value as the original
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(fx, Spline_Fixture) {
  // When
  auto                cubic = interpolate(x, y, InterpolationType::CUBIC_SPLINE);
  std::vector<double> result{};
  for (double xValue : x) {
    result.push_back((*cubic)(xValue));
  }
  double outside1 = (*cubic)(-11.);
  double outside2 = (*cubic)(11.);

  // Then
  for (size_t i = 0; i < y.size(); i++) {
    if (std::abs(result[i]) <= eps) {
      BOOST_CHECK_SMALL(result[i], small_tolerance);
      BOOST_CHECK_SMALL(y[i], small_tolerance);
    } else {
      BOOST_CHECK_CLOSE(result[i], y[i], close_tolerance);
    }
  }
  BOOST_CHECK_SMALL(outside1, small_tolerance);
  BOOST_CHECK_SMALL(outside2, small_tolerance);
}

//-----------------------------------------------------------------------------
// Spline interpolation is piecewise, so check that for each knot, the value of
// the splines to each side match with the original value
//-----------------------------------------------------------------------------
BOOST_FIXTURE_TEST_CASE(Spline_fx, Spline_Fixture) {
  auto cubic_f = interpolate(x, y, InterpolationType::CUBIC_SPLINE);

  for (size_t i = 0; i < x.size() - 1; ++i) {
    auto x0        = x[i + 1];
    auto left      = x0 - std::numeric_limits<double>::epsilon();
    auto right     = x0 + std::numeric_limits<double>::epsilon();
    auto left_val  = (*cubic_f)(left);
    auto right_val = (*cubic_f)(right);

    if (std::abs(left_val) <= eps || std::abs(right_val) <= eps) {
      BOOST_CHECK_SMALL(left_val, small_tolerance);
      BOOST_CHECK_SMALL(right_val, small_tolerance);
      BOOST_CHECK_SMALL(y[i + 1], small_tolerance);
    } else {
      BOOST_CHECK_CLOSE(left_val, right_val, close_tolerance);
      BOOST_CHECK_CLOSE(left_val, y[i + 1], close_tolerance);
    }
  }
}

//-----------------------------------------------------------------------------
// Similarly, the first derivative of the splines to each side must match
//-----------------------------------------------------------------------------
BOOST_FIXTURE_TEST_CASE(Spline_dfx, Spline_Fixture) {
  auto cubic_f = interpolate(x, y, InterpolationType::CUBIC_SPLINE);

  for (size_t i = 0; i < x.size() - 1; ++i) {
    auto x0    = x[i + 1];
    auto left  = x0 - std::numeric_limits<double>::epsilon();
    auto right = x0 + std::numeric_limits<double>::epsilon();

    auto left_dy  = derivative(*cubic_f, left);
    auto right_dy = derivative(*cubic_f, right);

    if (std::abs(left_dy) <= eps || std::abs(right_dy) <= eps) {
      BOOST_CHECK_SMALL(left_dy, small_tolerance);
      BOOST_CHECK_SMALL(right_dy, small_tolerance);
    } else {
      BOOST_CHECK_CLOSE(left_dy, right_dy, close_tolerance);
    }
  }
}

//-----------------------------------------------------------------------------
// Not strictly a requirement for spline interpolation, for some applications
// also the second derivative of the splines to each side must match
//-----------------------------------------------------------------------------
BOOST_FIXTURE_TEST_CASE(Spline_ddfx, Spline_Fixture) {
  auto cubic_f = interpolate(x, y, InterpolationType::CUBIC_SPLINE);

  for (size_t i = 0; i < x.size() - 1; ++i) {
    auto x0    = x[i + 1];
    auto left  = x0 - std::numeric_limits<double>::epsilon();
    auto right = x0 + std::numeric_limits<double>::epsilon();

    auto left_ddy  = derivative2nd(*cubic_f, left);
    auto right_ddy = derivative2nd(*cubic_f, right);

    if (std::abs(left_ddy) <= eps || std::abs(right_ddy) <= eps) {
      BOOST_CHECK_SMALL(left_ddy, small_tolerance);
      BOOST_CHECK_SMALL(right_ddy, small_tolerance);
    } else {
      BOOST_CHECK_CLOSE(left_ddy, right_ddy, 2e-2);
    }
  }
}

//-----------------------------------------------------------------------------
// Second derivative at the endpoints should be 0 when extrapolating
//-----------------------------------------------------------------------------
BOOST_FIXTURE_TEST_CASE(Spline_extrapolation, Spline_Fixture) {
  auto cubic_f = interpolate(x, y, InterpolationType::CUBIC_SPLINE, true);

  auto left_ddy  = derivative2nd(*cubic_f, x.front());
  auto right_ddy = derivative2nd(*cubic_f, x.back());

  BOOST_CHECK_SMALL(left_ddy, 1e-4);
  BOOST_CHECK_SMALL(right_ddy, 1e-4);
}

//-----------------------------------------------------------------------------
// Extrapolate a single point
//-----------------------------------------------------------------------------
BOOST_FIXTURE_TEST_CASE(Spline_1DataPoint, Spline_Fixture) {

  // Given
  std::vector<double> x_test_value{2.};
  std::vector<double> y_test_value{42.};

  // When
  auto   linear = Euclid::MathUtils::interpolate(x_test_value, y_test_value,
                                                 Euclid::MathUtils::InterpolationType::CUBIC_SPLINE, true);
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
BOOST_FIXTURE_TEST_CASE(Spline_1DataPoint_NoExtrapolate, Spline_Fixture) {

  // Given
  std::vector<double> x_test_value{2.};
  std::vector<double> y_test_value{42.};

  // When
  auto   cubic  = Euclid::MathUtils::interpolate(x_test_value, y_test_value,
                                                 Euclid::MathUtils::InterpolationType::CUBIC_SPLINE, false);
  double value1 = (*cubic)(-2.);
  double value2 = (*cubic)(2.);
  double value3 = (*cubic)(5.);

  // Then
  BOOST_CHECK_EQUAL(value1, 0.);
  BOOST_CHECK_CLOSE(value2, 42., close_tolerance);
  BOOST_CHECK_EQUAL(value3, 0.);
}

//-----------------------------------------------------------------------------
// Integrate
//-----------------------------------------------------------------------------
BOOST_FIXTURE_TEST_CASE(Spline_Integrate, Spline_Fixture) {
  // When
  auto cubic = Euclid::MathUtils::interpolate(x, y, Euclid::MathUtils::InterpolationType::CUBIC_SPLINE, true);

  // Then
  BOOST_CHECK_CLOSE(Euclid::MathUtils::integrate(*cubic, 0.0, 1.0), 0.459697592, close_tolerance);
  BOOST_CHECK_CLOSE(Euclid::MathUtils::integrate(*cubic, 1.5, 3.5), 1.007193412, close_tolerance);
}

//-----------------------------------------------------------------------------
// Call with a vector
//-----------------------------------------------------------------------------
BOOST_FIXTURE_TEST_CASE(Spline_Vector, Spline_Fixture) {
  // When
  auto cubic = Euclid::MathUtils::interpolate(x, y, Euclid::MathUtils::InterpolationType::CUBIC_SPLINE, false);
  std::vector<double> xs{-20., -18., -16., -14., -12., -10., -8., -6., -4., -2.,
                         2.,   4.,   6.,   8.,   10.,  12.,  14., 16., 18., 20.};
  std::vector<double> output;

  // Then
  std::vector<double> expected{0.0,         0.0,          0.0,          0.0,         0.0,
                               0.544021111, -0.989358247, 0.279415498,  0.756802495, -0.909297427,
                               0.909297427, -0.756802495, -0.279415498, 0.989358247, 0.0,
                               0.0,         0.0,          0.0,          0.0,         0.0};

  (*cubic)(xs, output);
  BOOST_REQUIRE_EQUAL(output.size(), xs.size());
  for (size_t i = 0; i < xs.size(); ++i) {
    BOOST_CHECK_CLOSE(output[i], expected[i], close_tolerance);
  }
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(InterpolateAllOutside, Spline_Fixture) {
  // Given
  std::vector<double> x2{-30., -20., -15.};
  std::vector<double> x3{40., 50., 60., 80.};

  // When
  auto cubic = Euclid::MathUtils::interpolate(x, y, Euclid::MathUtils::InterpolationType::CUBIC_SPLINE, false);

  // Then
  std::vector<double> output;
  (*cubic)(x2, output);
  BOOST_CHECK_EQUAL(output.size(), x2.size());

  for (auto& v : output) {
    BOOST_CHECK_EQUAL(v, 0.);
  }

  (*cubic)(x3, output);
  BOOST_CHECK_EQUAL(output.size(), x3.size());
  for (auto& v : output) {
    BOOST_CHECK_EQUAL(v, 0.);
  }
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
