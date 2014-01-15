/**
 * Areader_test.cpp
 *
 *  Created on: Dec 26, 2013
 *      Author: dubath
 */
#include <iostream>
#include <cmath>
#include <map>
#include <iomanip>
#include <vector>
#include <boost/test/unit_test.hpp>
#include <boost/filesystem/path.hpp>

#include "ChDataHandling/Areader.h"

#include "ChDataModel/Enumerations/FilterTypes.h"
#include "ChDataModel/Enumerations/SurveyNames.h"
#include "ChDataModel/Catalog.h"
#include "ChDataModel/Survey.h"

namespace fs = boost::filesystem;

using namespace std;

//-----------------------------------------------------------------------------

struct AreaderFix {

  char* strPath;
  std::string alexandriaPath { };
  bool test_result { };
  double tolerence { };
//  clock_t     begin_time{};
//  string      interpolationMethodChosen{};
//
//  matrix::FluxMatrix* flux_matrix {};

  Areader aReader { };

  AreaderFix() {

    // Get Alexandria path
    strPath = getenv("ALEXANDRIA_PROJECT_ROOT");
    alexandriaPath = "";
    if (strPath != NULL) {
      alexandriaPath = std::string(strPath);
    } else {
      cout
          << "ERROR : <ALEXANDRIA_PROJECT_ROOT> environment variable is empty!!!";
    }

    test_result = true;
    tolerence = 0.0001;

//    const param::FluxModelingParameters tmpPtr  {
//          param::PhzParameterFactory::createFixedStepParameter("Z", 0., 2., 0.1),
//          param::PhzParameterFactory::createFixedStepParameter("E(B-V)", 0., 1., 0.1),
//          param::PhzParameterFactory::createSedParameterFromPath(alexandriaPath+"/PhotZAuxData/Sed/Cosmos"),
//          param::PhzParameterFactory::createFilterParameterFromPath(alexandriaPath+"/PhotZAuxData/Filter/Cosmos", ChDataModel::FilterTypes::EUCLID),
//          param::PhzParameterFactory::createExtLawParameterFromPath(alexandriaPath+"/PhotZAuxData/ExtLaw"), 10., interpolationMethodChosen
//    };

//matrix::FluxMatrix matrixFromParams {fmp};
//flux_matrix = new matrix::FluxMatrix(tmpPtr);

  }
  ~AreaderFix() {
    // teardown
    //delete flux_matrix;
  }

};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Areader_test)

//-----------------------------------------------------------------------------
//                       getInterpolationMethod_test
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( readFile_test, AreaderFix ) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the readFile function");
  BOOST_TEST_MESSAGE(" ");

//  std::vector<vector<string>> file_fields = aReader.readFile("/Users/dubath/euclid/MERchallenge/catalog/EUSIM_1FWHM_S1_v2.cat", 0, 6);
//
//  for (vector<string> line : file_fields) {
//    for(string col : line) {
//      cout << col << " ";
//    }
//    cout << endl;
//  }

}

BOOST_FIXTURE_TEST_CASE( AddSourceToCatalog_test, AreaderFix ) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the AddSourceToCatalog function");
  BOOST_TEST_MESSAGE(" ");

//  std::vector<vector<string>> file_fields = aReader.readFile("/Users/dubath/euclid/MERchallenge/catalog/EUSIM_1FWHM_S1_v2.cat", 1, 5);
//
//  ChDataModel::Survey survey {ChDataModel::SurveyNames::EUCLID};
//  ChDataModel::Catalog catalog = survey.createCatalog();
//
//  for (vector<string> line : file_fields) {
//    aReader.AddSourceToCatalog(catalog, line);
//  }
//  //cout << line << endl;
//  cout << "Everything is fine : work done" << endl;
//
//  std::map<int64_t, ChDataModel::Source> source_map = catalog.getSourceMap();
//
//    for( auto ii=source_map.begin(); ii!=source_map.end(); ++ii)
//      {
//      cout << "SourceId: " << (ii->second).getSourceId() << " and Gext_ACSf435w: "
//          << (ii->second).getPhotometry(ChDataModel::FilterNames::Gext_ACSf435w).getValue() << endl;
//      cout << "SpecZ: " << (ii->second).getSpecZ() << endl;
//      }

  cout << "Everything is fine checks done" << endl;

  //BOOST_CHECK_EQUAL(result, interpolationMethodChosen);

}

BOOST_FIXTURE_TEST_CASE( GetCatalog_test, AreaderFix ) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the GetCatalog function");
  BOOST_TEST_MESSAGE(" ");

//  cout << "Everything is fine" << endl;
//
//  ChDataModel::Catalog catalog = aReader.getCatalog("/Users/dubath/euclid/MERchallenge/catalog/EUSIM_1FWHM_S1_v2.cat", 1, 5);
//
//  cout << "Everything is fine: work done" << endl;
//
//  std::map<int64_t, ChDataModel::Source> source_map = catalog.getSourceMap();
//
//    for( auto ii=source_map.begin(); ii!=source_map.end(); ++ii)
//      {
//      cout << "SourceId: " << ((*ii).second).getSourceId() << " and Gext_ACSf435w: "
//          << ((*ii).second).getPhotometry(ChDataModel::FilterNames::Gext_ACSf435w).getValue() << endl;
//      }
//
//  cout << "Everything is fine: checks done" << endl;

  //BOOST_CHECK_EQUAL(result, interpolationMethodChosen);

}

BOOST_AUTO_TEST_SUITE_END ()
