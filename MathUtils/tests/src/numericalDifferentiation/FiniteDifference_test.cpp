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
 * @file tests/src/numericalDifferentiation/CentralDifference_test.cpp
 * @date January 9, 2020
 * @author Alejandro Alvarez Ayllon
 */

#include "MathUtils/function/FunctionAdapter.h"
#include "MathUtils/numericalDifferentiation/FiniteDifference.h"
#include <boost/test/unit_test.hpp>
#include <numeric>
#if BOOST_VERSION >= 105900
#include <boost/test/tools/floating_point_comparison.hpp>
#else
#include <boost/test/floating_point_comparison.hpp>
#endif
#include <cmath>

using namespace Euclid::MathUtils;

struct FiniteDifference_Fixture {
  double close_tolerance{1E-4};
  double small_tolerance{1E-20};

  std::vector<double> xs;

  FiniteDifference_Fixture() : xs(20) {
    std::iota(xs.begin(), xs.end(), -10.);
  }
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(FiniteDifference_test)

//-----------------------------------------------------------------------------
// Constant function: First and second derivatives are 0
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Constant, FiniteDifference_Fixture) {
  auto constant_f = FunctionAdapter([](double) { return 5; });

  for (auto x : xs) {
    auto dy  = derivative(constant_f, x);
    auto ddy = derivative2nd(constant_f, x);
    BOOST_CHECK_SMALL(dy, small_tolerance);
    BOOST_CHECK_SMALL(ddy, small_tolerance);
  }
}

//-----------------------------------------------------------------------------
// Linear function: first derivative is the slope, second is 0
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Linear, FiniteDifference_Fixture) {
  const float slope    = 5;
  auto        linear_f = FunctionAdapter([slope](double x) { return slope * x + 4; });

  for (auto x : xs) {
    auto dy  = derivative(linear_f, x);
    auto ddy = derivative2nd(linear_f, x);
    BOOST_CHECK_CLOSE(dy, slope, close_tolerance);
    BOOST_CHECK_SMALL(ddy, small_tolerance);
  }
}

//-----------------------------------------------------------------------------
// Quadratic function: first derivative is 2ax + b, second is 2a
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Quadratic, FiniteDifference_Fixture) {
  const float a = 3, b = 5, c = 42;
  auto        quadratic_f = FunctionAdapter([a, b, c](double x) {
    double y = a * x * x + b * x + c;
    return y;
  });

  for (auto x : xs) {
    auto dy  = derivative(quadratic_f, x);
    auto ddy = derivative2nd(quadratic_f, x);
    BOOST_CHECK_CLOSE(dy, 2 * a * x + b, close_tolerance);
    BOOST_CHECK_CLOSE(ddy, 2 * a, close_tolerance);
  }
}

//-----------------------------------------------------------------------------
// Sin function: first derivative is cos(x), second is -sin(x)
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Sin, FiniteDifference_Fixture) {
  auto sin_f = FunctionAdapter([](double x) { return std::sin(x); });

  for (auto x : xs) {
    auto dy  = derivative(sin_f, x);
    auto ddy = derivative2nd(sin_f, x);
    BOOST_CHECK_CLOSE(dy, cos(x), close_tolerance);
    BOOST_CHECK_CLOSE(ddy, -sin(x), close_tolerance);
  }
}

//-----------------------------------------------------------------------------
// e^x function: first and second derivative are e^x
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ex, FiniteDifference_Fixture) {
  auto ex_f = FunctionAdapter([](double x) { return std::pow(M_E, x); });

  for (auto x : xs) {
    auto dy  = derivative(ex_f, x);
    auto ddy = derivative2nd(ex_f, x);
    BOOST_CHECK_CLOSE(dy, ex_f(x), close_tolerance);
    BOOST_CHECK_CLOSE(ddy, ex_f(x), close_tolerance);
  }
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
