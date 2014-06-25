/** 
 * @file tests/src/AsciiReaderHelper_test.cpp
 * @date April 15, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "ElementsKernel/ElementsException.h"
#include "src/lib/AsciiReaderHelper.h"

struct AsciiReaderHelper_Fixture {
  std::string only_comments {
    "# First comment line\n"
    "# Second comment line\n"
    "# Third comment line"
  };
  
  std::string two_columns {
    "   # First Second\n"
    " \n"
    "  1.1E-12   Test  # Comment"
  };
  
  std::string no_names {
    "# This is a comment but with wrong number of words\n"
    "1 2 3 4 5"
  };
  
  std::string five_names {
    "# This is not a comment with the names\n"
    "# First Second# #Third #Fourth# Fifth\n"
    "#\n"
    "\n"
    "1 2 3 4 5"
  };
  
  std::string duplicate_names {
    "# This is not a comment with the names\n"
    "# First Second# #Third #Second# Fifth\n"
    "#\n"
    "\n"
    "1 2 3 4 5"
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
  
  std::string invalid_type {
    "# First Second# #Third #Second# Fifth\n"
    "# Wrong int int int int\n"
  };
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (AsciiReaderHelper_test)

//-----------------------------------------------------------------------------
// Test the StreamRewinder
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(StreamRewinder, AsciiReaderHelper_Fixture) {
  
  // Given
  std::stringstream stream {only_comments};
  
  // When
  std::string line;
  {
    getline(stream, line);
    ChTable::StreamRewinder rewinder {stream};
    getline(stream, line);
    getline(stream, line);
  }
  
  // Then
  BOOST_CHECK_EQUAL(line, "# Third comment line");
  getline(stream, line);
  BOOST_CHECK_EQUAL(line, "# Second comment line");
  
}

//-----------------------------------------------------------------------------
// Test the countColumns throws exception for no data lines
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(countColumnsNoDataLines, AsciiReaderHelper_Fixture) {
  
  // Given
  std::stringstream stream {only_comments};
  
  // Then
  BOOST_CHECK_THROW(ChTable::countColumns(stream, "#"), ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the countColumns counts correctly
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(countColumns, AsciiReaderHelper_Fixture) {
  
  // Given
  std::stringstream stream {two_columns};
  
  // When
  size_t size = ChTable::countColumns(stream, "#");
  
  // Then
  BOOST_CHECK_EQUAL(size, 2);
  
}

//-----------------------------------------------------------------------------
// Test the countColumns rewinds the stream
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(countColumnsRewinds, AsciiReaderHelper_Fixture) {
  
  // Given
  std::stringstream stream {two_columns};
  
  // When
  ChTable::countColumns(stream, "#");
  std::string line {};
  getline(stream, line);
  
  // Then
  BOOST_CHECK_EQUAL(line, "   # First Second");
  
}

//-----------------------------------------------------------------------------
// Test the autoDetectColumnNames without names in stream
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(autoDetectColumnNamesNoNames, AsciiReaderHelper_Fixture) {
  
  // Given
  std::stringstream stream {no_names};
  
  // When
  auto names = ChTable::autoDetectColumnNames(stream, "#", 5);
  
  // Then
  BOOST_CHECK_EQUAL(names.size(), 5);
  BOOST_CHECK_EQUAL(names[0], "col1");
  BOOST_CHECK_EQUAL(names[1], "col2");
  BOOST_CHECK_EQUAL(names[2], "col3");
  BOOST_CHECK_EQUAL(names[3], "col4");
  BOOST_CHECK_EQUAL(names[4], "col5");
  
}

//-----------------------------------------------------------------------------
// Test the autoDetectColumnNames with names in stream
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(autoDetectColumnNamesSuccess, AsciiReaderHelper_Fixture) {
  
  // Given
  std::stringstream stream {five_names};
  
  // When
  auto names = ChTable::autoDetectColumnNames(stream, "#", 5);
  
  // Then
  BOOST_CHECK_EQUAL(names.size(), 5);
  BOOST_CHECK_EQUAL(names[0], "First");
  BOOST_CHECK_EQUAL(names[1], "Second");
  BOOST_CHECK_EQUAL(names[2], "Third");
  BOOST_CHECK_EQUAL(names[3], "Fourth");
  BOOST_CHECK_EQUAL(names[4], "Fifth");
  
}

//-----------------------------------------------------------------------------
// Test the autoDetectColumnNames throws exception for duplicate names
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(autoDetectColumnNamesDuplicate, AsciiReaderHelper_Fixture) {
  
  // Given
  std::stringstream stream {duplicate_names};
  
  // Then
  BOOST_CHECK_THROW(ChTable::autoDetectColumnNames(stream, "#", 5), ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the autoDetectColumnTypes with types in stream
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(autoDetectColumnTypesSuccess, AsciiReaderHelper_Fixture) {
  
  // Given
  std::stringstream stream {all_types};
  
  // When
  auto types = ChTable::autoDetectColumnTypes(stream, "#", 9);
  
  // Then
  BOOST_CHECK_EQUAL(types.size(), 9);
  BOOST_CHECK(types[0] == typeid(bool));
  BOOST_CHECK(types[1] == typeid(bool));
  BOOST_CHECK(types[2] == typeid(int32_t));
  BOOST_CHECK(types[3] == typeid(int32_t));
  BOOST_CHECK(types[4] == typeid(int64_t));
  BOOST_CHECK(types[5] == typeid(int64_t));
  BOOST_CHECK(types[6] == typeid(float));
  BOOST_CHECK(types[7] == typeid(double));
  BOOST_CHECK(types[8] == typeid(std::string));
  
}

//-----------------------------------------------------------------------------
// Test the autoDetectColumnTypes without types in stream
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(autoDetectColumnTypesNoTypes, AsciiReaderHelper_Fixture) {
  
  // Given
  std::stringstream stream {five_names};
  
  // When
  auto types = ChTable::autoDetectColumnTypes(stream, "#", 5);
  
  // Then
  BOOST_CHECK_EQUAL(types.size(), 5);
  BOOST_CHECK(types[0] == typeid(std::string));
  BOOST_CHECK(types[1] == typeid(std::string));
  BOOST_CHECK(types[2] == typeid(std::string));
  BOOST_CHECK(types[3] == typeid(std::string));
  BOOST_CHECK(types[4] == typeid(std::string));
  
}

//-----------------------------------------------------------------------------
// Test the autoDetectColumnTypes throws exception for wrong type keywords
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(autoDetectColumnTypeWrongKeywords, AsciiReaderHelper_Fixture) {
  
  // Given
  std::stringstream stream {invalid_type};
  
  // Then
  BOOST_CHECK_THROW(ChTable::autoDetectColumnTypes(stream, "#", 5), ElementsException);
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()