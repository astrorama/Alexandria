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
 * @file tests/src/function/function_tools_test.cpp
 * @date February 19, 2014
 * @author Nikolaos Apostolakos
 */

#include "ElementsKernel/Exception.h"
#include "MathUtils/function/Function.h"
#include "MathUtils/function/Integrable.h"
#include "MathUtils/function/function_tools.h"
#include "MathUtils/function/multiplication.h"
#include "mocks.h"
#include <boost/test/unit_test.hpp>

class DummyMultiplyFunction : public Euclid::MathUtils::Function {

  double operator()(const double) const override {
    return 0;
  }

  void operator()(const std::vector<double>& xs, std::vector<double>& out) const override {
    out.resize(xs.size());
    std::fill(out.begin(), out.end(), 0);
  }

  std::unique_ptr<Euclid::MathUtils::Function> clone() const override {
    return std::unique_ptr<Euclid::MathUtils::Function>{new DummyMultiplyFunction{}};
  }
};

std::unique_ptr<Euclid::MathUtils::Function> dummyMultiply(const Euclid::MathUtils::Function&,
                                                           const Euclid::MathUtils::Function&) {
  return std::unique_ptr<Euclid::MathUtils::Function>(new DummyMultiplyFunction{});
}

class FunctionType1 : public Euclid::MathUtils::Function {
  double operator()(const double) const override {
    return 0;
  }

  void operator()(const std::vector<double>& xs, std::vector<double>& out) const override {
    out.resize(xs.size());
    std::fill(out.begin(), out.end(), 0);
  }

  std::unique_ptr<Euclid::MathUtils::Function> clone() const override {
    return std::unique_ptr<Euclid::MathUtils::Function>{new FunctionType1{}};
  }
};

class FunctionType2 : public Euclid::MathUtils::Function {
  double operator()(const double) const override {
    return 0;
  }

  void operator()(const std::vector<double>& xs, std::vector<double>& out) const override {
    out.resize(xs.size());
    std::fill(out.begin(), out.end(), 0);
  }

  std::unique_ptr<Euclid::MathUtils::Function> clone() const override {
    return std::unique_ptr<Euclid::MathUtils::Function>{new FunctionType2{}};
  }
};

struct Function_Tools_Fixture {
  double close_tolerance{1E-10};
  double small_tolerance{1E-20};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(function_tools_test)

//-----------------------------------------------------------------------------
// Test that integration of a non-integrable function throws an exception
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(NonIntegrableIntegration) {

  // Given
  FunctionMock f = FunctionMock{0.};

  // Then
  BOOST_CHECK_THROW(Euclid::MathUtils::integrate(f, 0, 1), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test that integration of an integrable function delegates the call
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(IntegrableIntegration) {

  // Given
  double         min      = -1.5;
  double         max      = 7.32;
  IntegrableMock f        = IntegrableMock{5.};
  double         expected = 5. * (max - min);

  // When
  double integral = Euclid::MathUtils::integrate(f, min, max);

  // Then
  BOOST_CHECK_EQUAL(integral, expected);
  BOOST_CHECK_EQUAL(f.m_min, min);
  BOOST_CHECK_EQUAL(f.m_max, max);
}

//-----------------------------------------------------------------------------
// Test that multiplying two functions with undefined multiplication works
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(NonMultipliableMultiplication, Function_Tools_Fixture) {

  // Given
  FunctionMock f1{4.};
  FunctionMock f2{3.};

  // When
  auto multiplication = Euclid::MathUtils::multiply(f1, f2);

  // Then
  BOOST_CHECK_CLOSE((*multiplication)(15.), 12., close_tolerance);
}

//-----------------------------------------------------------------------------
// Test multiplication function selection between a specific and a generic function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(SpecificGenericMultiplication, Function_Tools_Fixture) {

  // Given
  FunctionType1 f1{};
  FunctionType2 f2{};

  // When
  auto mult1 = Euclid::MathUtils::multiply(f1, f2);
  auto mult2 = Euclid::MathUtils::multiply(f2, f1);

  // Then
  BOOST_CHECK(dynamic_cast<DummyMultiplyFunction*>(mult1.get()) == nullptr);
  BOOST_CHECK(dynamic_cast<DummyMultiplyFunction*>(mult2.get()) == nullptr);

  // Given
  Euclid::MathUtils::multiplySpecificGenericMap[typeid(FunctionType1)] = dummyMultiply;

  // When
  mult1 = Euclid::MathUtils::multiply(f1, f2);
  mult2 = Euclid::MathUtils::multiply(f2, f1);

  // Then
  BOOST_CHECK(dynamic_cast<DummyMultiplyFunction*>(mult1.get()) != nullptr);
  BOOST_CHECK(dynamic_cast<DummyMultiplyFunction*>(mult2.get()) != nullptr);

  Euclid::MathUtils::multiplySpecificGenericMap.erase(typeid(FunctionType1));
}

//-----------------------------------------------------------------------------
// Test multiplication function selection between two specific functions
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(SpecificSpecificMultiplication, Function_Tools_Fixture) {

  // Given
  FunctionType1 f1{};
  FunctionType2 f2{};

  // When
  auto mult1 = Euclid::MathUtils::multiply(f1, f2);
  auto mult2 = Euclid::MathUtils::multiply(f2, f1);

  // Then
  BOOST_CHECK(dynamic_cast<DummyMultiplyFunction*>(mult1.get()) == nullptr);
  BOOST_CHECK(dynamic_cast<DummyMultiplyFunction*>(mult2.get()) == nullptr);

  // Given
  Euclid::MathUtils::multiplySpecificSpecificMap[{typeid(FunctionType1), typeid(FunctionType2)}] = dummyMultiply;

  // When
  mult1 = Euclid::MathUtils::multiply(f1, f2);
  mult2 = Euclid::MathUtils::multiply(f2, f1);

  // Then
  BOOST_CHECK(dynamic_cast<DummyMultiplyFunction*>(mult1.get()) != nullptr);
  BOOST_CHECK(dynamic_cast<DummyMultiplyFunction*>(mult2.get()) != nullptr);

  Euclid::MathUtils::multiplySpecificSpecificMap.erase({typeid(FunctionType1), typeid(FunctionType2)});
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
