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
 * @file tests/src/AsciiReaderHelper_test.cpp
 * @date April 15, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "ElementsKernel/Exception.h"
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
  
  std::string column_descriptions {
    "# Column: First bool (unit1) - This is the first description\n"
    "# Column: Second boolean\n"
    "# Column: Third int (unit3)\n"
    "# Column: Fourth int32 - This is the fourth description\n"
  };
  
  std::string all_types {
    "# Column: Bool1 bool (unit1) - This is the first description\n"
    "# Column: Bool2 boolean\n"
    "# Column: Int1 int (unit3)\n"
    "# Column: Int2 int32 - This is the fourth description\n"
    "# Column: Long1 long\n"
    "# Column: Long2 int64\n"
    "# Column: Float float\n"
    "# Column: Double double\n"
    "# Column: String string\n"
    "# Column: DoubleVector [double]\n"
    "\n"
    "# Bool1 Bool2   Int1 Int2  Long1 Long2 Float Double String DoubleVector\n"
    "\n"
    "  true  t       1    2     3     4     5.    6.     7      1.1,1.2,1.3\n"
    "  yes   y       8    9     10    11    1.2   1.3    14     2.1,2.2,2.3,2.4\n"
    "  1     false   15   16    17    18    1.9   2.0    21     3.1,3.2,3.3\n"
    "  f     no      22   23    24    25    2.6   2.7    28     4.1,4.2\n"
    "  n     0       29   30    31    32    3.3   3.4    35     5.1,5.2\n"
  };
  
  std::string invalid_type {
    "# Column: First Wrong\n"
    "# Column: Second boolean\n"
    "# Column: Third int\n"
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
    Euclid::Table::StreamRewinder rewinder {stream};
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
  BOOST_CHECK_THROW(Euclid::Table::countColumns(stream, "#"), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the countColumns counts correctly
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(countColumns, AsciiReaderHelper_Fixture) {
  
  // Given
  std::stringstream stream {two_columns};
  
  // When
  size_t size = Euclid::Table::countColumns(stream, "#");
  
  // Then
  BOOST_CHECK_EQUAL(size, 2u);
  
}

//-----------------------------------------------------------------------------
// Test the countColumns rewinds the stream
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(countColumnsRewinds, AsciiReaderHelper_Fixture) {
  
  // Given
  std::stringstream stream {two_columns};
  
  // When
  Euclid::Table::countColumns(stream, "#");
  std::string line {};
  getline(stream, line);
  
  // Then
  BOOST_CHECK_EQUAL(line, "   # First Second");
  
}

//-----------------------------------------------------------------------------
// Test the autoDetectColumnDescriptions
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(autoDetectColumnDescriptions, AsciiReaderHelper_Fixture) {
  
  // Given
  std::stringstream stream {column_descriptions};
  
  // When
  auto result = Euclid::Table::autoDetectColumnDescriptions(stream, "#");
  
  // Then
  BOOST_CHECK_EQUAL(result.size(), 4);
  
  BOOST_CHECK_EQUAL(result.count("First"), 1);
  BOOST_CHECK_EQUAL(result.count("Second"), 1);
  BOOST_CHECK_EQUAL(result.count("Third"), 1);
  BOOST_CHECK_EQUAL(result.count("Fourth"), 1);
  
  BOOST_CHECK_EQUAL(result.at("First").name, "First");
  BOOST_CHECK_EQUAL(result.at("Second").name, "Second");
  BOOST_CHECK_EQUAL(result.at("Third").name, "Third");
  BOOST_CHECK_EQUAL(result.at("Fourth").name, "Fourth");
  
  BOOST_CHECK_EQUAL(result.at("First").type.name(), typeid(bool).name());
  BOOST_CHECK_EQUAL(result.at("Second").type.name(), typeid(bool).name());
  BOOST_CHECK_EQUAL(result.at("Third").type.name(), typeid(int).name());
  BOOST_CHECK_EQUAL(result.at("Fourth").type.name(), typeid(int).name());
  
  BOOST_CHECK_EQUAL(result.at("First").unit, "unit1");
  BOOST_CHECK_EQUAL(result.at("Second").unit, "");
  BOOST_CHECK_EQUAL(result.at("Third").unit, "unit3");
  BOOST_CHECK_EQUAL(result.at("Fourth").unit, "");
  
  BOOST_CHECK_EQUAL(result.at("First").description, "This is the first description");
  BOOST_CHECK_EQUAL(result.at("Second").description, "");
  BOOST_CHECK_EQUAL(result.at("Third").description, "");
  BOOST_CHECK_EQUAL(result.at("Fourth").description, "This is the fourth description");
  
}

//-----------------------------------------------------------------------------
// Test the autoDetectColumnDescriptions
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(autoDetectColumnDescriptions_duplicateName) {
  
  // Given
  std::stringstream stream {
    "# Column: First bool (unit1) - This is the first description\n"
    "# Column: Second boolean\n"
    "# Column: Third int (unit3)\n"
    "# Column: Second int32 - This is the fourth description\n"
  };
  
  // Then
  BOOST_CHECK_THROW(Euclid::Table::autoDetectColumnDescriptions(stream, "#"), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the autoDetectColumnDescriptions
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(autoDetectColumnDescriptions_invalidType) {
  
  // Given
  std::stringstream stream {
    "# Column: First bool (unit1) - This is the first description\n"
    "# Column: Second boolean\n"
    "# Column: Third inta (unit3)\n"
    "# Column: Fourth int32 - This is the fourth description\n"
  };
  
  // Then
  BOOST_CHECK_THROW(Euclid::Table::autoDetectColumnDescriptions(stream, "#"), Elements::Exception);
  
}

//-----------------------------------------------------------------------------
// Test the autoDetectColumnNames without names in stream
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(autoDetectColumnNamesNoNames, AsciiReaderHelper_Fixture) {
  
  // Given
  std::stringstream stream {no_names};
  
  // When
  auto names = Euclid::Table::autoDetectColumnNames(stream, "#", 5);
  
  // Then
  BOOST_CHECK_EQUAL(names.size(), 5u);
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
  auto names = Euclid::Table::autoDetectColumnNames(stream, "#", 5);
  
  // Then
  BOOST_CHECK_EQUAL(names.size(), 5u);
  BOOST_CHECK_EQUAL(names[0], "First");
  BOOST_CHECK_EQUAL(names[1], "Second");
  BOOST_CHECK_EQUAL(names[2], "Third");
  BOOST_CHECK_EQUAL(names[3], "Fourth");
  BOOST_CHECK_EQUAL(names[4], "Fifth");
  
}

//-----------------------------------------------------------------------------
// Test the autoDetectColumnNames with names in stream
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(autoDetectColumnNamesSuccess_fromDescription) {
  
  // Given
  std::stringstream stream {
    "# This is not a comment with the names\n"
    "# Column: First\n"
    "# Column: Second double\n"
    "# Column: Third (unit)\n"
    "# Comment in between\n"
    "# Column: Fourth\n"
    "# Column: Fifth - Description\n"
    "# Some more comments here\n"
    "\n"
    "1 2 3 4 5"};
  
  // When
  auto names = Euclid::Table::autoDetectColumnNames(stream, "#", 5);
  
  // Then
  BOOST_CHECK_EQUAL(names.size(), 5u);
  BOOST_CHECK_EQUAL(names[0], "First");
  BOOST_CHECK_EQUAL(names[1], "Second");
  BOOST_CHECK_EQUAL(names[2], "Third");
  BOOST_CHECK_EQUAL(names[3], "Fourth");
  BOOST_CHECK_EQUAL(names[4], "Fifth");
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(autoDetectColumnNames_descriptionsUnordered) {
  
  // Given
  std::stringstream stream {
    "# This is not a comment with the names\n"
    "# Column: First\n"
    "# Column: Fourth\n"
    "# Column: Second double\n"
    "# Column: Third (unit)\n"
    "# Column: Fifth - Description\n"
    "# Some more comments here\n"
    "\n"
    "# First Second Third Fourth Fifth\n"
    "1 2 3 4 5"};
  
  // When
  auto names = Euclid::Table::autoDetectColumnNames(stream, "#", 5);
  
  // Then
  BOOST_CHECK_EQUAL(names.size(), 5u);
  BOOST_CHECK_EQUAL(names[0], "First");
  BOOST_CHECK_EQUAL(names[1], "Second");
  BOOST_CHECK_EQUAL(names[2], "Third");
  BOOST_CHECK_EQUAL(names[3], "Fourth");
  BOOST_CHECK_EQUAL(names[4], "Fifth");
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(autoDetectColumnNames_descriptionsMissing) {
  
  // Given
  std::stringstream stream {
    "# This is not a comment with the names\n"
    "# Column: First\n"
    "# Column: Second double\n"
    "# Column: Third (unit)\n"
    "# Column: Fifth - Description\n"
    "# Some more comments here\n"
    "\n"
    "# First Second Third Fourth Fifth\n"
    "1 2 3 4 5"};
  
  // When
  auto names = Euclid::Table::autoDetectColumnNames(stream, "#", 5);
  
  // Then
  BOOST_CHECK_EQUAL(names.size(), 5u);
  BOOST_CHECK_EQUAL(names[0], "First");
  BOOST_CHECK_EQUAL(names[1], "Second");
  BOOST_CHECK_EQUAL(names[2], "Third");
  BOOST_CHECK_EQUAL(names[3], "Fourth");
  BOOST_CHECK_EQUAL(names[4], "Fifth");
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(autoDetectColumnNames_lessDescriptions) {
  
  // Given
  std::stringstream stream {
    "# This is not a comment with the names\n"
    "# Column: First\n"
    "# Column: Second double\n"
    "\n"
    "1 2 3 4 5"};
  
  // When
  auto names = Euclid::Table::autoDetectColumnNames(stream, "#", 5);
  
  // Then
  BOOST_CHECK_EQUAL(names.size(), 5u);
  BOOST_CHECK_EQUAL(names[0], "First");
  BOOST_CHECK_EQUAL(names[1], "Second");
  BOOST_CHECK_EQUAL(names[2], "col3");
  BOOST_CHECK_EQUAL(names[3], "col4");
  BOOST_CHECK_EQUAL(names[4], "col5");
  
}

//-----------------------------------------------------------------------------
// Test the autoDetectColumnNames throws exception for duplicate names
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(autoDetectColumnNamesDuplicate, AsciiReaderHelper_Fixture) {
  
  // Given
  std::stringstream stream {duplicate_names};
  
  // Then
  BOOST_CHECK_THROW(Euclid::Table::autoDetectColumnNames(stream, "#", 5), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
