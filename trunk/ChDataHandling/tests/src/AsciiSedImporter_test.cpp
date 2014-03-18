/**
 * @file AsciiSedImporter_test.cpp
 *
 * Created on: Jun 19, 2013
 *     Author: Pavel Binko
 */

#include <boost/test/unit_test.hpp>
#include "ChDataHandling/AsciiSedImporter.h"

using namespace ChDataModel;
using namespace std;

//-----------------------------------------------------------------------------

struct AsciiSedImporterFix {

  AsciiSedImporter * input = new AsciiSedImporter();

  string path = "ChDataHandling/tests/PhotZAuxData/Sed/Cosmos";
  string expectedFirstFileName = path + "/Ell1_A_0.sed_20_lines";

  SedNames expectedSedName = SedNames::Ell1_A_0;

  ~AsciiSedImporterFix() {
    delete input;
  }

};

//-----------------------------------------------------------------------------
//
// Begin of the Boost tests
//
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (AsciiSedImporter_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( constructors_test, AsciiSedImporterFix ) {

  BOOST_CHECK(input != nullptr);

}  // Eof constructors_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( resolveFileNames_test, AsciiSedImporterFix ) {

  input->resolveFileNames(path);
  string actualFirstFileName = input->getFileNames().at(0);
  BOOST_CHECK(actualFirstFileName == expectedFirstFileName);

} // Eof resolveFileNames_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( importSedName_test, AsciiSedImporterFix ) {

  input->resolveFileNames(path);
  input->openFile(expectedFirstFileName);

  SedNames actualSedName = input->importSedName(expectedFirstFileName);

  BOOST_CHECK_EQUAL(actualSedName, expectedSedName);

  input->closeCurrentFile();

} // Eof importSedName_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( importSedData_test, AsciiSedImporterFix ) {

  input->resolveFileNames(path);
  input->openFile(expectedFirstFileName);
  VectorPair sedData = input->importSedData();

//  sedData.printVectorPair();

  double actualWaveLength = sedData.getX(1);
  double expectedWaveLength = 903.65;
  double tolerenceWaveLength = 0.00001;
  BOOST_CHECK_CLOSE(actualWaveLength, expectedWaveLength, tolerenceWaveLength);

  double actualIntensity = sedData.getY(5);
  double expectedIntensity = 0.0000159045;
  double tolerenceIntensity = 0.00001;
//  cout << "actual   = " << actualIntensity << endl;
//  cout << "expected = " << expectedIntensity << endl;
  BOOST_CHECK_CLOSE(actualIntensity, expectedIntensity, tolerenceIntensity);

  input->closeCurrentFile();

} // Eof importSedData_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( createSed_test, AsciiSedImporterFix ) {

  input->resolveFileNames(path);
  Sed sed = input->createSed(expectedFirstFileName);

  SedNames actualSedName = sed.getSedName();
  BOOST_CHECK_EQUAL(actualSedName, expectedSedName);

  double actualWaveLength = sed.getWaveLength(2);
  double expectedWaveLength = 905.73;
  double tolerenceWaveLength = 0.00001;
  BOOST_CHECK_CLOSE(actualWaveLength, expectedWaveLength, tolerenceWaveLength);

} // Eof createSed_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( importSeds_test, AsciiSedImporterFix ) {

  map<SedNames, Sed> sedMap = input->importSeds(path);

  int actualMapSize   = sedMap.size();
  int expectedMapSize = 2;
  BOOST_CHECK_EQUAL(actualMapSize, expectedMapSize);

//  cout << "Size of the SED map = " << sedMap.size() << endl;
//  for(auto it = sedMap.begin(); it != sedMap.end(); ++it) {
//    cout << it->first << endl;
//    it->second.printSed();
//  }

  double actualIntensity   = sedMap[SedNames::Ell1_A_0].getIntensity(1);
  double expectedIntensity = 0.0000163025;
  double tolerenceIntensity = 0.001;
  BOOST_CHECK_CLOSE(actualIntensity, expectedIntensity, tolerenceIntensity);

  double actualWaveLength   = sedMap[SedNames::Sa_A_1].getWaveLength(3);
  double expectedWaveLength = 918.33;
  double tolerenceWaveLength = 0.00001;
  BOOST_CHECK_CLOSE(actualWaveLength, expectedWaveLength, tolerenceWaveLength);

} // Eof importSeds_test

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()

//-----------------------------------------------------------------------------
//
// End of the Boost tests
//
//-----------------------------------------------------------------------------
