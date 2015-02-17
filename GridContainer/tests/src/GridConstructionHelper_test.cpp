/** 
 * @file tests/src/GridConstructionHelper_test.cpp
 * @date July 2, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "GridContainer/_impl/GridConstructionHelper.h"

struct GridConstructionHelper_Fixture {
  typedef Euclid::GridContainer::GridAxis<int> IntAxis;
  IntAxis axis1 {"Axis 1", {1, 2, 3, 4, 5}};
  IntAxis axis2 {"Axis 2", {1, 2, 3}};
  IntAxis axis3 {"Axis 3", {1, 2, 3, 4, 5, 6}};
  IntAxis axis4 {"Axis 4", {1, 2}};
  std::tuple<IntAxis, IntAxis, IntAxis, IntAxis> axes_tuple {axis1, axis2, axis3, axis4};
  typedef Euclid::GridContainer::GridConstructionHelper<int, int, int, int> Helper;
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (GridConstructionHelper_test)

//-----------------------------------------------------------------------------
// Test the createAxesSizesVector method
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(createAxesSizesVector, GridConstructionHelper_Fixture) {
  
  // When
  std::vector<size_t> result = Helper::createAxesSizesVector(axes_tuple, Euclid::GridContainer::TemplateLoopCounter<4>{});
            
  // Then
  BOOST_CHECK_EQUAL(result.size(), 4u);
  BOOST_CHECK_EQUAL(result[0], axis1.size());
  BOOST_CHECK_EQUAL(result[1], axis2.size());
  BOOST_CHECK_EQUAL(result[2], axis3.size());
  BOOST_CHECK_EQUAL(result[3], axis4.size());
}

//-----------------------------------------------------------------------------
// Test the createAxisIndexFactorVector method
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(createAxisIndexFactorVector, GridConstructionHelper_Fixture) {
  
  // When
  std::vector<size_t> result = Helper::createAxisIndexFactorVector(axes_tuple, Euclid::GridContainer::TemplateLoopCounter<4>{});
            
  // Then
  BOOST_CHECK_EQUAL(result.size(), 5u);
  BOOST_CHECK_EQUAL(result[0], 1u);
  BOOST_CHECK_EQUAL(result[1], axis1.size());
  BOOST_CHECK_EQUAL(result[2], axis1.size()*axis2.size());
  BOOST_CHECK_EQUAL(result[3], axis1.size()*axis2.size()*axis3.size());
  BOOST_CHECK_EQUAL(result[4], axis1.size()*axis2.size()*axis3.size()*axis4.size());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
