/** 
 * @file tests/src/MatrixIndexHelper_test.cpp
 * @date July 3, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "ChMatrix/MatrixIndexHelper.h"

#include <iostream>

struct MatrixIndexHelper_Fixture {
  typedef ChMatrix::AxisInfo<int> IntAxis;
  IntAxis axis1 {"Axis 1", {1, 2, 3, 4, 5}};
  IntAxis axis2 {"Axis 2", {1, 2, 3}};
  IntAxis axis3 {"Axis 3", {1, 2, 3, 4, 5, 6}};
  IntAxis axis4 {"Axis 4", {1, 2}};
  std::tuple<IntAxis, IntAxis, IntAxis, IntAxis> axes_tuple {axis1, axis2, axis3, axis4};
  size_t total_size = axis1.size() * axis2.size() * axis3.size() * axis4.size();
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (MatrixInstructionHelper_test)

//-----------------------------------------------------------------------------
// Test the axisIndex method
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(axisIndex, MatrixIndexHelper_Fixture) {
  
  // When
  auto helper = ChMatrix::makeMatrixIndexHelper(axes_tuple);
            
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
    
BOOST_FIXTURE_TEST_CASE(totalIndex, MatrixIndexHelper_Fixture) {
  
  // When
  auto helper = ChMatrix::makeMatrixIndexHelper(axes_tuple);
            
  // Then
  size_t array_index {0};
  for (size_t coord4=0; coord4<axis4.size(); ++coord4) {
    for (size_t coord3=0; coord3<axis3.size(); ++coord3) {
      for (size_t coord2=0; coord2<axis2.size(); ++coord2) {
        for (size_t coord1=0; coord1<axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(helper.totalIndex({coord1, coord2, coord3, coord4}), array_index);
          ++array_index;
        }
      }
    }
  }
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()