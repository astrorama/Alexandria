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
double tolerence = 1e-8;

//Photometry photometry {};
//ChDataModel::Photometry photometry {};

struct PhotometryFixture {

  Photometry photometry { };

  const FilterName expectedFilterName { "COSMOS", "V_band" };
  double expectedFlux = 0.46575674;
  double expectedError = 0.00001534;

  //photometry.addFlux(expectedFilterName, expectedFlux, expectedError);

  PhotometryFixture() {
//    cout << "setup" << endl;

  }
  ~PhotometryFixture() {
//    cout << "teardown" << endl;
  }
  //PhotometryFixture(const PhotometryFixture&) = delete;
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Photometry_test)

// BOOST_GLOBAL_FIXTURE(PV); // this does not work as test case do not have access to PV members!?!?

BOOST_FIXTURE_TEST_CASE( getter_test, PhotometryFixture ) {

  photometry.clear();
  photometry.addFlux(expectedFilterName, expectedFlux, expectedError);

  BOOST_CHECK_EQUAL(expectedFilterName.name(), "V_band");
  BOOST_CHECK_CLOSE(expectedFlux, photometry.getFlux(expectedFilterName), tolerence);
  BOOST_CHECK_CLOSE(expectedError, photometry.getFluxError(expectedFilterName), tolerence);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( unicity_test, PhotometryFixture ) {

  bool exception = false;
  try {
    photometry.addFlux(expectedFilterName, expectedFlux, expectedError);
    photometry.addFlux(expectedFilterName, expectedFlux, expectedError);
  } catch (const ElementsException & e) {
    string exception_str = e.what();
    exception =
    (exception_str.find("Photometry::addFlux") != string::npos);
  }
  BOOST_CHECK(exception);
  photometry.clear();
  photometry.addFlux(expectedFilterName, expectedFlux, expectedError);
  BOOST_CHECK_CLOSE(expectedFlux, photometry.getFlux(expectedFilterName), tolerence);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
