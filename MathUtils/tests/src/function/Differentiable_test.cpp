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
 * @file tests/src/function/Differentiable_test.cpp
 * @date February 19, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "MathUtils/function/Function.h"
#include "MathUtils/function/Differentiable.h"
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