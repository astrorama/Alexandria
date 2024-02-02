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
#include <iostream>

using Euclid::MathUtils::FunctionAdapter;
using Euclid::MathUtils::SecantEndReason;
using Euclid::MathUtils::secantMethod;
using Euclid::MathUtils::SecantParams;

namespace Euclid {
namespace MathUtils {

std::ostream& operator<<(std::ostream& out, SecantEndReason reason) {
  switch (reason) {
  case SecantEndReason::SUCCESS:
    out << "SUCCESS";
    break;
  case SecantEndReason::MAX_ITER:
    out << "MAX_ITER";
    break;
  case SecantEndReason::GRADIENT:
    out << "GRADIENT";
    break;
  case SecantEndReason::OUT_OF_BOUNDS:
    out << "OUT_OF_BOUNDS";
    break;
  case SecantEndReason::VALUE_ERROR:
    out << "VALUE_ERROR";
    break;
  }
  return out;
}

}  // namespace MathUtils
}  // namespace Euclid

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(SecantMethod_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(Success_test) {
  FunctionAdapter func([](double v) { return v; });
  auto            result = secantMethod(func, -10, 10);
  BOOST_CHECK_SMALL(result.root, 1e-8);
  BOOST_CHECK_EQUAL(result.reason, SecantEndReason::SUCCESS);
  BOOST_CHECK_GT(result.iterations, 0);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(Sin_test) {
  FunctionAdapter func(static_cast<double (*)(double)>(&std::sin));
  auto            result = secantMethod(func, -M_PI_2, M_PI_2);
  BOOST_CHECK_SMALL(result.root, 1e-8);
  BOOST_CHECK_EQUAL(result.reason, SecantEndReason::SUCCESS);
  BOOST_CHECK_GT(result.iterations, 0);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(Cos_test) {
  FunctionAdapter func(static_cast<double (*)(double)>(&std::cos));
  auto            result = secantMethod(func, 0, M_PI);
  BOOST_CHECK_CLOSE(result.root, M_PI_2, 1e-8);
  BOOST_CHECK_EQUAL(result.reason, SecantEndReason::SUCCESS);
  BOOST_CHECK_GT(result.iterations, 0);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(NotSolvable_test) {
  FunctionAdapter func([](double) { return 1.; });
  auto            result = secantMethod(func, -10, 10);
  BOOST_CHECK_EQUAL(result.reason, SecantEndReason::GRADIENT);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(NotSolvableButClose_test) {
  SecantParams params;
  params.min = 1;
  params.max = 10;

  FunctionAdapter func([](double v) { return 1 + v; });
  auto            result = secantMethod(func, 5, 10, params);
  BOOST_CHECK_CLOSE(result.root, 1., 1e-8);
  BOOST_CHECK_EQUAL(result.reason, SecantEndReason::OUT_OF_BOUNDS);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(ValueError_test) {
  SecantParams params;
  params.min = 1;
  params.max = 10;

  FunctionAdapter func(static_cast<double (*)(double)>(&std::log));
  auto            result = secantMethod(func, -1, 1, params);
  BOOST_CHECK_EQUAL(result.reason, SecantEndReason::VALUE_ERROR);

  result = secantMethod(func, 0.5, -1, params);
  BOOST_CHECK_EQUAL(result.reason, SecantEndReason::VALUE_ERROR);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
