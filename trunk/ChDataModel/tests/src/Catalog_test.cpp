/**
 * @file Catalog_test.cpp
 *
 *  Created on: March 1, 2013
 *      Author: dubath
 */

#include <boost/test/unit_test.hpp>
#include "ChDataModel/Enumerations/SurveyNames.h"
#include "ChDataModel/Source.h"
#include "ChDataModel/Catalog.h"
#include "ChDataModel/Survey.h"

#include "ElementsKernel/ElementsException.h"

#include <iostream>
#include <map>

using namespace ChDataModel;
using namespace std;

//-----------------------------------------------------------------------------

typedef Source* SourcePtr;

struct CatalogFix {

  Survey survey = Survey(SurveyNames::COSMOS);
  Catalog catalog = Catalog(survey);

  Source source_1 = Source(1, 1.334, -4.5);
  Source source_2 = Source(2, 2.7364, 89.6465);

  CatalogFix() {
    // setup
    catalog.addSource(source_1);
    catalog.addSource(source_2);

  }
  ~CatalogFix() {
    // teardown
  }

};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Catalog_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( constructors_test, CatalogFix ) {
  Survey * survey_ptr {nullptr};
  Catalog* catalogConstructorTest = nullptr;
  BOOST_CHECK(nullptr == catalogConstructorTest);
  catalogConstructorTest = new Catalog();
  BOOST_CHECK(catalogConstructorTest);
  catalogConstructorTest->setSurveyPtr(survey_ptr);
  BOOST_CHECK_EQUAL(catalogConstructorTest->getSurveyPtr(), survey_ptr);
  delete catalogConstructorTest;
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( getters_test, CatalogFix ) {
  //
  int64_t actualSourceId = catalog.getSource(1).getSourceId();
  BOOST_CHECK_EQUAL(actualSourceId, 1);
  double tolerence = 0.00001;
  double actualRa = catalog.getSource(2).getRa();
  BOOST_CHECK_CLOSE( actualRa, 2.7364, tolerence);
  BOOST_CHECK_EQUAL(catalog.getSurveyPtr(), &survey);
  map<int64_t, Source> actualSourceMap = catalog.getSourceMap();
  BOOST_CHECK_EQUAL(actualSourceMap.size(), 2);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( addSource_exception_test, CatalogFix ) {
  //
  bool exception = false;
  try {
    catalog.addSource(source_1);
  } catch (const ElementsException & e) {
    //exception = true;
    string exception_str = e.what();
    exception =
        (exception_str.find(
            "Catalog::addSource : source ")
            != string::npos);
  }
  BOOST_CHECK(exception);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( getPhotometry_exception_test, CatalogFix ) {
  //
  bool exception = false;
  try {
    int64_t source_id = 17;
    Source source = catalog.getSource(source_id);
  } catch (const ElementsException & e) {
    string exception_str = e.what();
    exception = (exception_str.find("Catalog::getSource : source ")
        != string::npos);
  }
  BOOST_CHECK(exception);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
