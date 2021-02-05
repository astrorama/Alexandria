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
 * @file tests/src/ProgramOptionsHelper_test.cpp
 * @date 06/15/16
 * @author nikoapos
 */

#include <boost/test/unit_test.hpp>

#include "Configuration/ProgramOptionsHelper.h"

using poh = Euclid::Configuration::ProgramOptionsHelper;

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(ProgramOptionsHelper_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(wildcard_only_name_test) {

  // Given
  std::string name = "option";

  // When
  auto result = poh::wildcard(name);

  // Then
  BOOST_CHECK_EQUAL(result, name + "-*");
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(wildcard_with_instance_test) {

  // Given
  std::string name     = "option";
  std::string instance = "instance";

  // When
  auto result = poh::wildcard(name, instance);

  // Then
  BOOST_CHECK_EQUAL(result, name + "-" + instance);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(findWildcardNames_test) {

  // Given
  std::string name1     = "option1";
  std::string name2     = "option2";
  std::string instance1 = "instance1";
  std::string instance2 = "instance2";
  std::string instance3 = "instance3";

  std::map<std::string, boost::program_options::variable_value> options{{poh::wildcard(name1, instance1), {}},
                                                                        {poh::wildcard(name1, instance2), {}},
                                                                        {poh::wildcard(name2, instance2), {}},
                                                                        {poh::wildcard(name2, instance3), {}}};

  // When
  auto result = poh::findWildcardNames({name1, name2}, options);

  // Then
  BOOST_CHECK_EQUAL(result.size(), 3);
  BOOST_CHECK_EQUAL(result.count(instance1), 1);
  BOOST_CHECK_EQUAL(result.count(instance2), 1);
  BOOST_CHECK_EQUAL(result.count(instance3), 1);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
