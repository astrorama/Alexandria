/** 
 * @file Row_test.cpp
 * @date April 8, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "ElementsKernel/ElementsException.h"
#include "AsciiTable/Row.h"

struct Row_Fixture {
  std::vector<std::string> column_names {"First", "Second", "Third", "Fourth", "Fifth"};
  std::shared_ptr<AsciiTable::ColumnInfo> column_info {new AsciiTable::ColumnInfo {column_names}};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Row_test)

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for number of values
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorWrongNumberOfValues, Row_Fixture) {
  
  // Given
  std::vector<std::string> values {"One", "Two", "Three"};
  
  // Then
  BOOST_CHECK_THROW(AsciiTable::Row(values, column_info), ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for null column_info
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorNullColumnInfo, Row_Fixture) {
  
  // Given
  std::vector<std::string> values {"One", "Two", "Three", "Four", "Five"};
  std::shared_ptr<AsciiTable::ColumnInfo> null_col_info {};
  
  // Then
  BOOST_CHECK_THROW(AsciiTable::Row(values, null_col_info), ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the getColumnInfo method
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getColumnInfo, Row_Fixture) {
  
  // Given
  std::vector<std::string> values {"One", "Two", "Three", "Four", "Five"};
  AsciiTable::Row row {values, column_info};
  
  // When
  auto result = row.getColumnInfo();
  
  // Then
  BOOST_CHECK(*result == *column_info);
  
}

//-----------------------------------------------------------------------------
// Test the size
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Size, Row_Fixture) {
  
  // Given
  std::vector<std::string> values {"One", "Two", "Three", "Four", "Five"};
  AsciiTable::Row row {values, column_info};
  
  // When
  std::size_t size = row.size();
  
  // Then
  BOOST_CHECK_EQUAL(size, values.size());
  
}

//-----------------------------------------------------------------------------
// Test the operator[size_t]
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(IndexBracketOperator, Row_Fixture) {
  
  // Given
  std::vector<std::string> values {"One", "Two", "Three", "Four", "Five"};
  AsciiTable::Row row {values, column_info};
  
  // When
  std::string value0 = row[0];
  std::string value1 = row[1];
  std::string value2 = row[2];
  std::string value3 = row[3];
  std::string value4 = row[4];
  
  // Then
  BOOST_CHECK_EQUAL(value0, values[0]);
  BOOST_CHECK_EQUAL(value1, values[1]);
  BOOST_CHECK_EQUAL(value2, values[2]);
  BOOST_CHECK_EQUAL(value3, values[3]);
  BOOST_CHECK_EQUAL(value4, values[4]);
  BOOST_CHECK_THROW(row[5], ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the operator[string]
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(StringBracketOperator, Row_Fixture) {
  
  // Given
  std::vector<std::string> values {"One", "Two", "Three", "Four", "Five"};
  AsciiTable::Row row {values, column_info};
  
  // When
  std::string value0 = row["First"];
  std::string value1 = row["Second"];
  std::string value2 = row["Third"];
  std::string value3 = row["Fourth"];
  std::string value4 = row["Fifth"];
  
  // Then
  BOOST_CHECK_EQUAL(value0, values[0]);
  BOOST_CHECK_EQUAL(value1, values[1]);
  BOOST_CHECK_EQUAL(value2, values[2]);
  BOOST_CHECK_EQUAL(value3, values[3]);
  BOOST_CHECK_EQUAL(value4, values[4]);
  BOOST_CHECK_THROW(row["None"], ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the iterator
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Iterator, Row_Fixture) {
  
  // Given
  std::vector<std::string> values {"One", "Two", "Three", "Four", "Five"};
  AsciiTable::Row row {values, column_info};
  auto valuesIter = values.cbegin();
  
  // When
  for (auto cell : row) {
    // Then
    BOOST_CHECK_EQUAL(cell, *valuesIter);
    ++valuesIter;
  }
  BOOST_CHECK(valuesIter == values.cend());
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()