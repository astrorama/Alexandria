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
 * @file tests/src/PhotometricBandMappingConfig_test.cpp
 * @date 11/11/15
 * @author nikoapos
 */

#include <fstream>
#include <boost/test/unit_test.hpp>
#include <boost/filesystem.hpp>

#include "ElementsKernel/Temporary.h"

#include "Configuration/PhotometricBandMappingConfig.h"
#include "ConfigManager_fixture.h"

using namespace Euclid::Configuration;
namespace po = boost::program_options;
namespace fs = boost::filesystem;

struct BaseDirConfig : public Configuration {
  BaseDirConfig(long id) : Configuration(id) {
    declareDependency<PhotometricBandMappingConfig>();
  }
  void preInitialize(const UserValues& args) override {
    getDependency<PhotometricBandMappingConfig>().setBaseDir(args.at("test-base-dir").as<std::string>());
  }
};

struct PhotometricBandMappingConfig_fixture : public ConfigManager_fixture {
  
  const std::string FILTER_MAPPING_FILE {"filter-mapping-file"};
  const std::string EXCLUDE_FILTER {"exclude-filter"};
  
  Elements::TempDir temp_dir;
  std::string filter_mapping_filename {"mapping.txt"};
  fs::path relative_filename {fs::path{"relative"} / filter_mapping_filename};
  fs::path absolute_filename {temp_dir.path() / "absolute" / filter_mapping_filename};
  std::string wrong_format_filename {"wrong.txt"};
  
  std::map<std::string, po::variable_value> options_map {};
  
  PhotometricBandMappingConfig_fixture() {
    
    std::string mapping {
      "#Comment\n"
      "Filter1 F1 F1_ERR\n"
      "Filter2 F2 F2_ERR\n"
    };
    {
      std::ofstream out {(temp_dir.path()/filter_mapping_filename).string()};
      out << mapping;
    }
    {
      fs::create_directories((temp_dir.path()/relative_filename).parent_path());
      std::ofstream out {(temp_dir.path()/relative_filename).string()};
      out << mapping;
    }
    {
      fs::create_directories(absolute_filename.parent_path());
      std::ofstream out {absolute_filename.string()};
      out << mapping;
    }
    {
      std::ofstream out {(temp_dir.path()/wrong_format_filename).string()};
      out << "Filter1 F1 F1_ERR\n"
          << "Filter2 F2\n";
    }
    
    config_manager.registerConfiguration<BaseDirConfig>();
    
    options_map["test-base-dir"].value() = boost::any(temp_dir.path().string());
    options_map[FILTER_MAPPING_FILE].value() = boost::any(filter_mapping_filename);
    options_map[EXCLUDE_FILTER].value() = boost::any(std::vector<std::string>{});
    
  }
  
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (PhotometricBandMappingConfig_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getProgramOptions_test, PhotometricBandMappingConfig_fixture) {

  // Given
  config_manager.registerConfiguration<PhotometricBandMappingConfig>();
  
  // When
  auto options = config_manager.closeRegistration();
  
  // Then
  BOOST_CHECK_NO_THROW(options.find(FILTER_MAPPING_FILE, false));
  BOOST_CHECK_NO_THROW(options.find(EXCLUDE_FILTER, false));

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(nominalBandList_test, PhotometricBandMappingConfig_fixture) {

  // Given
  config_manager.registerConfiguration<PhotometricBandMappingConfig>();
  config_manager.closeRegistration();
  
  // When
  config_manager.initialize(options_map);
  auto& result = config_manager.getConfiguration<PhotometricBandMappingConfig>().getPhotometricBandMapping();
  
  // Then
  BOOST_CHECK_EQUAL(result.size(), 2);
  BOOST_CHECK_EQUAL(result[0].first, "Filter1");
  BOOST_CHECK_EQUAL(result[0].second.first, "F1");
  BOOST_CHECK_EQUAL(result[0].second.second, "F1_ERR");
  BOOST_CHECK_EQUAL(result[1].first, "Filter2");
  BOOST_CHECK_EQUAL(result[1].second.first, "F2");
  BOOST_CHECK_EQUAL(result[1].second.second, "F2_ERR");

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(relativePath_test, PhotometricBandMappingConfig_fixture) {

  // Given
  config_manager.registerConfiguration<PhotometricBandMappingConfig>();
  config_manager.closeRegistration();
  options_map[FILTER_MAPPING_FILE].value() = boost::any(relative_filename.string());
  
  // When
  config_manager.initialize(options_map);
  auto& result = config_manager.getConfiguration<PhotometricBandMappingConfig>().getPhotometricBandMapping();
  
  // Then
  BOOST_CHECK_EQUAL(result.size(), 2);
  BOOST_CHECK_EQUAL(result[0].first, "Filter1");
  BOOST_CHECK_EQUAL(result[0].second.first, "F1");
  BOOST_CHECK_EQUAL(result[0].second.second, "F1_ERR");
  BOOST_CHECK_EQUAL(result[1].first, "Filter2");
  BOOST_CHECK_EQUAL(result[1].second.first, "F2");
  BOOST_CHECK_EQUAL(result[1].second.second, "F2_ERR");

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(absolutePath_test, PhotometricBandMappingConfig_fixture) {

  // Given
  config_manager.registerConfiguration<PhotometricBandMappingConfig>();
  config_manager.closeRegistration();
  options_map[FILTER_MAPPING_FILE].value() = boost::any(absolute_filename.string());
  
  // When
  config_manager.initialize(options_map);
  auto& result = config_manager.getConfiguration<PhotometricBandMappingConfig>().getPhotometricBandMapping();
  
  // Then
  BOOST_CHECK_EQUAL(result.size(), 2);
  BOOST_CHECK_EQUAL(result[0].first, "Filter1");
  BOOST_CHECK_EQUAL(result[0].second.first, "F1");
  BOOST_CHECK_EQUAL(result[0].second.second, "F1_ERR");
  BOOST_CHECK_EQUAL(result[1].first, "Filter2");
  BOOST_CHECK_EQUAL(result[1].second.first, "F2");
  BOOST_CHECK_EQUAL(result[1].second.second, "F2_ERR");

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(missingFile_test, PhotometricBandMappingConfig_fixture) {

  // Given
  config_manager.registerConfiguration<PhotometricBandMappingConfig>();
  config_manager.closeRegistration();
  
  // When
  options_map[FILTER_MAPPING_FILE].value() = boost::any(std::string{"missing.txt"});
  
  // Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(fileFormatError_test, PhotometricBandMappingConfig_fixture) {

  // Given
  config_manager.registerConfiguration<PhotometricBandMappingConfig>();
  config_manager.closeRegistration();
  
  // When
  options_map[FILTER_MAPPING_FILE].value() = boost::any(wrong_format_filename);
  
  // Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(excludeFilter_test, PhotometricBandMappingConfig_fixture) {

  // Given
  config_manager.registerConfiguration<PhotometricBandMappingConfig>();
  config_manager.closeRegistration();
  options_map[EXCLUDE_FILTER].as<std::vector<std::string>>().push_back("Filter1");
  
  // When
  config_manager.initialize(options_map);
  auto& result = config_manager.getConfiguration<PhotometricBandMappingConfig>().getPhotometricBandMapping();
  
  // Then
  BOOST_CHECK_EQUAL(result.size(), 1);
  BOOST_CHECK_EQUAL(result[0].first, "Filter2");
  BOOST_CHECK_EQUAL(result[0].second.first, "F2");
  BOOST_CHECK_EQUAL(result[0].second.second, "F2_ERR");
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(wrongExcludeFilter_test, PhotometricBandMappingConfig_fixture) {

  // Given
  config_manager.registerConfiguration<PhotometricBandMappingConfig>();
  config_manager.closeRegistration();
  
  // When
  options_map[EXCLUDE_FILTER].as<std::vector<std::string>>().push_back("Filter1");
  options_map[EXCLUDE_FILTER].as<std::vector<std::string>>().push_back("wrong");
  
  // Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


