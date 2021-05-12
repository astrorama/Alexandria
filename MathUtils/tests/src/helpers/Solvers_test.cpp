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

#include "MathUtils/helpers/Solvers.h"
#include <boost/test/unit_test.hpp>
#include <cmath>

static constexpr double tolerance = 1e-40;

using namespace Euclid::MathUtils;

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(Solvers_test)

//-----------------------------------------------------------------------------

// y = 2x^2 + 4^x + 5
BOOST_AUTO_TEST_CASE(SolveSquare_test) {
  double x0, x1;

  std::tie(x0, x1) = solveSquare(2, 4, 5, 75);
  BOOST_CHECK_CLOSE(x0, -7, tolerance);
  BOOST_CHECK_CLOSE(x1, 5, tolerance);

  std::tie(x0, x1) = solveSquare(2, 4, 5, 8);
  BOOST_CHECK_CLOSE(x0, -2.58113883008419, tolerance);
  BOOST_CHECK_CLOSE(x1, 0.58113883008418976, tolerance);

  std::tie(x0, x1) = solveSquare(2, 4, 5, -8);
  BOOST_CHECK(std::isnan(x0));
  BOOST_CHECK(std::isnan(x1));
}

//-----------------------------------------------------------------------------

// y = 9^x - 7
BOOST_AUTO_TEST_CASE(SolveLinear_test) {
  double x0, x1;

  std::tie(x0, x1) = solveSquare(0, 9, -7, 100);
  BOOST_CHECK_CLOSE(x0, 11.88888888888889, tolerance);
  BOOST_CHECK_CLOSE(x1, x0, tolerance);

  std::tie(x0, x1) = solveSquare(0, 9, -7, 0);
  BOOST_CHECK_CLOSE(x0, 0.7777777777777778, tolerance);
  BOOST_CHECK_CLOSE(x1, x0, tolerance);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(Unsolvable_test) {
  BOOST_CHECK_THROW(solveSquare(0, 0, 1, 100), Elements::Exception);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
