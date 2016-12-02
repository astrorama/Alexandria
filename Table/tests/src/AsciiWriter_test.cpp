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

#include "ElementsKernel/Exception.h"
#include "Table/AsciiWriter.h"


using namespace Euclid::Table;

struct AsciiWriter_Fixture {
  std::vector<ColumnInfo::info_type> info_list {
      ColumnInfo::info_type("Boolean", typeid(bool), "unit1", "Desc1"),
      ColumnInfo::info_type("ThisIsAVeryLongColumnName", typeid(std::string)),
      ColumnInfo::info_type("Integer", typeid(int32_t), "unit3"),
      ColumnInfo::info_type("D", typeid(double), "", "Desc4"),
      ColumnInfo::info_type("F", typeid(float)),
      ColumnInfo::info_type("DoubleVector", typeid(std::vector<double>))
  };
  std::shared_ptr<ColumnInfo> column_info {new ColumnInfo {info_list}};
  std::vector<Row::cell_type> values0 {true, std::string{"Two-1"}, 1, 4.1, 0.f, std::vector<double>{1.1, 1.2}};
  Row row0 {values0, column_info};
  std::vector<Row::cell_type> values1 {false, std::string{"Two-2"}, 1234567890, 42e-16, 0.f, std::vector<double>{2.1, 2.2}};
  Row row1 {values1, column_info};
  std::vector<Row::cell_type> values2 {true, std::string{"Two-3"}, 234, 4.3, 0.f, std::vector<double>{3.1, 3.2, 3.3, 3.4}};
  Row row2 {values2, column_info};
  std::vector<Row> row_list {row0, row1, row2};
  Table table {row_list};
};


//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (AsciiWriter_test)

//-----------------------------------------------------------------------------
// Test that setting the empty string as comment indicator throws exception
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(EmptyCommentIndicator) {
  
  // Given
  std::stringstream stream {};
  std::string comment = "";
  
  // When
  AsciiWriter writer {stream};
  
  // Then
  BOOST_CHECK_THROW(writer.setCommentIndicator(comment), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the addData method
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(addData, AsciiWriter_Fixture) {
  
  // Given
  std::stringstream stream_hash {};
  std::stringstream stream_double_slash {};
  AsciiWriter writer_hash {stream_hash};
  AsciiWriter writer_double_slash {stream_double_slash};
  writer_double_slash.setCommentIndicator("//");
  
  // When
  writer_hash.addData(table);
  writer_double_slash.addData(table);
  
  // Then
  BOOST_CHECK_EQUAL(stream_hash.str(),
    "# Column: Boolean bool (unit1) - Desc1\n"
    "# Column: ThisIsAVeryLongColumnName string\n"
    "# Column: Integer int (unit3)\n"
    "# Column: D double - Desc4\n"
    "# Column: F float\n"
    "# Column: DoubleVector [double]\n"
    "\n"
    "# Boolean ThisIsAVeryLongColumnName    Integer       D F    DoubleVector\n"
    "\n"
    "        1                     Two-1          1     4.1 0         1.1,1.2\n"
    "        0                     Two-2 1234567890 4.2e-15 0         2.1,2.2\n"
    "        1                     Two-3        234     4.3 0 3.1,3.2,3.3,3.4\n"
  );
  BOOST_CHECK_EQUAL(stream_double_slash.str(),
    "// Column: Boolean bool (unit1) - Desc1\n"
    "// Column: ThisIsAVeryLongColumnName string\n"
    "// Column: Integer int (unit3)\n"
    "// Column: D double - Desc4\n"
    "// Column: F float\n"
    "// Column: DoubleVector [double]\n"
    "\n"
    "// Boolean ThisIsAVeryLongColumnName    Integer       D F    DoubleVector\n"
    "\n"
    "         1                     Two-1          1     4.1 0         1.1,1.2\n"
    "         0                     Two-2 1234567890 4.2e-15 0         2.1,2.2\n"
    "         1                     Two-3        234     4.3 0 3.1,3.2,3.3,3.4\n"
  );
  
}

//-----------------------------------------------------------------------------
// Test the addData method without column info comments
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(addDataNoColumnInfo, AsciiWriter_Fixture) {
  
  // Given
  std::stringstream stream_hash {};
  std::stringstream stream_double_slash {};
  AsciiWriter writer_hash {stream_hash};
  AsciiWriter writer_double_slash {stream_double_slash};
  writer_double_slash.setCommentIndicator("//");
  
  // When
  writer_hash.showColumnInfo(false);
  writer_hash.addData(table);
  writer_double_slash.showColumnInfo(false);
  writer_double_slash.addData(table);
  
  // Then
  BOOST_CHECK_EQUAL(stream_hash.str(),
    "# Boolean ThisIsAVeryLongColumnName    Integer       D F    DoubleVector\n"
    "\n"
    "        1                     Two-1          1     4.1 0         1.1,1.2\n"
    "        0                     Two-2 1234567890 4.2e-15 0         2.1,2.2\n"
    "        1                     Two-3        234     4.3 0 3.1,3.2,3.3,3.4\n"
  );
  BOOST_CHECK_EQUAL(stream_double_slash.str(),
    "// Boolean ThisIsAVeryLongColumnName    Integer       D F    DoubleVector\n"
    "\n"
    "         1                     Two-1          1     4.1 0         1.1,1.2\n"
    "         0                     Two-2 1234567890 4.2e-15 0         2.1,2.2\n"
    "         1                     Two-3        234     4.3 0 3.1,3.2,3.3,3.4\n"
  );
  
}

//-----------------------------------------------------------------------------
// Test the addData method with comments
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(addDataComments, AsciiWriter_Fixture) {
  
  // Given
  std::stringstream stream_hash {};
  std::stringstream stream_double_slash {};
  AsciiWriter writer_hash {stream_hash};
  AsciiWriter writer_double_slash {stream_double_slash};
  writer_double_slash.setCommentIndicator("//");
  std::vector<std::string> comments {
    "First comment",
    "Second comment"
  };
  
  // When
  for (auto& c : comments) {
    writer_hash.addComment(c);
    writer_double_slash.addComment(c);
  }
  writer_hash.addData(table);
  writer_double_slash.addData(table);
  
  // Then
  BOOST_CHECK_EQUAL(stream_hash.str(),
    "# First comment\n"
    "# Second comment\n"
    "\n"
    "# Column: Boolean bool (unit1) - Desc1\n"
    "# Column: ThisIsAVeryLongColumnName string\n"
    "# Column: Integer int (unit3)\n"
    "# Column: D double - Desc4\n"
    "# Column: F float\n"
    "# Column: DoubleVector [double]\n"
    "\n"
    "# Boolean ThisIsAVeryLongColumnName    Integer       D F    DoubleVector\n"
    "\n"
    "        1                     Two-1          1     4.1 0         1.1,1.2\n"
    "        0                     Two-2 1234567890 4.2e-15 0         2.1,2.2\n"
    "        1                     Two-3        234     4.3 0 3.1,3.2,3.3,3.4\n"
  );
  BOOST_CHECK_EQUAL(stream_double_slash.str(),
    "// First comment\n"
    "// Second comment\n"
    "\n"
    "// Column: Boolean bool (unit1) - Desc1\n"
    "// Column: ThisIsAVeryLongColumnName string\n"
    "// Column: Integer int (unit3)\n"
    "// Column: D double - Desc4\n"
    "// Column: F float\n"
    "// Column: DoubleVector [double]\n"
    "\n"
    "// Boolean ThisIsAVeryLongColumnName    Integer       D F    DoubleVector\n"
    "\n"
    "         1                     Two-1          1     4.1 0         1.1,1.2\n"
    "         0                     Two-2 1234567890 4.2e-15 0         2.1,2.2\n"
    "         1                     Two-3        234     4.3 0 3.1,3.2,3.3,3.4\n"
  );
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


