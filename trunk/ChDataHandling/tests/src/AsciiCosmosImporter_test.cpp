/**
 * @file AsciiCosmosImporter_test.cpp
 *
 * Created on: May 30, 2013
 *     Author: Pavel Binko
 */

#include <boost/test/unit_test.hpp>
#include "ChDataHandling/AsciiCosmosImporter.h"

#include <string>
#include <vector>
#include <iostream>

using namespace ChDataModel;
using namespace std;

//-----------------------------------------------------------------------------

struct AsciiCosmosImporterFix {

  AsciiCosmosImporter * input = new AsciiCosmosImporter();

  string path = "ChDataHandling/tests/PhotometryData/Cosmos";
  string expectedFirstFileName = path + "/cosmos_IB_band_2008_2.tbl_30_lines";

  ~AsciiCosmosImporterFix() {
    delete input;
  }

};

//-----------------------------------------------------------------------------
//
// Begin of the Boost tests
//
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (AsciiCosmosImporter_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( constructors_test, AsciiCosmosImporterFix ) {

  BOOST_CHECK(input != nullptr);

}  // Eof constructors_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( readCosmosAsciiHeader_test, AsciiCosmosImporterFix ) {

  input->resolveFileNames(path);
  input->readCosmosAsciiHeader();

  string actualID = input->getHeader().at(0).at(0);
  string expectedID = "ID";
  BOOST_CHECK(actualID == expectedID);

  string actualZMagType = input->getHeader().at(1).at(25);
  string expectedZMagType = "double";
  BOOST_CHECK(actualZMagType == expectedZMagType);

} // Eof readCosmosAsciiHeader_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( readCosmosAsciiData_test, AsciiCosmosImporterFix ) {

  input->resolveFileNames(path);
  input->readCosmosAsciiHeader();

  Catalog cat;
  int startRow = 5;
  int numRows = 25;
  input->readCosmosAsciiData(cat, startRow, numRows);
//  cat.printCatalog();

  int64_t actualID = cat.getSourceMap().at(300001).getSourceId();
  int64_t expectedID = 300001;
  BOOST_CHECK_EQUAL(actualID, expectedID);

  double actualDec = cat.getSourceMap().at(599999).getDec();
  double expectedDec = 1.916156;
  double tolerenceDec = 0.00001;
  BOOST_CHECK_CLOSE(actualDec, expectedDec, tolerenceDec);

  double actualPixelX = cat.getSourceMap().at(599999).getPhotometry(FilterNames::z_Subaru).getValue();
  double expectedPixelX = 26.6751;
  double tolerencePixelX = 0.00001;
  BOOST_CHECK_CLOSE(actualPixelX, expectedPixelX, tolerencePixelX);

} // Eof readCosmosAsciiData_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( addSourceToCatalog_test, AsciiCosmosImporterFix ) {

  map<string,int> columnMap = {
      make_pair("ID", 0),
      make_pair("ra", 1),
      make_pair("dec",2),
      make_pair("u",  3),
      make_pair("du", 4),
      make_pair("B",  5),
      make_pair("dB", 6)
  };
  input->setColumnMap(columnMap);
  vector<string> tokenizedRow = {"11", "22", "33", "44", "55", "66", "77"};

  Catalog cat;
  input->addSourceToCatalog(cat, tokenizedRow);
//  cat->printCatalog();

  double expectedRa  = 22;
  double tolerenceRa = 0.00001;
  double actualRa    = cat.getSource(11).getRa();
  BOOST_CHECK_CLOSE(actualRa, expectedRa, tolerenceRa);

} // Eof addSourceToCatalog_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( importCatalog_test, AsciiCosmosImporterFix ) {

  int startRow =  5;
  int numRows  = 25;
  Catalog cat;
  input->importCatalog(cat, path, startRow, numRows);
//  cat.printCatalog();

  double tolerence = 0.00001;
  double expectedIA484 = 26.0432;
  double actualIA484 = cat.getSource(599999).getPhotometry(FilterNames::IA624_Subaru).getValue();
  BOOST_CHECK_CLOSE(actualIA484, expectedIA484, tolerence);

} // Eof importCatalog_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( importCatalog2_test, AsciiCosmosImporterFix ) {

  int startRow = 5;
  int numRows  = 3;
  vector<string> vectorOfFilenames = {"ChDataHandling/tests/PhotometryData/Cosmos/cosmos_IB_band_2008_3.tbl_30_lines"};
  Catalog cat;
  input->importCatalog(cat, path, startRow, numRows);
//  cat->printCatalog();

  double tolerence = 0.00001;
  double expected_u_CFHT = 0.7574;
  double actual_u_CFHT = cat.getSource(300003).getPhotometry(FilterNames::u_CFHT).getValueError();
  BOOST_CHECK_CLOSE(actual_u_CFHT, expected_u_CFHT, tolerence);

} // Eof importCatalog2_test

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()

//-----------------------------------------------------------------------------
//
// End of the Boost tests
//
//-----------------------------------------------------------------------------
