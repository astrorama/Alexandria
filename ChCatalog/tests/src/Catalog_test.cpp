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

using namespace ChCatalog;
using namespace std;



struct CatalogFix {

  Source* sourcePtr1{};
  Source* sourcePtr2{};

  double tolerence = 1e-8;
  size_t expected_cat_size = 2;

  const FilterName expectedFilterName { "COSMOS", "V_band" };
  double expectedFlux  = 0.46575674;
  double expectedError = 0.00001534;

  int64_t expectedSourceId1 = 1273684;
  int64_t expectedSourceId2 = 2345678;

  double expectedRa1  = 181.4657;
  double expectedDec1 = -36.27363;
  double expectedRa2  = 281.4657;
  double expectedDec2 = -26.27363;

  double expectedZvalue1 = 3.;
  double expectedZerror1 = 0.01;
  double expectedZvalue2 = 2.;
  double expectedZerror2 = 0.01;

  vector<shared_ptr<Attribute>> attribute_vector1 {};
  vector<shared_ptr<Attribute>> attribute_vector2 {};

  vector<Source> source_vector {};

  Catalog* catPtr {};

  CatalogFix() {

    // First source
    shared_ptr<Coordinates> coordinates_ptr1(new Coordinates(expectedRa1, expectedDec1));
    shared_ptr<SpectroscopicRedshift> spec_redshift_ptr1(new SpectroscopicRedshift(expectedZvalue1, expectedZerror1));
    shared_ptr<Photometry> photometry_ptr1(new Photometry{createPhotometryMap()});
    attribute_vector1.push_back(coordinates_ptr1);
    attribute_vector1.push_back(spec_redshift_ptr1);
    attribute_vector1.push_back(photometry_ptr1);

    // Second source
    shared_ptr<Coordinates> coordinates_ptr2(new Coordinates(expectedRa2, expectedDec2));
    shared_ptr<SpectroscopicRedshift> spec_redshift_ptr2(new SpectroscopicRedshift(expectedZvalue2, expectedZerror2));
    attribute_vector2.push_back(coordinates_ptr2);
    attribute_vector2.push_back(spec_redshift_ptr2);

    // Store sources in a vector
    source_vector.push_back(Source(expectedSourceId1, attribute_vector1));
    source_vector.push_back(Source(expectedSourceId2, attribute_vector2));

    catPtr = new Catalog(source_vector);

  }
  ~CatalogFix() {
    // teardown
    delete catPtr;
  }

  map< FilterName, pair<double, double> > createPhotometryMap() {
    map< FilterName, pair<double, double> > phot_map {};
    phot_map.insert(make_pair(expectedFilterName, make_pair(expectedFlux, expectedError)));
    return phot_map;
  }

};

//-----------------------------------------------------------------------------
//

BOOST_AUTO_TEST_SUITE (Catalog_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( size_test, CatalogFix ) {

  BOOST_TEST_MESSAGE("--> size test ");
  BOOST_CHECK_EQUAL(expected_cat_size, catPtr->size());

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( find_test, CatalogFix ) {

  BOOST_TEST_MESSAGE("--> find test ");

  shared_ptr<Source> pSource(catPtr->find(expectedSourceId2));
  shared_ptr<Coordinates> sourceCoord(pSource->getAttribute<Coordinates>());

  BOOST_CHECK_EQUAL(expectedRa2, sourceCoord->getRa());
  BOOST_CHECK_EQUAL(expectedDec2, sourceCoord->getDec());

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( find_missig_source_test, CatalogFix ) {

  BOOST_TEST_MESSAGE("--> find test ");

  shared_ptr<Source> pSource(catPtr->find(999999));

  BOOST_CHECK(nullptr == pSource);

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( identical_sources_test, CatalogFix ) {

  BOOST_TEST_MESSAGE("--> identical_sources test ");

  vector<Source> source_vector_identical {};

  source_vector_identical.push_back(Source(expectedSourceId1, attribute_vector1));
  source_vector_identical.push_back(Source(expectedSourceId2, attribute_vector2));
  source_vector_identical.push_back(Source(expectedSourceId2, attribute_vector2));

  bool identical = false;
  Catalog* catidenticalPtr {};

  try {
    catidenticalPtr = new Catalog(source_vector_identical);
  }
  catch (ElementsException e) {
    identical = true;
  };

  delete catidenticalPtr;

  BOOST_CHECK_EQUAL(identical, true);

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
