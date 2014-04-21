/** 
 * @file FitsReaderHelper_test.cpp
 * @date April 17, 2014
 * @author Nikolaos Apostolakos
 */

#include <memory>
#include <boost/test/unit_test.hpp>
#include <CCfits/CCfits>
#include "ElementsKernel/ElementsException.h"
#include "ChTable/FitsReader.h"

struct FitsReader_Fixture {
  std::unique_ptr<CCfits::FITS> fits {
          new CCfits::FITS("!/tmp/FitsReader_test.fits", CCfits::RWmode::Write)};
  const CCfits::PHDU& primary_hdu = fits->pHDU();
  std::vector<long> image_size {2,2};
  CCfits::ExtHDU* image_hdu = fits->addImage("Image", FLOAT_IMG, image_size);
//  CCfits::Table* ascii_table_hdu = fits->addT
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (AsciiReader_test)

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for duplicate column names
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(ConstructorDuplicateColumnNames) {
  
  // Given
  std::vector<std::string> names {"First", "Second", "Third", "Second"};
  
  // Then
  BOOST_CHECK_THROW(ChTable::FitsReader reader {names}, ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for empty string column names
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(ConstructorEmptyColumnNames) {
  
  // Given
  std::vector<std::string> names {"First", "Second", "", "Forth"};
  
  // Then
  BOOST_CHECK_THROW(ChTable::FitsReader reader {names}, ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the constructor throws an exception for column names names with whitespaces
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(ConstructorColumnNamesWithWhitespaces) {
  
  // Given
  std::vector<std::string> space {"Sp ace"};
  std::vector<std::string> tab {"T\tab"};
  std::vector<std::string> carriage_return {"Carriage\rReturn"};
  std::vector<std::string> new_line {"New\nLine"};
  std::vector<std::string> new_page {"New\fPage"};
  
  // Then
  BOOST_CHECK_THROW(ChTable::FitsReader reader {space}, ElementsException);
  BOOST_CHECK_THROW(ChTable::FitsReader reader {tab}, ElementsException);
  BOOST_CHECK_THROW(ChTable::FitsReader reader {carriage_return}, ElementsException);
  BOOST_CHECK_THROW(ChTable::FitsReader reader {new_line}, ElementsException);
  BOOST_CHECK_THROW(ChTable::FitsReader reader {new_page}, ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the read throws exception for non table HDUs
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(readNonTable, FitsReader_Fixture) {
  
  // Given
  ChTable::FitsReader reader {};

  // Then
  BOOST_CHECK_THROW(reader.read(primary_hdu), ElementsException);
  BOOST_CHECK_THROW(reader.read(*image_hdu), ElementsException);
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()