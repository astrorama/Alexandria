/** 
 * @file tests/src/MatrixConstructionHelper_test.cpp
 * @date July 2, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "ChMatrix/_impl/MatrixConstructionHelper.h"

struct MatrixConstructionHelper_Fixture {
  typedef ChMatrix::AxisInfo<int> IntAxis;
  IntAxis axis1 {"Axis 1", {1, 2, 3, 4, 5}};
  IntAxis axis2 {"Axis 2", {1, 2, 3}};
  IntAxis axis3 {"Axis 3", {1, 2, 3, 4, 5, 6}};
  IntAxis axis4 {"Axis 4", {1, 2}};
  std::tuple<IntAxis, IntAxis, IntAxis, IntAxis> axes_tuple {axis1, axis2, axis3, axis4};
  typedef ChMatrix::MatrixConstructionHelper<int, int, int, int> Helper;
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (MatrixConstructionHelper_test)

//-----------------------------------------------------------------------------
// Test the createAxesSizesVector method
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(createAxesSizesVector, MatrixConstructionHelper_Fixture) {
  
  // When
  std::vector<size_t> result = Helper::createAxesSizesVector(axes_tuple, ChMatrix::TemplateLoopCounter<4>{});
            
  // Then
  BOOST_CHECK_EQUAL(result.size(), 4);
  BOOST_CHECK_EQUAL(result[0], axis1.size());
  BOOST_CHECK_EQUAL(result[1], axis2.size());
  BOOST_CHECK_EQUAL(result[2], axis3.size());
  BOOST_CHECK_EQUAL(result[3], axis4.size());
}

//-----------------------------------------------------------------------------
// Test the createAxisIndexFactorVector method
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(createAxisIndexFactorVector, MatrixConstructionHelper_Fixture) {
  
  // When
  std::vector<size_t> result = Helper::createAxisIndexFactorVector(axes_tuple, ChMatrix::TemplateLoopCounter<4>{});
            
  // Then
  BOOST_CHECK_EQUAL(result.size(), 5);
  BOOST_CHECK_EQUAL(result[0], 1);
  BOOST_CHECK_EQUAL(result[1], axis1.size());
  BOOST_CHECK_EQUAL(result[2], axis1.size()*axis2.size());
  BOOST_CHECK_EQUAL(result[3], axis1.size()*axis2.size()*axis3.size());
  BOOST_CHECK_EQUAL(result[4], axis1.size()*axis2.size()*axis3.size()*axis4.size());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()