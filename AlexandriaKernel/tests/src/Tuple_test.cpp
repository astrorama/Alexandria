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

#include "AlexandriaKernel/Tuples.h"
#include <boost/test/unit_test.hpp>
#include <memory>

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(Tuple_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(GetTail) {
  std::tuple<double, int, char> tuple{42., 128, 'a'};
  auto                          tuple2 = Euclid::Tuple::Tail(tuple);
  static_assert(std::is_same<decltype(tuple2), std::tuple<int, char>>::value, "Compile time check!");
  BOOST_CHECK_EQUAL(std::get<0>(tuple2), 128);
  BOOST_CHECK_EQUAL(std::get<1>(tuple2), 'a');
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(MoveTail) {
  std::unique_ptr<std::string> str_ptr(new std::string("HELLO THERE!"));
  std::vector<int> vector{1,2,3,4};
  std::tuple<double, std::vector<int>, std::unique_ptr<std::string>> tuple(55., vector, std::move(str_ptr));

  // This will not compile
  // auto tuple2 = Euclid::Tuple::Tail(tuple);

  auto tuple3 = Euclid::Tuple::Tail(std::move(tuple));
  static_assert(std::is_same<decltype(tuple3), std::tuple<std::vector<int>, std::unique_ptr<std::string>>>::value,
                "Compile time check!");

  std::vector<int> expected{1, 2, 3, 4};
  const auto&      e0 = std::get<0>(tuple3);
  BOOST_CHECK_EQUAL_COLLECTIONS(expected.begin(), expected.end(), e0.begin(), e0.end());
  BOOST_REQUIRE(std::get<1>(tuple3));
  BOOST_CHECK_EQUAL(*std::get<1>(tuple3), "HELLO THERE!");
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
