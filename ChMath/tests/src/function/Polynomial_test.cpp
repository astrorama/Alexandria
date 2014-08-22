/** 
 * @file tests/src/function/Polynomial_test.cpp
 * @date February 19, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include <boost/test/floating_point_comparison.hpp>
#include <boost/test/test_tools.hpp>
#include <memory>
#include "ChMath/function/Polynomial.h"

struct Polynomial_Fixture {
  double close_tolerance {1E-10};
  double small_tolerance {1E-20};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Polynomial_test)

//-----------------------------------------------------------------------------
// Test that the constructor sets the coefficients correctly
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Constructor, Polynomial_Fixture) {
  
  // Given
  std::vector<double> coef {2.5, 0.8, -1.3, 0.02};
  Euclid::ChMath::Polynomial polynomial {coef};
  
  // When
  std::vector<double> resCoef = polynomial.getCoefficients();
  
  // Then
  BOOST_CHECK_EQUAL_COLLECTIONS(resCoef.begin(), resCoef.end(), coef.begin(), coef.end());
  
}

//-----------------------------------------------------------------------------
// Test that the clone works correctly
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Clone, Polynomial_Fixture) {
  
  // Given
  std::vector<double> coef {2.5, 0.8, -1.3, 0.02};
  Euclid::ChMath::Polynomial polynomial {coef};
  
  // When
  auto clonePtr = polynomial.clone();
  
  // Then
  BOOST_CHECK(clonePtr);
  Euclid::ChMath::Polynomial* resPol = dynamic_cast<Euclid::ChMath::Polynomial*>(clonePtr.get());
  BOOST_CHECK(resPol);
  std::vector<double> resCoef = resPol->getCoefficients();
  BOOST_CHECK_EQUAL_COLLECTIONS(resCoef.begin(), resCoef.end(), coef.begin(), coef.end());
  
}

//-----------------------------------------------------------------------------
// Test that the polynomial works correctly as a function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(FunctionOperator, Polynomial_Fixture) {

  // Given
  std::vector<double> coef {2.5, 0.8, -1.3, 0.02};
  Euclid::ChMath::Polynomial polynomial {coef};
  
  for (double x=-10.; x <=10.; x+=0.1) {
    
    // When
    double expected = 2.5 + 0.8*x -1.3*x*x + 0.02*x*x*x;
    double polValue = polynomial(x);
    
    // Then
    if (polValue == 0 || expected == 0) {
      BOOST_CHECK_SMALL(polValue+expected, small_tolerance);
    } else {
      BOOST_CHECK_CLOSE(polValue, expected, close_tolerance);
    }
  }

}

//-----------------------------------------------------------------------------
// Test the derivative
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Derivative, Polynomial_Fixture) {
  
  // Given
  std::vector<double> polCoef {2.5, 0.8, -1.3, 0.02};
  std::vector<double> expectedCoef {0.8, -2.6, 0.06};
  Euclid::ChMath::Polynomial polynomial {polCoef};
  
  // When
  auto derivative = std::dynamic_pointer_cast<Euclid::ChMath::Polynomial>(polynomial.derivative());
  
  // Then
  BOOST_CHECK(derivative);
  std::vector<double> derCoef = derivative->getCoefficients();
  BOOST_CHECK_EQUAL_COLLECTIONS(derCoef.begin(), derCoef.end(), expectedCoef.begin(), expectedCoef.end());
}

//-----------------------------------------------------------------------------
// Test the indefinite integral
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(IndefiniteIntegral, Polynomial_Fixture) {
  
  // Given
  std::vector<double> polCoef {2.5, 0.8, -1.5, 0.02};
  std::vector<double> expectedCoef {0., 2.5, 0.4, -0.5, 0.005};
  Euclid::ChMath::Polynomial polynomial {polCoef};
  
  // When
  auto indefiniteIntegral = std::dynamic_pointer_cast<Euclid::ChMath::Polynomial>(polynomial.indefiniteIntegral());
  
  // Then
  BOOST_CHECK(indefiniteIntegral);
  std::vector<double> indefIntCoef = indefiniteIntegral->getCoefficients();
  BOOST_CHECK_EQUAL_COLLECTIONS(indefIntCoef.begin(), indefIntCoef.end(), expectedCoef.begin(), expectedCoef.end());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()