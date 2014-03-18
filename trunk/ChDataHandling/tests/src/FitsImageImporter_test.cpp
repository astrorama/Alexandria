/**
 * @file FitsImageImporter_test.cpp
 *
 * Created on: Oct 21, 2013
 *     Author: Pavel Binko
 */

#include <boost/test/unit_test.hpp>
#include "ChDataHandling/FitsImageImporter.h"
#include "ChDataModel/Fits/Image.h"
#include "ChDataModel/Fits/Header.h"
#include "ChDataModel/Fits/Keyword.h"

using namespace ChDataModel;
using namespace Fits;
using namespace std;

//------------------------------------------------------------------------------

struct FitsImageImporterFix {

  string fitsFile = "ChDataHandling/tests/FitsData/images_tables.fits.gz";
  FitsImageImporter * input = new FitsImageImporter(fitsFile);

  ~FitsImageImporterFix() {
    delete input;
  }

};

//------------------------------------------------------------------------------
//
// Begin of the Boost tests
//
//------------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (FitsImageImporter_test)

//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( constructors_test, FitsImageImporterFix ) {

  BOOST_CHECK(input != nullptr);

}  // Eof constructors_test

//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( read_fits_header_test, FitsImageImporterFix ) {

  Image * image = new Image();
  input->readFitsHeader_extHDU("ds", image);

  string keywordName = "";

  try {

    keywordName = "OFF-AXIS";
    BoolKeyword & boolKeyword = image->getHeader()->getKeyword(keywordName);
    bool actualBoolKeywordValue = boolKeyword.getValue();
    bool expectedBoolKeywordValue = true;      // Or "1"
    BOOST_CHECK_EQUAL(actualBoolKeywordValue, expectedBoolKeywordValue);

    keywordName = "DEC_OBJ";
    DoubleKeyword & doubleKeyword = image->getHeader()->getKeyword(keywordName);
    double actualDoubleKeywordValue = doubleKeyword.getValue();
    double expectedDoubleKeywordValue = 39.405728;
    double precission = 1e-10;
    BOOST_CHECK_CLOSE(actualDoubleKeywordValue, expectedDoubleKeywordValue,
        precission);

    keywordName = "NAXIS1";
    LongKeyword & longKeyword = image->getHeader()->getKeyword(keywordName);
    long actualLongKeywordValue = longKeyword.getValue();
    long expectedLongKeywordValue = 512;
    BOOST_CHECK_EQUAL(actualLongKeywordValue, expectedLongKeywordValue);

    keywordName = "TIMESYS";
    StringKeyword & stringKeyword = image->getHeader()->getKeyword(keywordName);
    string actualStringKeywordValue = stringKeyword.getValue();
    string expectedStringKeywordValue = "MJD";
    BOOST_CHECK_EQUAL(actualStringKeywordValue, expectedStringKeywordValue);

  }
  catch (const std::out_of_range & e) {

    // All keywords above should have been found
    //   If the exception was catched here, the read header test is wrong
    cout << "Keyword name with problem = " << keywordName << endl;
    BOOST_CHECK(false);

  }

}  // Eof read_fits_header_test

//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( read_fits_image_test, FitsImageImporterFix ) {

  Image * image = new Image();
  input->readFitsHeader_extHDU("ds", image);  // Needed because of NAXIS1 and NAXIS2
  input->readFitsImage_extHDU("ds", image);

  long actualDataSize = image->getData().size();
  long sizeX = dynamic_cast<LongKeyword &>(image->getHeader()->getKeyword(
      "NAXIS1")).getValue();
  long sizeY = dynamic_cast<LongKeyword &>(image->getHeader()->getKeyword(
      "NAXIS2")).getValue();
  long expectedDataSize = sizeX * sizeY;
  BOOST_CHECK_EQUAL(actualDataSize, expectedDataSize);

} // Eof read_fits_image_test

//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( import_image_test, FitsImageImporterFix ) {

  try {
    Image * image = input->importImage("ds");
    image->print();
  }
  catch (const std::exception & e) {
    // The whole image has been imported without any exception
    BOOST_CHECK(false);
  }

}  // Eof import_image_test

//------------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()

//------------------------------------------------------------------------------
//
// End of the Boost tests
//
//------------------------------------------------------------------------------
