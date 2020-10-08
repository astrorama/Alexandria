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
 * @file tests/src/TableWriter_test.cpp
 * @date 11/30/16
 * @author nikoapos
 */

#include "ElementsKernel/EnableGMock.h"
#include "ElementsKernel/Exception.h"
#include "Table/TableWriter.h"
#include <boost/test/unit_test.hpp>

using namespace Euclid::Table;
using namespace testing;

class MockTableWriter : public TableWriter {

public:
  MOCK_METHOD1(addComment, void(const std::string&));
  MOCK_METHOD1(init, void(const Table&));
  MOCK_METHOD1(append, void(const Table&));
};

struct TableWriter_Fixture {

  std::vector<ColumnInfo::info_type> info_list{ColumnInfo::info_type("Column", typeid(int))};
  std::shared_ptr<ColumnInfo>        column_info{new ColumnInfo{info_list}};

  Row   row1{{1}, column_info};
  Table table1{{row1}};

  Row   row2{{2}, column_info};
  Table table2{{row2}};

  Row   row3{{3}, column_info};
  Table table3{{row3}};

  std::vector<ColumnInfo::info_type> wrong_info_list{ColumnInfo::info_type("WrongColumn", typeid(int))};
  std::shared_ptr<ColumnInfo>        wrong_column_info{new ColumnInfo{wrong_info_list}};

  Row   wrong_row{{4}, wrong_column_info};
  Table wrong_table{{wrong_row}};
};

MATCHER_P(ColumnInfoFirstName, expected, "") {
  return arg.getColumnInfo()->getDescription(0).name == expected;
}

MATCHER_P(TableFirstValue, expected, "") {
  return boost::get<int>(arg[0][0]) == expected;
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(TableWriter_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(addDataSuccess_test, TableWriter_Fixture) {

  // Given
  MockTableWriter writer{};

  // Expect
  InSequence dummy;
  EXPECT_CALL(writer, init(ColumnInfoFirstName("Column"))).Times(1);
  EXPECT_CALL(writer, append(TableFirstValue(1))).Times(1);
  EXPECT_CALL(writer, append(TableFirstValue(2))).Times(1);
  EXPECT_CALL(writer, append(TableFirstValue(3))).Times(1);

  // When
  writer.addData(table1);
  writer.addData(table2);
  writer.addData(table3);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(addDataWrongColumn_test, TableWriter_Fixture) {

  // Given
  MockTableWriter writer{};

  // Expect
  InSequence dummy;
  EXPECT_CALL(writer, init(ColumnInfoFirstName("Column"))).Times(1);
  EXPECT_CALL(writer, append(TableFirstValue(1))).Times(1);

  // When
  writer.addData(table1);

  // Then
  BOOST_CHECK_THROW(writer.addData(wrong_table), Elements::Exception);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
