/**
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
 * @file tests/src/FitsWriter_test.cpp
 * @date 12/01/16
 * @author nikoapos
 */

#include "ElementsKernel/Temporary.h"
#include "Table/FitsWriter.h"
#include <CCfits/CCfits>
#include <boost/test/unit_test.hpp>

using namespace Euclid::Table;
using namespace Euclid::NdArray;

struct BinaryFitsWriter_Fixture {
  std::vector<ColumnInfo::info_type> info_list{
      ColumnInfo::info_type("Boolean", typeid(bool), "deg", "Desc1"),
      ColumnInfo::info_type("Integer", typeid(int32_t), "mag", "Desc2"),
      ColumnInfo::info_type("Long", typeid(int64_t), "", "Desc3"),
      ColumnInfo::info_type("Float", typeid(float), "ph", "Desc4"),
      ColumnInfo::info_type("Double", typeid(double), "s", "Desc5"),
      ColumnInfo::info_type("String", typeid(std::string), "m", "Desc6"),
      ColumnInfo::info_type("NdArray", typeid(NdArray<double>), "x", "Desc7"),
      ColumnInfo::info_type("ScalarNdArray", typeid(NdArray<double>), "x", "Desc8"),
      ColumnInfo::info_type("Vector", typeid(std::vector<float>), "", "Desc9"),
  };
  std::shared_ptr<ColumnInfo> column_info{new ColumnInfo{info_list}};
  std::vector<Row::cell_type> values0{true,
                                      1,
                                      int64_t{123},
                                      0.F,
                                      0.,
                                      std::string{"first"},
                                      NdArray<double>({2, 3}, {1, 2, 3, 4, 5, 6}),
                                      NdArray<double>({1}, std::vector<double>{41.}),
                                      std::vector<float>{1.5, 2.6, 3.7}};
  Row                         row0{values0, column_info};
  std::vector<Row::cell_type> values1{false,
                                      12345,
                                      int64_t{123456789},
                                      2.3e-2F,
                                      1.12345e-18,
                                      std::string{"second with spaces on top of that"},
                                      NdArray<double>({2, 3}, {6, 5, 4, 3, 2, 1}),
                                      NdArray<double>({1}, std::vector<double>{42.}),
                                      std::vector<float>{4.8, 5.9, 6.1}};
  Row                         row1{values1, column_info};
  std::vector<Row>            row_list{row0, row1};
  Table                       table{row_list};
  Table                       empty_table{column_info};
  Elements::TempDir           temp_dir;
  std::string                 fits_file_path = (temp_dir.path() / "FitsWriter_test.fits").native();
};

struct AsciiFitsWriter_Fixture {
  std::vector<ColumnInfo::info_type> info_list{ColumnInfo::info_type("Boolean", typeid(bool), "deg", "Desc1"),
                                               ColumnInfo::info_type("Integer", typeid(int32_t), "mag", "Desc2"),
                                               ColumnInfo::info_type("Long", typeid(int64_t), "", "Desc3"),
                                               ColumnInfo::info_type("Float", typeid(float), "ph", "Desc4"),
                                               ColumnInfo::info_type("Double", typeid(double), "s", "Desc5"),
                                               ColumnInfo::info_type("String", typeid(std::string), "m", "Desc6")};
  std::shared_ptr<ColumnInfo>        column_info{new ColumnInfo{info_list}};
  std::vector<Row::cell_type>        values0{true, 1, int64_t{123}, 0.F, 0., std::string{"first"}};
  Row                                row0{values0, column_info};
  std::vector<Row::cell_type>        values1{false,   12345,       int64_t{123456789},
                                      2.3e-2F, 1.12345e-18, std::string{"very spaced"}};
  Row                                row1{values1, column_info};
  std::vector<Row>                   row_list{row0, row1};
  Table                              table{row_list};
  Table                              empty_table{column_info};
  Elements::TempDir                  temp_dir;
  std::string                        fits_file_path = (temp_dir.path() / "FitsWriter_test.fits").native();
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(FitsWriter_test)

//-----------------------------------------------------------------------------
// Test the write Binary
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(writeBinary, BinaryFitsWriter_Fixture) {

  // Given
  FitsWriter writer{fits_file_path};
  writer.setFormat(FitsWriter::Format::BINARY);
  writer.setHduName("BinaryTable");
  writer.setHeader("MYSTR", std::string("MyValue"), "This is a comment");
  writer.setHeader("MYINT", 1234, "Another comment");

  // When
  writer.addData(table);
  CCfits::FITS fits{fits_file_path, CCfits::RWmode::Read};
  auto&        result = fits.extension("BinaryTable");
  result.readAllKeys();

  // Then
  BOOST_CHECK_EQUAL(result.rows(), 2);
  BOOST_CHECK_EQUAL(result.numCols(), 9);

  BOOST_CHECK_EQUAL(result.column(1).name(), "Boolean");
  BOOST_CHECK_EQUAL(result.column(2).name(), "Integer");
  BOOST_CHECK_EQUAL(result.column(3).name(), "Long");
  BOOST_CHECK_EQUAL(result.column(4).name(), "Float");
  BOOST_CHECK_EQUAL(result.column(5).name(), "Double");
  BOOST_CHECK_EQUAL(result.column(6).name(), "String");
  BOOST_CHECK_EQUAL(result.column(7).name(), "NdArray");
  BOOST_CHECK_EQUAL(result.column(8).name(), "ScalarNdArray");

  BOOST_CHECK_EQUAL(result.column(1).format(), "L");
  BOOST_CHECK_EQUAL(result.column(2).format(), "J");
  BOOST_CHECK_EQUAL(result.column(3).format(), "K");
  BOOST_CHECK_EQUAL(result.column(4).format(), "E");
  BOOST_CHECK_EQUAL(result.column(5).format(), "D");
  BOOST_CHECK_EQUAL(result.column(6).format(), "33A");
  BOOST_CHECK_EQUAL(result.column(7).format(), "6D");
  BOOST_CHECK_EQUAL(result.column(8).format(), "1D");

  BOOST_CHECK_EQUAL(result.column(1).unit(), "deg");
  BOOST_CHECK_EQUAL(result.column(2).unit(), "mag");
  BOOST_CHECK_EQUAL(result.column(3).unit(), "");
  BOOST_CHECK_EQUAL(result.column(4).unit(), "ph");
  BOOST_CHECK_EQUAL(result.column(5).unit(), "s");
  BOOST_CHECK_EQUAL(result.column(6).unit(), "m");
  BOOST_CHECK_EQUAL(result.column(7).unit(), "x");

  std::string tmp;
  BOOST_CHECK_EQUAL(result.keyWord("TDESC1").value(tmp), "Desc1");
  BOOST_CHECK_EQUAL(result.keyWord("TDESC2").value(tmp), "Desc2");
  BOOST_CHECK_EQUAL(result.keyWord("TDESC3").value(tmp), "Desc3");
  BOOST_CHECK_EQUAL(result.keyWord("TDESC4").value(tmp), "Desc4");
  BOOST_CHECK_EQUAL(result.keyWord("TDESC5").value(tmp), "Desc5");
  BOOST_CHECK_EQUAL(result.keyWord("TDESC6").value(tmp), "Desc6");
  BOOST_CHECK_EQUAL(result.keyWord("TDESC7").value(tmp), "Desc7");

  // When
  std::vector<bool> bool_data{};
  result.column(1).read(bool_data, 1, 2);

  // Then
  BOOST_CHECK(bool_data[0]);
  BOOST_CHECK(!bool_data[1]);

  // When
  std::vector<int32_t> int_data{};
  result.column(2).read(int_data, 1, 2);

  // Then
  BOOST_CHECK_EQUAL(int_data[0], 1);
  BOOST_CHECK_EQUAL(int_data[1], 12345);

  // When
  std::vector<int64_t> long_data{};
  result.column(3).read(long_data, 1, 2);

  // Then
  BOOST_CHECK_EQUAL(long_data[0], 123);
  BOOST_CHECK_EQUAL(long_data[1], 123456789);

  // When
  std::vector<float> float_data{};
  result.column(4).read(float_data, 1, 2);

  // Then
  BOOST_CHECK_EQUAL(float_data[0], 0.F);
  BOOST_CHECK_EQUAL(float_data[1], 2.3e-2F);

  // When
  std::vector<double> double_data{};
  result.column(5).read(double_data, 1, 2);

  // Then
  BOOST_CHECK_EQUAL(double_data[0], 0.F);
  BOOST_CHECK_EQUAL(double_data[1], 1.12345e-18);

  // When
  std::vector<std::string> string_data{};
  auto&                    str_col = result.column(6);
  str_col.setDimen();
  BOOST_CHECK(str_col.dimen().empty());

  str_col.read(string_data, 1, 2);

  // Then
  BOOST_CHECK_EQUAL(string_data[0], "first");
  BOOST_CHECK_EQUAL(string_data[1], "second with spaces on top of that");

  // When
  std::valarray<double> na1, na2;
  std::valarray<double> expected1{1, 2, 3, 4, 5, 6};
  std::valarray<double> expected2{6, 5, 4, 3, 2, 1};
  auto&                 nd_col = result.column(7);

  nd_col.read(na1, 1);
  nd_col.read(na2, 2);

  // Then
  nd_col.setDimen();
  BOOST_CHECK_EQUAL(nd_col.dimen(), "(3,2)");
  BOOST_CHECK_EQUAL_COLLECTIONS(std::begin(na1), std::end(na1), std::begin(expected1), std::end(expected1));
  BOOST_CHECK_EQUAL_COLLECTIONS(std::begin(na2), std::end(na2), std::begin(expected2), std::end(expected2));

  // When
  std::vector<double> sna;
  auto&               vec_col = result.column(8);
  vec_col.setDimen();
  BOOST_CHECK(vec_col.dimen().empty());
  vec_col.read(sna, 1, 2);

  // Then
  BOOST_CHECK_EQUAL(sna[0], 41);
  BOOST_CHECK_EQUAL(sna[1], 42);

  // When
  std::valarray<float> vector;
  std::valarray<float> expectedv{1.5, 2.6, 3.7};
  result.column(9).read(vector, 1);
  BOOST_CHECK_EQUAL_COLLECTIONS(std::begin(vector), std::end(vector), std::begin(expectedv), std::end(expectedv));

  // When
  std::string my_string_val;
  int my_int_val;

  auto& my_string = result.keyWord("MYSTR");
  auto& my_int = result.keyWord("MYINT");

  my_string.value(my_string_val);
  my_int.value(my_int_val);

  // Then
  BOOST_CHECK_EQUAL(my_string_val, "MyValue");
  BOOST_CHECK_EQUAL(my_int_val, 1234);
  BOOST_CHECK_EQUAL(my_string.comment(), "This is a comment");
  BOOST_CHECK_EQUAL(my_int.comment(), "Another comment");
}

//-----------------------------------------------------------------------------
// Test the write ASCII
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(writeAscii, AsciiFitsWriter_Fixture) {

  // Given
  FitsWriter writer{fits_file_path};
  writer.setFormat(FitsWriter::Format::ASCII);
  writer.setHduName("AsciiTable");

  // When
  writer.addData(table);
  CCfits::FITS fits{fits_file_path, CCfits::RWmode::Read};
  auto&        result = fits.extension("AsciiTable");
  result.readAllKeys();

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
  BOOST_CHECK_EQUAL(result.column(6).format(), "A11");

  BOOST_CHECK_EQUAL(result.column(1).unit(), "deg");
  BOOST_CHECK_EQUAL(result.column(2).unit(), "mag");
  BOOST_CHECK_EQUAL(result.column(3).unit(), "");
  BOOST_CHECK_EQUAL(result.column(4).unit(), "ph");
  BOOST_CHECK_EQUAL(result.column(5).unit(), "s");
  BOOST_CHECK_EQUAL(result.column(6).unit(), "m");

  std::string tmp;
  BOOST_CHECK_EQUAL(result.keyWord("TDESC1").value(tmp), "Desc1");
  BOOST_CHECK_EQUAL(result.keyWord("TDESC2").value(tmp), "Desc2");
  BOOST_CHECK_EQUAL(result.keyWord("TDESC3").value(tmp), "Desc3");
  BOOST_CHECK_EQUAL(result.keyWord("TDESC4").value(tmp), "Desc4");
  BOOST_CHECK_EQUAL(result.keyWord("TDESC5").value(tmp), "Desc5");
  BOOST_CHECK_EQUAL(result.keyWord("TDESC6").value(tmp), "Desc6");

  // When
  std::vector<int32_t> bool_data{};
  result.column(1).read(bool_data, 1, 2);

  // Then
  BOOST_CHECK_EQUAL(bool_data[0], 1);
  BOOST_CHECK_EQUAL(bool_data[1], 0);

  // When
  std::vector<int32_t> int_data{};
  result.column(2).read(int_data, 1, 2);

  // Then
  BOOST_CHECK_EQUAL(int_data[0], 1);
  BOOST_CHECK_EQUAL(int_data[1], 12345);

  // When
  std::vector<int64_t> long_data{};
  result.column(3).read(long_data, 1, 2);

  // Then
  BOOST_CHECK_EQUAL(long_data[0], 123);
  BOOST_CHECK_EQUAL(long_data[1], 123456789);

  // When
  std::vector<float> float_data{};
  result.column(4).read(float_data, 1, 2);

  // Then
  BOOST_CHECK_EQUAL(float_data[0], 0.F);
  BOOST_CHECK_EQUAL(float_data[1], 2.3e-2F);

  // When
  std::vector<double> double_data{};
  result.column(5).read(double_data, 1, 2);

  // Then
  BOOST_CHECK_EQUAL(double_data[0], 0.F);
  BOOST_CHECK_CLOSE(double_data[1], 1.12345e-18, 0.001);

  // When
  std::vector<std::string> string_data{};
  result.column(6).read(string_data, 1, 2);

  // Then
  BOOST_CHECK_EQUAL(string_data[0], "first");
  BOOST_CHECK_EQUAL(string_data[1], "very spaced");
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(addExisting, BinaryFitsWriter_Fixture) {
  // Given
  {
    FitsWriter writer{fits_file_path};
    writer.setFormat(FitsWriter::Format::BINARY);
    writer.setHduName("BinaryTable");
    writer.addData(table);
  }

  // When
  FitsWriter writer{fits_file_path};
  writer.setFormat(FitsWriter::Format::BINARY);
  writer.setHduName("BinaryTable");
  writer.addData(table);

  // Then
  CCfits::FITS fits{fits_file_path, CCfits::RWmode::Read};
  auto&        result = fits.extension("BinaryTable");
  result.readAllKeys();

  BOOST_CHECK_EQUAL(result.rows(), 4);
  BOOST_CHECK_EQUAL(result.numCols(), 9);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(emptyBinaryCatalog, BinaryFitsWriter_Fixture) {
  // Given
  FitsWriter writer{fits_file_path};
  writer.setFormat(FitsWriter::Format::BINARY);
  writer.setHduName("EmptyBinaryTable");

  // When
  writer.addData(empty_table);
  CCfits::FITS fits{fits_file_path, CCfits::RWmode::Read};
  auto&        result = fits.extension("EmptyBinaryTable");
  result.readAllKeys();

  // Then
  BOOST_CHECK_EQUAL(result.rows(), 0);
  BOOST_CHECK_EQUAL(result.numCols(), 9);

  BOOST_CHECK_EQUAL(result.column(1).name(), "Boolean");
  BOOST_CHECK_EQUAL(result.column(2).name(), "Integer");
  BOOST_CHECK_EQUAL(result.column(3).name(), "Long");
  BOOST_CHECK_EQUAL(result.column(4).name(), "Float");
  BOOST_CHECK_EQUAL(result.column(5).name(), "Double");
  BOOST_CHECK_EQUAL(result.column(6).name(), "String");
  BOOST_CHECK_EQUAL(result.column(7).name(), "NdArray");
  BOOST_CHECK_EQUAL(result.column(8).name(), "ScalarNdArray");
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(emptyAsciiCatalog, AsciiFitsWriter_Fixture) {
  // Given
  FitsWriter writer{fits_file_path};
  writer.setFormat(FitsWriter::Format::ASCII);
  writer.setHduName("EmptyAsciiTable");

  // When
  writer.addData(empty_table);
  CCfits::FITS fits{fits_file_path, CCfits::RWmode::Read};
  auto&        result = fits.extension("EmptyAsciiTable");
  result.readAllKeys();

  // Then
  BOOST_CHECK_EQUAL(result.rows(), 0);
  BOOST_CHECK_EQUAL(result.numCols(), 6);

  BOOST_CHECK_EQUAL(result.column(1).name(), "Boolean");
  BOOST_CHECK_EQUAL(result.column(2).name(), "Integer");
  BOOST_CHECK_EQUAL(result.column(3).name(), "Long");
  BOOST_CHECK_EQUAL(result.column(4).name(), "Float");
  BOOST_CHECK_EQUAL(result.column(5).name(), "Double");
  BOOST_CHECK_EQUAL(result.column(6).name(), "String");

  BOOST_CHECK_EQUAL(result.column(1).format(), "I1");
  BOOST_CHECK_EQUAL(result.column(2).format(), "I1");
  BOOST_CHECK_EQUAL(result.column(3).format(), "I1");
  BOOST_CHECK_EQUAL(result.column(4).format(), "E1");
  BOOST_CHECK_EQUAL(result.column(5).format(), "E1");
  BOOST_CHECK_EQUAL(result.column(6).format(), "A1");
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
