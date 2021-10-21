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
#include "NdArray/NdArray.h"
#include "Table/ColumnInfo.h"
#include "Table/Row.h"
#include "Table/Table.h"
#include "src/lib/FitsWriterHelper.h"
#include <boost/test/unit_test.hpp>

using Euclid::NdArray::NdArray;

struct FitsWriterHelper_Fixture {
  std::vector<Euclid::Table::ColumnInfo::info_type> info_list{
      Euclid::Table::ColumnInfo::info_type("Boolean", typeid(bool)),
      Euclid::Table::ColumnInfo::info_type("Integer", typeid(int32_t)),
      Euclid::Table::ColumnInfo::info_type("Long", typeid(int64_t)),
      Euclid::Table::ColumnInfo::info_type("Float", typeid(float)),
      Euclid::Table::ColumnInfo::info_type("Double", typeid(double)),
      Euclid::Table::ColumnInfo::info_type("String", typeid(std::string)),
      Euclid::Table::ColumnInfo::info_type("VectorInt", typeid(std::vector<int32_t>)),
      Euclid::Table::ColumnInfo::info_type("VectorFloat", typeid(std::vector<float>)),
      Euclid::Table::ColumnInfo::info_type("NdArrayInt", typeid(NdArray<int64_t>)),
      Euclid::Table::ColumnInfo::info_type("NdArrayDouble", typeid(NdArray<double>)),
  };

  std::vector<Euclid::Table::Row::cell_type> values0{true,
                                                     1,
                                                     int64_t{123},
                                                     0.f,
                                                     0.,
                                                     std::string{"first"},
                                                     std::vector<int32_t>{1, 2, 3},
                                                     std::vector<float>{.4, .5},
                                                     NdArray<int64_t>({3, 2}, {1, 2, 3, 4, 5, 6}),
                                                     NdArray<double>({2, 2}, {.5, .6, .7, .8})};
  std::vector<Euclid::Table::Row::cell_type> values1{false,
                                                     12345,
                                                     int64_t{123456789},
                                                     2.3e-2f,
                                                     1.12345e-18,
                                                     std::string{"second"},
                                                     std::vector<int32_t>{8, 9, 10},
                                                     std::vector<float>{.11, .22},
                                                     NdArray<int64_t>({3, 2}, {9, 8, 7, 6, 5, 4}),
                                                     NdArray<double>({2, 2}, {.6, .4, .2, .1})

  };
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(FitsWriterHelper_test)

//-----------------------------------------------------------------------------
// Test the getAsciiFormatList method
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getAsciiFormatList, FitsWriterHelper_Fixture) {

  // The ASCII format does not support multidimensional outputs
  info_list.resize(6, Euclid::Table::ColumnDescription("x"));
  values0.resize(6);
  values1.resize(6);

  auto column_info = std::make_shared<Euclid::Table::ColumnInfo>(info_list);
  Euclid::Table::Row              row0{values0, column_info};
  Euclid::Table::Row              row1{values1, column_info};
  std::vector<Euclid::Table::Row> row_list{row0, row1};
  Euclid::Table::Table            table{row_list};

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

  auto column_info = std::make_shared<Euclid::Table::ColumnInfo>(info_list);
  Euclid::Table::Row              row0{values0, column_info};
  Euclid::Table::Row              row1{values1, column_info};
  std::vector<Euclid::Table::Row> row_list{row0, row1};
  Euclid::Table::Table            table{row_list};

  // When
  auto format_list = Euclid::Table::getBinaryFormatList(table);

  // Then
  BOOST_CHECK_EQUAL(format_list.size(), info_list.size());
  BOOST_CHECK_EQUAL(format_list[0], "L");
  BOOST_CHECK_EQUAL(format_list[1], "J");
  BOOST_CHECK_EQUAL(format_list[2], "K");
  BOOST_CHECK_EQUAL(format_list[3], "E");
  BOOST_CHECK_EQUAL(format_list[4], "D");
  BOOST_CHECK_EQUAL(format_list[5], "6A");
  BOOST_CHECK_EQUAL(format_list[6], "3J");
  BOOST_CHECK_EQUAL(format_list[7], "2E");
  BOOST_CHECK_EQUAL(format_list[8], "6K");
  BOOST_CHECK_EQUAL(format_list[9], "4D");

  BOOST_CHECK_EQUAL(getTDIM(table, 6), "");
  BOOST_CHECK_EQUAL(getTDIM(table, 7), "");
  BOOST_CHECK_EQUAL(getTDIM(table, 8), "(2,3)");
  BOOST_CHECK_EQUAL(getTDIM(table, 9), "(2,2)");
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
