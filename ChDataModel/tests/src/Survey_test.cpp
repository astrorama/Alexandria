/**
 * @file Survey_test.cpp
 *
 *  Created on: March 1, 2013
 *      Author: dubath
 */

#include <boost/test/unit_test.hpp>
#include "ChDataModel/Source.h"
#include "ChDataModel/Catalog.h"
#include "ChDataModel/Survey.h"

#include <iostream>
#include <map>

using namespace ChDataModel;
using namespace std;

//-----------------------------------------------------------------------------

typedef Source* SourcePtr;

struct SurveyFix {

  Survey survey = Survey(SurveyNames::COSMOS);
  Catalog & catalog_1 = survey.createCatalog();
  Catalog & catalog_2 = survey.createCatalog();
  Catalog & catalog_3 = survey.createCatalog();

  SurveyFix()  {
    // setup
    Source source1(1, 14.55, -35.44);
    catalog_2.addSource(source1);
    Source source2(2, 24.55, -35.44);
    catalog_2.addSource(source2);
    Source source3(3, 34.55, -35.44);
    catalog_2.addSource(source3);
  }
  ~SurveyFix() {
    // teardown
  }

};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Survey_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( constructors_test, SurveyFix ) {
  Survey * survey_ptr_contructor_test = nullptr;
  survey_ptr_contructor_test = new Survey(SurveyNames::COSMOS);
  BOOST_CHECK(survey_ptr_contructor_test);
  delete survey_ptr_contructor_test;
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( getters_test, SurveyFix ) {
  //
  double tolerence = 0.00001;
  BOOST_CHECK(survey.getSurveyName() == SurveyNames::COSMOS);
  BOOST_CHECK(survey.getCatalogMap().size() == 3);
  Catalog & catalog = survey.getCatalogMap()[0];
  BOOST_CHECK(catalog.getSourceMap().size() == 0);
  int64_t sourceId = 1;
  BOOST_CHECK_CLOSE(catalog_2.getSource(sourceId).getRa(), 14.55, tolerence);
  Catalog & catalog_test = (survey.getCatalogMap()[1]);
  BOOST_CHECK(catalog_test.getSourceMap().size() == 3);
  BOOST_CHECK_CLOSE(catalog_test.getSource(sourceId).getRa() , 14.55, tolerence);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
