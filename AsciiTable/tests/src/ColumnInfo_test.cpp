/** 
 * @file ColumnInfo_test.cpp
 * @date April 7, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "ElementsKernel/ElementsException.h"
#include "AsciiTable/ColumnInfo.h"

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (ColumnInfo_test)

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for empty names list
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(ConstructorEmptyNamesList) {
  
  // Given
  std::vector<std::string> names {};
  
  // Then
  BOOST_CHECK_THROW(AsciiTable::ColumnInfo {names}, ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for duplicated column names
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(ConstructorDuplicateNames) {
  
  // Given
  std::vector<std::string> names {"First", "Second", "Third", "Second", "Fifth"};
  
  // Then
  BOOST_CHECK_THROW(AsciiTable::ColumnInfo {names}, ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for empty string name
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(ConstructorEmptyStringName) {
  
  // Given
  std::vector<std::string> names {"First", "Second", "Third", "", "Fifth"};
  
  // Then
  BOOST_CHECK_THROW(AsciiTable::ColumnInfo {names}, ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for names with whitespace characters
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(ConstructorNameWithWhitespaceChars) {
  
  // Given
  std::vector<std::string> space {"Sp ace"};
  std::vector<std::string> tab {"Ta\tb"};
  std::vector<std::string> carriage_return {"Carriage\rReturn"};
  std::vector<std::string> new_line {"New\nLine"};
  std::vector<std::string> new_page {"New\fPage"};
  
  // Then
  BOOST_CHECK_THROW(AsciiTable::ColumnInfo {space}, ElementsException);
  BOOST_CHECK_THROW(AsciiTable::ColumnInfo {tab}, ElementsException);
  BOOST_CHECK_THROW(AsciiTable::ColumnInfo {carriage_return}, ElementsException);
  BOOST_CHECK_THROW(AsciiTable::ColumnInfo {new_line}, ElementsException);
  BOOST_CHECK_THROW(AsciiTable::ColumnInfo {new_page}, ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the equality operators
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(equalityOperators) {
  
  // Given
  std::vector<std::string> names1 {"First", "Second", "Third", "Fourth", "Fifth"};
  std::vector<std::string> names2 {"First", "Second", "Third", "Fourth", "Fifth"};
  
  // When
  AsciiTable::ColumnInfo columnInfo1 {names1};
  AsciiTable::ColumnInfo columnInfo2 {names2};
  
  // Then
  BOOST_CHECK(columnInfo1 == columnInfo2);
  BOOST_CHECK(!(columnInfo1 != columnInfo2));
  
  // Given
  std::vector<std::string> names3 {"First", "Second", "Third", "Fourth"};
  
  // When
  AsciiTable::ColumnInfo columnInfo3 {names3};
  
  // Then
  BOOST_CHECK(!(columnInfo1 == columnInfo3));
  BOOST_CHECK(columnInfo1 != columnInfo3);
  
  // Given
  std::vector<std::string> names4 {"First", "Second", "WRONG", "Fourth", "Fifth"};
  
  // When
  AsciiTable::ColumnInfo columnInfo4 {names4};
  
  // Then
  BOOST_CHECK(!(columnInfo1 == columnInfo4));
  BOOST_CHECK(columnInfo1 != columnInfo4);
  
}

//-----------------------------------------------------------------------------
// Test the size method
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(size) {
  
  // Given
  std::vector<std::string> names {"First", "Second", "Third", "Fourth", "Fifth"};
  AsciiTable::ColumnInfo columnInfo {names};
  
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
  std::vector<std::string> names {"First", "Second", "Third", "Fourth", "Fifth"};
  AsciiTable::ColumnInfo columnInfo {names};
  
  // When
  std::unique_ptr<std::string> name0  = columnInfo.getName(0);
  std::unique_ptr<std::string> name1  = columnInfo.getName(1);
  std::unique_ptr<std::string> name2  = columnInfo.getName(2);
  std::unique_ptr<std::string> name3  = columnInfo.getName(3);
  std::unique_ptr<std::string> name4  = columnInfo.getName(4);
  std::unique_ptr<std::string> name5  = columnInfo.getName(5);
  std::unique_ptr<std::string> name6  = columnInfo.getName(10);
  
  // Then
  BOOST_CHECK(name0);
  BOOST_CHECK_EQUAL(*name0, "First");
  BOOST_CHECK(name1);
  BOOST_CHECK_EQUAL(*name1, "Second");
  BOOST_CHECK(name2);
  BOOST_CHECK_EQUAL(*name2, "Third");
  BOOST_CHECK(name3);
  BOOST_CHECK_EQUAL(*name3, "Fourth");
  BOOST_CHECK(name4);
  BOOST_CHECK_EQUAL(*name4, "Fifth");
  BOOST_CHECK(!name5);
  BOOST_CHECK(!name6);
  
}

//-----------------------------------------------------------------------------
// Test the getIndex method
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(getIndex) {
  
  // Given
  std::vector<std::string> names {"First", "Second", "Third", "Fourth", "Fifth"};
  AsciiTable::ColumnInfo columnInfo {names};
  
  // When
  std::unique_ptr<size_t> index0  = columnInfo.getIndex("First");
  std::unique_ptr<size_t> index1  = columnInfo.getIndex("Second");
  std::unique_ptr<size_t> index2  = columnInfo.getIndex("Third");
  std::unique_ptr<size_t> index3  = columnInfo.getIndex("Fourth");
  std::unique_ptr<size_t> index4  = columnInfo.getIndex("Fifth");
  std::unique_ptr<size_t> index5  = columnInfo.getIndex("NotThere");
  
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