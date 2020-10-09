/**
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

#include <ElementsKernel/Exception.h>
#include <boost/test/unit_test.hpp>

#include "AlexandriaKernel/StringUtils.h"

using namespace Euclid;

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(StringUtils_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(vectorOfInt) {
  std::vector<int> expected{123, 345, 567};

  auto v = stringToVector<int>("123,345,567");
  BOOST_CHECK_EQUAL_COLLECTIONS(expected.begin(), expected.end(), v.begin(), v.end());

  v = stringToVector<int>("123, 345, 567 ");
  BOOST_CHECK_EQUAL_COLLECTIONS(expected.begin(), expected.end(), v.begin(), v.end());

  BOOST_CHECK_THROW(stringToVector<int>("123.4,345,567"), Elements::Exception);
  BOOST_CHECK_THROW(stringToVector<int>("123,string,567"), Elements::Exception);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(vectorOfFloat) {
  std::vector<float> expected{42.24, 365.12, 987.00};

  auto v = stringToVector<float>("42.24,365.12,987");
  BOOST_CHECK_EQUAL_COLLECTIONS(expected.begin(), expected.end(), v.begin(), v.end());

  v = stringToVector<float>("42.24, 365.12, 987");
  BOOST_CHECK_EQUAL_COLLECTIONS(expected.begin(), expected.end(), v.begin(), v.end());

  BOOST_CHECK_THROW(stringToVector<float>("42.24,str.12,987"), Elements::Exception);
  BOOST_CHECK_THROW(stringToVector<float>("42.24,365.12.7,987"), Elements::Exception);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(vectorOfString) {
  std::vector<std::string> expected{"abcdef", "1234.56", "42"};

  auto v = stringToVector<std::string>("abcdef,1234.56,42");
  BOOST_CHECK_EQUAL_COLLECTIONS(expected.begin(), expected.end(), v.begin(), v.end());

  // Override the separator
  std::vector<std::string> expected2{"en un lugar", "de la,mancha", "de cuyo nombre...acordarme"};
  v = stringToVector<std::string>("en un lugar:de la,mancha;de cuyo nombre...acordarme", ":;");
  BOOST_CHECK_EQUAL_COLLECTIONS(expected2.begin(), expected2.end(), v.begin(), v.end());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
