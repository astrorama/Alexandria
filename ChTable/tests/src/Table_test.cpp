/** 
 * @file tests/src/Table_test.cpp
 * @date April 9, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "ElementsKernel/ElementsException.h"
#include "ChTable/Table.h"

struct Table_Fixture {
  std::vector<ChTable::ColumnInfo::info_type> info_list {
      ChTable::ColumnInfo::info_type("First", typeid(std::string)),
      ChTable::ColumnInfo::info_type("Second", typeid(std::string)),
      ChTable::ColumnInfo::info_type("Third", typeid(double)),
      ChTable::ColumnInfo::info_type("Fourth", typeid(double)),
      ChTable::ColumnInfo::info_type("Fifth", typeid(int))
  };
  std::shared_ptr<ChTable::ColumnInfo> column_info {new ChTable::ColumnInfo {info_list}};
  std::vector<ChTable::Row::cell_type> values0 {std::string{"One-1"}, std::string{"Two-1"}, 3.1, 4.1, 51};
  ChTable::Row row0 {values0, column_info};
  std::vector<ChTable::Row::cell_type> values1 {std::string{"One-2"}, std::string{"Two-2"}, 3.2, 4.2, 52};
  ChTable::Row row1 {values1, column_info};
  std::vector<ChTable::Row::cell_type> values2 {std::string{"One-3"}, std::string{"Two-3"}, 3.3, 4.3, 53};
  ChTable::Row row2 {values2, column_info};
  std::vector<ChTable::Row> row_list {row0, row1, row2};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (ColumnInfo_test)

//-----------------------------------------------------------------------------
// Test the constructor throws an exception if any row has different column info
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorDifferentColumnInfo, Table_Fixture) {
  
  // Given
  std::vector<ChTable::ColumnInfo::info_type> wrong_info_list {
      ChTable::ColumnInfo::info_type("First", typeid(std::string))
  };
  std::shared_ptr<ChTable::ColumnInfo> wrong_column_info {new ChTable::ColumnInfo(wrong_info_list)};
  ChTable::Row wrong_row ({std::string{"Test"}}, wrong_column_info);
  std::vector<ChTable::Row> wrong_row_list {row_list.cbegin(), row_list.cend()};
  wrong_row_list.push_back(wrong_row);
  
  BOOST_CHECK_THROW(ChTable::Table{wrong_row_list}, ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception if no rows are given
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorNoRows, Table_Fixture) {
  
  // Given
  std::vector<ChTable::Row> wrong_row_list {};
  
  BOOST_CHECK_THROW(ChTable::Table{wrong_row_list}, ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the getColumnInfo method
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getColumnInfo, Table_Fixture) {
  
  // Given
  ChTable::Table table{row_list};
  
  // When
  auto result = table.getColumnInfo();
  
  // Then
  BOOST_CHECK(*result == *column_info);
  
}

//-----------------------------------------------------------------------------
// Test the size
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(size, Table_Fixture) {
  
  // Given
  ChTable::Table table{row_list};
  
  // When
  std::size_t size = table.size();
  
  // Then
  BOOST_CHECK_EQUAL(size, row_list.size());
  
}

//-----------------------------------------------------------------------------
// Test the operator[]
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(BracketOperator, Table_Fixture) {
  
  // Given
  ChTable::Table table{row_list};
  
  // When
  auto result0 = table[0];
  auto result1 = table[1];
  auto result2 = table[2];
  
  // Then
  for(std::size_t i=0; i<column_info->size(); ++i) {
    BOOST_CHECK_EQUAL(result0[i], row0[i]);
    BOOST_CHECK_EQUAL(result1[i], row1[i]);
    BOOST_CHECK_EQUAL(result2[i], row2[i]);
  }
  BOOST_CHECK_THROW(table[3], ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the iterator
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Iterator, Table_Fixture) {
  
  // Given
  ChTable::Table table{row_list};
  auto rows_iter = row_list.cbegin();
  
  // When
  for (auto row : table) {
    // Then
    for(std::size_t i=0; i<column_info->size(); ++i) {
      BOOST_CHECK_EQUAL(row[i], (*rows_iter)[i]);
    }
    ++rows_iter;
  }
  BOOST_CHECK(rows_iter == row_list.cend());
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()