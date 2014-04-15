/**
 * @file Photometry_test.cpp
 *
 * Created on: Jan 20, 2014
 *     Author: Pierre Dubath
 */
#include <boost/test/unit_test.hpp>
#include <iostream>

#include "ChCatalog/SourceAttributes/Photometry.h"
#include "ChCatalog/FilterName.h"

using namespace ChCatalog;
using namespace std;

//-----------------------------------------------------------------------------

struct PhotometryFixture {

  const FilterName expectedFilterName1 { "COSMOS", "V_band" };
  double expectedFlux1  = 0.46575674;
  double expectedError1 = 0.00001534;

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
    phot_map.insert(make_pair(expectedFilterName1, make_pair(expectedFlux1, expectedError1)));
    phot_map.insert(make_pair(expectedFilterName2, make_pair(expectedFlux2, expectedError2)));
    return phot_map;
  }

};

//----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Photometry_test)

BOOST_FIXTURE_TEST_CASE( find_test, PhotometryFixture ) {

  BOOST_TEST_MESSAGE("--> find test ");

  shared_ptr<pair<double,double>> ptr1 = photometry.find(expectedFilterName1);
  shared_ptr<pair<double,double>> ptr2 = photometry.find(expectedFilterName2);

  BOOST_CHECK_EQUAL(expectedFlux1, ptr1->first);
  BOOST_CHECK_EQUAL(expectedError1, ptr1->second);
  BOOST_CHECK_EQUAL(expectedFlux2, ptr2->first);
  BOOST_CHECK_EQUAL(expectedError2, ptr2->second);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( iterator_test, PhotometryFixture ) {

  BOOST_TEST_MESSAGE("--> iterator test ");

  std::map< FilterName, std::pair<double, double>>::const_iterator itBegin = photometry.cbegin();
  std::map< FilterName, std::pair<double, double>>::const_iterator itEnd   = photometry.cend();

  vector<string> nameVector {};
  for (auto it=itBegin; it!=itEnd; ++it)
  {
    nameVector.push_back((it->first).name());
  }

  BOOST_CHECK_EQUAL(expectedFilterName1.name(), nameVector[0]);
  BOOST_CHECK_EQUAL(expectedFilterName2.name(), nameVector[1]);

}

BOOST_AUTO_TEST_SUITE_END ()
