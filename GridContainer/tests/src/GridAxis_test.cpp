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
// Test the equality operators for axes with same type
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(equalityOperatorSameType) {
  
  // Given
  std::string name_1 = "Axis1";
  std::vector<double> knots_1 {{1., 2., 2.5, 3.8}};
  std::string name_2 = "Axis2";
  std::vector<double> knots_2 {{1., 2., 2.5, 3.8}};
  
  // When
  Euclid::GridContainer::GridAxis<double> axis_1 {name_1, knots_1};
  Euclid::GridContainer::GridAxis<double> axis_2 {name_2, knots_2};
  
  // Then
  BOOST_CHECK(axis_1 == axis_2);
  BOOST_CHECK(axis_2 == axis_1);
  BOOST_CHECK(!(axis_1 != axis_2));
  BOOST_CHECK(!(axis_2 != axis_1));
  
}

//-----------------------------------------------------------------------------
// Test the equality operators for axes with same type and different values
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(equalityOperatorSameTypeDifferentValues) {
  
  // Given
  std::string name_1 = "Axis1";
  std::vector<double> knots_1 {{1., 2., 2.5, 3.8}};
  std::string name_2 = "Axis2";
  std::vector<double> knots_2 {{1., 2., 3.5, 3.8}};
  
  // When
  Euclid::GridContainer::GridAxis<double> axis_1 {name_1, knots_1};
  Euclid::GridContainer::GridAxis<double> axis_2 {name_2, knots_2};
  
  // Then
  BOOST_CHECK(axis_1 != axis_2);
  BOOST_CHECK(axis_2 != axis_1);
  BOOST_CHECK(!(axis_1 == axis_2));
  BOOST_CHECK(!(axis_2 == axis_1));
  
}

//-----------------------------------------------------------------------------
// Test the equality operators for axes with same type and different size
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(equalityOperatorSameTypeDifferentSize) {
  
  // Given
  std::string name_1 = "Axis1";
  std::vector<double> knots_1 {{1., 2., 2.5, 3.8}};
  std::string name_2 = "Axis2";
  std::vector<double> knots_2 {{1., 2., 2.5, 3.8, 4.}};
  
  // When
  Euclid::GridContainer::GridAxis<double> axis_1 {name_1, knots_1};
  Euclid::GridContainer::GridAxis<double> axis_2 {name_2, knots_2};
  
  // Then
  BOOST_CHECK(axis_1 != axis_2);
  BOOST_CHECK(axis_2 != axis_1);
  BOOST_CHECK(!(axis_1 == axis_2));
  BOOST_CHECK(!(axis_2 == axis_1));
  
}

//-----------------------------------------------------------------------------
// Test the equality operators for axes with different type
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(equalityOperatorDifferentType) {
  
  // Given
  std::string name_1 = "Axis1";
  std::vector<double> knots_1 {{1., 2., 3., 4.}};
  std::string name_2 = "Axis2";
  std::vector<int> knots_2 {{1, 2, 3, 4}};
  
  // When
  Euclid::GridContainer::GridAxis<double> axis_1 {name_1, knots_1};
  Euclid::GridContainer::GridAxis<int> axis_2 {name_2, knots_2};
  
  // Then
  BOOST_CHECK(axis_1 == axis_2);
  BOOST_CHECK(axis_2 == axis_1);
  BOOST_CHECK(!(axis_1 != axis_2));
  BOOST_CHECK(!(axis_2 != axis_1));
  
}

//-----------------------------------------------------------------------------
// Test the equality operators for axes with different type and different values
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(equalityOperatorDifferentTypeDifferentValues) {
  
  // Given
  std::string name_1 = "Axis1";
  std::vector<double> knots_1 {{1., 2., 3.5, 4.}};
  std::string name_2 = "Axis2";
  std::vector<int> knots_2 {{1, 2, 3, 4}};
  
  // When
  Euclid::GridContainer::GridAxis<double> axis_1 {name_1, knots_1};
  Euclid::GridContainer::GridAxis<int> axis_2 {name_2, knots_2};
  
  // Then
  BOOST_CHECK(axis_1 != axis_2);
  BOOST_CHECK(axis_2 != axis_1);
  BOOST_CHECK(!(axis_1 == axis_2));
  BOOST_CHECK(!(axis_2 == axis_1));
  
}

//-----------------------------------------------------------------------------
// Test the equality operators for axes with different type and different size
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(equalityOperatorDifferentTypeDifferentSize) {
  
  // Given
  std::string name_1 = "Axis1";
  std::vector<double> knots_1 {{1., 2., 3., 4.}};
  std::string name_2 = "Axis2";
  std::vector<int> knots_2 {{1, 2, 3, 4, 5}};
  
  // When
  Euclid::GridContainer::GridAxis<double> axis_1 {name_1, knots_1};
  Euclid::GridContainer::GridAxis<int> axis_2 {name_2, knots_2};
  
  // Then
  BOOST_CHECK(axis_1 != axis_2);
  BOOST_CHECK(axis_2 != axis_1);
  BOOST_CHECK(!(axis_1 == axis_2));
  BOOST_CHECK(!(axis_2 == axis_1));
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
