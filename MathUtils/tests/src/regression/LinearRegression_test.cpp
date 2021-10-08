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

#include "MathUtils/regression/LinearRegression.h"
#include <ElementsKernel/Exception.h>
#include <boost/test/unit_test.hpp>

using Euclid::MathUtils::linearRegression;

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(LinearRegression_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(regression_test) {
  std::vector<double> delta_lambda{-100, -50, -20, -10, 10, 20, 50, 100};
  std::vector<double> tild_coef{1, 1.5, 1.8, 1.9, 2.1, 2.2, 2.5, 3};

  double expected_a = 0.01;
  double expected_b = 2.0;

  auto res = linearRegression(delta_lambda, tild_coef);

  BOOST_CHECK_CLOSE(res.first, expected_a, 0.01);
  BOOST_CHECK_CLOSE(res.second, expected_b, 0.01);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(wrong_size) {
  BOOST_CHECK_THROW(linearRegression(std::vector<double>{1, 2, 3}, std::vector<double>{1, 2}), Elements::Exception);
  BOOST_CHECK_THROW(linearRegression(std::vector<double>{}, std::vector<double>{}), Elements::Exception);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------