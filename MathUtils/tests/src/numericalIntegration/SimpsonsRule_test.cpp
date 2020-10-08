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
 * @file tests/src/numericalIntegration/SimpsonRule_test.cpp
 * @date 29 oct. 2015
 * @author Florian Dubath
 */
#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Real.h"
#include "MathUtils/function/Function.h"
#include "MathUtils/numericalIntegration/SimpsonsRule.h"
#include <boost/test/unit_test.hpp>
#include <set>

struct simpsonsRule_Fixture {
  Euclid::MathUtils::SimpsonsRule quadrature{};

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

  /**
   * function f(x)->ax+b
   */
  class AffineFunction : public Euclid::MathUtils::Function {
  public:
    AffineFunction(double a, double b) : m_a{a}, m_b{b} {};

    double operator()(const double x) const override {
      return m_a * x + m_b;
    }

    std::unique_ptr<Function> clone() const override {
      return std::unique_ptr<Function>{new AffineFunction(m_a, m_b)};
    }

  private:
    double m_a;
    double m_b;
  };

  /**
   * function f(x)->ax^2+bx+c
   */
  class QuadraticFunction : public Euclid::MathUtils::Function {
  public:
    QuadraticFunction(double a, double b, double c) : m_a{a}, m_b{b}, m_c{c} {};

    double operator()(const double x) const override {
      return m_a * x * x + m_b * x + m_c;
    }

    std::unique_ptr<Function> clone() const override {
      return std::unique_ptr<Function>{new QuadraticFunction(m_a, m_b, m_c)};
    }

  private:
    double m_a;
    double m_b;
    double m_c;
  };

  /**
   * function f(x)->ax^3+bx^2+cx+d
   */
  class CubicFunction : public Euclid::MathUtils::Function {
  public:
    CubicFunction(double a, double b, double c, double d) : m_a{a}, m_b{b}, m_c{c}, m_d{d} {};

    double operator()(const double x) const override {
      return m_a * x * x * x + m_b * x * x + m_c * x + m_d;
    }

    std::unique_ptr<Function> clone() const override {
      return std::unique_ptr<Function>{new CubicFunction(m_a, m_b, m_c, m_d)};
    }

  private:
    double m_a;
    double m_b;
    double m_c;
    double m_d;
  };

  /**
   * function f(x)->a exp(bx)
   */
  class ExpFunction : public Euclid::MathUtils::Function {
  public:
    ExpFunction(double a, double b) : m_a{a}, m_b{b} {};

    double operator()(const double x) const override {
      return m_a * std::exp(x * m_b);
    }

    std::unique_ptr<Function> clone() const override {
      return std::unique_ptr<Function>{new ExpFunction(m_a, m_b)};
    }

  private:
    double m_a;
    double m_b;
  };

  /**
   * function f(x)->1/ sqrt(x*x*x)
   */
  class TestFunction : public Euclid::MathUtils::Function {
  public:
    double operator()(const double x) const override {
      return 1. / std::sqrt(x * x * x);
    }

    std::unique_ptr<Function> clone() const override {
      return std::unique_ptr<Function>{new TestFunction()};
    }
  };

  class MockFunction : public Euclid::MathUtils::Function {
  public:
    double operator()(const double x) const override {
      int value = std::floor(x + 0.0001);
      m_called.insert(value);
      m_called_number++;
      return m_result[value];
    }

    std::unique_ptr<Function> clone() const override {
      return std::unique_ptr<Function>{new MockFunction()};
    }

    mutable std::set<int> m_called{};
    mutable size_t        m_called_number = 0;

    std::vector<double> m_result{};
  };
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(simpsonsRule_test)

// check that when called with order bellow the minimal order an exception is thrown.
BOOST_FIXTURE_TEST_CASE(error_test, simpsonsRule_Fixture) {
  ConstFunction constant_function{1.0};

  BOOST_CHECK_THROW(quadrature(constant_function, 0., 1., 0), Elements::Exception);
  BOOST_CHECK_THROW(quadrature(constant_function, 0., 1., 1), Elements::Exception);
  BOOST_CHECK_THROW(quadrature(constant_function, 0., 1., 2), Elements::Exception);
  BOOST_CHECK_NO_THROW(quadrature(constant_function, 0., 1., 3));
  BOOST_CHECK_NO_THROW(quadrature(constant_function, 0., 1., 4));

  BOOST_CHECK_THROW(quadrature(constant_function, 0., 1., 1., 2), Elements::Exception);
  BOOST_CHECK_THROW(quadrature(constant_function, 0., 1., 1., 3), Elements::Exception);
  BOOST_CHECK_NO_THROW(quadrature(constant_function, 0., 1., 1., 4));
  BOOST_CHECK_NO_THROW(quadrature(constant_function, 0., 1., 1., 5));
}

BOOST_FIXTURE_TEST_CASE(Linear, simpsonsRule_Fixture) {
  ConstFunction  constant_function{1.0};
  AffineFunction affine_function{1.0, 0.0};
  double         result = quadrature(constant_function, 0., 1., 3);
  BOOST_CHECK(Elements::isEqual(result, 1.));

  result = quadrature(affine_function, 0., 1., 3);
  BOOST_CHECK(Elements::isEqual(result, 0.5));

  result = quadrature(affine_function, -1., 1., 3);
  BOOST_CHECK(Elements::isEqual(result, 0.));
}

BOOST_FIXTURE_TEST_CASE(quadratic, simpsonsRule_Fixture) {
  QuadraticFunction quadratic_func_test{
      1.0,
      0.,
      0,
  };
  double result = quadrature(quadratic_func_test, 0., 1., 3);
  BOOST_CHECK(Elements::isEqual(result, 1. / 3.));
}

BOOST_FIXTURE_TEST_CASE(cubic, simpsonsRule_Fixture) {
  CubicFunction cubic_func_test{1., 0., 0., 0.};
  double        result = quadrature(cubic_func_test, 0., 1., 3);
  BOOST_CHECK(Elements::isEqual(result, 1. / 4.));
}

BOOST_FIXTURE_TEST_CASE(recursion, simpsonsRule_Fixture) {
  CubicFunction cubic{1., 0., 0., 0.};
  for (int order = 3; order < 10; order++) {
    double result_o   = quadrature(cubic, 0., 1., order);
    double result_o1  = quadrature(cubic, 0., 1., order + 1);
    double result_rec = quadrature(cubic, 0., 1., result_o, order + 1);
    BOOST_CHECK(Elements::isEqual(result_rec, result_o1));
  }

  TestFunction test_function{};
  for (int order = 3; order < 10; order++) {
    double result_o   = quadrature(test_function, 0., 1., order);
    double result_o1  = quadrature(test_function, 0., 1., order + 1);
    double result_rec = quadrature(test_function, 0., 1., result_o, order + 1);
    BOOST_CHECK(Elements::isEqual(result_rec, result_o1));
  }
}

BOOST_FIXTURE_TEST_CASE(exp_decr, simpsonsRule_Fixture) {
  ExpFunction exp_function{1.0, -1.0};
  double      result = quadrature(exp_function, 0., 1., 3);

  double expected = (1. - exp(-1.));
  BOOST_CHECK((result - expected) / expected < 0.00001);

  result = quadrature(exp_function, 0., 1., 4);
  BOOST_CHECK((result - expected) / expected < 0.000001);

  TestFunction test_function{};
  expected = 2. * (1. - 1. / std::sqrt(2.));
  std::vector<double> precisions{0.0001, 0.00001, 0.000001, 0.0000001};
  std::vector<int>    orders{3, 4, 5, 6};
  for (size_t step = 0; step < orders.size(); step++) {
    result = quadrature(test_function, 1., 2., orders[step]);
    BOOST_CHECK_MESSAGE((result - expected) / expected < precisions[step],
                        "Expected:" + std::to_string(expected) + " Actual :" + std::to_string(result) +
                            " Diff:" + std::to_string(100. * (result - expected) / expected) + "%");
  }
}

BOOST_FIXTURE_TEST_CASE(implementation_test, simpsonsRule_Fixture) {
  MockFunction mock_function{};
  mock_function.m_result = {1, 1, 1, 1, 1, 1, 1, 1, 1};
  double result          = quadrature(mock_function, 0, 8, 3);

  // expected 3/8f(0)+7/6f(1)+23/24f(2)+f(3)+f(4)+f(5) +23/24f(6)+7/6f(7)+3/8f(8)
  double expected = 8.;

  BOOST_CHECK_EQUAL(result, expected);

  BOOST_CHECK_EQUAL(mock_function.m_called.size(), 9);
  BOOST_CHECK_EQUAL(mock_function.m_called_number, 9);

  int value = 0;
  for (auto called : mock_function.m_called) {
    BOOST_CHECK_EQUAL(value, called);
    ++value;
  }

  mock_function.m_called = {};
  mock_function.m_result = {100, 33, 0.1, 1000, 2, 10000, 0.001, 333, 1};
  result                 = quadrature(mock_function, 0, 8, 3);

  // expected 3/8f(0)+7/6f(1)+23/24f(2)+f(3)+f(4)+f(5) +23/24f(6)+7/6f(7)+3/8f(8)
  expected = 11466.97179166666666666666666666666666666666666666666666666666;

  BOOST_CHECK_EQUAL(result, expected);
}

BOOST_FIXTURE_TEST_CASE(implementation_next_step_test, simpsonsRule_Fixture) {
  MockFunction mock_function{};
  mock_function.m_result = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
  double result          = quadrature(mock_function, 0, 16, 16., 4);

  double expected = 16.;

  BOOST_CHECK_EQUAL(result, expected);

  // one expect the new points to be called (8) + the second and third on both
  // ends to correct the factor (+2 +2)

  std::vector<int> values = {1, 2, 3, 4, 5, 7, 9, 11, 12, 13, 14, 15};
  BOOST_CHECK_EQUAL(mock_function.m_called.size(), values.size());
  BOOST_CHECK_EQUAL(mock_function.m_called_number, values.size());
  int id = 0;
  for (auto called : mock_function.m_called) {
    BOOST_CHECK_EQUAL(values[id], called);
    ++id;
  }
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
