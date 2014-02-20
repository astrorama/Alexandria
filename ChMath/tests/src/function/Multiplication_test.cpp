/** 
 * @file Multiplication_test.cpp
 * @date February 19, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include <boost/test/test_tools.hpp>
#include <memory>
#include "ChMath/function/function_tools.h"
#include "ChMath/function/Polynomial.h"
#include "ChMath/function/Piecewise.h"
#include "mocks.h"

struct Multiplication_Fixture {
  double close_tolerance {1E-10};
  double small_tolerance {1E-20};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Multiplication_test)

//-----------------------------------------------------------------------------
// Test multiplication between two polynomials
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(PolynomialWithPolynomial, Multiplication_Fixture) {
  
  // Given
  ChMath::Polynomial p1 {{1., 0.5, -2.}};
  ChMath::Polynomial p2 {{3., 0., 2.}};
  std::vector<double> expectedCoef {3., 1.5, -4., 1., -4.};
  
  // When
  auto multPointer = ChMath::multiply(p1, p2);
  
  // Then
  BOOST_CHECK(multPointer);
  ChMath::Polynomial* polPointer = dynamic_cast<ChMath::Polynomial*>(multPointer.get());
  BOOST_CHECK(polPointer);
  std::vector<double> multCoef = polPointer->getCoefficients();
  BOOST_CHECK_EQUAL_COLLECTIONS(multCoef.begin(), multCoef.end(), expectedCoef.begin(), expectedCoef.end());
}

//-----------------------------------------------------------------------------
// Test multiplication between a piecewise and a generic
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(PiecewiseWithGeneric, Multiplication_Fixture) {
  
  // Given
  std::vector<double> knots {-1.,0.,1.,2.};
  std::vector<std::shared_ptr<ChMath::Function> > functions {};
  functions.push_back(std::shared_ptr<ChMath::Function>(new IntegrableMock(1.)));
  functions.push_back(std::shared_ptr<ChMath::Function>(new IntegrableMock(2.)));
  functions.push_back(std::shared_ptr<ChMath::Function>(new IntegrableMock(1.)));
  ChMath::Piecewise piecewise{knots, functions};
  IntegrableMock generic {5.};
  
  // When
  auto multPointer = ChMath::multiply(piecewise, generic);
  double value1 = (*multPointer)(-2.);
  double value2 = (*multPointer)(-1.);
  double value3 = (*multPointer)(-.5);
  double value4 = (*multPointer)(0.);
  double value5 = (*multPointer)(.5);
  double value6 = (*multPointer)(1.);
  double value7 = (*multPointer)(1.5);
  double value8 = (*multPointer)(2.);
  double value9 = (*multPointer)(2.5);
  
  // Then
  BOOST_CHECK(multPointer);
  ChMath::Piecewise* piecePointer = dynamic_cast<ChMath::Piecewise*>(multPointer.get());
  BOOST_CHECK(piecePointer);
  BOOST_CHECK_CLOSE(value1, 0., close_tolerance);
  BOOST_CHECK_CLOSE(value2, 5., close_tolerance);
  BOOST_CHECK_CLOSE(value3, 5., close_tolerance);
  BOOST_CHECK_CLOSE(value4, 5., close_tolerance);
  BOOST_CHECK_CLOSE(value5, 10., close_tolerance);
  BOOST_CHECK_CLOSE(value6, 10., close_tolerance);
  BOOST_CHECK_CLOSE(value7, 5., close_tolerance);
  BOOST_CHECK_CLOSE(value8, 5., close_tolerance);
  BOOST_CHECK_CLOSE(value9, 0., close_tolerance);
}

//-----------------------------------------------------------------------------
// Test multiplication between two piecewises
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(PiecewiseWithPiecewise, Multiplication_Fixture) {
  
  // Given
  std::vector<double> knots1 {-1.,0.,1.,2.};
  std::vector<std::shared_ptr<ChMath::Function> > functions1 {};
  functions1.push_back(std::shared_ptr<ChMath::Function>(new IntegrableMock(1.)));
  functions1.push_back(std::shared_ptr<ChMath::Function>(new IntegrableMock(2.)));
  functions1.push_back(std::shared_ptr<ChMath::Function>(new IntegrableMock(1.)));
  ChMath::Piecewise p1{knots1, functions1};
  std::vector<double> knots2 {.5,.7,1.,1.5,4.,6};
  std::vector<std::shared_ptr<ChMath::Function> > functions2 {};
  functions2.push_back(std::shared_ptr<ChMath::Function>(new IntegrableMock(3.)));
  functions2.push_back(std::shared_ptr<ChMath::Function>(new IntegrableMock(2.)));
  functions2.push_back(std::shared_ptr<ChMath::Function>(new IntegrableMock(1.)));
  functions2.push_back(std::shared_ptr<ChMath::Function>(new IntegrableMock(3.)));
  functions2.push_back(std::shared_ptr<ChMath::Function>(new IntegrableMock(4.)));
  ChMath::Piecewise p2{knots2, functions2};
  
  // When
  auto multPointer = ChMath::multiply(p1, p2);
  double value1 = (*multPointer)(0.);
  double value2 = (*multPointer)(.5);
  double value3 = (*multPointer)(.6);
  double value4 = (*multPointer)(.7);
  double value5 = (*multPointer)(.88);
  double value6 = (*multPointer)(1.);
  double value7 = (*multPointer)(1.3);
  double value8 = (*multPointer)(1.5);
  double value9 = (*multPointer)(2.);
  
  // Then
  BOOST_CHECK(multPointer);
  ChMath::Piecewise* piecePointer = dynamic_cast<ChMath::Piecewise*>(multPointer.get());
  BOOST_CHECK(piecePointer);
  auto resKnots = piecePointer->getKnots();
  std::vector<double> expectedKnots {.5,.7,1.,1.5,2.};
  BOOST_CHECK_EQUAL_COLLECTIONS(resKnots.begin(), resKnots.end(), expectedKnots.begin(), expectedKnots.end());
  BOOST_CHECK_CLOSE(value1, 0., close_tolerance);
  BOOST_CHECK_CLOSE(value2, 6., close_tolerance);
  BOOST_CHECK_CLOSE(value3, 6., close_tolerance);
  BOOST_CHECK_CLOSE(value4, 6., close_tolerance);
  BOOST_CHECK_CLOSE(value5, 4., close_tolerance);
  BOOST_CHECK_CLOSE(value6, 4., close_tolerance);
  BOOST_CHECK_CLOSE(value7, 1., close_tolerance);
  BOOST_CHECK_CLOSE(value8, 1., close_tolerance);
  BOOST_CHECK_CLOSE(value9, 3., close_tolerance);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()