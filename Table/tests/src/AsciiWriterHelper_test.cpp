/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
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
 * @file tests/src/AsciiWriterHelper_test.cpp
 * @date April 11, 2014
 * @author Nikolaos Apostolakos
 */

#include "ElementsKernel/Exception.h"
#include "Table/ColumnInfo.h"
#include "Table/Row.h"
#include "Table/Table.h"
#include "src/lib/AsciiWriterHelper.h"
#include <boost/test/unit_test.hpp>

struct AsciiWriterHelper_Fixture {
  std::vector<Euclid::Table::ColumnInfo::info_type> info_list{
      Euclid::Table::ColumnInfo::info_type("Boolean", typeid(bool)),
      Euclid::Table::ColumnInfo::info_type("ThisIsAVeryLongColumnName", typeid(std::string)),
      Euclid::Table::ColumnInfo::info_type("Integer", typeid(int32_t)),
      Euclid::Table::ColumnInfo::info_type("D", typeid(double)),
      Euclid::Table::ColumnInfo::info_type("F", typeid(float)),
      Euclid::Table::ColumnInfo::info_type("DoubleVector", typeid(std::vector<double>))};
  std::shared_ptr<Euclid::Table::ColumnInfo> column_info{new Euclid::Table::ColumnInfo{info_list}};
  std::vector<Euclid::Table::Row::cell_type> values0{true, std::string{"Two-1"}, 1, 4.1, 0.f, std::vector<double>{1.1, 1.2}};
  Euclid::Table::Row                         row0{values0, column_info};
  std::vector<Euclid::Table::Row::cell_type> values1{false, std::string{"Two-2"},         1234567890, 42e-16,
                                                     0.f,   std::vector<double>{2.1, 2.2}};
  Euclid::Table::Row                         row1{values1, column_info};
  std::vector<Euclid::Table::Row::cell_type> values2{
      true, std::string{"Two-3"}, 234, 4.3, 0.f, std::vector<double>{3.1, 3.2, 3.3, 3.4}};
  Euclid::Table::Row              row2{values2, column_info};
  std::vector<Euclid::Table::Row> row_list{row0, row1, row2};
  Euclid::Table::Table            table{row_list};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(AsciiWriterHelper_test)

//-----------------------------------------------------------------------------
// Test the typeToKeyword
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(typeToKeyword, AsciiWriterHelper_Fixture) {

  // When
  std::string bool_key          = Euclid::Table::typeToKeyword(typeid(bool));
  std::string int32_key         = Euclid::Table::typeToKeyword(typeid(int32_t));
  std::string int64_key         = Euclid::Table::typeToKeyword(typeid(int64_t));
  std::string float_key         = Euclid::Table::typeToKeyword(typeid(float));
  std::string double_key        = Euclid::Table::typeToKeyword(typeid(double));
  std::string string_key        = Euclid::Table::typeToKeyword(typeid(std::string));
  std::string vector_bool_key   = Euclid::Table::typeToKeyword(typeid(std::vector<bool>));
  std::string vector_int32_key  = Euclid::Table::typeToKeyword(typeid(std::vector<int32_t>));
  std::string vector_int64_key  = Euclid::Table::typeToKeyword(typeid(std::vector<int64_t>));
  std::string vector_float_key  = Euclid::Table::typeToKeyword(typeid(std::vector<float>));
  std::string vector_double_key = Euclid::Table::typeToKeyword(typeid(std::vector<double>));

  // Then
  BOOST_CHECK_EQUAL(bool_key, "bool");
  BOOST_CHECK_EQUAL(int32_key, "int");
  BOOST_CHECK_EQUAL(int64_key, "long");
  BOOST_CHECK_EQUAL(float_key, "float");
  BOOST_CHECK_EQUAL(double_key, "double");
  BOOST_CHECK_EQUAL(string_key, "string");
  BOOST_CHECK_EQUAL(vector_bool_key, "[bool]");
  BOOST_CHECK_EQUAL(vector_int32_key, "[int]");
  BOOST_CHECK_EQUAL(vector_int64_key, "[long]");
  BOOST_CHECK_EQUAL(vector_float_key, "[float]");
  BOOST_CHECK_EQUAL(vector_double_key, "[double]");
}

//-----------------------------------------------------------------------------
// Test the calculateColumnLengths
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(calculateColumnLengths, AsciiWriterHelper_Fixture) {

  // When
  auto sizes = Euclid::Table::calculateColumnLengths(table);

  // Then
  BOOST_CHECK_EQUAL(sizes[0], 8);
  BOOST_CHECK_EQUAL(sizes[1], 26);
  BOOST_CHECK_EQUAL(sizes[2], 11);
  BOOST_CHECK_EQUAL(sizes[3], 8);
  BOOST_CHECK_EQUAL(sizes[4], 2);
  BOOST_CHECK_EQUAL(sizes[5], 16);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()