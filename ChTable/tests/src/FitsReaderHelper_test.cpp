/** 
 * @file tests/src/FitsReaderHelper_test.cpp
 * @date April 17, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include <CCfits/CCfits>
#include "ElementsKernel/ElementsException.h"
#include "ElementsKernel/Temporary.h"
#include "src/lib/FitsReaderHelper.h"

struct FitsReaderHelper_Fixture {
  TempDir temp_dir;
  std::unique_ptr<CCfits::FITS> fits {new CCfits::FITS(
        (temp_dir.path()/"FitsReaderHelper_test.fits").native(), CCfits::RWmode::Write)};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (AsciiReaderHelper_test)

//-----------------------------------------------------------------------------
// Test the autoDetectColumnNames method
//-----------------------------------------------------------------------------
 
BOOST_FIXTURE_TEST_CASE(autoDetectColumnNames, FitsReaderHelper_Fixture) {
  
  // Given
  std::vector<std::string> names {"First","Second","","Fourth"};
  std::vector<std::string> types {"J","J","J","J"};
  CCfits::Table* table_hdu = fits->addTable("CheckNames", 0, names, types);
  
  // When
  std::vector<std::string> result = Euclid::ChTable::autoDetectColumnNames(*table_hdu);
  
  // Then
  BOOST_CHECK_EQUAL(result.size(), 4);
  BOOST_CHECK_EQUAL(result[0], "First");
  BOOST_CHECK_EQUAL(result[1], "Second");
  BOOST_CHECK_EQUAL(result[2], "Col3");
  BOOST_CHECK_EQUAL(result[3], "Fourth");
  
}

//-----------------------------------------------------------------------------
// Test the autoDetectColumnTypes method for ASCII table
//-----------------------------------------------------------------------------
 
BOOST_FIXTURE_TEST_CASE(autoDetectColumnTypesAscii, FitsReaderHelper_Fixture) {
  
  // Given
  std::vector<std::string> names {"String","Integer","Float1","Float2","Float3"};
  std::vector<std::string> types {"A10","I6","F4.3","E6.5","D8.7"};
  std::vector<std::string> units {"","","","",""};
  CCfits::Table* table_hdu = fits->addTable("ASCII", 0, names, types, units, CCfits::HduType::AsciiTbl);
  
  // When
  std::vector<std::type_index> result = Euclid::ChTable::autoDetectColumnTypes(*table_hdu);
  
  // Then
  BOOST_CHECK_EQUAL(result.size(), 5);
  BOOST_CHECK(result[0] == typeid(std::string));
  BOOST_CHECK(result[1] == typeid(int64_t));
  BOOST_CHECK(result[2] == typeid(double));
  BOOST_CHECK(result[3] == typeid(double));
  BOOST_CHECK(result[4] == typeid(double));
  
}

//-----------------------------------------------------------------------------
// Test the autoDetectColumnTypes method for binary table
//-----------------------------------------------------------------------------
 
BOOST_FIXTURE_TEST_CASE(autoDetectColumnTypesBinary, FitsReaderHelper_Fixture) {
  
  // Given
  std::vector<std::string> names {"Bool","Byte","Short","Int","Long","String","Float","Double"};
  std::vector<std::string> types {"L","B","I","J","K","10A","E","D"};
  CCfits::Table* table_hdu = fits->addTable("Binary", 0, names, types);
  
  // When
  std::vector<std::type_index> result = Euclid::ChTable::autoDetectColumnTypes(*table_hdu);
  
  // Then
  BOOST_CHECK_EQUAL(result.size(), 8);
  BOOST_CHECK(result[0] == typeid(bool));
  BOOST_CHECK(result[1] == typeid(int32_t));
  BOOST_CHECK(result[2] == typeid(int32_t));
  BOOST_CHECK(result[3] == typeid(int32_t));
  BOOST_CHECK(result[4] == typeid(int64_t));
  BOOST_CHECK(result[5] == typeid(std::string));
  BOOST_CHECK(result[6] == typeid(float));
  BOOST_CHECK(result[7] == typeid(double));
  
}

//-----------------------------------------------------------------------------
// Test the autoDetectColumnTypes method for binary table throws for unsupported types
//-----------------------------------------------------------------------------
 
BOOST_FIXTURE_TEST_CASE(autoDetectColumnTypesBinaryUnsupportedTypes, FitsReaderHelper_Fixture) {
  
  // Given
  std::vector<std::string> names {"Bit"};
  std::vector<std::string> types {"X"};
  CCfits::Table* table_hdu = fits->addTable("Bit", 0, names, types);
  
  // Then
  BOOST_CHECK_THROW(Euclid::ChTable::autoDetectColumnTypes(*table_hdu), ElementsException);
  
  // Given
  names = {"FloatComplex"};
  types = {"C"};
  table_hdu = fits->addTable("FloatComplex", 0, names, types);
  
  // Then
  BOOST_CHECK_THROW(Euclid::ChTable::autoDetectColumnTypes(*table_hdu), ElementsException);
  
  // Given
  names = {"DoubleComplex"};
  types = {"M"};
  table_hdu = fits->addTable("DoubleComplex", 0, names, types);
  
  // Then
  BOOST_CHECK_THROW(Euclid::ChTable::autoDetectColumnTypes(*table_hdu), ElementsException);
  
  // Given
  names = {"IntArray"};
  types = {"15K"};
  table_hdu = fits->addTable("IntArray", 0, names, types);
  
  // Then
  BOOST_CHECK_THROW(Euclid::ChTable::autoDetectColumnTypes(*table_hdu), ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the translateColumn method
//-----------------------------------------------------------------------------
 
BOOST_FIXTURE_TEST_CASE(translateColumn, FitsReaderHelper_Fixture) {
  
  // Given
  std::vector<std::string> names {"Bool","Int","Long","String","Float","Double"};
  std::vector<std::string> types {"L","J","K","10A","E","D"};
  CCfits::Table* table_hdu = fits->addTable("TranslateColumn", 2, names, types);
  std::vector<bool> bool_values {true, false};
  table_hdu->column(1).write(bool_values, 1);
  std::vector<int32_t> int_values {3, -2346};
  table_hdu->column(2).write(int_values, 1);
  std::vector<int64_t> long_values {123456789, -6};
  table_hdu->column(3).write(long_values, 1);
  std::vector<std::string> string_values {"Small", "1234567890"};
  table_hdu->column(4).write(string_values, 1);
  std::vector<float> float_values {3.4f, 2.1e-3f};
  table_hdu->column(5).write(float_values, 1);
  std::vector<double> double_values {3.4, 2.1e-13};
  table_hdu->column(6).write(double_values, 1);
  
  
  // When
  auto bool_result = Euclid::ChTable::translateColumn(table_hdu->column(1), typeid(bool));
  auto int_result = Euclid::ChTable::translateColumn(table_hdu->column(2), typeid(int32_t));
  auto long_result = Euclid::ChTable::translateColumn(table_hdu->column(3), typeid(int64_t));
  auto string_result = Euclid::ChTable::translateColumn(table_hdu->column(4), typeid(std::string));
  auto float_result = Euclid::ChTable::translateColumn(table_hdu->column(5), typeid(float));
  auto double_result = Euclid::ChTable::translateColumn(table_hdu->column(6), typeid(double));
  
  // Then
  BOOST_CHECK_EQUAL(bool_result.size(), 2);
  BOOST_CHECK_EQUAL(boost::get<bool>(bool_result[0]), true);
  BOOST_CHECK_EQUAL(boost::get<bool>(bool_result[1]), false);
  BOOST_CHECK_EQUAL(int_result.size(), 2);
  BOOST_CHECK_EQUAL(boost::get<int32_t>(int_result[0]), 3);
  BOOST_CHECK_EQUAL(boost::get<int32_t>(int_result[1]), -2346);
  BOOST_CHECK_EQUAL(long_result.size(), 2);
  BOOST_CHECK_EQUAL(boost::get<int64_t>(long_result[0]), 123456789);
  BOOST_CHECK_EQUAL(boost::get<int64_t>(long_result[1]), -6);
  BOOST_CHECK_EQUAL(string_result.size(), 2);
  BOOST_CHECK_EQUAL(boost::get<std::string>(string_result[0]), "Small");
  BOOST_CHECK_EQUAL(boost::get<std::string>(string_result[1]), "1234567890");
  BOOST_CHECK_EQUAL(float_result.size(), 2);
  BOOST_CHECK_EQUAL(boost::get<float>(float_result[0]),3.4f);
  BOOST_CHECK_EQUAL(boost::get<float>(float_result[1]), 2.1e-3f);
  BOOST_CHECK_EQUAL(double_result.size(), 2);
  BOOST_CHECK_EQUAL(boost::get<double>(double_result[0]),3.4);
  BOOST_CHECK_EQUAL(boost::get<double>(double_result[1]), 2.1e-13);
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()