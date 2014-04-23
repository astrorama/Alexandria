/** 
 * @file FitsWriter_test.cpp
 * @date April 23, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "ElementsKernel/ElementsException.h"
#include "ChTable/Table.h"
#include "ChTable/ColumnInfo.h"
#include "ChTable/Row.h"
#include "ChTable/FitsWriter.h"

struct FitsWriter_Fixture {
  std::vector<ChTable::ColumnInfo::info_type> info_list {
      ChTable::ColumnInfo::info_type("Boolean", typeid(bool)),
      ChTable::ColumnInfo::info_type("Integer", typeid(int32_t)),
      ChTable::ColumnInfo::info_type("Long", typeid(int64_t)),
      ChTable::ColumnInfo::info_type("Float", typeid(float)),
      ChTable::ColumnInfo::info_type("Double", typeid(double)),
      ChTable::ColumnInfo::info_type("String", typeid(std::string))
  };
  std::shared_ptr<ChTable::ColumnInfo> column_info {new ChTable::ColumnInfo {info_list}};
  std::vector<ChTable::Row::cell_type> values0 {true, 1, 123L, 0.F, 0., std::string{"first"}};
  ChTable::Row row0 {values0, column_info};
  std::vector<ChTable::Row::cell_type> values1 {false, 12345, 123456789L, 2.3e-2F, 1.12345e-18, std::string{"second"}};
  ChTable::Row row1 {values1, column_info};
  std::vector<ChTable::Row> row_list {row0, row1};
  ChTable::Table table {row_list};
  std::unique_ptr<CCfits::FITS> fits {new CCfits::FITS(
                    "!/tmp/FitsWriter_test.fits", CCfits::RWmode::Write)};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (FitsWriter_test)

//-----------------------------------------------------------------------------
// Test the write Binary
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(writeBinary, FitsWriter_Fixture) {
  
  // Given
  ChTable::FitsWriter writer (ChTable::FitsWriter::Format::BINARY);
  
  // When
  writer.write(*fits, "BinaryTable", table);
  auto& result = fits->extension("BinaryTable");
  
  // Then
  BOOST_CHECK_EQUAL(result.rows(), 2);
  BOOST_CHECK_EQUAL(result.numCols(), 6);
  
  BOOST_CHECK_EQUAL(result.column(1).name(), "Boolean");
  BOOST_CHECK_EQUAL(result.column(2).name(), "Integer");
  BOOST_CHECK_EQUAL(result.column(3).name(), "Long");
  BOOST_CHECK_EQUAL(result.column(4).name(), "Float");
  BOOST_CHECK_EQUAL(result.column(5).name(), "Double");
  BOOST_CHECK_EQUAL(result.column(6).name(), "String");
  
  BOOST_CHECK_EQUAL(result.column(1).format(), "L");
  BOOST_CHECK_EQUAL(result.column(2).format(), "J");
  BOOST_CHECK_EQUAL(result.column(3).format(), "K");
  BOOST_CHECK_EQUAL(result.column(4).format(), "E");
  BOOST_CHECK_EQUAL(result.column(5).format(), "D");
  BOOST_CHECK_EQUAL(result.column(6).format(), "6A");
  
  // When
  std::vector<bool> bool_data {};
  result.column(1).read(bool_data, 1, 2);
  
  // Then
  BOOST_CHECK_EQUAL(bool_data[0], true);
  BOOST_CHECK_EQUAL(bool_data[1], false);
  
  // When
  std::vector<int32_t> int_data {};
  result.column(2).read(int_data, 1, 2);
  
  // Then
  BOOST_CHECK_EQUAL(int_data[0], 1);
  BOOST_CHECK_EQUAL(int_data[1], 12345);
  
  // When
  std::vector<int64_t> long_data {};
  result.column(3).read(long_data, 1, 2);
  
  // Then
  BOOST_CHECK_EQUAL(long_data[0], 123);
  BOOST_CHECK_EQUAL(long_data[1], 123456789);
  
  // When
  std::vector<float> float_data {};
  result.column(4).read(float_data, 1, 2);
  
  // Then
  BOOST_CHECK_EQUAL(float_data[0], 0.F);
  BOOST_CHECK_EQUAL(float_data[1], 2.3e-2F);
  
  // When
  std::vector<double> double_data {};
  result.column(5).read(double_data, 1, 2);
  
  // Then
  BOOST_CHECK_EQUAL(double_data[0], 0.F);
  BOOST_CHECK_EQUAL(double_data[1], 1.12345e-18);
  
  // When
  std::vector<std::string> string_data {};
  result.column(6).read(string_data, 1, 2);
  
  // Then
  BOOST_CHECK_EQUAL(string_data[0], "first");
  BOOST_CHECK_EQUAL(string_data[1], "second");
  
}

//-----------------------------------------------------------------------------
// Test the write ASCII
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(writeAscii, FitsWriter_Fixture) {
  
  // Given
  ChTable::FitsWriter writer (ChTable::FitsWriter::Format::ASCII);
  
  // When
  writer.write(*fits, "AsciiTable", table);
  auto& result = fits->extension("AsciiTable");
  
  // Then
  BOOST_CHECK_EQUAL(result.rows(), 2);
  BOOST_CHECK_EQUAL(result.numCols(), 6);
  
  BOOST_CHECK_EQUAL(result.column(1).name(), "Boolean");
  BOOST_CHECK_EQUAL(result.column(2).name(), "Integer");
  BOOST_CHECK_EQUAL(result.column(3).name(), "Long");
  BOOST_CHECK_EQUAL(result.column(4).name(), "Float");
  BOOST_CHECK_EQUAL(result.column(5).name(), "Double");
  BOOST_CHECK_EQUAL(result.column(6).name(), "String");
  
  BOOST_CHECK_EQUAL(result.column(1).format(), "I1");
  BOOST_CHECK_EQUAL(result.column(2).format(), "I5");
  BOOST_CHECK_EQUAL(result.column(3).format(), "I9");
  BOOST_CHECK_EQUAL(result.column(4).format(), "E12");
  BOOST_CHECK_EQUAL(result.column(5).format(), "E12");
  BOOST_CHECK_EQUAL(result.column(6).format(), "A6");
  
  // When
  std::vector<int32_t> bool_data {};
  result.column(1).read(bool_data, 1, 2);
  
  // Then
  BOOST_CHECK_EQUAL(bool_data[0], 1);
  BOOST_CHECK_EQUAL(bool_data[1], 0);
  
  // When
  std::vector<int32_t> int_data {};
  result.column(2).read(int_data, 1, 2);
  
  // Then
  BOOST_CHECK_EQUAL(int_data[0], 1);
  BOOST_CHECK_EQUAL(int_data[1], 12345);
  
  // When
  std::vector<int64_t> long_data {};
  result.column(3).read(long_data, 1, 2);
  
  // Then
  BOOST_CHECK_EQUAL(long_data[0], 123);
  BOOST_CHECK_EQUAL(long_data[1], 123456789);
  
  // When
  std::vector<float> float_data {};
  result.column(4).read(float_data, 1, 2);
  
  // Then
  BOOST_CHECK_EQUAL(float_data[0], 0.F);
  BOOST_CHECK_EQUAL(float_data[1], 2.3e-2F);
  
  // When
  std::vector<double> double_data {};
  result.column(5).read(double_data, 1, 2);
  
  // Then
  BOOST_CHECK_EQUAL(double_data[0], 0.F);
  BOOST_CHECK_CLOSE(double_data[1], 1.12345e-18, 0.001);
  
  // When
  std::vector<std::string> string_data {};
  result.column(6).read(string_data, 1, 2);
  
  // Then
  BOOST_CHECK_EQUAL(string_data[0], "first");
  BOOST_CHECK_EQUAL(string_data[1], "second");
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
