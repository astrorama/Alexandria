/** 
 * @file tests/src/interpolation/Spline_test.cpp
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include <boost/test/floating_point_comparison.hpp>
#include <memory>
#include <cmath>
#include "ChMath/function/Function.h"
#include "ChMath/interpolation/interpolation.h"

struct Spline_Fixture {
  double close_tolerance {1.2E-2};
  double small_tolerance {1E-20};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Spline_test)

//-----------------------------------------------------------------------------
// Test the spline interpolation
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Spline, Spline_Fixture) {
  
  // Given
  std::vector<double> x {};
  std::vector<double> y {};
  for (double xValue=-10.; xValue<=10.; xValue+=0.1) {
    x.push_back(xValue);
    y.push_back(sin(xValue));
  }
  
  // When
  auto linear = ChMath::interpolate(x, y, ChMath::InterpolationType::CUBIC_SPLINE);
  std::vector<double> result {};
  for (double xValue : x) {
    result.push_back((*linear)(xValue));
  }
  double outside1 = (*linear)(-11.);
  double outside2 = (*linear)(11.);
  
  // Then
  for (size_t i=0; i< y.size(); i++) {
    BOOST_CHECK_CLOSE(result[i], y[i], close_tolerance);
  }
  BOOST_CHECK_SMALL(outside1, small_tolerance);
  BOOST_CHECK_SMALL(outside2, small_tolerance);
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
