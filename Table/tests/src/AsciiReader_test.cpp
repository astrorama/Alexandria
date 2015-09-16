/** 
 * @file tests/src/AsciiReader_test.cpp
 * @date April 11, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "ElementsKernel/Exception.h"
#include "Table/AsciiReader.h"

struct AsciiReader_Fixture {
  std::string only_hash_comments {
    "# This string contains no data\n"
    "# only hash comments"
  };
  std::string only_double_slash_comments {
    "// This string contains no data\n"
    "// only double slash comments"
  };
  std::string different_number_of_columns {
    "1 2 3 4 5\n"
    "1 2 3 4 5 6"
  };
  std::string duplicate_column_names {
    "# First Second Third Second Fifth\n"
    "  1     2      3     4      5"
  };
  std::string multiple_comments {
    "# This is a comment line before the column names\n"
    "\n"
    "# First Second Third Fourth Fifth\n"
    "# This is a comment line after the column names\n"
    "\n"
    "  1     2      3     4      5"
  };
  
  std::string all_types {
    "# Bool1 Bool2   Int1 Int2  Long1 Long2 Float Double String\n"
    "# Dummy line\n"
    "# bool #boolean int# int32 long  int64 float double string #\n"
    "# Trying to confuse with comments\n"
    "  true  t       1    2     3     4     5.    6.     7\n"
    "  yes   y       8    9     10    11    1.2   1.3    14\n"
    "  1     false   15   16    17    18    1.9   2.0    21\n"
    "  f     no      22   23    24    25    2.6   2.7    28\n"
    "  n     0       29   30    31    32    3.3   3.4    35\n"
  };
  
  std::string wrong_bool {
    "# Bool\n"
    "# bool\n"
    "  7"
  };
  
  std::string wrong_int32 {
    "# Int\n"
    "# int\n"
    "  7.2"
  };
  
  std::string wrong_int64 {
    "# Int\n"
    "# long\n"
    "  7.2"
  };
  
  std::string wrong_float {
    "# Float\n"
    "# float\n"
    "  true"
  };
  
  std::string wrong_double {
    "# Double\n"
    "# double\n"
    "  Something"
  };
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (AsciiReader_test)

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for empty comment
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorEmptyComment, AsciiReader_Fixture) {
  
  // Given
  std::string comment = "";
  
  // Then
  BOOST_CHECK_THROW(Euclid::Table::AsciiReader({} ,{} ,comment), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for duplicate column names
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorDuplicateColumnNames, AsciiReader_Fixture) {
  
  // Given
  std::vector<std::string> names {"First", "Second", "Third", "Second"};
  
  // Then
  BOOST_CHECK_THROW(Euclid::Table::AsciiReader({} , names), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for empty string column names
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorEmptyColumnNames, AsciiReader_Fixture) {
  
  // Given
  std::vector<std::string> names {"First", "Second", "", "Forth"};
  
  // Then
  BOOST_CHECK_THROW(Euclid::Table::AsciiReader({}, names), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for column names names with whitespaces
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorColumnNamesWithWhitespaces, AsciiReader_Fixture) {
  
  // Given
  std::vector<std::string> space {"Sp ace"};
  std::vector<std::string> tab {"T\tab"};
  std::vector<std::string> carriage_return {"Carriage\rReturn"};
  std::vector<std::string> new_line {"New\nLine"};
  std::vector<std::string> new_page {"New\fPage"};
  
  // Then
  BOOST_CHECK_THROW(Euclid::Table::AsciiReader({}, space), Elements::Exception);
  BOOST_CHECK_THROW(Euclid::Table::AsciiReader({}, tab), Elements::Exception);
  BOOST_CHECK_THROW(Euclid::Table::AsciiReader({}, carriage_return), Elements::Exception);
  BOOST_CHECK_THROW(Euclid::Table::AsciiReader({}, new_line), Elements::Exception);
  BOOST_CHECK_THROW(Euclid::Table::AsciiReader({}, new_page), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for column names and types of different sizes
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ConstructorColumnNameTypeDifferentSize, AsciiReader_Fixture) {
  
  // Given
  std::vector<std::string> names {"First", "Second"};
  std::vector<std::type_index> types {typeid(int)};
  
  // Then
  BOOST_CHECK_THROW(Euclid::Table::AsciiReader(types, names), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the read successfully all types
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadSuccess, AsciiReader_Fixture) {
  
  // Given
  Euclid::Table::AsciiReader reader {};
  std::stringstream in {all_types};
  
  // When
  Euclid::Table::Table table = reader.read(in);
  auto column_info = table.getColumnInfo();
  
  // Then
  BOOST_CHECK_EQUAL(column_info->getName(0), "Bool1");
  BOOST_CHECK_EQUAL(column_info->getName(1), "Bool2");
  BOOST_CHECK_EQUAL(column_info->getName(2), "Int1");
  BOOST_CHECK_EQUAL(column_info->getName(3), "Int2");
  BOOST_CHECK_EQUAL(column_info->getName(4), "Long1");
  BOOST_CHECK_EQUAL(column_info->getName(5), "Long2");
  BOOST_CHECK_EQUAL(column_info->getName(6), "Float");
  BOOST_CHECK_EQUAL(column_info->getName(7), "Double");
  BOOST_CHECK_EQUAL(column_info->getName(8), "String");
  BOOST_CHECK(column_info->getType(0) == typeid(bool));
  BOOST_CHECK(column_info->getType(1) == typeid(bool));
  BOOST_CHECK(column_info->getType(2) == typeid(int32_t));
  BOOST_CHECK(column_info->getType(3) == typeid(int32_t));
  BOOST_CHECK(column_info->getType(4) == typeid(int64_t));
  BOOST_CHECK(column_info->getType(5) == typeid(int64_t));
  BOOST_CHECK(column_info->getType(6) == typeid(float));
  BOOST_CHECK(column_info->getType(7) == typeid(double));
  BOOST_CHECK(column_info->getType(8) == typeid(std::string));
  
  BOOST_CHECK_EQUAL(boost::get<bool>(table[0][0]), true);
  BOOST_CHECK_EQUAL(boost::get<bool>(table[0][1]), true);
  BOOST_CHECK_EQUAL(boost::get<int32_t>(table[0][2]), 1);
  BOOST_CHECK_EQUAL(boost::get<int32_t>(table[0][3]), 2);
  BOOST_CHECK_EQUAL(boost::get<int64_t>(table[0][4]), 3);
  BOOST_CHECK_EQUAL(boost::get<int64_t>(table[0][5]), 4);
  BOOST_CHECK_EQUAL(boost::get<float>(table[0][6]), 5.);
  BOOST_CHECK_EQUAL(boost::get<double>(table[0][7]), 6.);
  BOOST_CHECK_EQUAL(boost::get<std::string>(table[0][8]), "7");
  BOOST_CHECK_EQUAL(boost::get<bool>(table[1][0]), true);
  BOOST_CHECK_EQUAL(boost::get<bool>(table[1][1]), true);
  BOOST_CHECK_EQUAL(boost::get<bool>(table[2][0]), true);
  BOOST_CHECK_EQUAL(boost::get<bool>(table[2][1]), false);
  BOOST_CHECK_EQUAL(boost::get<bool>(table[3][0]), false);
  BOOST_CHECK_EQUAL(boost::get<bool>(table[3][1]), false);
  BOOST_CHECK_EQUAL(boost::get<bool>(table[4][0]), false);
  BOOST_CHECK_EQUAL(boost::get<bool>(table[4][1]), false);
  
}

//-----------------------------------------------------------------------------
// Test the read with override types
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadOverrideTypes, AsciiReader_Fixture) {
  
  // Given
  Euclid::Table::AsciiReader reader {{typeid(bool), typeid(std::string), typeid(int32_t), typeid(int32_t), typeid(int32_t)}};
  std::stringstream in {multiple_comments};
  
  // When
  Euclid::Table::Table table = reader.read(in);
  auto column_info = table.getColumnInfo();
  
  // Then
  BOOST_CHECK(column_info->getType(0) == typeid(bool));
  BOOST_CHECK(column_info->getType(1) == typeid(std::string));
  BOOST_CHECK(column_info->getType(2) == typeid(int32_t));
  BOOST_CHECK(column_info->getType(3) == typeid(int32_t));
  BOOST_CHECK(column_info->getType(4) == typeid(int32_t));
  
}

//-----------------------------------------------------------------------------
// Test the read with override names
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadOverrideNames, AsciiReader_Fixture) {
  
  // Given
  Euclid::Table::AsciiReader reader {{}, {"A","B","C","D","E"}};
  std::stringstream in {multiple_comments};
  
  // When
  Euclid::Table::Table table = reader.read(in);
  auto column_info = table.getColumnInfo();
  
  // Then
  BOOST_CHECK_EQUAL(column_info->getName(0), "A");
  BOOST_CHECK_EQUAL(column_info->getName(1), "B");
  BOOST_CHECK_EQUAL(column_info->getName(2), "C");
  BOOST_CHECK_EQUAL(column_info->getName(3), "D");
  BOOST_CHECK_EQUAL(column_info->getName(4), "E");
  
}

//-----------------------------------------------------------------------------
// Test the read throws an exception for no data
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadNoData, AsciiReader_Fixture) {
  
  // Given
  Euclid::Table::AsciiReader hashReader {{},{},"#"};
  Euclid::Table::AsciiReader doubleSlashReader {{},{},"//"};
  std::stringstream in1 {only_hash_comments};
  std::stringstream in2 {only_double_slash_comments};
  
  // Then
  BOOST_CHECK_THROW(hashReader.read(in1), Elements::Exception);
  BOOST_CHECK_THROW(doubleSlashReader.read(in2), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the read throws an exception for wrong number of column names
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadWrongColumnNamesNumber, AsciiReader_Fixture) {
  
  // Given
  std::vector<std::string> wrong_names_less {"1","2","3"};
  std::vector<std::string> wrong_names_more {"1","2","3","4","5","6","7","8","9","10"};
  Euclid::Table::AsciiReader lessReader {{}, wrong_names_less};
  Euclid::Table::AsciiReader moreReader {{}, wrong_names_more};
  std::stringstream inless {all_types};
  std::stringstream inmore {all_types};
  
  // Then
  BOOST_CHECK_THROW(lessReader.read(inless), Elements::Exception);
  BOOST_CHECK_THROW(moreReader.read(inmore), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the read throws an exception for wrong number of column types
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadWrongColumnTypesNumber, AsciiReader_Fixture) {
  
  // Given
  std::vector<std::type_index> wrong_types_less {typeid(bool),typeid(bool),typeid(bool)};
  std::vector<std::type_index> wrong_types_more {typeid(bool),typeid(bool),typeid(bool),typeid(bool),
                                                 typeid(bool),typeid(bool),typeid(bool),typeid(bool),
                                                 typeid(bool),typeid(bool),typeid(bool),typeid(bool)};
  Euclid::Table::AsciiReader lessReader {wrong_types_less};
  Euclid::Table::AsciiReader moreReader {wrong_types_more};
  std::stringstream inless {all_types};
  std::stringstream inmore {all_types};
  
  // Then
  BOOST_CHECK_THROW(lessReader.read(inless), Elements::Exception);
  BOOST_CHECK_THROW(moreReader.read(inmore), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the read throws an exception for rows with different number of columns
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadDifferentNumberOfColumns, AsciiReader_Fixture) {
  
  // Given
  Euclid::Table::AsciiReader hashReader {};
  std::stringstream in {different_number_of_columns};
  
  // Then
  BOOST_CHECK_THROW(hashReader.read(in), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the read throws an exception for duplicate column names
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadDuplicateColumnNames, AsciiReader_Fixture) {
  
  // Given
  Euclid::Table::AsciiReader reader {};
  std::stringstream in {duplicate_column_names};
  
  // Then
  BOOST_CHECK_THROW(reader.read(in), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the read throws an exception for unconvertible cell values
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadWrongCellValues, AsciiReader_Fixture) {
  
  // Given
  Euclid::Table::AsciiReader reader {};
  std::stringstream bool_in {wrong_bool};
  std::stringstream int32_in {wrong_int32};
  std::stringstream int64_in {wrong_int64};
  std::stringstream float_in {wrong_float};
  std::stringstream double_in {wrong_double};
  
  // Then
  BOOST_CHECK_THROW(reader.read(bool_in), Elements::Exception);
  BOOST_CHECK_THROW(reader.read(int32_in), Elements::Exception);
  BOOST_CHECK_THROW(reader.read(int64_in), Elements::Exception);
  BOOST_CHECK_THROW(reader.read(float_in), Elements::Exception);
  BOOST_CHECK_THROW(reader.read(double_in), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()