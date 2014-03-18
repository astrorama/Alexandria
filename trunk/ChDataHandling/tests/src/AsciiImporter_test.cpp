/**
 * @file AsciiImporter_test.cpp
 *
 * Created on: May 30, 2013
 *     Author: Pavel Binko
 */

#include <boost/test/unit_test.hpp>
#include "ChDataHandling/AsciiImporter.h"

#include <string>
#include <vector>
#include <iostream>

using namespace ChDataModel;
using namespace std;

//-----------------------------------------------------------------------------

struct AsciiImporterFix {

  AsciiImporter * asciiImporter = new AsciiImporter();

  string path = "ChDataHandling/tests/PhotometryData/Cosmos";
  string expectedFirstFileName = path + "/cosmos_IB_band_2008_2.tbl_30_lines";

  ~AsciiImporterFix() {
    delete asciiImporter;
  }

};

//-----------------------------------------------------------------------------
//
// Begin of the Boost tests
//
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (AsciiImporter_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( constructors_test, AsciiImporterFix ) {

  BOOST_CHECK(asciiImporter != nullptr);

}  // Eof constructors_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( resolveFileNames_test, AsciiImporterFix ) {

  asciiImporter->resolveFileNames(path);
  string actualFirstFileName = asciiImporter->getFileNames().at(0);
  BOOST_CHECK(actualFirstFileName == expectedFirstFileName);

} // Eof resolveFileNames_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( openFile_test, AsciiImporterFix ) {

  // If no exception thrown, file will be opened
  asciiImporter->openFile(expectedFirstFileName);

} // Eof openFile_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( openNextFile_test, AsciiImporterFix ) {

  // If no exception thrown, both files will be opened consecutively
  asciiImporter->resolveFileNames(path);
  asciiImporter->openNextFile();
  // Without this closeCurrentFile, the second openNextFile would throw an exception
  asciiImporter->closeCurrentFile();
  asciiImporter->openNextFile();

} // Eof openNextFile_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( tokenizeRow_test, AsciiImporterFix ) {

  vector<string> tokens;
  string delim = "#| \t";

  // Data row test
  string headerRow = "  \t  1 2 3";
  tokens = asciiImporter->tokenizeRow(headerRow, delim);

  string actualFirstToken = tokens.at(0);
  string expectedFirstToken = "1";
  BOOST_CHECK(actualFirstToken == expectedFirstToken);

  // Header row test
  headerRow = "#ID RA DEC  \t  ";
  tokens = asciiImporter->tokenizeRow(headerRow, delim);

  actualFirstToken = tokens.at(0);
  expectedFirstToken = "ID";
  BOOST_CHECK(actualFirstToken == expectedFirstToken);

} // Eof tokenizeRow_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( readNextRow_test, AsciiImporterFix ) {

  asciiImporter->openFile(expectedFirstFileName);

  string actualNextRow = "";
  vector<string> tokenizedRow = {};
  bool isData = true;

  // Next row test
  asciiImporter->readNextRow(actualNextRow, tokenizedRow, isData);
  string expectedNextRow =
      "|                                    ID|                               ID_2006|                                  tile|                                    ra|                                   dec|                               pixel_x|                               pixel_y|                                i_fwhm|                                 i_max|                                i_star|                                i_auto|                           auto_offset|                             auto_flag|                                     u|                                    du|                                     B|                                    dB|                                     V|                                    dV|                                     g|                                    dg|                                     r|                                    dr|                                     i|                                    di|                                 z_mag|                                    dz|                                     K|                                    dK|                                    ic|                                   dic|                                    us|                                   dus|                                    gs|                                   dgs|                                    rs|                                   drs|                                    is|                                   dis|                                    zs|                                   dzs|                                 F814W|                                dF814W|                                 NB816|                                dNB816|                                 IA427|                                dIA427|                                 IA464|                                dIA464|                                 IA505|                                dIA505|                                 IA574|                                dIA574|                                 IA709|                                dIA709|                                 IA827|                                dIA827|                                 NB711|                                dNB711|                                    Kc|                                   dKc|                                     J|                                    dJ|                                 IA484|                                dIA484|                                 IA527|                                dIA527|                                 IA624|                                dIA624|                                 IA679|                                dIA679|                                 IA738|                                dIA738|                                 IA767|                                dIA767|                                  Eb_v|                                   FUV|                                  dFUV|                                   NUV|                                  dNUV|                              mask_FUV|                              mask_NUV|                                B_mask|                                V_mask|                                i_mask|                                z_mask|                             deep_mask|";
  BOOST_CHECK(actualNextRow == expectedNextRow);

  // Token row
  string actualToken = tokenizedRow.at(0);
  string expectedToken = "ID";
  BOOST_CHECK(actualToken == expectedToken);

  // Is data or header test
  BOOST_CHECK(isData == false);

} // Eof readNextRow_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( conversion_test, AsciiImporterFix ) {

  map<string,int> columnMap = {
      make_pair("ID", 0),
      make_pair("ra", 1),
      make_pair("dec",2),
      make_pair("u",  3),
      make_pair("du", 4),
      make_pair("B",  5),
      make_pair("dB", 6)
  };
  asciiImporter->setColumnMap(columnMap);
  vector<string> tokenizedRow = {"11", "22", "33.33", "44", "55", "66", "77"};

  double expectedDec = 33.33;
  double tolerenceDec = 0.00001;
  double actualDec = asciiImporter->getDoubleFromTokens(tokenizedRow, "dec");
  BOOST_CHECK_CLOSE(actualDec, expectedDec, tolerenceDec);

  long expectedId = 11;
  long actualId = asciiImporter->getInt64FromTokens(tokenizedRow, "ID");
  BOOST_CHECK_EQUAL(actualId, expectedId);

} // Eof conversion_test

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()

//-----------------------------------------------------------------------------
//
// End of the Boost tests
//
//-----------------------------------------------------------------------------
