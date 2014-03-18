/**
 * @file AsciiFilterImporter_test.cpp
 *
 * Created on: Jun 19, 2013
 *     Author: Pavel Binko
 */

#include <boost/test/unit_test.hpp>
#include "ChDataHandling/AsciiFilterImporter.h"

#include <string>
#include <vector>
#include <iostream>

using namespace ChDataModel;
using namespace std;

//-----------------------------------------------------------------------------

struct AsciiFilterImporterFix {

  AsciiFilterImporter * input = new AsciiFilterImporter();

  string path = "ChDataHandling/tests/PhotZAuxData/Filter/Cosmos";
  string expectedFirstFileName = path + "/IA709.res";

  ~AsciiFilterImporterFix() {
    delete input;
  }

};

//-----------------------------------------------------------------------------
//
// Begin of the Boost tests
//
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (AsciiFilterImporter_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( constructors_test, AsciiFilterImporterFix ) {

  BOOST_CHECK(input != nullptr);

}  // Eof constructors_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( resolveFileNames_test, AsciiFilterImporterFix ) {

  input->resolveFileNames(path);
  string actualFirstFileName = input->getFileNames().at(0);
  BOOST_CHECK(actualFirstFileName == expectedFirstFileName);

} // Eof resolveFileNames_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( importFilterName_test, AsciiFilterImporterFix ) {

  input->resolveFileNames(path);
  input->openFile(expectedFirstFileName);

  FilterNames actualFilterName = input->importFilterName(expectedFirstFileName);
  FilterNames expectedFilterName = FilterNames::IA709_Subaru;

  BOOST_CHECK_EQUAL(actualFilterName, expectedFilterName);

  input->closeCurrentFile();

} // Eof importFilterName_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( importFilterData_test, AsciiFilterImporterFix ) {

  input->resolveFileNames(path);
  input->openFile(expectedFirstFileName);
  VectorPair filterData = input->importFilterData();

//  filterData.printVectorPair();

  double actualWaveLength = filterData.getX(1);
  double expectedWaveLength = 6764.0;
  double tolerenceWaveLength = 0.00001;
  BOOST_CHECK_CLOSE(actualWaveLength, expectedWaveLength, tolerenceWaveLength);

  double actualEfficiency = filterData.getY(5);
  double expectedEfficiency = 3.90786428746e-05;
  double tolerenceEfficiency = 0.00001;
//  cout << "actual   = " << actualEfficiency << endl;
//  cout << "expected = " << expectedEfficiency << endl;
  BOOST_CHECK_CLOSE(actualEfficiency, expectedEfficiency, tolerenceEfficiency);

  input->closeCurrentFile();

} // Eof importFilterData_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( createFilter_test, AsciiFilterImporterFix ) {

  input->resolveFileNames(path);
  FilterTypes expectedFilterType = FilterTypes::EUCLID;
  Filter filter = input->createFilter(expectedFirstFileName, expectedFilterType);

  FilterTypes actualFilterType = filter.getFilterType();
  BOOST_CHECK_EQUAL(actualFilterType, expectedFilterType);

  FilterNames expectedFilterName = FilterNames::IA709_Subaru;
  FilterNames actualFilterName = filter.getFilterName();
  BOOST_CHECK_EQUAL(actualFilterName, expectedFilterName);

  double actualWaveLength = filter.getWaveLength(1);
  double expectedWaveLength = 6764.0;
  double tolerenceWaveLength = 0.00001;
  BOOST_CHECK_CLOSE(actualWaveLength, expectedWaveLength, tolerenceWaveLength);

} // Eof createFilter_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( importFilters_test, AsciiFilterImporterFix ) {

  map<FilterNames, Filter> map = input->importFilters(path, FilterTypes::EUCLID);

  int actualMapSize   = map.size();
  int expectedMapSize = 2;
  BOOST_CHECK_EQUAL(actualMapSize, expectedMapSize);

//  cout << "Size of the filter map = " << map.size() << endl;
//  for(auto it = map.begin(); it != map.end(); ++it) {
//    cout << it->first << endl;
//    it->second.printFilter();
//  }

  double actualEfficiency   = map[FilterNames::IA709_Subaru].getEfficiencyValue(1);
  double expectedEfficiency = 1.27435e-05;
  double tolerenceEfficiency = 0.001;
  BOOST_CHECK_CLOSE(actualEfficiency, expectedEfficiency, tolerenceEfficiency);

  double actualWaveLength   = map[FilterNames::g_Subaru].getWaveLength(3);
  double expectedWaveLength = 3820.0;
  double tolerenceWaveLength = 0.00001;
  BOOST_CHECK_CLOSE(actualWaveLength, expectedWaveLength, tolerenceWaveLength);

} // Eof importFilters_test

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()

//-----------------------------------------------------------------------------
//
// End of the Boost tests
//
//-----------------------------------------------------------------------------
