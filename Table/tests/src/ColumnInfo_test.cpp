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
 * @file tests/src/ColumnInfo_test.cpp
 * @date April 7, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "ElementsKernel/Exception.h"
#include "Table/ColumnInfo.h"

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (ColumnInfo_test)

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for empty names list
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(ConstructorEmptyNamesList) {
  
  // Given
  std::vector<Euclid::Table::ColumnInfo::info_type> info_list {};
  
  // Then
  BOOST_CHECK_THROW(Euclid::Table::ColumnInfo {info_list}, Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for duplicated column names
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(ConstructorDuplicateNames) {
  
  // Given
  std::vector<Euclid::Table::ColumnInfo::info_type> info_list {};
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("First", typeid(std::string)));
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("Second", typeid(std::string)));
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("Third", typeid(double)));
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("Second", typeid(double)));
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("Fifth", typeid(int)));
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("Sixth", typeid(std::vector<double>)));
  
  // Then
  BOOST_CHECK_THROW(Euclid::Table::ColumnInfo {info_list}, Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the equality operators
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(equalityOperators) {
  
  // Given
  std::vector<Euclid::Table::ColumnInfo::info_type> info_list_1 {};
  info_list_1.push_back(Euclid::Table::ColumnInfo::info_type("First", typeid(std::string)));
  info_list_1.push_back(Euclid::Table::ColumnInfo::info_type("Second", typeid(std::string)));
  info_list_1.push_back(Euclid::Table::ColumnInfo::info_type("Third", typeid(double)));
  info_list_1.push_back(Euclid::Table::ColumnInfo::info_type("Fourth", typeid(double)));
  info_list_1.push_back(Euclid::Table::ColumnInfo::info_type("Fifth", typeid(int)));
  info_list_1.push_back(Euclid::Table::ColumnInfo::info_type("Sixth", typeid(std::vector<double>)));
  std::vector<Euclid::Table::ColumnInfo::info_type> info_list_2 {};
  info_list_2.push_back(Euclid::Table::ColumnInfo::info_type("First", typeid(std::string)));
  info_list_2.push_back(Euclid::Table::ColumnInfo::info_type("Second", typeid(std::string)));
  info_list_2.push_back(Euclid::Table::ColumnInfo::info_type("Third", typeid(double)));
  info_list_2.push_back(Euclid::Table::ColumnInfo::info_type("Fourth", typeid(double)));
  info_list_2.push_back(Euclid::Table::ColumnInfo::info_type("Fifth", typeid(int)));
  info_list_2.push_back(Euclid::Table::ColumnInfo::info_type("Sixth", typeid(std::vector<double>)));
  
  // When
  Euclid::Table::ColumnInfo columnInfo1 {info_list_1};
  Euclid::Table::ColumnInfo columnInfo2 {info_list_2};
  
  // Then
  BOOST_CHECK(columnInfo1 == columnInfo2);
  BOOST_CHECK(!(columnInfo1 != columnInfo2));
  
  // Given
  std::vector<Euclid::Table::ColumnInfo::info_type> info_list_3 {};
  info_list_3.push_back(Euclid::Table::ColumnInfo::info_type("First", typeid(std::string)));
  info_list_3.push_back(Euclid::Table::ColumnInfo::info_type("Second", typeid(std::string)));
  info_list_3.push_back(Euclid::Table::ColumnInfo::info_type("Third", typeid(double)));
  info_list_3.push_back(Euclid::Table::ColumnInfo::info_type("Fourth", typeid(double)));
  info_list_1.push_back(Euclid::Table::ColumnInfo::info_type("Fifth", typeid(int)));
  
  // When
  Euclid::Table::ColumnInfo columnInfo3 {info_list_3};
  
  // Then
  BOOST_CHECK(!(columnInfo1 == columnInfo3));
  BOOST_CHECK(columnInfo1 != columnInfo3);
  
  // Given
  std::vector<Euclid::Table::ColumnInfo::info_type> info_list_4 {};
  info_list_4.push_back(Euclid::Table::ColumnInfo::info_type("First", typeid(std::string)));
  info_list_4.push_back(Euclid::Table::ColumnInfo::info_type("Second", typeid(std::string)));
  info_list_4.push_back(Euclid::Table::ColumnInfo::info_type("WRONG", typeid(double)));
  info_list_4.push_back(Euclid::Table::ColumnInfo::info_type("Fourth", typeid(double)));
  info_list_4.push_back(Euclid::Table::ColumnInfo::info_type("Fifth", typeid(int)));
  info_list_2.push_back(Euclid::Table::ColumnInfo::info_type("Sixth", typeid(std::vector<double>)));
  
  // When
  Euclid::Table::ColumnInfo columnInfo4 {info_list_4};
  
  // Then
  BOOST_CHECK(!(columnInfo1 == columnInfo4));
  BOOST_CHECK(columnInfo1 != columnInfo4);
  
}

//-----------------------------------------------------------------------------
// Test the size method
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(size) {
  
  // Given
  std::vector<Euclid::Table::ColumnInfo::info_type> info_list {};
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("First", typeid(std::string)));
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("Second", typeid(std::string)));
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("Third", typeid(double)));
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("Fourth", typeid(double)));
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("Fifth", typeid(int)));
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("Sixth", typeid(std::vector<double>)));
  Euclid::Table::ColumnInfo columnInfo {info_list};
  
  // When
  std::size_t size = columnInfo.size();
  
  // Then
  BOOST_CHECK_EQUAL(size, 6u);
  
}

//-----------------------------------------------------------------------------
// Test the getDescription method
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(getDescription) {
  
  // Given
  std::vector<Euclid::Table::ColumnInfo::info_type> info_list {};
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("First", typeid(std::string), "deg", "Desc1"));
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("Second", typeid(std::string), "mag", "Desc2"));
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("Third", typeid(double), "", "Desc3"));
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("Fourth", typeid(double), "ph", "Desc4"));
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("Fifth", typeid(int), "s"));
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("Sixth", typeid(std::vector<double>)));
  Euclid::Table::ColumnInfo columnInfo {info_list};
  
  // When
  auto& desc0  = columnInfo.getDescription(0);
  auto& desc1  = columnInfo.getDescription(1);
  auto& desc2  = columnInfo.getDescription(2);
  auto& desc3  = columnInfo.getDescription(3);
  auto& desc4  = columnInfo.getDescription(4);
  auto& desc5  = columnInfo.getDescription(5);
  
  // Then
  BOOST_CHECK_EQUAL(desc0.name, info_list[0].name);
  BOOST_CHECK_EQUAL(desc0.type.name(), info_list[0].type.name());
  BOOST_CHECK_EQUAL(desc0.unit, info_list[0].unit);
  BOOST_CHECK_EQUAL(desc0.description, info_list[0].description);
  
  BOOST_CHECK_EQUAL(desc1.name, info_list[1].name);
  BOOST_CHECK_EQUAL(desc1.type.name(), info_list[1].type.name());
  BOOST_CHECK_EQUAL(desc1.unit, info_list[1].unit);
  BOOST_CHECK_EQUAL(desc1.description, info_list[1].description);
  
  BOOST_CHECK_EQUAL(desc2.name, info_list[2].name);
  BOOST_CHECK_EQUAL(desc2.type.name(), info_list[2].type.name());
  BOOST_CHECK_EQUAL(desc2.unit, info_list[2].unit);
  BOOST_CHECK_EQUAL(desc2.description, info_list[2].description);
  
  BOOST_CHECK_EQUAL(desc3.name, info_list[3].name);
  BOOST_CHECK_EQUAL(desc3.type.name(), info_list[3].type.name());
  BOOST_CHECK_EQUAL(desc3.unit, info_list[3].unit);
  BOOST_CHECK_EQUAL(desc3.description, info_list[3].description);
  
  BOOST_CHECK_EQUAL(desc4.name, info_list[4].name);
  BOOST_CHECK_EQUAL(desc4.type.name(), info_list[4].type.name());
  BOOST_CHECK_EQUAL(desc4.unit, info_list[4].unit);
  BOOST_CHECK_EQUAL(desc4.description, info_list[4].description);
  
  BOOST_CHECK_EQUAL(desc5.name, info_list[5].name);
  BOOST_CHECK_EQUAL(desc5.type.name(), info_list[5].type.name());
  BOOST_CHECK_EQUAL(desc5.unit, info_list[5].unit);
  BOOST_CHECK_EQUAL(desc5.description, info_list[5].description);
  
  BOOST_CHECK_THROW(columnInfo.getDescription(6), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the find method
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(find) {
  
  // Given
  std::vector<Euclid::Table::ColumnInfo::info_type> info_list {};
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("First", typeid(std::string)));
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("Second", typeid(std::string)));
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("Third", typeid(double)));
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("Fourth", typeid(double)));
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("Fifth", typeid(int)));
  info_list.push_back(Euclid::Table::ColumnInfo::info_type("Sixth", typeid(std::vector<double>)));
  Euclid::Table::ColumnInfo columnInfo {info_list};
  
  // When
  std::unique_ptr<size_t> index0  = columnInfo.find("First");
  std::unique_ptr<size_t> index1  = columnInfo.find("Second");
  std::unique_ptr<size_t> index2  = columnInfo.find("Third");
  std::unique_ptr<size_t> index3  = columnInfo.find("Fourth");
  std::unique_ptr<size_t> index4  = columnInfo.find("Fifth");
  std::unique_ptr<size_t> index5  = columnInfo.find("Sixth");
  std::unique_ptr<size_t> index6  = columnInfo.find("NotThere");
  
  // Then
  BOOST_CHECK(index0);
  BOOST_CHECK_EQUAL(*index0, 0u);
  BOOST_CHECK(index1);
  BOOST_CHECK_EQUAL(*index1, 1u);
  BOOST_CHECK(index2);
  BOOST_CHECK_EQUAL(*index2, 2u);
  BOOST_CHECK(index3);
  BOOST_CHECK_EQUAL(*index3, 3u);
  BOOST_CHECK(index4);
  BOOST_CHECK_EQUAL(*index4, 4u);
  BOOST_CHECK(index5);
  BOOST_CHECK_EQUAL(*index5, 5u);
  BOOST_CHECK(!index6);
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
