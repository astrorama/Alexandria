/**
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
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
 * @file tests/src/Row_test.cpp
 * @date April 8, 2014
 * @author Nikolaos Apostolakos
 */

#include "ElementsKernel/Exception.h"
#include "Table/Row.h"
#include "Table/TestHelper.h"
#include <boost/test/unit_test.hpp>

struct Row_Fixture {
  std::vector<Euclid::Table::ColumnInfo::info_type> info_list{
      Euclid::Table::ColumnInfo::info_type("First", typeid(std::string)),
      Euclid::Table::ColumnInfo::info_type("Second", typeid(std::string)),
      Euclid::Table::ColumnInfo::info_type("Third", typeid(double)),
      Euclid::Table::ColumnInfo::info_type("Fourth", typeid(double)),
      Euclid::Table::ColumnInfo::info_type("Fifth", typeid(int)),
      Euclid::Table::ColumnInfo::info_type("Sixth", typeid(std::vector<double>))};
  std::shared_ptr<Euclid::Table::ColumnInfo> column_info{new Euclid::Table::ColumnInfo{info_list}};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(Row_test)

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for wrong number of cell values
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorWrongNumberOfValues, Row_Fixture) {

  // Given
  std::vector<Euclid::Table::Row::cell_type> values{std::string{"One"}, std::string{"Two"}, 3.};

  // Then
  BOOST_CHECK_THROW(Euclid::Table::Row(values, column_info), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for null column_info
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorNullColumnInfo, Row_Fixture) {

  // Given
  std::vector<Euclid::Table::Row::cell_type> values{std::string{"One"},           std::string{"Two"}, 3., 4., 5,
                                                    std::vector<double>{6.1, 6.2}};
  std::shared_ptr<Euclid::Table::ColumnInfo> null_col_info{};

  // Then
  BOOST_CHECK_THROW(Euclid::Table::Row(values, null_col_info), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for wrong cell type
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorWrongCellType, Row_Fixture) {

  // Given
  std::vector<Euclid::Table::Row::cell_type> values{std::string{"One"},           std::string{"Two"}, std::string{"Three"}, 4., 5,
                                                    std::vector<double>{6.1, 6.2}};

  // Then
  BOOST_CHECK_THROW(Euclid::Table::Row(values, column_info), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for empty string cell values
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorEmptyCellValue, Row_Fixture) {

  // Given
  std::vector<Euclid::Table::Row::cell_type> values{std::string{"One"}, std::string{""}, 3., 4., 5, std::vector<double>{6.1, 6.2}};

  // Then
  BOOST_CHECK_THROW(Euclid::Table::Row(values, column_info), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for cell values with whitespace chars
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorCellValueWithWhitespace, Row_Fixture) {

  // Given
  std::vector<Euclid::Table::Row::cell_type> space{std::string{"One"},           std::string{"Sp ace"}, 3., 4., 5,
                                                   std::vector<double>{6.1, 6.2}};
  std::vector<Euclid::Table::Row::cell_type> tab{std::string{"One"},           std::string{"T\tab"}, 3., 4., 5,
                                                 std::vector<double>{6.1, 6.2}};
  std::vector<Euclid::Table::Row::cell_type> carriage_return{
      std::string{"One"}, std::string{"Carriage\rReturn"}, 3., 4., 5, std::vector<double>{6.1, 6.2}};
  std::vector<Euclid::Table::Row::cell_type> new_line{std::string{"One"},           std::string{"New\nLine"}, 3., 4., 5,
                                                      std::vector<double>{6.1, 6.2}};
  std::vector<Euclid::Table::Row::cell_type> new_page{std::string{"One"},           std::string{"New\fPage"}, 3., 4., 5,
                                                      std::vector<double>{6.1, 6.2}};

  // Then
  [[maybe_unused]] Euclid::Table::Row row_with_spaces(space, column_info);
  [[maybe_unused]] Euclid::Table::Row row_with_tabs(tab, column_info);
  BOOST_CHECK_THROW(Euclid::Table::Row(carriage_return, column_info), Elements::Exception);
  BOOST_CHECK_THROW(Euclid::Table::Row(new_line, column_info), Elements::Exception);
  BOOST_CHECK_THROW(Euclid::Table::Row(new_page, column_info), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test the getColumnInfo method
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getColumnInfo, Row_Fixture) {

  // Given
  std::vector<Euclid::Table::Row::cell_type> values{std::string{"One"},           std::string{"Two"}, 3., 4., 5,
                                                    std::vector<double>{6.1, 6.2}};
  Euclid::Table::Row                         row{values, column_info};

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
  std::vector<Euclid::Table::Row::cell_type> values{std::string{"One"},           std::string{"Two"}, 3., 4., 5,
                                                    std::vector<double>{6.1, 6.2}};
  Euclid::Table::Row                         row{values, column_info};

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
  std::vector<Euclid::Table::Row::cell_type> values{std::string{"One"},           std::string{"Two"}, 3., 4., 5,
                                                    std::vector<double>{6.1, 6.2}};
  Euclid::Table::Row                         row{values, column_info};

  // When
  Euclid::Table::Row::cell_type value0 = row[0];
  Euclid::Table::Row::cell_type value1 = row[1];
  Euclid::Table::Row::cell_type value2 = row[2];
  Euclid::Table::Row::cell_type value3 = row[3];
  Euclid::Table::Row::cell_type value4 = row[4];
  Euclid::Table::Row::cell_type value5 = row[5];

  // Then
  BOOST_CHECK_EQUAL(value0, values[0]);
  BOOST_CHECK_EQUAL(value1, values[1]);
  BOOST_CHECK_EQUAL(value2, values[2]);
  BOOST_CHECK_EQUAL(value3, values[3]);
  BOOST_CHECK_EQUAL(value4, values[4]);
  BOOST_CHECK_EQUAL(value5, values[5]);
  BOOST_CHECK_THROW(row[6], Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test the operator[string]
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(StringBracketOperator, Row_Fixture) {

  // Given
  std::vector<Euclid::Table::Row::cell_type> values{std::string{"One"},           std::string{"Two"}, 3., 4., 5,
                                                    std::vector<double>{6.1, 6.2}};
  Euclid::Table::Row                         row{values, column_info};

  // When
  Euclid::Table::Row::cell_type value0 = row["First"];
  Euclid::Table::Row::cell_type value1 = row["Second"];
  Euclid::Table::Row::cell_type value2 = row["Third"];
  Euclid::Table::Row::cell_type value3 = row["Fourth"];
  Euclid::Table::Row::cell_type value4 = row["Fifth"];
  Euclid::Table::Row::cell_type value5 = row["Sixth"];

  // Then
  BOOST_CHECK_EQUAL(value0, values[0]);
  BOOST_CHECK_EQUAL(value1, values[1]);
  BOOST_CHECK_EQUAL(value2, values[2]);
  BOOST_CHECK_EQUAL(value3, values[3]);
  BOOST_CHECK_EQUAL(value4, values[4]);
  BOOST_CHECK_EQUAL(value5, values[5]);
  BOOST_CHECK_THROW(row["None"], Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test the iterator
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Iterator, Row_Fixture) {

  // Given
  std::vector<Euclid::Table::Row::cell_type> values{std::string{"One"},           std::string{"Two"}, 3., 4., 5,
                                                    std::vector<double>{6.1, 6.2}};
  Euclid::Table::Row                         row{values, column_info};
  auto                                       valuesIter = values.cbegin();

  // When
  for (auto cell : row) {
    // Then
    BOOST_CHECK_EQUAL(cell, *valuesIter);
    ++valuesIter;
  }
  BOOST_CHECK(valuesIter == values.cend());
}

//-----------------------------------------------------------------------------
// Test the copying of a row
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Copy, Row_Fixture) {

  // Given
  Euclid::Table::Row::cell_type source{std::string{"One"}};
  Euclid::Table::Row::cell_type target;

  // When
  Euclid::Table::Row::cell_type target_constructor{source};
  target = source;  // this will fail to compile if any of the cell_type variants can not be copy-assigned

  // Then
  BOOST_CHECK(target == source);
  BOOST_CHECK(target_constructor == source);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
