/** 
 * @file FilterName_test.cpp
 * @date January 17, 2014
 * @author Nikolaos Apostolakos
 */

#include <string>
#include <set>
#include <stdexcept>
#include <boost/test/unit_test.hpp>

#include "ChCatalog/FilterName.h"

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (FilterName_test)

//-----------------------------------------------------------------------------
// Check that invalid constructor arguments throw exceptions
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(constructorExceptions_test) {
  
  BOOST_CHECK_THROW((ChCatalog::FilterName{"", "b"}), std::invalid_argument);
  BOOST_CHECK_THROW((ChCatalog::FilterName{"asd/sad", "b"}), std::invalid_argument);
  BOOST_CHECK_THROW((ChCatalog::FilterName{"a", ""}), std::invalid_argument);
  BOOST_CHECK_THROW((ChCatalog::FilterName{"a", "bdf/sdf"}), std::invalid_argument);
  
}

//-----------------------------------------------------------------------------
// Check group, name and qualifiedName methods work
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(nameMethods_test) {
  
  // Given
  std::string group = "TestGroup";
  std::string name = "TestName";
  
  // When
  ChCatalog::FilterName filterName {group, name};
  
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
  ChCatalog::FilterName filterName1 {"group", "name"};
  ChCatalog::FilterName filterName2 {"group", "name"};
  
  // Then
  BOOST_CHECK_EQUAL(filterName1.hash(), filterName2.hash());
  
  // Given
  filterName1 = ChCatalog::FilterName {"group", "name"};
  filterName2 = ChCatalog::FilterName {"group", "name2"};
  
  // Then
  BOOST_CHECK_NE(filterName1.hash(), filterName2.hash());
  
  // Given
  filterName1 = ChCatalog::FilterName {"group", "name"};
  filterName2 = ChCatalog::FilterName {"grou2", "name"};
  
  // Then
  BOOST_CHECK_NE(filterName1.hash(), filterName2.hash());
  
  // Given
  filterName1 = ChCatalog::FilterName {"group", "name"};
  filterName2 = ChCatalog::FilterName {"group2", "name2"};
  
  // Then
  BOOST_CHECK_NE(filterName1.hash(), filterName2.hash());
  
  // Given
  std::hash<ChCatalog::FilterName> stdHashFunction;
  
  // Then
  BOOST_CHECK_EQUAL(filterName1.hash(), stdHashFunction(filterName1));
}

//-----------------------------------------------------------------------------
// Check the comparison operator
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(comparison_test) {
  
  // Given
  ChCatalog::FilterName filterName1 {"group", "name"};
  ChCatalog::FilterName filterName2 {"group", "name"};
  
  // Then
  BOOST_CHECK(!(filterName1 < filterName2));
  BOOST_CHECK(!(filterName2 < filterName1));
  
  // Given
  filterName1 = ChCatalog::FilterName {"agroup", "aname"};
  filterName2 = ChCatalog::FilterName {"bgroup", "aname"};
  ChCatalog::FilterName filterName3 {"bgroup", "bname"};
  
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
  ChCatalog::FilterName filterName1 {"group", "name"};
  ChCatalog::FilterName filterName2 {"group", "name"};
  
  // Then
  BOOST_CHECK(filterName1 == filterName2);
  
  // Given
  filterName1 = ChCatalog::FilterName {"agroup", "aname"};
  filterName2 = ChCatalog::FilterName {"bgroup", "aname"};
  ChCatalog::FilterName filterName3 {"bgroup", "bname"};
  
  // Then
  BOOST_CHECK(!(filterName1 == filterName2));
  BOOST_CHECK(!(filterName2 == filterName3));
  BOOST_CHECK(!(filterName1 == filterName3));

}

//-----------------------------------------------------------------------------
// Check the ordering by hash
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(hashOrdering_test) {
  
  // Given
  ChCatalog::FilterName filterName1 {"SDSS", "g"};
  ChCatalog::FilterName filterName2 {"COSMOS", "g"};
  ChCatalog::FilterName filterName3 {"COSMOS", "z"};
  
  // When
  std::set<ChCatalog::FilterName> filterSet {};
  filterSet.insert(filterName1);
  filterSet.insert(filterName2);
  filterSet.insert(filterName3);
  
  // Then
  BOOST_CHECK(filterName3.hash() < filterName2.hash());
  BOOST_CHECK(filterName2.hash() < filterName1.hash());
  BOOST_CHECK(filterName3.hash() < filterName1.hash());
  auto iterator = filterSet.begin();
  BOOST_CHECK((*iterator) == filterName3);
  ++iterator;
  BOOST_CHECK((*iterator) == filterName2);
  ++iterator;
  BOOST_CHECK((*iterator) == filterName1);
  
}

//-----------------------------------------------------------------------------
// Check the ordering alphabetically
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(alphabeticalOrdering_test) {
  
  // Given
  ChCatalog::FilterName filterName1 {"SDSS", "g"};
  ChCatalog::FilterName filterName2 {"COSMOS", "g"};
  ChCatalog::FilterName filterName3 {"COSMOS", "z"};
  
  // When
  std::set<ChCatalog::FilterName, ChCatalog::FilterName::AlphabeticalComparator> filterSet {};
  filterSet.insert(filterName1);
  filterSet.insert(filterName2);
  filterSet.insert(filterName3);
  
  // Then
  BOOST_CHECK(filterName3.hash() < filterName2.hash());
  BOOST_CHECK(filterName2.hash() < filterName1.hash());
  BOOST_CHECK(filterName3.hash() < filterName1.hash());
  auto iterator = filterSet.begin();
  BOOST_CHECK((*iterator) == filterName2);
  ++iterator;
  BOOST_CHECK((*iterator) == filterName3);
  ++iterator;
  BOOST_CHECK((*iterator) == filterName1);
  
}

BOOST_AUTO_TEST_SUITE_END ()
