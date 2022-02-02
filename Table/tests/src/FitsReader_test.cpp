/*
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
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
 * @file tests/src/FitsReader_test.cpp
 * @date 12/05/16
 * @author nikoapos
 */

#include <boost/test/unit_test.hpp>

#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Temporary.h"

#include "Table/FitsReader.h"

using namespace Euclid::Table;
using namespace Euclid::NdArray;

CCfits::Table* addTable(CCfits::FITS& fits) {

  std::vector<std::string> names{"Bool",      "Int",          "Long",    "String",  "Float",        "Double",
                                 "IntVector", "DoubleVector", "NdArray", "Double1", "VectorWithDim"};
  std::vector<std::string> types{"L", "J", "K", "10A", "E", "D", "2J", "2D", "6D", "1D", "4D"};
  std::vector<std::string> units{"deg", "mag", "erg", "ph", "s", "m", "pc", "count", "x", "x", "x"};
  CCfits::Table*           table_hdu = fits.addTable("Success", 2, names, types, units);
  std::vector<bool>        bool_values{true, false};
  table_hdu->column(1).write(bool_values, 1);
  std::vector<int32_t> int_values{3, -2346};
  table_hdu->column(2).write(int_values, 1);
  std::vector<int64_t> long_values{123456789, -6};
  table_hdu->column(3).write(long_values, 1);
  std::vector<std::string> string_values{"Small", "1234567890"};
  table_hdu->column(4).write(string_values, 1);
  std::vector<float> float_values{3.4f, 2.1e-3f};
  table_hdu->column(5).write(float_values, 1);
  std::vector<double> double_values{3.4, 2.1e-13};
  table_hdu->column(6).write(double_values, 1);
  std::vector<std::valarray<int32_t>> int_vectors{{1, 2}, {3, 4}};
  table_hdu->column(7).writeArrays(int_vectors, 1);
  std::vector<std::valarray<double>> double_vectors{{1.1, 1.2}, {2.1, 2.2}};
  table_hdu->column(8).writeArrays(double_vectors, 1);
  std::vector<std::valarray<double>> double_ndarrays{{1, 2, 3, 4, 5, 6}, {6, 5, 4, 3, 2, 1}};
  table_hdu->column(9).writeArrays(double_ndarrays, 1);
  table_hdu->column(10).write(double_values, 1);
  std::vector<std::valarray<double>> double2_values{{1., 10., 100., 1000.}, {2., 20., 200., 2000.}};
  table_hdu->column(11).writeArrays(double2_values, 1);

  for (int i = 1; i <= 9; i = i + 2) {
    table_hdu->addKey("TDESC" + std::to_string(i), "Desc" + std::to_string(i), "");
  }
  table_hdu->addKey("TDIM9", "(3,2)", "");
  table_hdu->addKey("TDIM11", "(4)", "");
  table_hdu->writeComment("TEST COMMENT\nWITH LINES");
  return table_hdu;
}

struct FitsReader_Fixture {

  Elements::TempDir             temp_dir;
  std::unique_ptr<CCfits::FITS> fits{
      new CCfits::FITS((temp_dir.path() / "FitsReader_test.fits").native(), CCfits::RWmode::Write)};
  const CCfits::PHDU& primary_hdu = fits->pHDU();
  std::vector<long>   image_size{2, 2};
  CCfits::ExtHDU*     image_hdu = fits->addImage("Image", FLOAT_IMG, image_size);
  CCfits::ExtHDU*     table_hdu = addTable(*fits);
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(FitsReader_test)

//-----------------------------------------------------------------------------
// Test the exception for duplicate column names
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(DuplicateColumnNames, FitsReader_Fixture) {

  // Given
  std::vector<std::string> names{"First", "Second", "Third", "Second"};

  // When
  FitsReader reader{*table_hdu};

  // Then
  BOOST_CHECK_THROW(reader.fixColumnNames(names), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test the exception for empty string column names
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(EmptyColumnNames, FitsReader_Fixture) {

  // Given
  std::vector<std::string> names{"First", "Second", "", "Forth"};

  // When
  FitsReader reader{*table_hdu};

  // Then
  BOOST_CHECK_THROW(reader.fixColumnNames(names), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test the exception for column names names with whitespaces
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ColumnNamesWithWhitespaces, FitsReader_Fixture) {

  // Given
  std::vector<std::string> space{"Sp ace"};
  std::vector<std::string> tab{"T\tab"};
  std::vector<std::string> carriage_return{"Carriage\rReturn"};
  std::vector<std::string> new_line{"New\nLine"};
  std::vector<std::string> new_page{"New\fPage"};

  // When
  FitsReader reader{*table_hdu};

  // Then
  BOOST_CHECK_THROW(reader.fixColumnNames(space), Elements::Exception);
  BOOST_CHECK_THROW(reader.fixColumnNames(tab), Elements::Exception);
  BOOST_CHECK_THROW(reader.fixColumnNames(carriage_return), Elements::Exception);
  BOOST_CHECK_THROW(reader.fixColumnNames(new_line), Elements::Exception);
  BOOST_CHECK_THROW(reader.fixColumnNames(new_page), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test the read throws exception for non table HDUs
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(readNonTable, FitsReader_Fixture) {

  // Given
  FitsReader reader_primary{primary_hdu};
  FitsReader reader_image{*image_hdu};

  // Then
  BOOST_CHECK_THROW(reader_primary.read(), Elements::Exception);
  BOOST_CHECK_THROW(reader_image.read(), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test the read throws exception for wrong number of column names
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadWrongColumnNamesNumber, FitsReader_Fixture) {

  // Given
  std::vector<std::string> names{"First", "Second"};
  FitsReader               reader{*table_hdu};

  // When
  reader.fixColumnNames(names);

  // Then
  BOOST_CHECK_THROW(reader.read(), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test the read successfully
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadSuccess, FitsReader_Fixture) {

  // Given
  FitsReader reader{*table_hdu};

  // When
  auto  table       = reader.read();
  auto& column_info = reader.getInfo();

  // Then
  BOOST_CHECK_EQUAL(column_info.size(), 11);
  BOOST_CHECK_EQUAL(column_info.getDescription(0).name, "Bool");
  BOOST_CHECK_EQUAL(column_info.getDescription(1).name, "Int");
  BOOST_CHECK_EQUAL(column_info.getDescription(2).name, "Long");
  BOOST_CHECK_EQUAL(column_info.getDescription(3).name, "String");
  BOOST_CHECK_EQUAL(column_info.getDescription(4).name, "Float");
  BOOST_CHECK_EQUAL(column_info.getDescription(5).name, "Double");
  BOOST_CHECK_EQUAL(column_info.getDescription(6).name, "IntVector");
  BOOST_CHECK_EQUAL(column_info.getDescription(7).name, "DoubleVector");
  BOOST_CHECK_EQUAL(column_info.getDescription(8).name, "NdArray");
  BOOST_CHECK_EQUAL(column_info.getDescription(9).name, "Double1");
  BOOST_CHECK_EQUAL(column_info.getDescription(10).name, "VectorWithDim");

  BOOST_CHECK(column_info.getDescription(0).type == typeid(bool));
  BOOST_CHECK(column_info.getDescription(1).type == typeid(int32_t));
  BOOST_CHECK(column_info.getDescription(2).type == typeid(int64_t));
  BOOST_CHECK(column_info.getDescription(3).type == typeid(std::string));
  BOOST_CHECK(column_info.getDescription(4).type == typeid(float));
  BOOST_CHECK(column_info.getDescription(5).type == typeid(double));
  BOOST_CHECK(column_info.getDescription(6).type == typeid(std::vector<int32_t>));
  BOOST_CHECK(column_info.getDescription(7).type == typeid(std::vector<double>));
  BOOST_CHECK(column_info.getDescription(8).type == typeid(NdArray<double>));
  BOOST_CHECK(column_info.getDescription(9).type == typeid(double));
  BOOST_CHECK(column_info.getDescription(10).type == typeid(std::vector<double>));

  BOOST_CHECK_EQUAL(column_info.getDescription(3).size, 10);

  std::vector<std::string> units{"deg", "mag", "erg", "ph", "s", "m", "pc", "count", "x", "x", "x"};
  for (size_t i = 0; i < column_info.size(); ++i) {
    BOOST_CHECK_EQUAL(column_info.getDescription(i).unit, units[i]);
  }

  std::vector<std::string> descriptions{"Desc1", "", "Desc3", "", "Desc5", "", "Desc7", "", "Desc9", "", ""};
  for (size_t i = 0; i < column_info.size(); ++i) {
    BOOST_CHECK_EQUAL(column_info.getDescription(i).description, descriptions[i]);
  }

  BOOST_CHECK_EQUAL(boost::get<bool>(table[0][0]), true);
  BOOST_CHECK_EQUAL(boost::get<int32_t>(table[0][1]), 3);
  BOOST_CHECK_EQUAL(boost::get<int64_t>(table[0][2]), 123456789);
  BOOST_CHECK_EQUAL(boost::get<std::string>(table[0][3]), "Small");
  BOOST_CHECK_EQUAL(boost::get<float>(table[0][4]), 3.4f);
  BOOST_CHECK_EQUAL(boost::get<double>(table[0][5]), 3.4);
  BOOST_CHECK_EQUAL(boost::get<bool>(table[1][0]), false);
  BOOST_CHECK_EQUAL(boost::get<int32_t>(table[1][1]), -2346);
  BOOST_CHECK_EQUAL(boost::get<int64_t>(table[1][2]), -6);
  BOOST_CHECK_EQUAL(boost::get<std::string>(table[1][3]), "1234567890");
  BOOST_CHECK_EQUAL(boost::get<float>(table[1][4]), 2.1e-3f);
  BOOST_CHECK_EQUAL(boost::get<double>(table[1][5]), 2.1e-13);
  BOOST_CHECK_EQUAL(boost::get<std::vector<int32_t>>(table[0][6]).size(), 2);
  BOOST_CHECK_EQUAL(boost::get<std::vector<int32_t>>(table[0][6])[0], 1);
  BOOST_CHECK_EQUAL(boost::get<std::vector<int32_t>>(table[0][6])[1], 2);
  BOOST_CHECK_EQUAL(boost::get<std::vector<int32_t>>(table[1][6]).size(), 2);
  BOOST_CHECK_EQUAL(boost::get<std::vector<int32_t>>(table[1][6])[0], 3);
  BOOST_CHECK_EQUAL(boost::get<std::vector<int32_t>>(table[1][6])[1], 4);
  BOOST_CHECK_EQUAL(boost::get<std::vector<double>>(table[0][7]).size(), 2);
  BOOST_CHECK_EQUAL(boost::get<std::vector<double>>(table[0][7])[0], 1.1);
  BOOST_CHECK_EQUAL(boost::get<std::vector<double>>(table[0][7])[1], 1.2);
  BOOST_CHECK_EQUAL(boost::get<std::vector<double>>(table[1][7]).size(), 2);
  BOOST_CHECK_EQUAL(boost::get<std::vector<double>>(table[1][7])[0], 2.1);
  BOOST_CHECK_EQUAL(boost::get<std::vector<double>>(table[1][7])[1], 2.2);
  BOOST_CHECK_EQUAL(boost::get<double>(table[0][9]), 3.4);
  BOOST_CHECK_EQUAL(boost::get<double>(table[1][9]), 2.1e-13);

  auto ndarray = boost::get<NdArray<double>>(table[1][8]);
  BOOST_CHECK_EQUAL(ndarray.shape()[0], 2);
  BOOST_CHECK_EQUAL(ndarray.shape()[1], 3);
  BOOST_CHECK_EQUAL(ndarray.at(0, 0), 6);
  BOOST_CHECK_EQUAL(ndarray.at(1, 2), 1);

  auto vector = boost::get<std::vector<double>>(table[1][10]);
  BOOST_CHECK_EQUAL(vector.size(), 4);

  BOOST_CHECK_EQUAL(reader.getComment(), "TEST COMMENT\nWITH LINES");
}

//-----------------------------------------------------------------------------
// Regression test for an off-by-one bug in hasMoreRows
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ReadInChunks_test, FitsReader_Fixture) {
  FitsReader reader{*table_hdu};
  BOOST_CHECK(reader.hasMoreRows());
  BOOST_CHECK_EQUAL(reader.rowsLeft(), 2);

  auto rows = reader.read(1);
  BOOST_CHECK_EQUAL(rows.size(), 1);
  BOOST_CHECK(reader.hasMoreRows());
  BOOST_CHECK_EQUAL(reader.rowsLeft(), 1);

  rows = reader.read(1);
  BOOST_CHECK_EQUAL(rows.size(), 1);
  BOOST_CHECK(!reader.hasMoreRows());
  BOOST_CHECK_EQUAL(reader.rowsLeft(), 0);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
