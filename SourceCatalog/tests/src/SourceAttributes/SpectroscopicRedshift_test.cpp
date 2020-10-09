/*
 * Copyright (C) 2012-2020 Euclid Science Ground Segment
 *
 * This library is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free
 * Software Foundation; either version 3.0 of the License, or (at your option)
 * any later version.
 *
 * This library is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
 * details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this library; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 */

/**
 * @file tests/src/SourceAttributes/SpectroscopicRedshift_test.cpp
 *
 * @author Nicolas Morisset
 *
 * Created on: Feb 5, 2014
 */

#include "SourceCatalog/SourceAttributes/SpectroscopicRedshift.h"
#include <boost/test/unit_test.hpp>
#include <iostream>

using namespace Euclid::SourceCatalog;

//-----------------------------------------------------------------------------

struct SpectroscopicRedshiftFixture {

  double expected_value;
  double expected_error;

  SpectroscopicRedshiftFixture() {
    expected_value = 1.5;
    expected_error = 0.01;
  }
  ~SpectroscopicRedshiftFixture() {}
};

//----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(SpectroscopicRedshift_test)

BOOST_FIXTURE_TEST_CASE(getter_test, SpectroscopicRedshiftFixture) {

  SpectroscopicRedshift spectroscopicRedshift(expected_value, expected_error);

  double value_result = spectroscopicRedshift.getValue();
  double error_result = spectroscopicRedshift.getError();

  BOOST_CHECK_EQUAL(expected_value, value_result);
  BOOST_CHECK_EQUAL(expected_error, error_result);
}

BOOST_AUTO_TEST_SUITE_END()
