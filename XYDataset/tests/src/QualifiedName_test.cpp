/** 
 * @file tests/src/QualifiedName_test.cpp
 * @date May 19, 2014
 * @author Nikolaos Apostolakos
 */

#include <string>
#include <set>
#include <boost/test/unit_test.hpp>

#include "ElementsKernel/Exception.h"
#include "XYDataset/QualifiedName.h"

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (QualifiedName_test)

//-----------------------------------------------------------------------------
// Check that invalid constructor arguments throw exceptions
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(constructorExceptions_test) {
  
  BOOST_CHECK_THROW((Euclid::XYDataset::QualifiedName{{"","g"}, "b"}),Elements::Exception);
  BOOST_CHECK_THROW((Euclid::XYDataset::QualifiedName{{"asd/sad", "g"}, "b"}), Elements::Exception);
  BOOST_CHECK_THROW((Euclid::XYDataset::QualifiedName{{"a","g"}, ""}), Elements::Exception);
  BOOST_CHECK_THROW((Euclid::XYDataset::QualifiedName{{"a","g"}, "bdf/sdf"}), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Check groups, name and qualifiedName methods work
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(nameMethods_test) {
  
  // Given
  std::string group1 = "TestGroup1";
  std::string group2 = "TestGroup2";
  std::string name = "TestName";
  
  // When
  Euclid::XYDataset::QualifiedName qualifiedName1 {{group1,group2}, name};
  auto groups1 = qualifiedName1.groups();
  Euclid::XYDataset::QualifiedName qualifiedName2 {{group1}, name};
  auto groups2 = qualifiedName2.groups();
  Euclid::XYDataset::QualifiedName qualifiedName3 {{}, name};
  auto groups3 = qualifiedName3.groups();
  
  // Then
  BOOST_CHECK_EQUAL(groups1.size(), 2);
  BOOST_CHECK_EQUAL(groups1[0], group1);
  BOOST_CHECK_EQUAL(groups1[1], group2);
  BOOST_CHECK_EQUAL(qualifiedName1.datasetName(), name);
  BOOST_CHECK_EQUAL(qualifiedName1.qualifiedName(), group1+"/"+group2+"/"+name);
  BOOST_CHECK_EQUAL(groups2.size(), 1);
  BOOST_CHECK_EQUAL(groups2[0], group1);
  BOOST_CHECK_EQUAL(qualifiedName2.datasetName(), name);
  BOOST_CHECK_EQUAL(qualifiedName2.qualifiedName(), group1+"/"+name);
  BOOST_CHECK_EQUAL(groups3.size(), 0);
  BOOST_CHECK_EQUAL(qualifiedName3.datasetName(), name);
  BOOST_CHECK_EQUAL(qualifiedName3.qualifiedName(), name);
  
}

//-----------------------------------------------------------------------------
// Check the hash method
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(hashMethod_test) {
  
  // Given
  Euclid::XYDataset::QualifiedName qualifiedName1 {{"group1","group2"}, "name"};
  Euclid::XYDataset::QualifiedName qualifiedName2 {{"group1","group2"}, "name"};
  
  // Then
  BOOST_CHECK_EQUAL(qualifiedName1.hash(), qualifiedName2.hash());
  
  // Given
  qualifiedName1 = Euclid::XYDataset::QualifiedName {{"group1","group2"}, "name"};
  qualifiedName2 = Euclid::XYDataset::QualifiedName {{"group1","group2"}, "name2"};
  
  // Then
  BOOST_CHECK_NE(qualifiedName1.hash(), qualifiedName2.hash());
  
  // Given
  qualifiedName1 = Euclid::XYDataset::QualifiedName {{"group1","group2"}, "name"};
  qualifiedName2 = Euclid::XYDataset::QualifiedName {{"group1","grou2"}, "name"};
  
  // Then
  BOOST_CHECK_NE(qualifiedName1.hash(), qualifiedName2.hash());
  
  // Given
  qualifiedName1 = Euclid::XYDataset::QualifiedName {{"group1","group2"}, "name"};
  qualifiedName2 = Euclid::XYDataset::QualifiedName {{"group1","group2"}, "name2"};
  
  // Then
  BOOST_CHECK_NE(qualifiedName1.hash(), qualifiedName2.hash());
  
  // Given
  std::hash<Euclid::XYDataset::QualifiedName> stdHashFunction;
  
  // Then
  BOOST_CHECK_EQUAL(qualifiedName1.hash(), stdHashFunction(qualifiedName1));
}

//-----------------------------------------------------------------------------
// Check the comparison operator
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(comparison_test) {
  
  // Given
  Euclid::XYDataset::QualifiedName qualifiedName1 {{"group1","group2"}, "name"};
  Euclid::XYDataset::QualifiedName qualifiedName2 {{"group1","group2"}, "name"};
  
  // Then
  BOOST_CHECK(!(qualifiedName1 < qualifiedName2));
  BOOST_CHECK(!(qualifiedName2 < qualifiedName1));
  
  // Given
  qualifiedName1 = Euclid::XYDataset::QualifiedName {{"agroup"}, "aname"};
  qualifiedName2 = Euclid::XYDataset::QualifiedName {{"bgroup"}, "aname"};
  Euclid::XYDataset::QualifiedName qualifiedName3 {{"bgroup"}, "bname"};
  
  // Then
  BOOST_CHECK_EQUAL(qualifiedName1 < qualifiedName2, qualifiedName1.hash() < qualifiedName2.hash());
  BOOST_CHECK_EQUAL(qualifiedName2 < qualifiedName3, qualifiedName2.hash() < qualifiedName3.hash());
  BOOST_CHECK_EQUAL(qualifiedName1 < qualifiedName3, qualifiedName1.hash() < qualifiedName3.hash());

}

//-----------------------------------------------------------------------------
// Check the equality operator
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(equality_test) {
  
  
  // Given
  Euclid::XYDataset::QualifiedName qualifiedName1 {{"group1","group2"}, "name"};
  Euclid::XYDataset::QualifiedName qualifiedName2 {{"group1","group2"}, "name"};
  
  // Then
  BOOST_CHECK(qualifiedName1 == qualifiedName2);
  
  // Given
  qualifiedName1 = Euclid::XYDataset::QualifiedName {{"agroup"}, "aname"};
  qualifiedName2 = Euclid::XYDataset::QualifiedName {{"bgroup"}, "aname"};
  Euclid::XYDataset::QualifiedName qualifiedName3 {{"bgroup"}, "bname"};
  
  // Then
  BOOST_CHECK(!(qualifiedName1 == qualifiedName2));
  BOOST_CHECK(!(qualifiedName2 == qualifiedName3));
  BOOST_CHECK(!(qualifiedName1 == qualifiedName3));

}

//-----------------------------------------------------------------------------
// Check the ordering by hash
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(hashOrdering_test) {
  
  // Given
  Euclid::XYDataset::QualifiedName qualifiedName1 {{"SDSS"}, "g"};
  Euclid::XYDataset::QualifiedName qualifiedName2 {{"COSMOS"}, "g"};
  Euclid::XYDataset::QualifiedName qualifiedName3 {{"COSMOS"}, "z"};
  
  // When
  std::set<Euclid::XYDataset::QualifiedName> filterSet {};
  filterSet.insert(qualifiedName1);
  filterSet.insert(qualifiedName2);
  filterSet.insert(qualifiedName3);
  
  // Then
  BOOST_CHECK(qualifiedName3.hash() < qualifiedName2.hash());
  BOOST_CHECK(qualifiedName2.hash() < qualifiedName1.hash());
  BOOST_CHECK(qualifiedName3.hash() < qualifiedName1.hash());
  auto iterator = filterSet.begin();
  BOOST_CHECK((*iterator) == qualifiedName3);
  ++iterator;
  BOOST_CHECK((*iterator) == qualifiedName2);
  ++iterator;
  BOOST_CHECK((*iterator) == qualifiedName1);
  
}

//-----------------------------------------------------------------------------
// Check the ordering alphabetically
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(alphabeticalOrdering_test) {
  
  // Given
  Euclid::XYDataset::QualifiedName qualifiedName1 {{"SDSS"}, "g"};
  Euclid::XYDataset::QualifiedName qualifiedName2 {{"COSMOS"}, "g"};
  Euclid::XYDataset::QualifiedName qualifiedName3 {{"COSMOS"}, "z"};
  
  // When
  std::set<Euclid::XYDataset::QualifiedName, Euclid::XYDataset::QualifiedName::AlphabeticalComparator> filterSet {};
  filterSet.insert(qualifiedName1);
  filterSet.insert(qualifiedName2);
  filterSet.insert(qualifiedName3);
  
  // Then
  BOOST_CHECK(qualifiedName3.hash() < qualifiedName2.hash());
  BOOST_CHECK(qualifiedName2.hash() < qualifiedName1.hash());
  BOOST_CHECK(qualifiedName3.hash() < qualifiedName1.hash());
  auto iterator = filterSet.begin();
  BOOST_CHECK((*iterator) == qualifiedName2);
  ++iterator;
  BOOST_CHECK((*iterator) == qualifiedName3);
  ++iterator;
  BOOST_CHECK((*iterator) == qualifiedName1);
  
}

BOOST_AUTO_TEST_SUITE_END ()
