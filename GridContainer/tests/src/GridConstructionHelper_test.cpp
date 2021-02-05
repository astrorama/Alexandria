/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
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
 * @file tests/src/GridConstructionHelper_test.cpp
 * @date July 2, 2014
 * @author Nikolaos Apostolakos
 */

#include "GridContainer/_impl/GridConstructionHelper.h"
#include <boost/test/unit_test.hpp>

struct GridConstructionHelper_Fixture {
  typedef Euclid::GridContainer::GridAxis<int>                              IntAxis;
  IntAxis                                                                   axis1{"Axis 1", {1, 2, 3, 4, 5}};
  IntAxis                                                                   axis2{"Axis 2", {1, 2, 3}};
  IntAxis                                                                   axis3{"Axis 3", {1, 2, 3, 4, 5, 6}};
  IntAxis                                                                   axis4{"Axis 4", {1, 2}};
  std::tuple<IntAxis, IntAxis, IntAxis, IntAxis>                            axes_tuple{axis1, axis2, axis3, axis4};
  typedef Euclid::GridContainer::GridConstructionHelper<int, int, int, int> Helper;
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(GridConstructionHelper_test)

//-----------------------------------------------------------------------------
// Test the createAxesSizesVector method
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(createAxesSizesVector, GridConstructionHelper_Fixture) {

  // When
  std::vector<size_t> result = Helper::createAxesSizesVector(axes_tuple, Euclid::GridContainer::TemplateLoopCounter<4>{});

  // Then
  BOOST_CHECK_EQUAL(result.size(), 4u);
  BOOST_CHECK_EQUAL(result[0], axis1.size());
  BOOST_CHECK_EQUAL(result[1], axis2.size());
  BOOST_CHECK_EQUAL(result[2], axis3.size());
  BOOST_CHECK_EQUAL(result[3], axis4.size());
}

//-----------------------------------------------------------------------------
// Test the createAxisIndexFactorVector method
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(createAxisIndexFactorVector, GridConstructionHelper_Fixture) {

  // When
  std::vector<size_t> result = Helper::createAxisIndexFactorVector(axes_tuple, Euclid::GridContainer::TemplateLoopCounter<4>{});

  // Then
  BOOST_CHECK_EQUAL(result.size(), 5u);
  BOOST_CHECK_EQUAL(result[0], 1u);
  BOOST_CHECK_EQUAL(result[1], axis1.size());
  BOOST_CHECK_EQUAL(result[2], axis1.size() * axis2.size());
  BOOST_CHECK_EQUAL(result[3], axis1.size() * axis2.size() * axis3.size());
  BOOST_CHECK_EQUAL(result[4], axis1.size() * axis2.size() * axis3.size() * axis4.size());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
