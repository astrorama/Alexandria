/** 
 * @file tests/src/function/Piecewise_test.cpp
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "ElementsKernel/Exception.h"
#include <memory>
#include "MathUtils/function/Function.h"
#include "MathUtils/function/Integrable.h"
#include "MathUtils/function/Piecewise.h"
#include "mocks.h"

struct Piecewise_Fixture {
  double close_tolerance {1E-10};
  double small_tolerance {1E-20};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Piecewise_test)

//-----------------------------------------------------------------------------
// Test that the constructor sets the knots and the functions correctly
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Constructor, Piecewise_Fixture) {
  
  // Given
  std::vector<double> knots {-1.,-0.5,0.25,10.};
  std::vector<std::shared_ptr<Euclid::ChMath::Function> > functions {};
  for (double knot : knots) {
    functions.push_back(std::shared_ptr<Euclid::ChMath::Function>(new IntegrableMock(knot)));
  }
  functions.pop_back();
  
  // When
  Euclid::ChMath::Piecewise piecewise{knots, functions};
  auto resKnots = piecewise.getKnots();
  auto resFuncs = piecewise.getFunctions();
  
  // Then
  BOOST_CHECK_EQUAL_COLLECTIONS(resKnots.begin(), resKnots.end(), knots.begin(), knots.end());
  BOOST_CHECK_EQUAL_COLLECTIONS(resFuncs.begin(), resFuncs.end(), functions.begin(), functions.end());
  
}

//-----------------------------------------------------------------------------
// Test that the construction fails if knots are not ordered
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorUnorderedKnots, Piecewise_Fixture) {
  
  // Given
  std::vector<double> knots {-1.,0.5,0.25,10.};
  std::vector<std::shared_ptr<Euclid::ChMath::Function> > functions {};
  for (double knot : knots) {
    functions.push_back(std::shared_ptr<Euclid::ChMath::Function>(new IntegrableMock(knot)));
  }
  functions.pop_back();
  
  // Then
  BOOST_CHECK_THROW(Euclid::ChMath::Piecewise(knots, functions), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test that the construction fails if vector sizes are wrong
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorWrongSizes, Piecewise_Fixture) {
  
  // Given
  std::vector<double> knots {-1.,-0.5,0.25,10.};
  std::vector<std::shared_ptr<Euclid::ChMath::Function> > functions {};
  for (double knot : knots) {
    functions.push_back(std::shared_ptr<Euclid::ChMath::Function>(new IntegrableMock(knot)));
  }
  
  // Then
  BOOST_CHECK_THROW(Euclid::ChMath::Piecewise(knots, functions), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test that the clone works correctly
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Clone, Piecewise_Fixture) {
  
  // Given
  std::vector<double> knots {-1.,-0.5,0.25,10.};
  std::vector<std::shared_ptr<Euclid::ChMath::Function> > functions {};
  for (double knot : knots) {
    functions.push_back(std::shared_ptr<Euclid::ChMath::Function>(new IntegrableMock(knot)));
  }
  functions.pop_back();
  Euclid::ChMath::Piecewise piecewise{knots, functions};
  
  // When
  auto clonePtr = piecewise.clone();
  
  // Then
  BOOST_CHECK(clonePtr);
  Euclid::ChMath::Piecewise* resPiece = dynamic_cast<Euclid::ChMath::Piecewise*>(clonePtr.get());
  BOOST_CHECK(resPiece);
  auto resKnots = resPiece->getKnots();
  auto resFuncs = resPiece->getFunctions();
  BOOST_CHECK_EQUAL_COLLECTIONS(resKnots.begin(), resKnots.end(), knots.begin(), knots.end());
  BOOST_CHECK_EQUAL_COLLECTIONS(resFuncs.begin(), resFuncs.end(), functions.begin(), functions.end());
  
}

//-----------------------------------------------------------------------------
// Test that the piecewise works as a function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(FunctionOperator, Piecewise_Fixture) {
  
  // Given
  std::vector<double> knots {-1.,-0.5,0.25,10.};
  std::vector<std::shared_ptr<Euclid::ChMath::Function> > functions {};
  for (double knot : knots) {
    functions.push_back(std::shared_ptr<Euclid::ChMath::Function>(new IntegrableMock(knot)));
  }
  functions.pop_back();
  
  // When
  Euclid::ChMath::Piecewise piecewise{knots, functions};
  
  // Then
  BOOST_CHECK_SMALL(piecewise(-2.), small_tolerance);
  BOOST_CHECK_CLOSE(piecewise(-1.), -1., close_tolerance);
  BOOST_CHECK_CLOSE(piecewise(-.75), -1., close_tolerance);
  BOOST_CHECK_CLOSE(piecewise(-.5), -1., close_tolerance);
  BOOST_CHECK_CLOSE(piecewise(0.), -.5, close_tolerance);
  BOOST_CHECK_CLOSE(piecewise(.25), -.5, close_tolerance);
  BOOST_CHECK_CLOSE(piecewise(5.), .25, close_tolerance);
  BOOST_CHECK_CLOSE(piecewise(10.), .25, close_tolerance);
  BOOST_CHECK_SMALL(piecewise(11.), small_tolerance);
  
}

//-----------------------------------------------------------------------------
// Test that the integration works inside the range of the function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(IntegrateInRange, Piecewise_Fixture) {
  
  // Given
  std::vector<double> knots {-1.,0.,1.,2.};
  std::vector<std::shared_ptr<Euclid::ChMath::Function> > functions {};
  functions.push_back(std::shared_ptr<Euclid::ChMath::Function>(new IntegrableMock(1.)));
  functions.push_back(std::shared_ptr<Euclid::ChMath::Function>(new IntegrableMock(2.)));
  functions.push_back(std::shared_ptr<Euclid::ChMath::Function>(new IntegrableMock(1.)));
  Euclid::ChMath::Piecewise piecewise{knots, functions};
  
  // When
  double integral1 = piecewise.integrate(-1., 2.);
  double integral2 = piecewise.integrate(-.5, .5);
  double integral3 = piecewise.integrate(-.5, 1.5);
  double integral4 = piecewise.integrate(0., 1.);
  double integral5 = piecewise.integrate(.5, .5);
  double integral6 = piecewise.integrate(0., 0.);
  double integral7 = piecewise.integrate(2., -1.);
  double integral8 = piecewise.integrate(.5, -.5);
  double integral9 = piecewise.integrate(1.5, -.5);
  double integral10 = piecewise.integrate(1., 0.);
  
  // Then
  BOOST_CHECK_CLOSE(integral1, 4., close_tolerance);
  BOOST_CHECK_CLOSE(integral2, 1.5, close_tolerance);
  BOOST_CHECK_CLOSE(integral3, 3., close_tolerance);
  BOOST_CHECK_CLOSE(integral4, 2., close_tolerance);
  BOOST_CHECK_SMALL(integral5, small_tolerance);
  BOOST_CHECK_SMALL(integral6, small_tolerance);
  BOOST_CHECK_CLOSE(integral7, -4., close_tolerance);
  BOOST_CHECK_CLOSE(integral8, -1.5, close_tolerance);
  BOOST_CHECK_CLOSE(integral9, -3., close_tolerance);
  BOOST_CHECK_CLOSE(integral10, -2., close_tolerance);
  
}

//-----------------------------------------------------------------------------
// Test that the integration works outside the range of the function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(IntegrateOutOfRange, Piecewise_Fixture) {
  
  // Given
  std::vector<double> knots {-1.,0.,1.,2.};
  std::vector<std::shared_ptr<Euclid::ChMath::Function> > functions {};
  functions.push_back(std::shared_ptr<Euclid::ChMath::Function>(new IntegrableMock(1.)));
  functions.push_back(std::shared_ptr<Euclid::ChMath::Function>(new IntegrableMock(2.)));
  functions.push_back(std::shared_ptr<Euclid::ChMath::Function>(new IntegrableMock(1.)));
  Euclid::ChMath::Piecewise piecewise{knots, functions};
  
  // When
  double integral1 = piecewise.integrate(-5., 10.);
  double integral2 = piecewise.integrate(-5., .5);
  double integral3 = piecewise.integrate(.5, 10.);
  double integral4 = piecewise.integrate(-5., -4.);
  double integral5 = piecewise.integrate(8., 9.);
  
  // Then
  BOOST_CHECK_CLOSE(integral1, 4., close_tolerance);
  BOOST_CHECK_CLOSE(integral2, 2., close_tolerance);
  BOOST_CHECK_CLOSE(integral3, 2., close_tolerance);
  BOOST_CHECK_SMALL(integral4, small_tolerance);
  BOOST_CHECK_SMALL(integral5, small_tolerance);
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()