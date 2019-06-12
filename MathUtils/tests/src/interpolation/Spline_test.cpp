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
 * @file tests/src/interpolation/Spline_test.cpp
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include <boost/test/floating_point_comparison.hpp>
#include <memory>
#include <cmath>
#include "MathUtils/function/Function.h"
#include "MathUtils/interpolation/interpolation.h"

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
  auto linear = Euclid::MathUtils::interpolate(x, y, Euclid::MathUtils::InterpolationType::CUBIC_SPLINE);
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
