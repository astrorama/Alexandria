/** 
 * @file FilterName_test.cpp
 * @date January 17, 2014
 * @author Nikolaos Apostolakos
 */

#include <string>
#include <boost/test/unit_test.hpp>

#include "ChDataModel/FilterName.h"

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (FilterName_test)

//-----------------------------------------------------------------------------
// Check group, name and qualifiedName methods work
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(nameMethods_test) {
  
  // Given
  std::string group = "TestGroup";
  std::string name = "TestName";
  
  // When
  ChDataModel::FilterName filterName {group, name};
  
  // Then
  BOOST_CHECK_EQUAL(filterName.group(), group);
  BOOST_CHECK_EQUAL(filterName.name(), name);
  BOOST_CHECK_EQUAL(filterName.qualifiedName(), "TestGroup/TestName");
  
}

//-----------------------------------------------------------------------------
// Check the hash method
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(hashMethod_test) {
  
  // Given
  ChDataModel::FilterName filterName1 {"group", "name"};
  ChDataModel::FilterName filterName2 {"group", "name"};
  
  // Then
  BOOST_CHECK_EQUAL(filterName1.hash(), filterName2.hash());
}

BOOST_AUTO_TEST_SUITE_END ()