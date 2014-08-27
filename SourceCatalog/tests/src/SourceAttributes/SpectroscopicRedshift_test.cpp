/**
 * @file tests/src/SourceAttributes/SpectroscopicRedshift_test.cpp
 *
 * @author Nicolas Morisset
 *
 * Created on: Feb 5, 2014
 */

#include <boost/test/unit_test.hpp>
#include <iostream>
#include "SourceCatalog/SourceAttributes/SpectroscopicRedshift.h"

using namespace Euclid::ChCatalog;
using namespace std;

//-----------------------------------------------------------------------------


struct SpectroscopicRedshiftFixture {

  double expected_value;
  double expected_error;

  SpectroscopicRedshiftFixture() {
    expected_value = 1.5;
    expected_error = 0.01;
  }
  ~SpectroscopicRedshiftFixture() {
  }
};

//----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (SpectroscopicRedshift_test)

BOOST_FIXTURE_TEST_CASE( getter_test, SpectroscopicRedshiftFixture ) {

  SpectroscopicRedshift spectroscopicRedshift(expected_value, expected_error);

  double value_result = spectroscopicRedshift.getValue();
  double error_result = spectroscopicRedshift.getError();

  BOOST_CHECK_EQUAL(expected_value, value_result);
  BOOST_CHECK_EQUAL(expected_error, error_result);

}

BOOST_AUTO_TEST_SUITE_END ()
