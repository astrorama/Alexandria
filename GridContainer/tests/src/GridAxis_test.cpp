/** 
 * @file tests/src/GridAxis_test.cpp
 * @date June 16, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "GridContainer/GridAxis.h"

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (GridAxis_test)

//-----------------------------------------------------------------------------
// Test the name is set correctly
//-----------------------------------------------------------------------------
    
BOOST_AUTO_TEST_CASE(name) {
  
  // Given
  std::string name = "AxisName";
  std::vector<double> knots {};
  Euclid::GridContainer::GridAxis<double> axis {name, knots};
  
  // When
  auto& result = axis.name();
  
  // Then
  BOOST_CHECK_EQUAL(result, name);
  
}

//-----------------------------------------------------------------------------
// Test the number of knots is counted correctly
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(size) {
  
  // Given
  std::string name = "AxisName";
  std::vector<double> knots {{1., 2., 2.5, 3.8}};
  Euclid::GridContainer::GridAxis<double> axis {name, knots};
  
  // When
  auto size = axis.size();
  
  // Then
  BOOST_CHECK_EQUAL(size, knots.size());
  
}

//-----------------------------------------------------------------------------
// Test the iterator
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(iterator) {
  
  // Given
  std::string name = "AxisName";
  std::vector<double> knots {{1., 2., 2.5, 3.8}};
  Euclid::GridContainer::GridAxis<double> axis {name, knots};
  
  // When
  auto axis_iter = axis.begin();
  auto axis_end = axis.end();
  auto knots_iter = knots.begin();
  
  // Then
  while (axis_iter != axis_end) {
    BOOST_CHECK_EQUAL(*axis_iter, *knots_iter);
    ++axis_iter;
    ++ knots_iter;
  }
  
}

//-----------------------------------------------------------------------------
// Test knot access based on index
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(indexAccess) {
  
  // Given
  std::string name = "AxisName";
  std::vector<double> knots {{1., 2., 2.5, 3.8}};
  Euclid::GridContainer::GridAxis<double> axis {name, knots};
  
  // When
  auto axis_iter = axis.begin();
  auto axis_end = axis.end();
  auto knots_iter = knots.begin();
  
  // Then
  while (axis_iter != axis_end) {
    BOOST_CHECK_EQUAL(*axis_iter, *knots_iter);
    ++axis_iter;
    ++ knots_iter;
  }
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
