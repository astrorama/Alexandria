/**
 * @file Catalog_test.cpp
 *
 *  Created on: March 1, 2013
 *      Author: Pierre Dubath
 */

#include <boost/test/unit_test.hpp>
#include "ChCatalog/Enumerations/SurveyNames.h"
#include "ChCatalog/Source.h"
#include "ChCatalog/Catalog.h"

#include "ElementsKernel/ElementsException.h"

#include <iostream>
#include <map>

//-----------------------------------------------------------------------------
// Include the CatalogFixture which include a photometry mock object we use here for the test
#include "tests/src/CatalogFixture.h"


using namespace ChCatalog;
using namespace std;




//-----------------------------------------------------------------------------
//

BOOST_AUTO_TEST_SUITE (Catalog_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( size_test, CatalogFixture ) {

  BOOST_TEST_MESSAGE("--> size test ");
  BOOST_CHECK_EQUAL(source_vector.size(), catalog.size());

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( find_test, CatalogFixture ) {

  BOOST_TEST_MESSAGE("--> find test ");

  shared_ptr<Source> a_source(catalog.find(expected_source_id_2));
  shared_ptr<Coordinates> coordinates(a_source->getAttribute<Coordinates>());

  BOOST_CHECK_EQUAL(expected_ra_2, coordinates->getRa());
  BOOST_CHECK_EQUAL(expected_dec_2, coordinates->getDec());

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( find_missig_source_test, CatalogFixture ) {

  BOOST_TEST_MESSAGE("--> find test ");

  shared_ptr<Source> pSource(catalog.find(999999));

  BOOST_CHECK(nullptr == pSource);

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( identical_sources_test, CatalogFixture ) {

  BOOST_TEST_MESSAGE("--> identical_sources test ");

  vector<Source> source_vector_identical {};

  source_vector_identical.push_back(Source(expected_source_id_1, attribute_vector_1));
  source_vector_identical.push_back(Source(expected_source_id_2, attribute_vector_2));
  source_vector_identical.push_back(Source(expected_source_id_1, attribute_vector_1));

  bool identical = false;
  Catalog* catidenticalPtr {};

  try {
    Catalog catalog {source_vector_identical};
  }
  catch (ElementsException e) {
    identical = true;
  };

  BOOST_CHECK_EQUAL(identical, true);

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
