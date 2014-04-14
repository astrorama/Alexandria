/** 
 * @file Row_test.cpp
 * @date April 8, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "ElementsKernel/ElementsException.h"
#include "AsciiTable/Row.h"

struct Row_Fixture {
  std::vector<AsciiTable::ColumnInfo::info_type> info_list {
      AsciiTable::ColumnInfo::info_type("First", typeid(std::string)),
      AsciiTable::ColumnInfo::info_type("Second", typeid(std::string)),
      AsciiTable::ColumnInfo::info_type("Third", typeid(double)),
      AsciiTable::ColumnInfo::info_type("Fourth", typeid(double)),
      AsciiTable::ColumnInfo::info_type("Fifth", typeid(int))
  };
  std::shared_ptr<AsciiTable::ColumnInfo> column_info {new AsciiTable::ColumnInfo {info_list}};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Row_test)

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for wrong number of cell values
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorWrongNumberOfValues, Row_Fixture) {
  
  // Given
  std::vector<AsciiTable::Row::cell_type> values {std::string{"One"}, std::string{"Two"}, 3.};
  
  // Then
  BOOST_CHECK_THROW(AsciiTable::Row(values, column_info), ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for null column_info
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorNullColumnInfo, Row_Fixture) {
  
  // Given
  std::vector<AsciiTable::Row::cell_type> values {std::string{"One"}, std::string{"Two"}, 3., 4., 5};
  std::shared_ptr<AsciiTable::ColumnInfo> null_col_info {};
  
  // Then
  BOOST_CHECK_THROW(AsciiTable::Row(values, null_col_info), ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for wrong cell type
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorWrongCellType, Row_Fixture) {
  
  // Given
  std::vector<AsciiTable::Row::cell_type> values {std::string{"One"}, std::string{"Two"}, std::string{"Three"}, 4., 5};

  // Then
  BOOST_CHECK_THROW(AsciiTable::Row(values, column_info), ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for empty string cell values
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorEmptyCellValue, Row_Fixture) {
  
  // Given
  std::vector<AsciiTable::Row::cell_type> values {std::string{"One"}, std::string{""}, 3., 4., 5};
  
  // Then
  BOOST_CHECK_THROW(AsciiTable::Row(values, column_info), ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for cell values with whitespace chars
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorCellValueWithWhitespace, Row_Fixture) {
  
  // Given
  std::vector<AsciiTable::Row::cell_type> space {std::string{"One"}, std::string{"Sp ace"}, 3., 4., 5};
  std::vector<AsciiTable::Row::cell_type> tab {std::string{"One"}, std::string{"T\tab"}, 3., 4., 5};
  std::vector<AsciiTable::Row::cell_type> carriage_return {std::string{"One"}, std::string{"Carriage\rReturn"}, 3., 4., 5};
  std::vector<AsciiTable::Row::cell_type> new_line {std::string{"One"}, std::string{"New\nLine"}, 3., 4., 5};
  std::vector<AsciiTable::Row::cell_type> new_page {std::string{"One"}, std::string{"New\fPage"}, 3., 4., 5};
  
  // Then
  BOOST_CHECK_THROW(AsciiTable::Row(space, column_info), ElementsException);
  BOOST_CHECK_THROW(AsciiTable::Row(tab, column_info), ElementsException);
  BOOST_CHECK_THROW(AsciiTable::Row(carriage_return, column_info), ElementsException);
  BOOST_CHECK_THROW(AsciiTable::Row(new_line, column_info), ElementsException);
  BOOST_CHECK_THROW(AsciiTable::Row(new_page, column_info), ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the getColumnInfo method
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getColumnInfo, Row_Fixture) {
  
  // Given
  std::vector<AsciiTable::Row::cell_type> values {std::string{"One"}, std::string{"Two"}, 3., 4., 5};
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
  std::vector<AsciiTable::Row::cell_type> values {std::string{"One"}, std::string{"Two"}, 3., 4., 5};
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
  std::vector<AsciiTable::Row::cell_type> values {std::string{"One"}, std::string{"Two"}, 3., 4., 5};
  AsciiTable::Row row {values, column_info};
  
  // When
  AsciiTable::Row::cell_type value0 = row[0];
  AsciiTable::Row::cell_type value1 = row[1];
  AsciiTable::Row::cell_type value2 = row[2];
  AsciiTable::Row::cell_type value3 = row[3];
  AsciiTable::Row::cell_type value4 = row[4];
  
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
  std::vector<AsciiTable::Row::cell_type> values {std::string{"One"}, std::string{"Two"}, 3., 4., 5};
  AsciiTable::Row row {values, column_info};
  
  // When
  AsciiTable::Row::cell_type value0 = row["First"];
  AsciiTable::Row::cell_type value1 = row["Second"];
  AsciiTable::Row::cell_type value2 = row["Third"];
  AsciiTable::Row::cell_type value3 = row["Fourth"];
  AsciiTable::Row::cell_type value4 = row["Fifth"];
  
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
  std::vector<AsciiTable::Row::cell_type> values {std::string{"One"}, std::string{"Two"}, 3., 4., 5};
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