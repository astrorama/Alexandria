/*
 * Copyright (C) 2022 Euclid Science Ground Segment
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

#include "MathUtils/function/FunctionAdapter.h"
#include "MathUtils/root/SecantMethod.h"
#include <boost/test/unit_test.hpp>
#include <cmath>

using Euclid::MathUtils::FunctionAdapter;
using Euclid::MathUtils::SecantEndReason;
using Euclid::MathUtils::secantMethod;

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(SecantMethod_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(Success_test) {
  FunctionAdapter func([](double v) { return v; });
  auto            result = secantMethod(func, -10, 10);
  BOOST_CHECK_SMALL(result.first, 1e-8);
  BOOST_CHECK(result.second == SecantEndReason::SUCCESS);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(Sin_test) {
  FunctionAdapter func(static_cast<double (*)(double)>(&std::sin));
  auto            result = secantMethod(func, -M_PI_2, M_PI_2);
  BOOST_CHECK_SMALL(result.first, 1e-8);
  BOOST_CHECK(result.second == SecantEndReason::SUCCESS);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(Cos_test) {
  FunctionAdapter func(static_cast<double (*)(double)>(&std::cos));
  auto            result = secantMethod(func, 0, M_PI);
  BOOST_CHECK_CLOSE(result.first, M_PI_2, 1e-8);
  BOOST_CHECK(result.second == SecantEndReason::TOLERANCE);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(NotSolvable_test) {
  FunctionAdapter func([](double) { return 1.; });
  auto            result = secantMethod(func, -10, 10);
  BOOST_CHECK(result.second == SecantEndReason::FAILED);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(NotSolvableButClose_test) {
  FunctionAdapter func([](double v) { return 1 + v; });
  auto            result = secantMethod(func, 5, 10, {100, 1e-8, 1, 10});
  BOOST_CHECK_CLOSE(result.first, 1., 1e-8);
  BOOST_CHECK(result.second == SecantEndReason::FAILED);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
