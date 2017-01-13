/** 
 * @file Differentiable_test.cpp
 * @date February 19, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "ChMath/function/Function.h"
#include "ChMath/function/Differentiable.h"
#include "mocks.h"

struct Differentiable_Fixture {
  double close_tolerance {1E-10};
  double small_tolerance {1E-40};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Differentiable_test)

//-----------------------------------------------------------------------------
// Test that the integration uses the indefinite integral
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Constructor, Differentiable_Fixture) {
  
  // Given
  DifferentiableMock differentiable {};
  
  // When
  double integral1 = differentiable.integrate(-1,5);
  double integral2 = differentiable.integrate(-1,15);
  double integral3 = differentiable.integrate(-1,-4);
  double integral4 = differentiable.integrate(1,5);
  
  // Then
  BOOST_CHECK_CLOSE(integral1, 1., close_tolerance);
  BOOST_CHECK_CLOSE(integral2, 1., close_tolerance);
  BOOST_CHECK_SMALL(integral3, small_tolerance);
  BOOST_CHECK_SMALL(integral4, small_tolerance);
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()