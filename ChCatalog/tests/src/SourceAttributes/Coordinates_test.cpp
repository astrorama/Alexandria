/**
 * @file tests/src/SourceAttributes/Coordinates_test.cpp
 *
 * @author Nicolas Morisset
 *
 * Created on: Feb 5, 2014
 */

#include <boost/test/unit_test.hpp>
#include <iostream>
#include "ChCatalog/SourceAttributes/Coordinates.h"

using namespace ChCatalog;
using namespace std;

//-----------------------------------------------------------------------------


struct CoordinatesFixture {

  double expected_ra;
  double expected_dec;

  CoordinatesFixture() {
    expected_ra  = 1.5;
    expected_dec = 2.8;
  }
  ~CoordinatesFixture() {
  }
};

//----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Coordinates_test)

BOOST_FIXTURE_TEST_CASE( getter_test, CoordinatesFixture ) {

  Coordinates coordinates(expected_ra, expected_dec);

  double ra_result  = coordinates.getRa();
  double dec_result = coordinates.getDec();

  BOOST_CHECK_EQUAL(expected_ra, ra_result);
  BOOST_CHECK_EQUAL(expected_dec, dec_result);

}

BOOST_AUTO_TEST_SUITE_END ()
