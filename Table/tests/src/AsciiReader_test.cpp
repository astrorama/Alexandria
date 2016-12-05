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
 * @file tests/src/AsciiReader_test.cpp
 * @date 12/02/16
 * @author nikoapos
 */

#include <boost/test/unit_test.hpp>

#include "ElementsKernel/Exception.h"
#include "Table/AsciiReader.h"
#include "Table/TableWriter.h"

using namespace Euclid::Table;

struct AsciiReader_Fixture {
  std::string only_hash_comments {
    "# This string contains no data\n"
    "# only hash comments\n"
  };
  std::string only_double_slash_comments {
    "// This string contains no data\n"
    "// only double slash comments\n"
  };
  std::string different_number_of_columns {
    "1 2 3 4 5\n"
    "1 2 3 4 5 6\n"
  };
  std::string duplicate_column_names {
    "# First Second Third Second Fifth\n"
    "  1     2      3     4      5"
  };
  std::string multiple_comments {
    "# This is a comment line before the column names\n"
    "\n"
    "# First Second Third Fourth Fifth\n"
    "\n"
    "  1     2      3     4      5"
  };
  
  std::string all_types {
    "# Column: Bool1 bool\n"
    "# Column: Bool2 boolean\n"
    "# Column: Int1 int\n"
    "# Column: Int2 int32\n"
    "# Column: Long1 long\n"
    "# Column: Long2 int64\n"
    "# Column: Float float\n"
    "# Column: Double double\n"
    "# Column: String string\n"
    "# Column: DoubleVector [double]\n"
    "\n"
    "# Bool1 Bool2   Int1 Int2  Long1 Long2 Float Double String DoubleVector\n"
    "\n"
    "  true  t       1    2     3     4     5.    6.     7      1.1,1.2\n"
    "  yes   y       8    9     10    11    1.2   1.3    14     2.1,2.2,2.3\n"
    "  1     false   15   16    17    18    1.9   2.0    21     3.1,3.2\n"
    "  f     no      22   23    24    25    2.6   2.7    28     4.1,4.2,4.3\n"
    "  n     0       29   30    31    32    3.3   3.4    35     5.1\n"
  };
  
  std::string wrong_bool {
    "# Column: Bool bool\n"
    "  7"
  };
  
  std::string wrong_int32 {
    "# Column: Int int\n"
    "  7.2"
  };
  
  std::string wrong_int64 {
    "# Column: Int long\n"
    "  7.2"
  };
  
  std::string wrong_float {
    "# Column: Float float\n"
    "  true"
  };
  
  std::string wrong_double {
    "# Column: Double double\n"
    "  Something"
  };
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (AsciiReader_test)

//-----------------------------------------------------------------------------
// Test that setting empty comment indicator throws exception
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(EmptyCommentIndicator, AsciiReader_Fixture) {
  
  // Given
  std::string comment = "";
  std::stringstream in {all_types};
  
  // When
  AsciiReader reader {in};
  
  // Then
  BOOST_CHECK_THROW(reader.setCommentIndicator(comment), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test duplicate column names throw exception
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(DuplicateColumnNames, AsciiReader_Fixture) {
  
  // Given
  std::vector<std::string> names {"First", "Second", "Third", "Second"};
  std::stringstream in {all_types};
  
  // When
  AsciiReader reader {in};
  
  // Then
  BOOST_CHECK_THROW(reader.fixColumnNames(names), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test exception for empty string column names
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(EmptyColumnNames, AsciiReader_Fixture) {
  
  // Given
  std::vector<std::string> names {"First", "Second", "", "Forth"};
  std::stringstream in {all_types};
  
  // When
  AsciiReader reader {in};
  
  // Then
  BOOST_CHECK_THROW(reader.fixColumnNames(names), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test exception for column names names with whitespaces
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ColumnNamesWithWhitespaces, AsciiReader_Fixture) {
  
  // Given
  std::vector<std::string> space {"Sp ace"};
  std::vector<std::string> tab {"T\tab"};
  std::vector<std::string> carriage_return {"Carriage\rReturn"};
  std::vector<std::string> new_line {"New\nLine"};
  std::vector<std::string> new_page {"New\fPage"};
  std::stringstream in {all_types};
  
  // Then
  BOOST_CHECK_THROW(AsciiReader{in}.fixColumnNames(space), Elements::Exception);
  BOOST_CHECK_THROW(AsciiReader{in}.fixColumnNames(tab), Elements::Exception);
  BOOST_CHECK_THROW(AsciiReader{in}.fixColumnNames(carriage_return), Elements::Exception);
  BOOST_CHECK_THROW(AsciiReader{in}.fixColumnNames(new_line), Elements::Exception);
  BOOST_CHECK_THROW(AsciiReader{in}.fixColumnNames(new_page), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test exception for column names and types of different sizes
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ColumnNameTypeDifferentSize, AsciiReader_Fixture) {
  
  // Given
  std::vector<std::string> names {"First", "Second"};
  std::vector<std::type_index> types {typeid(int)};
  std::stringstream in {all_types};
  
  // Then
  BOOST_CHECK_THROW(AsciiReader{in}.fixColumnNames(names).fixColumnTypes(types), Elements::Exception);
  BOOST_CHECK_THROW(AsciiReader{in}.fixColumnTypes(types).fixColumnNames(names), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the read successfully all types
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadSuccess, AsciiReader_Fixture) {
  
  // Given
  std::stringstream in {all_types};
  
  // When
  AsciiReader reader {in};
  Euclid::Table::Table table = reader.read();
  auto column_info = table.getColumnInfo();
  
  // Then
  BOOST_CHECK_EQUAL(column_info->getDescription(0).name, "Bool1");
  BOOST_CHECK_EQUAL(column_info->getDescription(1).name, "Bool2");
  BOOST_CHECK_EQUAL(column_info->getDescription(2).name, "Int1");
  BOOST_CHECK_EQUAL(column_info->getDescription(3).name, "Int2");
  BOOST_CHECK_EQUAL(column_info->getDescription(4).name, "Long1");
  BOOST_CHECK_EQUAL(column_info->getDescription(5).name, "Long2");
  BOOST_CHECK_EQUAL(column_info->getDescription(6).name, "Float");
  BOOST_CHECK_EQUAL(column_info->getDescription(7).name, "Double");
  BOOST_CHECK_EQUAL(column_info->getDescription(8).name, "String");
  BOOST_CHECK_EQUAL(column_info->getDescription(9).name, "DoubleVector");
  BOOST_CHECK(column_info->getDescription(0).type == typeid(bool));
  BOOST_CHECK(column_info->getDescription(1).type == typeid(bool));
  BOOST_CHECK(column_info->getDescription(2).type == typeid(int32_t));
  BOOST_CHECK(column_info->getDescription(3).type == typeid(int32_t));
  BOOST_CHECK(column_info->getDescription(4).type == typeid(int64_t));
  BOOST_CHECK(column_info->getDescription(5).type == typeid(int64_t));
  BOOST_CHECK(column_info->getDescription(6).type == typeid(float));
  BOOST_CHECK(column_info->getDescription(7).type == typeid(double));
  BOOST_CHECK(column_info->getDescription(8).type == typeid(std::string));
  BOOST_CHECK(column_info->getDescription(9).type == typeid(std::vector<double>));
  
  BOOST_CHECK_EQUAL(boost::get<bool>(table[0][0]), true);
  BOOST_CHECK_EQUAL(boost::get<bool>(table[0][1]), true);
  BOOST_CHECK_EQUAL(boost::get<int32_t>(table[0][2]), 1);
  BOOST_CHECK_EQUAL(boost::get<int32_t>(table[0][3]), 2);
  BOOST_CHECK_EQUAL(boost::get<int64_t>(table[0][4]), 3);
  BOOST_CHECK_EQUAL(boost::get<int64_t>(table[0][5]), 4);
  BOOST_CHECK_EQUAL(boost::get<float>(table[0][6]), 5.);
  BOOST_CHECK_EQUAL(boost::get<double>(table[0][7]), 6.);
  BOOST_CHECK_EQUAL(boost::get<std::string>(table[0][8]), "7");
  BOOST_CHECK_EQUAL(boost::get<std::vector<double>>(table[0][9]).size(), 2);
  BOOST_CHECK_EQUAL(boost::get<std::vector<double>>(table[0][9])[0], 1.1);
  BOOST_CHECK_EQUAL(boost::get<std::vector<double>>(table[0][9])[1], 1.2);
  BOOST_CHECK_EQUAL(boost::get<bool>(table[1][0]), true);
  BOOST_CHECK_EQUAL(boost::get<bool>(table[1][1]), true);
  BOOST_CHECK_EQUAL(boost::get<bool>(table[2][0]), true);
  BOOST_CHECK_EQUAL(boost::get<bool>(table[2][1]), false);
  BOOST_CHECK_EQUAL(boost::get<bool>(table[3][0]), false);
  BOOST_CHECK_EQUAL(boost::get<bool>(table[3][1]), false);
  BOOST_CHECK_EQUAL(boost::get<bool>(table[4][0]), false);
  BOOST_CHECK_EQUAL(boost::get<bool>(table[4][1]), false);
  BOOST_CHECK_EQUAL(boost::get<std::vector<double>>(table[3][9]).size(), 3);
  BOOST_CHECK_EQUAL(boost::get<std::vector<double>>(table[3][9])[0], 4.1);
  BOOST_CHECK_EQUAL(boost::get<std::vector<double>>(table[3][9])[1], 4.2);
  BOOST_CHECK_EQUAL(boost::get<std::vector<double>>(table[3][9])[2], 4.3);
  
}

//-----------------------------------------------------------------------------
// Test the read with override types
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadOverrideTypes, AsciiReader_Fixture) {
  
  // Given
  std::vector<std::type_index> types {typeid(bool), typeid(std::string), typeid(int32_t), typeid(int32_t), typeid(int32_t)};
  std::stringstream in {multiple_comments};
  
  // When
  AsciiReader reader {in};
  reader.fixColumnTypes(types);
  Table table = reader.read();
  auto column_info = table.getColumnInfo();
  
  // Then
  BOOST_CHECK(column_info->getDescription(0).type == typeid(bool));
  BOOST_CHECK(column_info->getDescription(1).type == typeid(std::string));
  BOOST_CHECK(column_info->getDescription(2).type == typeid(int32_t));
  BOOST_CHECK(column_info->getDescription(3).type == typeid(int32_t));
  BOOST_CHECK(column_info->getDescription(4).type == typeid(int32_t));
  
}

//-----------------------------------------------------------------------------
// Test the read with override names
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadOverrideNames, AsciiReader_Fixture) {
  
  // Given
  std::vector<std::string> names {"A","B","C","D","E"};
  std::stringstream in {multiple_comments};
  
  // When
  AsciiReader reader {in};
  reader.fixColumnNames(names);
  Table table = reader.read();
  auto column_info = table.getColumnInfo();
  
  // Then
  BOOST_CHECK_EQUAL(column_info->getDescription(0).name, "A");
  BOOST_CHECK_EQUAL(column_info->getDescription(1).name, "B");
  BOOST_CHECK_EQUAL(column_info->getDescription(2).name, "C");
  BOOST_CHECK_EQUAL(column_info->getDescription(3).name, "D");
  BOOST_CHECK_EQUAL(column_info->getDescription(4).name, "E");
  
}

//-----------------------------------------------------------------------------
// Test the read throws an exception for no data
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadNoData, AsciiReader_Fixture) {
  
  // Given
  std::stringstream in1 {only_hash_comments};
  std::stringstream in2 {only_double_slash_comments};
  
  // When
  AsciiReader hashReader {in1};
  hashReader.setCommentIndicator("#");
  AsciiReader doubleSlashReader {in2};
  doubleSlashReader.setCommentIndicator("//");
  
  // Then
  BOOST_CHECK_THROW(hashReader.read(), Elements::Exception);
  BOOST_CHECK_THROW(doubleSlashReader.read(), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the read throws an exception for wrong number of column names
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadWrongColumnNamesNumber, AsciiReader_Fixture) {
  
  // Given
  std::vector<std::string> wrong_names_less {"1","2","3"};
  std::vector<std::string> wrong_names_more {"1","2","3","4","5","6","7","8","9","10","11"};
  std::stringstream inless {all_types};
  std::stringstream inmore {all_types};
  
  // When
  AsciiReader lessReader {inless};
  lessReader.fixColumnNames(wrong_names_less);
  AsciiReader moreReader {inmore};
  moreReader.fixColumnNames(wrong_names_more);
  
  // Then
  BOOST_CHECK_THROW(lessReader.read(), Elements::Exception);
  BOOST_CHECK_THROW(moreReader.read(), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the read throws an exception for wrong number of column types
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadWrongColumnTypesNumber, AsciiReader_Fixture) {
  
  // Given
  std::vector<std::type_index> wrong_types_less {typeid(bool),typeid(bool),typeid(bool)};
  std::vector<std::type_index> wrong_types_more {typeid(bool),typeid(bool),typeid(bool),typeid(bool),
                                                 typeid(bool),typeid(bool),typeid(bool),typeid(bool),
                                                 typeid(bool),typeid(bool),typeid(bool),typeid(bool)};
  std::stringstream inless {all_types};
  std::stringstream inmore {all_types};
  
  // When
  AsciiReader lessReader {inless};
  lessReader.fixColumnTypes(wrong_types_less);
  AsciiReader moreReader {inmore};
  moreReader.fixColumnTypes(wrong_types_more);
  
  // Then
  BOOST_CHECK_THROW(lessReader.read(), Elements::Exception);
  BOOST_CHECK_THROW(moreReader.read(), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the read throws an exception for rows with different number of columns
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadDifferentNumberOfColumns, AsciiReader_Fixture) {
  
  // Given
  std::stringstream in {different_number_of_columns};
  
  //When
  AsciiReader reader {in};
  
  // Then
  BOOST_CHECK_THROW(reader.read(), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the read throws an exception for duplicate column names
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadDuplicateColumnNames, AsciiReader_Fixture) {
  
  // Given
  std::stringstream in {duplicate_column_names};
  
  //When
  AsciiReader reader {in};
  
  // Then
  BOOST_CHECK_THROW(reader.read(), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the read throws an exception for unconvertible cell values
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadWrongCellValues, AsciiReader_Fixture) {
  
  // Given
  std::stringstream bool_in {wrong_bool};
  std::stringstream int32_in {wrong_int32};
  std::stringstream int64_in {wrong_int64};
  std::stringstream float_in {wrong_float};
  std::stringstream double_in {wrong_double};
  
  // Then
  BOOST_CHECK_THROW(AsciiReader{bool_in}.read(), Elements::Exception);
  BOOST_CHECK_THROW(AsciiReader{int32_in}.read(), Elements::Exception);
  BOOST_CHECK_THROW(AsciiReader{int64_in}.read(), Elements::Exception);
  BOOST_CHECK_THROW(AsciiReader{float_in}.read(), Elements::Exception);
  BOOST_CHECK_THROW(AsciiReader{double_in}.read(), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


