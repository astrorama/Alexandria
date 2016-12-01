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
 * @file tests/src/AsciiWriter_test.cpp
 * @date 11/30/16
 * @author nikoapos
 */

#include <boost/test/unit_test.hpp>

#include "Table/AsciiWriter.h"


#include <iostream>
#include <fstream>

using namespace Euclid::Table;

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (AsciiWriter_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE( example_test ) {
  std::cout << "-------------------------\n";

  AsciiWriter writer = AsciiWriter::create(std::cout);
  
  writer.addComment("testing");
  writer.addComment("Another comment");
  writer.addComment("Another comment but now it has a\nnew line");
  
  std::vector<ColumnInfo::info_type> info_list {
      ColumnInfo::info_type("Column", typeid(int))
  };
  std::shared_ptr<ColumnInfo> column_info {new ColumnInfo {info_list}};
  
  Row row1 {{1}, column_info};
  Table table1 {{row1}};
  
  writer.addData(table1);

  std::cout << "-------------------------\n";
}
//
////-----------------------------------------------------------------------------
//
//BOOST_AUTO_TEST_CASE( example_test2) {
//
//  std::ofstream out_file {"/home/nikoapos/temp/testing.stream"};
//  AsciiWriter writer = AsciiWriter::create(out_file);
//  writer.addComment("testing\n");
//
//}
//
////-----------------------------------------------------------------------------
//
//BOOST_AUTO_TEST_CASE( example_test3) {
//
//  AsciiWriter writer = AsciiWriter::create<std::ofstream>("/home/nikoapos/temp/testing2.stream");
//  writer.addComment("testing2\n");
//
//}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


