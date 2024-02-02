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
 * @file tests/src/Table_test.cpp
 * @date April 9, 2014
 * @author Nikolaos Apostolakos
 */

#include "ElementsKernel/Exception.h"
#include "Table/Table.h"
#include "Table/TestHelper.h"
#include <boost/test/unit_test.hpp>

struct Table_Fixture {
  std::vector<Euclid::Table::ColumnInfo::info_type> info_list{
      Euclid::Table::ColumnInfo::info_type("First", typeid(std::string)),
      Euclid::Table::ColumnInfo::info_type("Second", typeid(std::string)),
      Euclid::Table::ColumnInfo::info_type("Third", typeid(double)),
      Euclid::Table::ColumnInfo::info_type("Fourth", typeid(double)),
      Euclid::Table::ColumnInfo::info_type("Fifth", typeid(int))};
  std::shared_ptr<Euclid::Table::ColumnInfo> column_info{new Euclid::Table::ColumnInfo{info_list}};
  std::vector<Euclid::Table::Row::cell_type> values0{std::string{"One-1"}, std::string{"Two-1"}, 3.1, 4.1, 51};
  Euclid::Table::Row                         row0{values0, column_info};
  std::vector<Euclid::Table::Row::cell_type> values1{std::string{"One-2"}, std::string{"Two-2"}, 3.2, 4.2, 52};
  Euclid::Table::Row                         row1{values1, column_info};
  std::vector<Euclid::Table::Row::cell_type> values2{std::string{"One-3"}, std::string{"Two-3"}, 3.3, 4.3, 53};
  Euclid::Table::Row                         row2{values2, column_info};
  std::vector<Euclid::Table::Row>            row_list{row0, row1, row2};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(ColumnInfo_test)

//-----------------------------------------------------------------------------
// Test the constructor throws an exception if any row has different column info
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorDifferentColumnInfo, Table_Fixture) {

  // Given
  std::vector<Euclid::Table::ColumnInfo::info_type> wrong_info_list{
      Euclid::Table::ColumnInfo::info_type("First", typeid(std::string))};
  std::shared_ptr<Euclid::Table::ColumnInfo> wrong_column_info{new Euclid::Table::ColumnInfo(wrong_info_list)};
  Euclid::Table::Row                         wrong_row({std::string{"Test"}}, wrong_column_info);
  std::vector<Euclid::Table::Row>            wrong_row_list{row_list.cbegin(), row_list.cend()};
  wrong_row_list.push_back(wrong_row);

  BOOST_CHECK_THROW(Euclid::Table::Table{wrong_row_list}, Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception if no rows are given
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorNoRows, Table_Fixture) {

  // Given
  std::vector<Euclid::Table::Row> wrong_row_list{};

  BOOST_CHECK_THROW(Euclid::Table::Table{wrong_row_list}, Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test the constructor with just metadata
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorColumnInfo, Table_Fixture) {
  Euclid::Table::Table table(column_info);
  BOOST_CHECK_EQUAL(table.getColumnInfo(), column_info);
  BOOST_CHECK_EQUAL(table.size(), 0);
  BOOST_CHECK(table.begin() == table.end());
}

//-----------------------------------------------------------------------------
// Test the getColumnInfo method
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getColumnInfo, Table_Fixture) {

  // Given
  Euclid::Table::Table table{row_list};

  // When
  auto result = table.getColumnInfo();

  // Then
  BOOST_CHECK(*result == *column_info);
}

//-----------------------------------------------------------------------------
// Test the size
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(size, Table_Fixture) {

  // Given
  Euclid::Table::Table table{row_list};

  // When
  std::size_t size_test_value = table.size();

  // Then
  BOOST_CHECK_EQUAL(size_test_value, row_list.size());
}

//-----------------------------------------------------------------------------
// Test the operator[]
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(BracketOperator, Table_Fixture) {

  // Given
  Euclid::Table::Table table{row_list};

  // When
  auto result0 = table[0];
  auto result1 = table[1];
  auto result2 = table[2];

  // Then
  for (std::size_t i = 0; i < column_info->size(); ++i) {
    BOOST_CHECK_EQUAL(result0[i], row0[i]);
    BOOST_CHECK_EQUAL(result1[i], row1[i]);
    BOOST_CHECK_EQUAL(result2[i], row2[i]);
  }
  BOOST_CHECK_THROW(table[3], Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test the iterator
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Iterator, Table_Fixture) {

  // Given
  Euclid::Table::Table table{row_list};
  auto                 rows_iter = row_list.cbegin();

  // When
  for (auto row : table) {
    // Then
    for (std::size_t i = 0; i < column_info->size(); ++i) {
      BOOST_CHECK_EQUAL(row[i], (*rows_iter)[i]);
    }
    ++rows_iter;
  }
  BOOST_CHECK(rows_iter == row_list.cend());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
