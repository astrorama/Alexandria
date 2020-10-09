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
 * @file tests/src/serialization/tuple_test.cpp
 * @date June 27, 2014
 * @author Nikolaos Apostolakos
 */

#include "DefaultConstructibleClass.h"
#include "GridContainer/serialization/GridAxis.h"
#include "GridContainer/serialization/tuple.h"
#include "NonDefaultConstructibleClass.h"
#include <boost/archive/binary_iarchive.hpp>
#include <boost/archive/binary_oarchive.hpp>
#include <boost/test/unit_test.hpp>
#include <sstream>
#include <tuple>

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(tuple_serialization_test)

//-----------------------------------------------------------------------------
// Test serialization of tuple with fundamental values
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(fundamentalValues) {

  // Given
  std::tuple<double, double, double> tuple{1E-12, 5., 3.4};

  // When
  std::stringstream               stream{};
  boost::archive::binary_oarchive boa{stream};
  boa << tuple;
  // Note that we must force the types we will read
  std::tuple<double, double, double> result;
  boost::archive::binary_iarchive    bia{stream};
  bia >> result;

  // Then
  BOOST_CHECK_EQUAL(std::get<0>(result), std::get<0>(tuple));
  BOOST_CHECK_EQUAL(std::get<1>(result), std::get<1>(tuple));
  BOOST_CHECK_EQUAL(std::get<2>(result), std::get<2>(tuple));
}

//-----------------------------------------------------------------------------
// Test serialization of tuple with default constructible values
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(defaultConstructibleValues) {

  typedef DefaultConstructibleClass DCC;
  // Given
  std::tuple<DCC, DCC, DCC> tuple{};
  std::get<0>(tuple).value = 1E-12;
  std::get<1>(tuple).value = 5.;
  std::get<2>(tuple).value = 3.4;

  // When
  std::stringstream               stream{};
  boost::archive::binary_oarchive boa{stream};
  boa << tuple;
  // Note that we must force the types we will read
  std::tuple<DCC, DCC, DCC>       result;
  boost::archive::binary_iarchive bia{stream};
  bia >> result;

  // Then
  BOOST_CHECK_EQUAL(std::get<0>(result).value, std::get<0>(tuple).value);
  BOOST_CHECK_EQUAL(std::get<1>(result).value, std::get<1>(tuple).value);
  BOOST_CHECK_EQUAL(std::get<2>(result).value, std::get<2>(tuple).value);
}

//-----------------------------------------------------------------------------
// Test serialization of tuple with non default constructible values
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(nonDefaultConstructibleValues) {

  typedef NonDefaultConstructibleClass NDCC;
  // Given
  std::tuple<NDCC, NDCC, NDCC> tuple{1E-12, 5., 3.4};

  // When
  std::stringstream               stream{};
  boost::archive::binary_oarchive boa{stream};
  boa << tuple;
  // Note that we must force the types we will read and that we have to use
  // some dummy default values which will be replaced with the ones from the
  // stream
  std::tuple<NDCC, NDCC, NDCC>    result{0., 0., 0.};
  boost::archive::binary_iarchive bia{stream};
  bia >> result;

  // Then
  BOOST_CHECK_EQUAL(std::get<0>(result).value, std::get<0>(tuple).value);
  BOOST_CHECK_EQUAL(std::get<1>(result).value, std::get<1>(tuple).value);
  BOOST_CHECK_EQUAL(std::get<2>(result).value, std::get<2>(tuple).value);
}

//-----------------------------------------------------------------------------
// Test serialization of tuple with combination of values
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(combinationOfValues) {

  typedef DefaultConstructibleClass    DCC;
  typedef NonDefaultConstructibleClass NDCC;

  // Given
  std::string                             name0 = "FundamentalAxis";
  std::vector<double>                     knots0{0., 3.4, 12E-15};
  Euclid::GridContainer::GridAxis<double> axis0{name0, knots0};
  std::string                             name1 = "DefaultConstructibleAxis";
  std::vector<DCC>                        knots1{DCC{}, DCC{}, DCC{}};
  knots1[0].value = 0.;
  knots1[1].value = 3.4;
  knots1[2].value = 12E-15;
  Euclid::GridContainer::GridAxis<DCC> axis1{name1, knots1};
  std::string                          name2 = "NonDefaultConstructibleAxis";
  std::vector<NDCC>                    knots2{};
  knots2.push_back(NDCC{0.});
  knots2.push_back(NDCC{3.4});
  knots2.push_back(NDCC{12E-15});
  Euclid::GridContainer::GridAxis<NDCC> axis2{name2, knots2};
  auto                                  tuple = std::make_tuple(axis0, axis1, axis2);

  // When
  std::stringstream               stream{};
  boost::archive::binary_oarchive boa{stream};
  boa << tuple;
  // Note that we must force the types we will read and that we have to use
  // some dummy default values which will be replaced with the ones from the
  // stream
  auto result = std::make_tuple(Euclid::GridContainer::GridAxis<double>{"", {}}, Euclid::GridContainer::GridAxis<DCC>{"", {}},
                                Euclid::GridContainer::GridAxis<NDCC>{"", {}});
  boost::archive::binary_iarchive bia{stream};
  bia >> result;

  // Then
  BOOST_CHECK_EQUAL(std::get<0>(result).name(), name0);
  BOOST_CHECK_EQUAL_COLLECTIONS(std::get<0>(result).begin(), std::get<0>(result).end(), knots0.begin(), knots0.end());
  BOOST_CHECK_EQUAL(std::get<1>(result).name(), name1);
  BOOST_CHECK_EQUAL(std::get<1>(result).size(), knots1.size());
  auto result_iter1 = std::get<1>(result).begin();
  auto knots_iter1  = knots1.begin();
  while (result_iter1 != std::get<1>(result).end()) {
    BOOST_CHECK_EQUAL(result_iter1->value, knots_iter1->value);
    ++result_iter1;
    ++knots_iter1;
  }
  BOOST_CHECK_EQUAL(std::get<2>(result).name(), name2);
  BOOST_CHECK_EQUAL(std::get<2>(result).size(), knots2.size());
  auto result_iter2 = std::get<2>(result).begin();
  auto knots_iter2  = knots2.begin();
  while (result_iter2 != std::get<2>(result).end()) {
    BOOST_CHECK_EQUAL(result_iter2->value, knots_iter2->value);
    ++result_iter2;
    ++knots_iter2;
  }
}

//-----------------------------------------------------------------------------
// Test serialization of tuple with GridAxis values. This test is performed
// because serialization of tuples is implemented only for this reason. Note
// that this test might detect problems related with the GridAxis serialization
// and not the tuple per se.
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(gridAxesValues) {

  typedef DefaultConstructibleClass    DCC;
  typedef NonDefaultConstructibleClass NDCC;
  // Given
  std::tuple<double, DCC, NDCC> tuple{1E-12, {}, 3.4};
  std::get<1>(tuple).value = 5.;

  // When
  std::stringstream               stream{};
  boost::archive::binary_oarchive boa{stream};
  boa << tuple;
  // Note that we must force the types we will read and that we have to use
  // some dummy default values which will be replaced with the ones from the
  // stream
  std::tuple<double, DCC, NDCC>   result{0., {}, 0.};
  boost::archive::binary_iarchive bia{stream};
  bia >> result;

  // Then
  BOOST_CHECK_EQUAL(std::get<0>(result), std::get<0>(tuple));
  BOOST_CHECK_EQUAL(std::get<1>(result).value, std::get<1>(tuple).value);
  BOOST_CHECK_EQUAL(std::get<2>(result).value, std::get<2>(tuple).value);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()