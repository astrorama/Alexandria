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
  std::vector<Euclid::ChTable::ColumnInfo::info_type> info_list {};
  
  // Then
  BOOST_CHECK_THROW(Euclid::ChTable::ColumnInfo {info_list}, Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for duplicated column names
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(ConstructorDuplicateNames) {
  
  // Given
  std::vector<Euclid::ChTable::ColumnInfo::info_type> info_list {};
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("First", typeid(std::string)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Second", typeid(std::string)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Third", typeid(double)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Second", typeid(double)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Fifth", typeid(int)));
  
  // Then
  BOOST_CHECK_THROW(Euclid::ChTable::ColumnInfo {info_list}, Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for empty string name
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(ConstructorEmptyStringName) {
  
  // Given
  std::vector<Euclid::ChTable::ColumnInfo::info_type> info_list {};
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("First", typeid(std::string)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Second", typeid(std::string)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Third", typeid(double)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("", typeid(double)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Fifth", typeid(int)));
  
  // Then
  BOOST_CHECK_THROW(Euclid::ChTable::ColumnInfo {info_list}, Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for names with whitespace characters
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(ConstructorNameWithWhitespaceChars) {
  
  // Given
  std::vector<Euclid::ChTable::ColumnInfo::info_type> space {Euclid::ChTable::ColumnInfo::info_type("Sp ace", typeid(std::string))};
  std::vector<Euclid::ChTable::ColumnInfo::info_type> tab {Euclid::ChTable::ColumnInfo::info_type("Ta\tb", typeid(std::string))};
  std::vector<Euclid::ChTable::ColumnInfo::info_type> carriage_return {Euclid::ChTable::ColumnInfo::info_type("Carriage\rReturn", typeid(double))};
  std::vector<Euclid::ChTable::ColumnInfo::info_type> new_line {Euclid::ChTable::ColumnInfo::info_type("New\nLine", typeid(double))};
  std::vector<Euclid::ChTable::ColumnInfo::info_type> new_page {Euclid::ChTable::ColumnInfo::info_type("New\fPage", typeid(int))};
  
  // Then
  BOOST_CHECK_THROW(Euclid::ChTable::ColumnInfo {space}, Elements::Exception);
  BOOST_CHECK_THROW(Euclid::ChTable::ColumnInfo {tab}, Elements::Exception);
  BOOST_CHECK_THROW(Euclid::ChTable::ColumnInfo {carriage_return}, Elements::Exception);
  BOOST_CHECK_THROW(Euclid::ChTable::ColumnInfo {new_line}, Elements::Exception);
  BOOST_CHECK_THROW(Euclid::ChTable::ColumnInfo {new_page}, Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the equality operators
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(equalityOperators) {
  
  // Given
  std::vector<Euclid::ChTable::ColumnInfo::info_type> info_list_1 {};
  info_list_1.push_back(Euclid::ChTable::ColumnInfo::info_type("First", typeid(std::string)));
  info_list_1.push_back(Euclid::ChTable::ColumnInfo::info_type("Second", typeid(std::string)));
  info_list_1.push_back(Euclid::ChTable::ColumnInfo::info_type("Third", typeid(double)));
  info_list_1.push_back(Euclid::ChTable::ColumnInfo::info_type("Fourth", typeid(double)));
  info_list_1.push_back(Euclid::ChTable::ColumnInfo::info_type("Fifth", typeid(int)));
  std::vector<Euclid::ChTable::ColumnInfo::info_type> info_list_2 {};
  info_list_2.push_back(Euclid::ChTable::ColumnInfo::info_type("First", typeid(std::string)));
  info_list_2.push_back(Euclid::ChTable::ColumnInfo::info_type("Second", typeid(std::string)));
  info_list_2.push_back(Euclid::ChTable::ColumnInfo::info_type("Third", typeid(double)));
  info_list_2.push_back(Euclid::ChTable::ColumnInfo::info_type("Fourth", typeid(double)));
  info_list_2.push_back(Euclid::ChTable::ColumnInfo::info_type("Fifth", typeid(int)));
  
  // When
  Euclid::ChTable::ColumnInfo columnInfo1 {info_list_1};
  Euclid::ChTable::ColumnInfo columnInfo2 {info_list_2};
  
  // Then
  BOOST_CHECK(columnInfo1 == columnInfo2);
  BOOST_CHECK(!(columnInfo1 != columnInfo2));
  
  // Given
  std::vector<Euclid::ChTable::ColumnInfo::info_type> info_list_3 {};
  info_list_3.push_back(Euclid::ChTable::ColumnInfo::info_type("First", typeid(std::string)));
  info_list_3.push_back(Euclid::ChTable::ColumnInfo::info_type("Second", typeid(std::string)));
  info_list_3.push_back(Euclid::ChTable::ColumnInfo::info_type("Third", typeid(double)));
  info_list_3.push_back(Euclid::ChTable::ColumnInfo::info_type("Fourth", typeid(double)));
  
  // When
  Euclid::ChTable::ColumnInfo columnInfo3 {info_list_3};
  
  // Then
  BOOST_CHECK(!(columnInfo1 == columnInfo3));
  BOOST_CHECK(columnInfo1 != columnInfo3);
  
  // Given
  std::vector<Euclid::ChTable::ColumnInfo::info_type> info_list_4 {};
  info_list_4.push_back(Euclid::ChTable::ColumnInfo::info_type("First", typeid(std::string)));
  info_list_4.push_back(Euclid::ChTable::ColumnInfo::info_type("Second", typeid(std::string)));
  info_list_4.push_back(Euclid::ChTable::ColumnInfo::info_type("WRONG", typeid(double)));
  info_list_4.push_back(Euclid::ChTable::ColumnInfo::info_type("Fourth", typeid(double)));
  info_list_4.push_back(Euclid::ChTable::ColumnInfo::info_type("Fifth", typeid(int)));
  
  // When
  Euclid::ChTable::ColumnInfo columnInfo4 {info_list_4};
  
  // Then
  BOOST_CHECK(!(columnInfo1 == columnInfo4));
  BOOST_CHECK(columnInfo1 != columnInfo4);
  
}

//-----------------------------------------------------------------------------
// Test the size method
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(size) {
  
  // Given
  std::vector<Euclid::ChTable::ColumnInfo::info_type> info_list {};
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("First", typeid(std::string)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Second", typeid(std::string)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Third", typeid(double)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Fourth", typeid(double)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Fifth", typeid(int)));
  Euclid::ChTable::ColumnInfo columnInfo {info_list};
  
  // When
  std::size_t size = columnInfo.size();
  
  // Then
  BOOST_CHECK_EQUAL(size, 5);
  
}

//-----------------------------------------------------------------------------
// Test the getName method
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(getName) {
  
  // Given
  std::vector<Euclid::ChTable::ColumnInfo::info_type> info_list {};
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("First", typeid(std::string)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Second", typeid(std::string)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Third", typeid(double)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Fourth", typeid(double)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Fifth", typeid(int)));
  Euclid::ChTable::ColumnInfo columnInfo {info_list};
  
  // When
  const std::string& name0  = columnInfo.getName(0);
  const std::string& name1  = columnInfo.getName(1);
  const std::string& name2  = columnInfo.getName(2);
  const std::string& name3  = columnInfo.getName(3);
  const std::string& name4  = columnInfo.getName(4);
  
  // Then
  BOOST_CHECK_EQUAL(name0, "First");
  BOOST_CHECK_EQUAL(name1, "Second");
  BOOST_CHECK_EQUAL(name2, "Third");
  BOOST_CHECK_EQUAL(name3, "Fourth");
  BOOST_CHECK_EQUAL(name4, "Fifth");
  BOOST_CHECK_THROW(columnInfo.getName(5), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the getType method
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(getType) {
  
  // Given
  std::vector<Euclid::ChTable::ColumnInfo::info_type> info_list {};
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("First", typeid(std::string)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Second", typeid(std::string)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Third", typeid(double)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Fourth", typeid(double)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Fifth", typeid(int)));
  Euclid::ChTable::ColumnInfo columnInfo {info_list};
  
  // When
  const std::type_index& type0  = columnInfo.getType(0);
  const std::type_index& type1  = columnInfo.getType(1);
  const std::type_index& type2  = columnInfo.getType(2);
  const std::type_index& type3  = columnInfo.getType(3);
  const std::type_index& type4  = columnInfo.getType(4);
  
  // Then
  BOOST_CHECK(type0 == typeid(std::string));
  BOOST_CHECK(type1 == typeid(std::string));
  BOOST_CHECK(type2 == typeid(double));
  BOOST_CHECK(type3 == typeid(double));
  BOOST_CHECK(type4 == typeid(int));
  BOOST_CHECK_THROW(columnInfo.getType(5), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the find method
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(find) {
  
  // Given
  std::vector<Euclid::ChTable::ColumnInfo::info_type> info_list {};
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("First", typeid(std::string)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Second", typeid(std::string)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Third", typeid(double)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Fourth", typeid(double)));
  info_list.push_back(Euclid::ChTable::ColumnInfo::info_type("Fifth", typeid(int)));
  Euclid::ChTable::ColumnInfo columnInfo {info_list};
  
  // When
  std::unique_ptr<size_t> index0  = columnInfo.find("First");
  std::unique_ptr<size_t> index1  = columnInfo.find("Second");
  std::unique_ptr<size_t> index2  = columnInfo.find("Third");
  std::unique_ptr<size_t> index3  = columnInfo.find("Fourth");
  std::unique_ptr<size_t> index4  = columnInfo.find("Fifth");
  std::unique_ptr<size_t> index5  = columnInfo.find("NotThere");
  
  // Then
  BOOST_CHECK(index0);
  BOOST_CHECK_EQUAL(*index0, 0);
  BOOST_CHECK(index1);
  BOOST_CHECK_EQUAL(*index1, 1);
  BOOST_CHECK(index2);
  BOOST_CHECK_EQUAL(*index2, 2);
  BOOST_CHECK(index3);
  BOOST_CHECK_EQUAL(*index3, 3);
  BOOST_CHECK(index4);
  BOOST_CHECK_EQUAL(*index4, 4);
  BOOST_CHECK(!index5);
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()