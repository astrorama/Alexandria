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
  
  // Given
  filterName1 = ChDataModel::FilterName {"group", "name"};
  filterName2 = ChDataModel::FilterName {"group", "name2"};
  
  // Then
  BOOST_CHECK_NE(filterName1.hash(), filterName2.hash());
  
  // Given
  filterName1 = ChDataModel::FilterName {"group", "name"};
  filterName2 = ChDataModel::FilterName {"grou2", "name"};
  
  // Then
  BOOST_CHECK_NE(filterName1.hash(), filterName2.hash());
  
  // Given
  filterName1 = ChDataModel::FilterName {"group", "name"};
  filterName2 = ChDataModel::FilterName {"group2", "name2"};
  
  // Then
  BOOST_CHECK_NE(filterName1.hash(), filterName2.hash());
  
  // Given
  std::hash<ChDataModel::FilterName> stdHashFunction;
  
  // Then
  BOOST_CHECK_EQUAL(filterName1.hash(), stdHashFunction(filterName1));
}

//-----------------------------------------------------------------------------
// Check the comparison operator
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(comparison_test) {
  
  // Given
  ChDataModel::FilterName filterName1 {"group", "name"};
  ChDataModel::FilterName filterName2 {"group", "name"};
  
  // Then
  BOOST_CHECK(!(filterName1 < filterName2));
  BOOST_CHECK(!(filterName2 < filterName1));
  
  // Given
  filterName1 = ChDataModel::FilterName {"agroup", "aname"};
  filterName2 = ChDataModel::FilterName {"bgroup", "aname"};
  ChDataModel::FilterName filterName3 {"bgroup", "bname"};
  
  // Then
  BOOST_CHECK_EQUAL(filterName1 < filterName2, filterName1.hash() < filterName2.hash());
  BOOST_CHECK_EQUAL(filterName2 < filterName3, filterName2.hash() < filterName3.hash());
  BOOST_CHECK_EQUAL(filterName1 < filterName3, filterName1.hash() < filterName3.hash());

}

//-----------------------------------------------------------------------------
// Check the equality operator
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(equality_test) {
  
  
  // Given
  ChDataModel::FilterName filterName1 {"group", "name"};
  ChDataModel::FilterName filterName2 {"group", "name"};
  
  // Then
  BOOST_CHECK(filterName1 == filterName2);
  
  // Given
  filterName1 = ChDataModel::FilterName {"agroup", "aname"};
  filterName2 = ChDataModel::FilterName {"bgroup", "aname"};
  ChDataModel::FilterName filterName3 {"bgroup", "bname"};
  
  // Then
  BOOST_CHECK(!(filterName1 == filterName2));
  BOOST_CHECK(!(filterName2 == filterName3));
  BOOST_CHECK(!(filterName1 == filterName3));

}

BOOST_AUTO_TEST_SUITE_END ()