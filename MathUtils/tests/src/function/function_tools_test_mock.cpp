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
 * @file tests/src/function/function_tools_mock.cpp
 * @date Oct 29, 2015
 * @author Florian Dubath
 */

#include "ElementsKernel/EnableGMock.h"
#include <boost/test/test_tools.hpp>
#include <boost/test/unit_test.hpp>

#include "MathUtils/function/Function.h"
#include "MathUtils/function/function_tools.h"
#include "mocks.h"

using namespace testing;

struct Function_Tools_Fixture {
  class MockScheme : public Euclid::MathUtils::NumericalIntegrationScheme {
  public:
    double operator()(const Euclid::MathUtils::Function& function, double min, double max) override {
      return functorCall(function, min, max);
    }

    MOCK_CONST_METHOD3(functorCall, double(const Euclid::MathUtils::Function&, double, double));
  };
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(function_tools_test_mock)

//-----------------------------------------------------------------------------
// Test that integration of a non-integrable function is delegated to
// the NumericalIntegrationScheme
//-----------------------------------------------------------------------------
BOOST_FIXTURE_TEST_CASE(NonIntegrableIntegration, Function_Tools_Fixture) {

  // Given
  FunctionMock                f = FunctionMock{0.};
  std::unique_ptr<MockScheme> scheme(new MockScheme{});
  EXPECT_CALL(*scheme, functorCall(_, _, _)).Times(1).WillOnce(Return(3.14));

  // Then
  double result = Euclid::MathUtils::integrate(f, 0, 1, std::move(scheme));
  BOOST_CHECK_EQUAL(result, 3.14);
}

//-----------------------------------------------------------------------------
// Test that integration of an integrable function is done without calling the
//  NumericalIntegrationScheme
//-----------------------------------------------------------------------------
BOOST_FIXTURE_TEST_CASE(Integrable, Function_Tools_Fixture) {

  // Given
  double                      min      = -1.5;
  double                      max      = 7.32;
  IntegrableMock              f        = IntegrableMock{5.};
  double                      expected = 5. * (max - min);
  std::unique_ptr<MockScheme> scheme(new MockScheme{});

  // When
  double integral = Euclid::MathUtils::integrate(f, min, max, std::move(scheme));

  // Then
  BOOST_CHECK_EQUAL(integral, expected);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
