/** 
 * @file Linear_test.cpp
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include <boost/test/floating_point_comparison.hpp>
#include <memory>
#include "ChMath/function/Function.h"
#include "ChMath/interpolation/interpolation.h"

struct Linear_Fixture {
  double close_tolerance {1E-10};
  double small_tolerance {1E-20};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Linear_test)

//-----------------------------------------------------------------------------
// Test the linear interpolation
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Linear, Linear_Fixture) {
  
  // Given
  std::vector<double> x {-1.,0.,1.,2.,8.,10.};
  std::vector<double> y {4.,3.,1.,2.,2.,20.};
  
  // When
  auto linear = ChMath::linearInterpolation(x, y);
  double value1 = (*linear)(-2.);
  double value2 = (*linear)(-1.);
  double value3 = (*linear)(-.5);
  double value4 = (*linear)(0.);
  double value5 = (*linear)(1.);
  double value6 = (*linear)(1.7);
  double value7 = (*linear)(5.);
  double value8 = (*linear)(9.);
  double value9 = (*linear)(10.1);
  
  // Then
  BOOST_CHECK_SMALL(value1, small_tolerance);
  BOOST_CHECK_CLOSE(value2, 4., close_tolerance);
  BOOST_CHECK_CLOSE(value3, 3.5, close_tolerance);
  BOOST_CHECK_CLOSE(value4, 3., close_tolerance);
  BOOST_CHECK_CLOSE(value5, 1., close_tolerance);
  BOOST_CHECK_CLOSE(value6, 1.7, close_tolerance);
  BOOST_CHECK_CLOSE(value7, 2., close_tolerance);
  BOOST_CHECK_CLOSE(value8, 11., close_tolerance);
  BOOST_CHECK_SMALL(value9, small_tolerance);
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()