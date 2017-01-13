/** 
 * @file tests/src/AsciiWriter_test.cpp
 * @date April 11, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "ElementsKernel/Exception.h"
#include "Table/AsciiWriter.h"

struct AsciiWriter_Fixture {
  std::vector<Euclid::Table::ColumnInfo::info_type> info_list {
      Euclid::Table::ColumnInfo::info_type("Boolean", typeid(bool), "unit1", "Desc1"),
      Euclid::Table::ColumnInfo::info_type("ThisIsAVeryLongColumnName", typeid(std::string)),
      Euclid::Table::ColumnInfo::info_type("Integer", typeid(int32_t), "unit3"),
      Euclid::Table::ColumnInfo::info_type("D", typeid(double), "", "Desc4"),
      Euclid::Table::ColumnInfo::info_type("F", typeid(float)),
      Euclid::Table::ColumnInfo::info_type("DoubleVector", typeid(std::vector<double>))
  };
  std::shared_ptr<Euclid::Table::ColumnInfo> column_info {new Euclid::Table::ColumnInfo {info_list}};
  std::vector<Euclid::Table::Row::cell_type> values0 {true, std::string{"Two-1"}, 1, 4.1, 0.f, std::vector<double>{1.1, 1.2}};
  Euclid::Table::Row row0 {values0, column_info};
  std::vector<Euclid::Table::Row::cell_type> values1 {false, std::string{"Two-2"}, 1234567890, 42e-16, 0.f, std::vector<double>{2.1, 2.2}};
  Euclid::Table::Row row1 {values1, column_info};
  std::vector<Euclid::Table::Row::cell_type> values2 {true, std::string{"Two-3"}, 234, 4.3, 0.f, std::vector<double>{3.1, 3.2, 3.3, 3.4}};
  Euclid::Table::Row row2 {values2, column_info};
  std::vector<Euclid::Table::Row> row_list {row0, row1, row2};
  Euclid::Table::Table table {row_list};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (AsciiWriter_test)

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for empty comment
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorEmptyComment, AsciiWriter_Fixture) {
  
  // Given
  std::string comment = "";
  
  // Then
  BOOST_CHECK_THROW(Euclid::Table::AsciiWriter {comment}, Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the write method
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(write, AsciiWriter_Fixture) {
  
  // Given
  std::stringstream stream_hash {};
  std::stringstream stream_double_slash {};
  Euclid::Table::AsciiWriter writer_hash {};
  Euclid::Table::AsciiWriter writer_double_slash {"//"};
  
  // When
  writer_hash.write(stream_hash, table);
  writer_double_slash.write(stream_double_slash, table);
  
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
// Test the write method without column info comments
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(writeNoColumnInfo, AsciiWriter_Fixture) {
  
  // Given
  std::stringstream stream_hash {};
  std::stringstream stream_double_slash {};
  Euclid::Table::AsciiWriter writer_hash {};
  Euclid::Table::AsciiWriter writer_double_slash {"//"};
  
  // When
  writer_hash.write(stream_hash, table, {}, false);
  writer_double_slash.write(stream_double_slash, table, {}, false);
  
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
// Test the write method with comments
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(writeComments, AsciiWriter_Fixture) {
  
  // Given
  std::stringstream stream_hash {};
  std::stringstream stream_double_slash {};
  Euclid::Table::AsciiWriter writer_hash {};
  Euclid::Table::AsciiWriter writer_double_slash {"//"};
  std::vector<std::string> comments {
    "First comment",
    "Second comment"
  };
  
  // When
  writer_hash.write(stream_hash, table, comments);
  writer_double_slash.write(stream_double_slash, table, comments);
  
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