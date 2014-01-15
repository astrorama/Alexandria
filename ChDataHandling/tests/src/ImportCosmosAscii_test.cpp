/**
 * @file ImportCosmosAscii_test.cpp
 *
 *  Created on: April 29, 2013
 *      Author: Pavel Binko
 */

#include <boost/test/unit_test.hpp>
#include "ChDataHandling/ImportCosmosAscii.h"

using namespace ChDataModel;
using namespace std;

//-----------------------------------------------------------------------------

struct ImportCosmosAsciiFix {

  Survey survey = Survey(SurveyNames::COSMOS);
  Catalog catalog = Catalog(survey);

  Source source_1 = Source(1, 1.334, -4.5);
  Source source_2 = Source(2, 2.7364, 89.6465);

  ImportCosmosAsciiFix() {
    // setup
    catalog.addSource(source_1);
    catalog.addSource(source_2);
  }

  ~ImportCosmosAsciiFix() {
    // teardown
  }

};

//-----------------------------------------------------------------------------
//
// Begin of the Boost tests
//
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (ImportCosmosAscii_test)

BOOST_FIXTURE_TEST_CASE( constructors_test, ImportCosmosAsciiFix ) {

  string fileName = "ChDataHandling/tests/PhotometryData/Cosmos/cosmos_IB_band_2008_2.tbl_30_lines";
  ImportCosmosAscii * input = nullptr;
  BOOST_CHECK(nullptr == input);
  input = new ImportCosmosAscii(fileName);
  BOOST_CHECK(nullptr != input);
  delete input;

}


//-----------------------------------------------------------------------------
// End of the Boost tests
BOOST_AUTO_TEST_SUITE_END ()
