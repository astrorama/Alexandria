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

/**
 * @file tests/src/function/FunctionAdapter_test_mock.cpp
 * @date November 2, 2015
 * @author FLorian Dubath
 */

#include "ElementsKernel/EnableGMock.h"
#include <boost/test/test_tools.hpp>
#include <boost/test/unit_test.hpp>

#include "MathUtils/function/FunctionAdapter.h"

using namespace testing;

class MockStdFunction {
public:
  virtual ~MockStdFunction() = default;
  MOCK_METHOD1(FunctorCall, double(double));
};

std::unique_ptr<MockStdFunction> mock_std_function_singleton{};

class TestFunction {
public:
  double operator()(double x) {
    if (mock_std_function_singleton == nullptr) {
      BOOST_FAIL("TestFunction was called when the MockStdFunction was not set");
    }
    return mock_std_function_singleton->FunctorCall(x);
  }
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(FunctionAdapter_test)

BOOST_AUTO_TEST_CASE(DirectCall) {
  mock_std_function_singleton.reset(new MockStdFunction{});
  EXPECT_CALL(*mock_std_function_singleton, FunctorCall(1.0)).Times(1).WillOnce(Return(3.14));

  Euclid::MathUtils::FunctionAdapter adapter{TestFunction()};

  BOOST_CHECK_EQUAL(adapter(1.0), 3.14);
  mock_std_function_singleton.reset(nullptr);
}

BOOST_AUTO_TEST_CASE(CloneCall) {
  mock_std_function_singleton.reset(new MockStdFunction{});
  EXPECT_CALL(*mock_std_function_singleton, FunctorCall(1.0)).Times(1).WillOnce(Return(3.14));

  Euclid::MathUtils::FunctionAdapter adapter{TestFunction()};
  auto                               cloned = adapter.clone();

  BOOST_CHECK_EQUAL((*cloned)(1.0), 3.14);
  mock_std_function_singleton.reset(nullptr);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
