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
 * @file tests/src/FitsWriterHelper_test.cpp
 * @date April 23, 2014
 * @author Nikolaos Apostolakos
 */

#include "ElementsKernel/Exception.h"
#include "Table/ColumnInfo.h"
#include "Table/Row.h"
#include "Table/Table.h"
#include "src/lib/FitsWriterHelper.h"
#include <boost/test/unit_test.hpp>

struct FitsWriterHelper_Fixture {
  std::vector<Euclid::Table::ColumnInfo::info_type> info_list{Euclid::Table::ColumnInfo::info_type("Boolean", typeid(bool)),
                                                              Euclid::Table::ColumnInfo::info_type("Integer", typeid(int32_t)),
                                                              Euclid::Table::ColumnInfo::info_type("Long", typeid(int64_t)),
                                                              Euclid::Table::ColumnInfo::info_type("Float", typeid(float)),
                                                              Euclid::Table::ColumnInfo::info_type("Double", typeid(double)),
                                                              Euclid::Table::ColumnInfo::info_type("String", typeid(std::string))};
  std::shared_ptr<Euclid::Table::ColumnInfo>        column_info{new Euclid::Table::ColumnInfo{info_list}};
  std::vector<Euclid::Table::Row::cell_type>        values0{true, 1, int64_t{123}, 0.f, 0., std::string{"first"}};
  Euclid::Table::Row                                row0{values0, column_info};
  std::vector<Euclid::Table::Row::cell_type> values1{false, 12345, int64_t{123456789}, 2.3e-2f, 1.12345e-18, std::string{"second"}};
  Euclid::Table::Row                         row1{values1, column_info};
  std::vector<Euclid::Table::Row>            row_list{row0, row1};
  Euclid::Table::Table                       table{row_list};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(FitsWriterHelper_test)

//-----------------------------------------------------------------------------
// Test the getAsciiFormatList method
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getAsciiFormatList, FitsWriterHelper_Fixture) {

  // When
  auto format_list = Euclid::Table::getAsciiFormatList(table);

  // Then
  BOOST_CHECK_EQUAL(format_list.size(), 6);
  BOOST_CHECK_EQUAL(format_list[0], "I1");
  BOOST_CHECK_EQUAL(format_list[1], "I5");
  BOOST_CHECK_EQUAL(format_list[2], "I9");
  BOOST_CHECK_EQUAL(format_list[3], "E12");
  BOOST_CHECK_EQUAL(format_list[4], "E12");
  BOOST_CHECK_EQUAL(format_list[5], "A6");
}

//-----------------------------------------------------------------------------
// Test the getBinaryFormatList method
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getBinaryFormatList, FitsWriterHelper_Fixture) {

  // When
  auto format_list = Euclid::Table::getBinaryFormatList(table);

  // Then
  BOOST_CHECK_EQUAL(format_list.size(), 6);
  BOOST_CHECK_EQUAL(format_list[0], "L");
  BOOST_CHECK_EQUAL(format_list[1], "J");
  BOOST_CHECK_EQUAL(format_list[2], "K");
  BOOST_CHECK_EQUAL(format_list[3], "E");
  BOOST_CHECK_EQUAL(format_list[4], "D");
  BOOST_CHECK_EQUAL(format_list[5], "6A");
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
