/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
 *
 * This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General
 * Public License as published by the Free Software Foundation; either version 3.0 of the License, or (at your option)
 * any later version.
 *
 * This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
 * warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
 * details.
 *
 * You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 */

/**
 * @file tests/src/Configuration_test.cpp
 * @date 11/05/15
 * @author nikoapos
 */

#include <boost/test/unit_test.hpp>

#include "ConfigManager_fixture.h"
#include "Configuration/Configuration.h"

using namespace Euclid::Configuration;

class Config1 : public Configuration {
public:
  explicit Config1(long id) : Configuration(id) {}
};

class Config2 : public Configuration {
public:
  explicit Config2(long id) : Configuration(id) {}
};

class Config3 : public Configuration {
public:
  explicit Config3(long id) : Configuration(id) {
    declareDependency<Config1>();
    declareDependency<Config2>();
  }
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(Configuration_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(state_test, ConfigManager_fixture) {

  // When
  Config1 config{timestamp};

  // Then
  BOOST_CHECK(config.getCurrentState() == Configuration::State::CONSTRUCTED);

  // When
  config.getCurrentState() = Configuration::State::PRE_INITIALIZED;

  // Then
  BOOST_CHECK(config.getCurrentState() == Configuration::State::PRE_INITIALIZED);

  // When
  config.getCurrentState() = Configuration::State::PRE_INITIALIZED;

  // Then
  BOOST_CHECK(config.getCurrentState() == Configuration::State::PRE_INITIALIZED);

  // When
  config.getCurrentState() = Configuration::State::INITIALIZED;

  // Then
  BOOST_CHECK(config.getCurrentState() == Configuration::State::INITIALIZED);

  // When
  config.getCurrentState() = Configuration::State::FINAL;

  // Then
  BOOST_CHECK(config.getCurrentState() == Configuration::State::FINAL);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(dependencies_test, ConfigManager_fixture) {

  // When
  Config3 config{timestamp};

  // Given
  auto& dependencies = config.getDependencies();

  // Then
  BOOST_CHECK_EQUAL(dependencies.size(), 2);
  BOOST_CHECK_EQUAL(dependencies.count(typeid(Config1)), 1);
  BOOST_CHECK_EQUAL(dependencies.count(typeid(Config2)), 1);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
