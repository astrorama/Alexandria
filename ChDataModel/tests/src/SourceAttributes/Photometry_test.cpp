/**
 * @file Photometry_test.cpp
 *
 * Created on: Jan 20, 2014
 *     Author: Pierre Dubath
 */
#include <boost/test/unit_test.hpp>
#include <iostream>
#include "ChDataModel/SourceAttributes/Photometry.h"
#include "ChDataModel/FilterName.h"

using namespace ChDataModel;
using namespace std;

//-----------------------------------------------------------------------------

struct PhotometryFixture {

  const FilterName expectedFilterName { "COSMOS", "V_band" };
  double expectedFlux  = 0.46575674;
  double expectedError = 0.00001534;

  const FilterName expectedFilterName2 { "COSMOS", "U_band" };
  double expectedFlux2  = 0.46575674;
  double expectedError2 = 0.00001534;

  Photometry photometry {createPhotometryMap()};

  PhotometryFixture() {

  }
  ~PhotometryFixture() {
  }

  map< FilterName, pair<double, double> > createPhotometryMap() {
    map< FilterName, pair<double, double> > phot_map {};
    phot_map.insert(make_pair(expectedFilterName, make_pair(expectedFlux, expectedError)));
    phot_map.insert(make_pair(expectedFilterName2, make_pair(expectedFlux2, expectedError2)));
    return phot_map;
  }

};

//----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Photometry_test)

BOOST_FIXTURE_TEST_CASE( getter_test, PhotometryFixture ) {

  shared_ptr<pair<double,double>> ptr1 = photometry.find(expectedFilterName);
  shared_ptr<pair<double,double>> ptr2 = photometry.find(expectedFilterName2);

  BOOST_CHECK_EQUAL(expectedFlux, ptr1->first);
  BOOST_CHECK_EQUAL(expectedError, ptr1->second);
  BOOST_CHECK_EQUAL(expectedFlux2, ptr2->first);
  BOOST_CHECK_EQUAL(expectedError2, ptr2->second);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
