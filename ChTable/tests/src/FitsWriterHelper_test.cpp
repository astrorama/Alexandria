/** 
 * @file FitsWriterHelper_test.cpp
 * @date April 23, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "ElementsKernel/ElementsException.h"
#include "ChTable/Table.h"
#include "ChTable/ColumnInfo.h"
#include "ChTable/Row.h"
#include "src/lib/FitsWriterHelper.h"

struct FitsWriterHelper_Fixture {
  std::vector<ChTable::ColumnInfo::info_type> info_list {
      ChTable::ColumnInfo::info_type("Boolean", typeid(bool)),
      ChTable::ColumnInfo::info_type("Integer", typeid(int32_t)),
      ChTable::ColumnInfo::info_type("Long", typeid(int64_t)),
      ChTable::ColumnInfo::info_type("Float", typeid(float)),
      ChTable::ColumnInfo::info_type("Double", typeid(double)),
      ChTable::ColumnInfo::info_type("String", typeid(std::string))
  };
  std::shared_ptr<ChTable::ColumnInfo> column_info {new ChTable::ColumnInfo {info_list}};
  std::vector<ChTable::Row::cell_type> values0 {true, 1, int64_t{123}, 0.f, 0., std::string{"first"}};
  ChTable::Row row0 {values0, column_info};
  std::vector<ChTable::Row::cell_type> values1 {false, 12345, int64_t{123456789}, 2.3e-2f, 1.12345e-18, std::string{"second"}};
  ChTable::Row row1 {values1, column_info};
  std::vector<ChTable::Row> row_list {row0, row1};
  ChTable::Table table {row_list};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (FitsWriterHelper_test)

//-----------------------------------------------------------------------------
// Test the getAsciiFormatList method
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getAsciiFormatList, FitsWriterHelper_Fixture) {

  // When
  auto format_list = ChTable::getAsciiFormatList(table);

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
  auto format_list = ChTable::getBinaryFormatList(table);

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

BOOST_AUTO_TEST_SUITE_END ()
