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
// Check the belongsInGroup method
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(belongsInGroup_test) {

  // Given
  Euclid::XYDataset::QualifiedName qualified_name {"group1/group2/group3/name"};

  // When
  Euclid::XYDataset::QualifiedName group1 {"group1"};
  Euclid::XYDataset::QualifiedName group1_group2 {"group1/group2"};
  Euclid::XYDataset::QualifiedName group1_group2_group3 {"group1/group2/group3"};
  Euclid::XYDataset::QualifiedName wrong_group_1 {"wrong_group"};
  Euclid::XYDataset::QualifiedName wrong_group_2 {"group1group2"};
  Euclid::XYDataset::QualifiedName wrong_group_3 {"group1/group4/group3"};

  // Then
  BOOST_CHECK(qualified_name.belongsInGroup(group1));
  BOOST_CHECK(qualified_name.belongsInGroup(group1_group2));
  BOOST_CHECK(qualified_name.belongsInGroup(group1_group2_group3));
  BOOST_CHECK(!qualified_name.belongsInGroup(wrong_group_1));
  BOOST_CHECK(!qualified_name.belongsInGroup(wrong_group_2));
  BOOST_CHECK(!qualified_name.belongsInGroup(wrong_group_3));
  BOOST_CHECK(!qualified_name.belongsInGroup(qualified_name));

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
  BOOST_CHECK(qualifiedName1 < qualifiedName2 ^ qualifiedName2 < qualifiedName1);
  BOOST_CHECK(qualifiedName2 < qualifiedName3 ^ qualifiedName3 < qualifiedName2);
  BOOST_CHECK(qualifiedName1 < qualifiedName3 ^ qualifiedName3 < qualifiedName1);
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
  BOOST_CHECK(qualifiedName3.hash() != qualifiedName2.hash());
  BOOST_CHECK(qualifiedName2.hash() != qualifiedName1.hash());
  BOOST_CHECK(qualifiedName3.hash() != qualifiedName1.hash());
  auto iterator = filterSet.begin();
  BOOST_CHECK((*iterator) == qualifiedName2);
  ++iterator;
  BOOST_CHECK((*iterator) == qualifiedName3);
  ++iterator;
  BOOST_CHECK((*iterator) == qualifiedName1);

}

BOOST_AUTO_TEST_SUITE_END ()
