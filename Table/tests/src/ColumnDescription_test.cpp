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
 * @file tests/src/ColumnDescription_test.cpp
 * @date 09/07/16
 * @author nikoapos
 */

#include <boost/test/unit_test.hpp>

#include "ElementsKernel/Exception.h"
#include "Table/ColumnDescription.h"

using namespace Euclid::Table;

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (ColumnDescription_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(NominalCase) {

  // Given
  std::string name = "Name";
  std::type_index type = typeid(double);
  std::string unit = "u";
  std::string description = "Desc";

  // When
  ColumnDescription result {name, type, unit, description};

  // Then
  BOOST_CHECK_EQUAL(result.name, name);
  BOOST_CHECK_EQUAL(result.type.name(), type.name());
  BOOST_CHECK_EQUAL(result.unit, unit);
  BOOST_CHECK_EQUAL(result.description, description);

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(DefaultValues) {

  // Given
  std::string name = "Name";

  // When
  ColumnDescription result {name};

  // Then
  BOOST_CHECK_EQUAL(result.name, name);
  BOOST_CHECK_EQUAL(result.type.name(), typeid(std::string).name());
  BOOST_CHECK_EQUAL(result.unit, "");
  BOOST_CHECK_EQUAL(result.description, "");

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(EmptyStringName) {

  // Given
  std::string name = "";

  // Then
  BOOST_CHECK_THROW(ColumnDescription{name}, Elements::Exception);

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(NameWithWhitespaces) {

  // Given
  std::string space = "Sp ace";
  std::string tab = "Ta\tb";
  std::string carriage_return = "Carrage\rReturn";
  std::string new_line = "New\nLine";
  std::string new_page = "New\fPage";

  // Then
  ColumnDescription{space};
  ColumnDescription{tab};
  BOOST_CHECK_THROW(ColumnDescription{carriage_return}, Elements::Exception);
  BOOST_CHECK_THROW(ColumnDescription{new_line}, Elements::Exception);
  BOOST_CHECK_THROW(ColumnDescription{new_page}, Elements::Exception);

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


