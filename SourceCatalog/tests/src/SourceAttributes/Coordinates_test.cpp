/*
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
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
 * @file tests/src/SourceAttributes/Coordinates_test.cpp
 *
 * @author Nicolas Morisset
 *
 * Created on: Feb 5, 2014
 */

#include "SourceCatalog/SourceAttributes/Coordinates.h"
#include <boost/test/unit_test.hpp>
#include <iostream>

using namespace Euclid::SourceCatalog;

//-----------------------------------------------------------------------------

struct CoordinatesFixture {
  double expected_ra  = 1.5;
  double expected_dec = 2.8;
};

//----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(Coordinates_test)

BOOST_FIXTURE_TEST_CASE(getter_test, CoordinatesFixture) {

  Coordinates coordinates(expected_ra, expected_dec);

  double ra_result  = coordinates.getRa();
  double dec_result = coordinates.getDec();

  BOOST_CHECK_EQUAL(expected_ra, ra_result);
  BOOST_CHECK_EQUAL(expected_dec, dec_result);
}

BOOST_AUTO_TEST_SUITE_END()
