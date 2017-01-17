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
 * @file tests/src/SpecZCatalogConfig_test.cpp
 * @date 11/06/15
 * @author nikoapos
 */

#include <fstream>
#include <boost/test/unit_test.hpp>
#include <boost/filesystem.hpp>

#include "ElementsKernel/Temporary.h"
#include "Table/AsciiWriter.h"
#include "SourceCatalog/SourceAttributes/SpectroscopicRedshift.h"

#include "Configuration/CatalogConfig.h"
#include "Configuration/SpecZCatalogConfig.h"
#include "ConfigManager_fixture.h"

using namespace Euclid::Table;
using namespace Euclid::Configuration;
using namespace Euclid::SourceCatalog;
namespace po = boost::program_options;
namespace fs = boost::filesystem;

static Table createTestTable() {
  std::vector<ColumnInfo::info_type> info_list {
    ColumnInfo::info_type {"ID", typeid(std::int64_t)},
    ColumnInfo::info_type {"SPECZ", typeid(double)},
    ColumnInfo::info_type {"ERR", typeid(double)}
  };
  auto column_info = std::make_shared<ColumnInfo>(std::move(info_list));
  
  std::vector<Row> row_list {
    {{std::int64_t{1}, 1.1, 0.1}, column_info},
    {{std::int64_t{2}, 1.2, 0.2}, column_info},
    {{std::int64_t{3}, 1.3, 0.3}, column_info}
  };
  
  return Table {std::move(row_list)};
}

struct BaseDirConfig : public Configuration {
  BaseDirConfig(long id) : Configuration(id) {
    declareDependency<CatalogConfig>();
  }
  void preInitialize(const UserValues& args) override {
    getDependency<CatalogConfig>().setBaseDir(args.at("test-base-dir").as<std::string>());
  }
};

struct SpecZCatalogConfig_fixture : public ConfigManager_fixture {
  
  const std::string SPECZ_COLUMN_NAME {"spec-z-column-name"};
  const std::string SPECZ_COLUMN_INDEX {"spec-z-column-index"};
  const std::string SPECZ_ERR_COLUMN_NAME {"spec-z-err-column-name"};
  const std::string SPECZ_ERR_COLUMN_INDEX {"spec-z-err-column-index"};
  
  Table table = createTestTable();
  
  Elements::TempDir temp_dir;
  std::string filename {"catalog.txt"};
  
  std::map<std::string, po::variable_value> options_map {};
  
  SpecZCatalogConfig_fixture() {
    
    {
      std::ofstream out {(temp_dir.path()/filename).string()};
      AsciiWriter(out).addData(table);
    }
    
    config_manager.registerConfiguration<BaseDirConfig>();
    
    options_map["test-base-dir"].value() = boost::any(temp_dir.path().string());
    options_map["input-catalog-file"].value() = boost::any(filename);
    options_map["input-catalog-format"].value() = boost::any(std::string{"AUTO"});
    options_map[SPECZ_COLUMN_NAME].value() = boost::any(std::string{"SPECZ"});
    options_map[SPECZ_ERR_COLUMN_NAME].value() = boost::any(std::string{"ERR"});
    
  }
  
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (SpecZCatalogConfig_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getProgramOptions_test, SpecZCatalogConfig_fixture) {

  // Given
  config_manager.registerConfiguration<SpecZCatalogConfig>();
  
  // When
  auto options = config_manager.closeRegistration();
  
  // Then
  BOOST_CHECK_NO_THROW(options.find(SPECZ_COLUMN_NAME, false));
  BOOST_CHECK_NO_THROW(options.find(SPECZ_COLUMN_INDEX, false));
  BOOST_CHECK_NO_THROW(options.find(SPECZ_ERR_COLUMN_NAME, false));
  BOOST_CHECK_NO_THROW(options.find(SPECZ_ERR_COLUMN_INDEX, false));

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(bothSpeczNameIndex_test, SpecZCatalogConfig_fixture) {
  
  // Given
  options_map[SPECZ_COLUMN_NAME].value() = boost::any(std::string{"SPECZ"});
  options_map[SPECZ_COLUMN_INDEX].value() = boost::any(2);
  
  // When
  config_manager.registerConfiguration<SpecZCatalogConfig>();
  config_manager.closeRegistration();
  
  //Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(noneOfSpeczNameIndex_test, SpecZCatalogConfig_fixture) {
  
  // Given
  options_map.erase(SPECZ_COLUMN_NAME);
  options_map.erase(SPECZ_COLUMN_INDEX);
  
  // When
  config_manager.registerConfiguration<SpecZCatalogConfig>();
  config_manager.closeRegistration();
  
  //Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(invalidSpeczIndex_test, SpecZCatalogConfig_fixture) {
  
  // Given
  options_map.erase(SPECZ_COLUMN_NAME);
  options_map[SPECZ_COLUMN_INDEX].value() = boost::any(0);
  
  // When
  config_manager.registerConfiguration<SpecZCatalogConfig>();
  config_manager.closeRegistration();
  
  //Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(bothErrNameIndex_test, SpecZCatalogConfig_fixture) {
  
  // Given
  options_map[SPECZ_ERR_COLUMN_NAME].value() = boost::any(std::string{"ERR"});
  options_map[SPECZ_ERR_COLUMN_INDEX].value() = boost::any(3);
  
  // When
  config_manager.registerConfiguration<SpecZCatalogConfig>();
  config_manager.closeRegistration();
  
  //Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(invalidErrIndex_test, SpecZCatalogConfig_fixture) {
  
  // Given
  options_map.erase(SPECZ_ERR_COLUMN_NAME);
  options_map[SPECZ_ERR_COLUMN_INDEX].value() = boost::any(0);
  
  // When
  config_manager.registerConfiguration<SpecZCatalogConfig>();
  config_manager.closeRegistration();
  
  //Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(nominal_test, SpecZCatalogConfig_fixture) {
  
  // Given
  config_manager.registerConfiguration<SpecZCatalogConfig>();
  config_manager.closeRegistration();
  
  // When
  config_manager.initialize(options_map);
  auto result = config_manager.getConfiguration<CatalogConfig>().getCatalog();
  
  //Then
  BOOST_CHECK_EQUAL(result.size(), 3);
  BOOST_CHECK_EQUAL(result.find(1)->getAttribute<SpectroscopicRedshift>()->getValue(), 1.1);
  BOOST_CHECK_EQUAL(result.find(1)->getAttribute<SpectroscopicRedshift>()->getError(), 0.1);
  BOOST_CHECK_EQUAL(result.find(2)->getAttribute<SpectroscopicRedshift>()->getValue(), 1.2);
  BOOST_CHECK_EQUAL(result.find(2)->getAttribute<SpectroscopicRedshift>()->getError(), 0.2);
  BOOST_CHECK_EQUAL(result.find(3)->getAttribute<SpectroscopicRedshift>()->getValue(), 1.3);
  BOOST_CHECK_EQUAL(result.find(3)->getAttribute<SpectroscopicRedshift>()->getError(), 0.3);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(noError_test, SpecZCatalogConfig_fixture) {
  
  // Given
  config_manager.registerConfiguration<SpecZCatalogConfig>();
  config_manager.closeRegistration();
  options_map.erase(SPECZ_ERR_COLUMN_INDEX);
  options_map.erase(SPECZ_ERR_COLUMN_NAME);
  
  // When
  config_manager.initialize(options_map);
  auto result = config_manager.getConfiguration<CatalogConfig>().getCatalog();
  
  //Then
  BOOST_CHECK_EQUAL(result.size(), 3);
  BOOST_CHECK_EQUAL(result.find(1)->getAttribute<SpectroscopicRedshift>()->getValue(), 1.1);
  BOOST_CHECK_EQUAL(result.find(1)->getAttribute<SpectroscopicRedshift>()->getError(), 0.);
  BOOST_CHECK_EQUAL(result.find(2)->getAttribute<SpectroscopicRedshift>()->getValue(), 1.2);
  BOOST_CHECK_EQUAL(result.find(2)->getAttribute<SpectroscopicRedshift>()->getError(), 0.);
  BOOST_CHECK_EQUAL(result.find(3)->getAttribute<SpectroscopicRedshift>()->getValue(), 1.3);
  BOOST_CHECK_EQUAL(result.find(3)->getAttribute<SpectroscopicRedshift>()->getError(), 0.);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(unknownSpeczName_test, SpecZCatalogConfig_fixture) {
  
  // Given
  options_map[SPECZ_COLUMN_NAME].value() = boost::any(std::string{"Unknown"});
  options_map.erase(SPECZ_COLUMN_INDEX);
  
  // When
  config_manager.registerConfiguration<SpecZCatalogConfig>();
  config_manager.closeRegistration();
  
  //Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(outOfBoundsSpeczIndex_test, SpecZCatalogConfig_fixture) {
  
  // Given
  options_map.erase(SPECZ_COLUMN_NAME);
  options_map[SPECZ_COLUMN_INDEX].value() = boost::any(10);
  
  // When
  config_manager.registerConfiguration<SpecZCatalogConfig>();
  config_manager.closeRegistration();
  
  //Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(unknownErrName_test, SpecZCatalogConfig_fixture) {
  
  // Given
  options_map[SPECZ_ERR_COLUMN_NAME].value() = boost::any(std::string{"Unknown"});
  options_map.erase(SPECZ_ERR_COLUMN_INDEX);
  
  // When
  config_manager.registerConfiguration<SpecZCatalogConfig>();
  config_manager.closeRegistration();
  
  //Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(outOfBoundsErrIndex_test, SpecZCatalogConfig_fixture) {
  
  // Given
  options_map.erase(SPECZ_ERR_COLUMN_NAME);
  options_map[SPECZ_ERR_COLUMN_INDEX].value() = boost::any(10);
  
  // When
  config_manager.registerConfiguration<SpecZCatalogConfig>();
  config_manager.closeRegistration();
  
  //Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


