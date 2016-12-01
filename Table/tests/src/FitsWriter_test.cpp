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
 * @file tests/src/FitsWriter_test.cpp
 * @date 12/01/16
 * @author nikoapos
 */

#include <boost/test/unit_test.hpp>

#include "Table/FitsWriter.h"

using namespace Euclid::Table;

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (FitsWriter_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE( example_test ) {
  FitsWriter writer = FitsWriter {"/home/nikoapos/temp/test.fits"};
//  writer.overrideFile(true);
//  writer.setHduName("Testing");
  
  writer.addComment("testing");
  writer.addComment("Another comment");
  writer.addComment("Another comment but now it has a\nnew line");
  
  std::vector<ColumnInfo::info_type> info_list {
      ColumnInfo::info_type("Column", typeid(int), "m", "This is a test")
  };
  std::shared_ptr<ColumnInfo> column_info {new ColumnInfo {info_list}};
  
  Row row1 {{1}, column_info};
  Row row2 {{2}, column_info};
  Table table1 {{row1, row2}};
  
  writer.addData(table1);

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


