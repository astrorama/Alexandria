/** 
 * @file tests/src/function/function_tools_test.cpp
 * @date February 19, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "ElementsKernel/ElementsException.h"
#include "ChMath/function/function_tools.h"
#include "ChMath/function/Function.h"
#include "ChMath/function/Integrable.h"
#include "ChMath/function/multiplication.h"
#include "mocks.h"

class DummyMultiplyFunction : public ChMath::Function {
  double operator()(const double) const {
    return 0;
  }
  std::unique_ptr<Function> clone() const override {
    return std::unique_ptr<Function> {new DummyMultiplyFunction{}};
  }
};

std::unique_ptr<ChMath::Function> dummyMultiply(const ChMath::Function&, const ChMath::Function&) {
  return std::unique_ptr<ChMath::Function>(new DummyMultiplyFunction {});
}

class FunctionType1 : public ChMath::Function {
  double operator()(const double) const {
    return 0;
  }
  std::unique_ptr<Function> clone() const override {
    return std::unique_ptr<Function> {new FunctionType1{}};
  }
};

class FunctionType2 : public ChMath::Function {
  double operator()(const double) const {
    return 0;
  }
  std::unique_ptr<Function> clone() const override {
    return std::unique_ptr<Function> {new FunctionType2{}};
  }
};

struct Function_Tools_Fixture {
  double close_tolerance {1E-10};
  double small_tolerance {1E-20};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (function_tools_test)

//-----------------------------------------------------------------------------
// Test that integration of a non-integrable function throws an exception
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(NonIntegrableIntegration) {
  
  // Given
  FunctionMock f = FunctionMock{0.};
  
  // Then
  BOOST_CHECK_THROW(ChMath::integrate(f,0,1), ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test that integration of an integrable function delegates the call
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(IntegrableIntegration) {
  
  // Given
  double min = -1.5;
  double max = 7.32;
  IntegrableMock f = IntegrableMock{5.};
  double expected = 5. * (max - min);
  
  // When
  double integral = ChMath::integrate(f, min, max);
  
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
  FunctionMock f1 {4.};
  FunctionMock f2 {3.};
  
  // When
  auto multiplication = ChMath::multiply(f1, f2);
  
  // Then
  BOOST_CHECK_CLOSE((*multiplication)(15.), 12., close_tolerance);
  
}

//-----------------------------------------------------------------------------
// Test multiplication function selection between a specific and a generic function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(SpecificGenericMultiplication, Function_Tools_Fixture) {
  
  // Given
  FunctionType1 f1 {};
  FunctionType2 f2 {};
  
  // When
  auto mult1 = ChMath::multiply(f1, f2);
  auto mult2 = ChMath::multiply(f2, f1);
  
  // Then
  BOOST_CHECK(typeid(*mult1) != typeid(DummyMultiplyFunction));
  BOOST_CHECK(typeid(*mult2) != typeid(DummyMultiplyFunction));
  
  // Given
  ChMath::multiplySpecificGenericMap[typeid(FunctionType1)] = dummyMultiply;
  
  // When
  mult1 = ChMath::multiply(f1, f2);
  mult2 = ChMath::multiply(f2, f1);
  
  // Then
  BOOST_CHECK(typeid(*mult1) == typeid(DummyMultiplyFunction));
  BOOST_CHECK(typeid(*mult2) == typeid(DummyMultiplyFunction));
  
  ChMath::multiplySpecificGenericMap.erase(typeid(FunctionType1));
  
}

//-----------------------------------------------------------------------------
// Test multiplication function selection between two specific functions
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(SpecificSpecificMultiplication, Function_Tools_Fixture) {
  
  // Given
  FunctionType1 f1 {};
  FunctionType2 f2 {};
  
  // When
  auto mult1 = ChMath::multiply(f1, f2);
  auto mult2 = ChMath::multiply(f2, f1);
  
  // Then
  BOOST_CHECK(typeid(*mult1) != typeid(DummyMultiplyFunction));
  BOOST_CHECK(typeid(*mult2) != typeid(DummyMultiplyFunction));
  
  // Given
  ChMath::multiplySpecificSpecificMap[{typeid(FunctionType1),typeid(FunctionType2)}] = dummyMultiply;
  
  // When
  mult1 = ChMath::multiply(f1, f2);
  mult2 = ChMath::multiply(f2, f1);
  
  // Then
  BOOST_CHECK(typeid(*mult1) == typeid(DummyMultiplyFunction));
  BOOST_CHECK(typeid(*mult2) == typeid(DummyMultiplyFunction));
  
  ChMath::multiplySpecificSpecificMap.erase({typeid(FunctionType1),typeid(FunctionType2)});
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()