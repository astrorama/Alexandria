/*
 * Copyright (C) 2012-2020 Euclid Science Ground Segment
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
 * @file tests/src/numericalIntegration/AdaptativeIntegration_test.cpp
 * @date 29 oct 2015
 * @author Florian Dubath
 */
#include "ElementsKernel/EnableGMock.h"
#include <boost/test/test_tools.hpp>
#include <boost/test/unit_test.hpp>
#include <vector>

#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Real.h"
#include "MathUtils/function/Function.h"
#include "MathUtils/numericalIntegration/AdaptativeIntegration.h"

using namespace testing;

struct AdaptativeIntegration_Fixture {
  class QuadratureMock1 {
  public:
    QuadratureMock1() {
      EXPECT_CALL(*this, functorCall(_, _, _, _)).Times(1).WillOnce(Return(1.0));
      EXPECT_CALL(*this, functorCallPrev(_, _, _, 1.0, _)).Times(1).WillOnce(Return(1.0));
    }

    double operator()(const Euclid::MathUtils::Function& function, double min, double max, int order) {
      return functorCall(function, min, max, order);
    }

    double operator()(const Euclid::MathUtils::Function& function, double min, double max, double previous_value, int order) {
      return functorCallPrev(function, min, max, previous_value, order);
    }

    MOCK_CONST_METHOD4(functorCall, double(const Euclid::MathUtils::Function&, double, double, int));
    MOCK_CONST_METHOD5(functorCallPrev, double(const Euclid::MathUtils::Function&, double, double, double, int));
  };
  class QuadratureMock2 {
  public:
    QuadratureMock2() {
      EXPECT_CALL(*this, functorCall(_, _, _, _)).Times(1).WillOnce(Return(1.0));
      EXPECT_CALL(*this, functorCallPrev(_, _, _, 1.0, 4)).Times(1).WillOnce(Return(1.1));
      EXPECT_CALL(*this, functorCallPrev(_, _, _, 1.1, 5)).Times(1).WillOnce(Return(1.1111));
      EXPECT_CALL(*this, functorCallPrev(_, _, _, 1.1111, 6)).Times(1).WillOnce(Return(1.1122111));
      EXPECT_CALL(*this, functorCallPrev(_, _, _, 1.1122111, 7)).Times(1).WillOnce(Return(1.1123223));
    }

    double operator()(const Euclid::MathUtils::Function& function, double min, double max, int order) {
      return functorCall(function, min, max, order);
    }

    double operator()(const Euclid::MathUtils::Function& function, double min, double max, double previous_value, int order) {
      return functorCallPrev(function, min, max, previous_value, order);
    }

    MOCK_CONST_METHOD4(functorCall, double(const Euclid::MathUtils::Function&, double, double, int));
    MOCK_CONST_METHOD5(functorCallPrev, double(const Euclid::MathUtils::Function&, double, double, double, int));
  };

  /**
   * function f(x)->a
   */
  class ConstFunction : public Euclid::MathUtils::Function {
  public:
    explicit ConstFunction(double a) : m_a{a} {};

    double operator()(const double) const override {
      return m_a;
    }

    std::unique_ptr<Function> clone() const override {
      return std::unique_ptr<Function>{new ConstFunction(m_a)};
    }

  private:
    double m_a;
  };
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(AdaptativeIntegration_test)

BOOST_FIXTURE_TEST_CASE(anchor_test, AdaptativeIntegration_Fixture) {

  ConstFunction                                             const_function{2.0};
  Euclid::MathUtils::AdaptativeIntegration<QuadratureMock1> integrator{0.1, 3};

  double result = integrator(const_function, 0.5, 1.33);
  BOOST_CHECK_EQUAL(result, 1.0);
}

BOOST_FIXTURE_TEST_CASE(recursion_test, AdaptativeIntegration_Fixture) {

  ConstFunction                                             const_function{2.0};
  Euclid::MathUtils::AdaptativeIntegration<QuadratureMock2> integrator{0.0002, 3};

  double result = integrator(const_function, 0.5, 1.33);
  BOOST_CHECK_EQUAL(result, 1.1123223);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
