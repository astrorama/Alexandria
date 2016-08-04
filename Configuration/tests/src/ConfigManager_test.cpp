/*  
 * Copyright (C) 2012-2020 Euclid Science Ground Segment    
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
 * @file tests/src/ConfigManager_test.cpp
 * @date 11/05/15
 * @author nikoapos
 */

#include <boost/test/unit_test.hpp>

#include "Configuration/ConfigManager.h"
#include "ConfigManager_fixture.h"

using namespace Euclid::Configuration;
namespace po = boost::program_options;

class Config1 : public Configuration {
public:
  Config1(long id) : Configuration(id) {}
  std::map<std::string, OptionDescriptionList> getProgramOptions() override {
    return {{"Test",{{"par-1", po::value<int>(), ""}}}};
  }
  bool pre_initialized = false;
  bool initialized = false;
  bool post_initialized = false;
  void preInitialize(const UserValues&) override {
    BOOST_CHECK(!pre_initialized);
    BOOST_CHECK(!initialized);
    BOOST_CHECK(!post_initialized);
    pre_initialized = true;
  }
  void initialize(const UserValues&) override {
    BOOST_CHECK(pre_initialized);
    BOOST_CHECK(!initialized);
    BOOST_CHECK(!post_initialized);
    initialized = true;
  }
  void postInitialize(const UserValues&) override {
    BOOST_CHECK(pre_initialized);
    BOOST_CHECK(initialized);
    BOOST_CHECK(!post_initialized);
    post_initialized = true;
  }
};

class Config2 : public Configuration {
public:
  Config2(long id) : Configuration(id) {}
  std::map<std::string, OptionDescriptionList> getProgramOptions() override {
    return {{"Test",{{"par-2", po::value<int>(), ""}}}};
  }
  bool pre_initialized = false;
  bool initialized = false;
  bool post_initialized = false;
  void preInitialize(const UserValues&) override {
    BOOST_CHECK(!pre_initialized);
    BOOST_CHECK(!initialized);
    BOOST_CHECK(!post_initialized);
    pre_initialized = true;
  }
  void initialize(const UserValues&) override {
    BOOST_CHECK(pre_initialized);
    BOOST_CHECK(!initialized);
    BOOST_CHECK(!post_initialized);
    initialized = true;
  }
  void postInitialize(const UserValues&) override {
    BOOST_CHECK(pre_initialized);
    BOOST_CHECK(initialized);
    BOOST_CHECK(!post_initialized);
    post_initialized = true;
  }
};

class Config3 : public Configuration {
public:
  Config3(long id) : Configuration(id) {
    declareDependency<Config1>();
    declareDependency<Config2>();
  }
  std::map<std::string, OptionDescriptionList> getProgramOptions() override {
    return {{"Test",{{"par-3", po::value<int>(), ""}}}};
  }
  bool pre_initialized = false;
  bool initialized = false;
  bool post_initialized = false;
  void preInitialize(const UserValues&) override {
    BOOST_CHECK(!pre_initialized);
    BOOST_CHECK(!initialized);
    BOOST_CHECK(!post_initialized);
    pre_initialized = true;
  }
  void initialize(const UserValues&) override {
    BOOST_CHECK(getDependency<Config1>().getCurrentState() == State::INITIALIZED);
    BOOST_CHECK(getDependency<Config2>().getCurrentState() == State::INITIALIZED);
    BOOST_CHECK(pre_initialized);
    BOOST_CHECK(!initialized);
    BOOST_CHECK(!post_initialized);
    initialized = true;
  }
  void postInitialize(const UserValues&) override {
    BOOST_CHECK(pre_initialized);
    BOOST_CHECK(initialized);
    BOOST_CHECK(!post_initialized);
    post_initialized = true;
  }
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (ConfigManager_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(registerConfiguration, ConfigManager_fixture) {

  // Given
  config_manager.registerConfiguration<Config3>();
  
  // When
  config_manager.closeRegistration();
  config_manager.initialize(std::map<std::string, po::variable_value>{});
  
  // Then
  BOOST_CHECK_NO_THROW(config_manager.getConfiguration<Config1>());
  BOOST_CHECK_NO_THROW(config_manager.getConfiguration<Config2>());
  BOOST_CHECK_NO_THROW(config_manager.getConfiguration<Config3>());

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(registerConfigurationWhenClosed, ConfigManager_fixture) {
  
  // When
  config_manager.closeRegistration();
  
  // Then
  BOOST_CHECK_THROW(config_manager.registerConfiguration<Config1>(), Elements::Exception);

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(circularDependency, ConfigManager_fixture) {
  
  // Given
  config_manager.registerConfiguration<Config3>();
  
  // When
  config_manager.registerDependency<Config1, Config3>();
  
  // Then
  BOOST_CHECK_THROW(config_manager.closeRegistration(), Elements::Exception);

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getProgramOptions, ConfigManager_fixture) {
  
  // Given
  config_manager.registerConfiguration<Config3>();
  
  // When
  auto options = config_manager.closeRegistration();
  
  // Then
  BOOST_CHECK_NO_THROW(options.find("par-1", false));
  BOOST_CHECK_NO_THROW(options.find("par-2", false));
  BOOST_CHECK_NO_THROW(options.find("par-3", false));

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(initialize, ConfigManager_fixture) {
  
  // Given
  config_manager.registerConfiguration<Config3>();
  
  // When
  config_manager.closeRegistration();
  config_manager.initialize(std::map<std::string, po::variable_value>{});
  auto& conf1 = config_manager.getConfiguration<Config1>();
  auto& conf2 = config_manager.getConfiguration<Config2>();
  auto& conf3 = config_manager.getConfiguration<Config3>();
  
  // Then
  BOOST_CHECK(conf1.pre_initialized);
  BOOST_CHECK(conf1.initialized);
  BOOST_CHECK(conf1.post_initialized);
  BOOST_CHECK(conf1.getCurrentState() == Configuration::State::FINAL);
  BOOST_CHECK(conf2.pre_initialized);
  BOOST_CHECK(conf2.initialized);
  BOOST_CHECK(conf2.post_initialized);
  BOOST_CHECK(conf2.getCurrentState() == Configuration::State::FINAL);
  BOOST_CHECK(conf3.pre_initialized);
  BOOST_CHECK(conf3.initialized);
  BOOST_CHECK(conf3.post_initialized);
  BOOST_CHECK(conf3.getCurrentState() == Configuration::State::FINAL);

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getConfigurationNotInitialized, ConfigManager_fixture) {
  
  // Given
  config_manager.registerConfiguration<Config1>();
  
  // When
  config_manager.closeRegistration();
  
  // Then
  BOOST_CHECK_THROW(config_manager.getConfiguration<Config1>(), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getConfigurationNotRegistered, ConfigManager_fixture) {
  
  // Given
  config_manager.registerConfiguration<Config1>();
  
  // When
  config_manager.closeRegistration();
  config_manager.initialize(std::map<std::string, po::variable_value>{});
  
  // Then
  BOOST_CHECK_THROW(config_manager.getConfiguration<Config2>(), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


