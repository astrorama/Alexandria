/** 
 * @file FitsReaderHelper_test.cpp
 * @date April 17, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include <CCfits/CCfits>
#include "ElementsKernel/ElementsException.h"
#include "src/lib/FitsReaderHelper.h"

struct FitsReaderHelper_Fixture {
  std::unique_ptr<CCfits::FITS> fits {new CCfits::FITS(
                    "!/tmp/FitsReaderHelper_test.fits", CCfits::RWmode::Write)};
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
  CCfits::Table* table_hdu = fits->addTable("", 0, names, types);
  
  // When
  std::vector<std::string> result = ChTable::autoDetectColumnNames(*table_hdu);
  
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
  CCfits::Table* table_hdu = fits->addTable("", 0, names, types, units, CCfits::HduType::AsciiTbl);
  
  // When
  std::vector<std::type_index> result = ChTable::autoDetectColumnTypes(*table_hdu);
  
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
  CCfits::Table* table_hdu = fits->addTable("", 0, names, types);
  
  // When
  std::vector<std::type_index> result = ChTable::autoDetectColumnTypes(*table_hdu);
  
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

BOOST_AUTO_TEST_SUITE_END ()