/**
 * @file Factory_test.cpp
 *
 *  Created on: May 22, 2013
 *      Author: Pierre Dubath
 */

#include <boost/test/unit_test.hpp>
#include "ChDataHandling/Factory.h"
#include "ChDataModel/Survey.h"
#include "ChDataModel/Catalog.h"
#include "ChDataModel/Source.h"
#include "ChDataModel/Enumerations/SurveyNames.h"

#include "ChDataModel/Fits/Image.h"
#include "ChDataModel/Fits/Header.h"
#include "ChDataModel/Fits/Keyword.h"

#include <string>

using namespace ChDataModel;
using namespace Fits;
using namespace std;

//------------------------------------------------------------------------------

struct FactoryFix {

  Survey* cosmosSurvey = Factory::createSurvey(SurveyNames::COSMOS);

  ~FactoryFix() {
    delete cosmosSurvey;
  }

};

//------------------------------------------------------------------------------
//
// Begin of the Boost tests
//
//------------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Factory_test)

//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( createSurvey_test, FactoryFix ) {

//  Catalog catalog = cosmosSurvey->getFirstCatalog();
  long actualNofCat = cosmosSurvey->getCatalogMap().size();
  long expectedNofCat = 0;
  BOOST_CHECK_EQUAL(actualNofCat, expectedNofCat);

  SurveyNames actualSurveyNames = cosmosSurvey->getSurveyName();
  SurveyNames expectedSurveyNames = SurveyNames::COSMOS;
  BOOST_CHECK_EQUAL(actualSurveyNames, expectedSurveyNames);

} // Eof createSurvey_test

//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( createCatalogInSurvey_test, FactoryFix ) {

  Catalog * cat =
      Factory::createCatalogInSurvey(cosmosSurvey,
          "ChDataHandling/tests/PhotometryData/Cosmos/cosmos_IB_band_2008_2.tbl_30_lines",
          5, 20);

  long actualNofSources =
      cosmosSurvey->getCatalogMap()[0].getSourceMap().size();
  long expectedNofSources = cat->getSourceMap().size();
  BOOST_CHECK_EQUAL(actualNofSources, expectedNofSources);

  cosmosSurvey->printSurvey();

  Catalog firstCatalog = cosmosSurvey->getFirstCatalog();
  long actualNofCat = cosmosSurvey->getCatalogMap().size();
  long expectedNofCat = 1;
  BOOST_CHECK_EQUAL(actualNofCat, expectedNofCat);

  long actualSrc = cosmosSurvey->getCatalogMap()[0].getSourceMap().size();
  long expectedSrc = 20;
  BOOST_CHECK_EQUAL(actualSrc, expectedSrc);

  long actualPhotMapSize = cosmosSurvey->getCatalogMap()[0].getSourceMap().at(
      300020).getPhotometryMap().size();
  long expectedPhotMapSize = 33;
  BOOST_CHECK_EQUAL(actualPhotMapSize, expectedPhotMapSize);

  long sourceId = 300001;
  Source source = firstCatalog.getSource(sourceId);
  source.printSource();

  double expectedRa = 150.48885;
  double tolerenceRa = 0.000001;
  double actualRa = source.getRa();

  BOOST_CHECK_CLOSE(actualRa, expectedRa, tolerenceRa);

  double expectedDec = 1.633714;
  double tolerenceDec = 0.000001;
  double actualDec = source.getDec();

  BOOST_CHECK_CLOSE(actualDec, expectedDec, tolerenceDec);

} // Eof createCatalogInSurvey_test

//------------------------------------------------------------------------------


BOOST_FIXTURE_TEST_CASE( createFitsImage_test, FactoryFix ) {

  Image * image = Factory::createFitsImage(
      "ChDataHandling/tests/FitsData/images_tables.fits.gz", "ds");

  image->print();

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
  long actualDataSize = image->getData().size();
  long sizeX = dynamic_cast<LongKeyword &>(image->getHeader()->getKeyword(
      "NAXIS1")).getValue();
  long sizeY = dynamic_cast<LongKeyword &>(image->getHeader()->getKeyword(
      "NAXIS2")).getValue();
  long expectedDataSize = sizeX * sizeY;
  BOOST_CHECK_EQUAL(actualDataSize, expectedDataSize);

} // Eof createFitsImage_test

//------------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()

//------------------------------------------------------------------------------
//
// End of the Boost tests
//
//------------------------------------------------------------------------------
