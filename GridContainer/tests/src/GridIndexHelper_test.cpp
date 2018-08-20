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
 * @file tests/src/GridIndexHelper_test.cpp
 * @date July 3, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "ElementsKernel/Exception.h"
#include "GridContainer/GridIndexHelper.h"

struct GridIndexHelper_Fixture {
  typedef Euclid::GridContainer::GridAxis<int> IntAxis;
  IntAxis axis1 {"Axis 1", {1, 2, 3, 4, 5}};
  IntAxis axis2 {"Axis 2", {1, 2, 3}};
  IntAxis axis3 {"Axis 3", {1, 2, 3, 4, 5, 6}};
  IntAxis axis4 {"Axis 4", {1, 2}};
  std::tuple<IntAxis, IntAxis, IntAxis, IntAxis> axes_tuple {axis1, axis2, axis3, axis4};
  size_t total_size = axis1.size() * axis2.size() * axis3.size() * axis4.size();
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (GridIndexHelper_test)

//-----------------------------------------------------------------------------
// Test the axisIndex method
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(axisIndex, GridIndexHelper_Fixture) {
  
  // When
  auto helper = Euclid::GridContainer::makeGridIndexHelper(axes_tuple);
            
  // Then
  size_t array_index {0};
  for (size_t coord4=0; coord4<axis4.size(); ++coord4) {
    for (size_t coord3=0; coord3<axis3.size(); ++coord3) {
      for (size_t coord2=0; coord2<axis2.size(); ++coord2) {
        for (size_t coord1=0; coord1<axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(helper.axisIndex(0, array_index), coord1);
          BOOST_CHECK_EQUAL(helper.axisIndex(1, array_index), coord2);
          BOOST_CHECK_EQUAL(helper.axisIndex(2, array_index), coord3);
          BOOST_CHECK_EQUAL(helper.axisIndex(3, array_index), coord4);
          ++array_index;
        }
      }
    }
  }
  
}

//-----------------------------------------------------------------------------
// Test the totalIndex method
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(totalIndex, GridIndexHelper_Fixture) {
  
  // When
  auto helper = Euclid::GridContainer::makeGridIndexHelper(axes_tuple);
            
  // Then
  size_t array_index {0};
  for (size_t coord4=0; coord4<axis4.size(); ++coord4) {
    for (size_t coord3=0; coord3<axis3.size(); ++coord3) {
      for (size_t coord2=0; coord2<axis2.size(); ++coord2) {
        for (size_t coord1=0; coord1<axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(helper.totalIndex(coord1, coord2, coord3, coord4), array_index);
          ++array_index;
        }
      }
    }
  }
  
}

//-----------------------------------------------------------------------------
// Test the totalIndexChecked method
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(totalIndexChecked, GridIndexHelper_Fixture) {
  
  // When
  auto helper = Euclid::GridContainer::makeGridIndexHelper(axes_tuple);
            
  // Then
  size_t array_index {0};
  for (size_t coord4=0; coord4<axis4.size(); ++coord4) {
    for (size_t coord3=0; coord3<axis3.size(); ++coord3) {
      for (size_t coord2=0; coord2<axis2.size(); ++coord2) {
        for (size_t coord1=0; coord1<axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(helper.totalIndexChecked(coord1, coord2, coord3, coord4), array_index);
          ++array_index;
        }
      }
    }
  }
  
}

//-----------------------------------------------------------------------------
// Test the totalIndexChecked method throws out of bound exception
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(totalIndexCheckedOutOfBounds, GridIndexHelper_Fixture) {
  
  // When
  auto helper = Euclid::GridContainer::makeGridIndexHelper(axes_tuple);
            
  // Then
  BOOST_CHECK_THROW(helper.totalIndexChecked(axis1.size(), 0, 0, 0), Elements::Exception);
  BOOST_CHECK_THROW(helper.totalIndexChecked(0, axis2.size(), 0, 0), Elements::Exception);
  BOOST_CHECK_THROW(helper.totalIndexChecked(0, 0, axis3.size(), 0), Elements::Exception);
  BOOST_CHECK_THROW(helper.totalIndexChecked(0, 0, 0, axis4.size()), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()