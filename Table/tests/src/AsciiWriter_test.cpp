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
      Euclid::Table::ColumnInfo::info_type("Boolean", typeid(bool)),
      Euclid::Table::ColumnInfo::info_type("ThisIsAVeryLongColumnName", typeid(std::string)),
      Euclid::Table::ColumnInfo::info_type("Integer", typeid(int32_t)),
      Euclid::Table::ColumnInfo::info_type("D", typeid(double)),
      Euclid::Table::ColumnInfo::info_type("F", typeid(float))
  };
  std::shared_ptr<Euclid::Table::ColumnInfo> column_info {new Euclid::Table::ColumnInfo {info_list}};
  std::vector<Euclid::Table::Row::cell_type> values0 {true, std::string{"Two-1"}, 1, 4.1, 0.f};
  Euclid::Table::Row row0 {values0, column_info};
  std::vector<Euclid::Table::Row::cell_type> values1 {false, std::string{"Two-2"}, 1234567890, 42e-16, 0.f};
  Euclid::Table::Row row1 {values1, column_info};
  std::vector<Euclid::Table::Row::cell_type> values2 {true, std::string{"Two-3"}, 234, 4.3, 0.f};
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
    "# Boolean ThisIsAVeryLongColumnName    Integer       D     F\n"
    "#    bool                    string        int  double float\n"
    "\n"
    "        1                     Two-1          1     4.1     0\n"
    "        0                     Two-2 1234567890 4.2e-15     0\n"
    "        1                     Two-3        234     4.3     0\n"
  );
  BOOST_CHECK_EQUAL(stream_double_slash.str(),
    "// Boolean ThisIsAVeryLongColumnName    Integer       D     F\n"
    "//    bool                    string        int  double float\n"
    "\n"
    "         1                     Two-1          1     4.1     0\n"
    "         0                     Two-2 1234567890 4.2e-15     0\n"
    "         1                     Two-3        234     4.3     0\n"
  );
  
}

//-----------------------------------------------------------------------------
// Test the write method without types line
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(writeNoTypes, AsciiWriter_Fixture) {
  
  // Given
  std::stringstream stream_hash {};
  std::stringstream stream_double_slash {};
  Euclid::Table::AsciiWriter writer_hash {};
  Euclid::Table::AsciiWriter writer_double_slash {"//"};
  
  // When
  writer_hash.write(stream_hash, table, false);
  writer_double_slash.write(stream_double_slash, table, false);
  
  // Then
  BOOST_CHECK_EQUAL(stream_hash.str(),
    "# Boolean ThisIsAVeryLongColumnName    Integer       D     F\n"
    "\n"
    "        1                     Two-1          1     4.1     0\n"
    "        0                     Two-2 1234567890 4.2e-15     0\n"
    "        1                     Two-3        234     4.3     0\n"
  );
  BOOST_CHECK_EQUAL(stream_double_slash.str(),
    "// Boolean ThisIsAVeryLongColumnName    Integer       D     F\n"
    "\n"
    "         1                     Two-1          1     4.1     0\n"
    "         0                     Two-2 1234567890 4.2e-15     0\n"
    "         1                     Two-3        234     4.3     0\n"
  );
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()