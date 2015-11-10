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
 * @file tests/src/PhotometryCatalogConfig_test.cpp
 * @date 11/06/15
 * @author nikoapos
 */

#include <fstream>
#include <boost/test/unit_test.hpp>
#include <boost/filesystem.hpp>

#include "ElementsKernel/Temporary.h"
#include "Table/AsciiWriter.h"
#include "SourceCatalog/SourceAttributes/Photometry.h"

#include "Configuration/CatalogConfig.h"
#include "Configuration/PhotometryCatalogConfig.h"
#include "ConfigManager_fixture.h"

using namespace Euclid::Table;
using namespace Euclid::Configuration;
using namespace Euclid::SourceCatalog;
namespace po = boost::program_options;
namespace fs = boost::filesystem;

static Table createTestTable() {
  std::vector<ColumnInfo::info_type> info_list {
    ColumnInfo::info_type {"ID", typeid(std::int64_t)},
    ColumnInfo::info_type {"F1", typeid(double)},
    ColumnInfo::info_type {"F1_ERR", typeid(double)},
    ColumnInfo::info_type {"F2", typeid(double)},
    ColumnInfo::info_type {"F2_ERR", typeid(double)}
  };
  auto column_info = std::make_shared<ColumnInfo>(std::move(info_list));
  
  std::vector<Row> row_list {
    {{1l, 1.1, 2.1, 3.1, 4.1}, column_info},
    {{2l, 1.2, 2.2, 3.2, 4.2}, column_info},
    {{3l, 1.3, 2.3, 3.3, 4.3}, column_info}
  };
  
  return Table {std::move(row_list)};
}

struct BaseDirConfig : public Configuration {
  BaseDirConfig(long id) : Configuration(id) {
    declareDependency<CatalogConfig>();
    declareDependency<PhotometryCatalogConfig>();
  }
  void preInitialize(const UserValues& args) override {
    getDependency<CatalogConfig>().setBaseDir(args.at("test-base-dir").as<std::string>());
    getDependency<PhotometryCatalogConfig>().setBaseDir(args.at("test-base-dir").as<std::string>());
  }
};

struct PhotometryCatalogConfig_fixture : public ConfigManager_fixture {
  
  const std::string FILTER_MAPPING_FILE {"filter-mapping-file"};
  const std::string EXCLUDE_FILTER {"exclude-filter"};
  const std::string MISSING_PHOTOMETRY_FLAG {"missing-photometry-flag"};

  Table table = createTestTable();
  
  Elements::TempDir temp_dir;
  std::string catalog_filename {"catalog.txt"};
  std::string filter_mapping_filename {"mapping.txt"};
  fs::path relative_filename {fs::path{"relative"} / filter_mapping_filename};
  fs::path absolute_filename {temp_dir.path() / "absolute" / filter_mapping_filename};
  std::string wrong_format_filename {"wrong.txt"};
  
  std::map<std::string, po::variable_value> options_map {};
  
  PhotometryCatalogConfig_fixture() {
    
    {
      std::ofstream out {(temp_dir.path()/catalog_filename).string()};
      AsciiWriter{}.write(out, table);
    }
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
    options_map["input-catalog-file"].value() = boost::any(catalog_filename);
    options_map["input-catalog-format"].value() = boost::any(std::string{"AUTO"});
    options_map[FILTER_MAPPING_FILE].value() = boost::any(filter_mapping_filename);
    options_map[EXCLUDE_FILTER].value() = boost::any(std::vector<std::string>{});
    options_map[MISSING_PHOTOMETRY_FLAG].value() = boost::any(-99.);
    
  }
  
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (PhotometryCatalogConfig_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getProgramOptions_test, PhotometryCatalogConfig_fixture) {

  // Given
  config_manager.registerConfiguration<PhotometryCatalogConfig>();
  
  // When
  auto options = config_manager.closeRegistration();
  
  // Then
  BOOST_CHECK_NO_THROW(options.find(FILTER_MAPPING_FILE, false));
  BOOST_CHECK_NO_THROW(options.find(EXCLUDE_FILTER, false));
  BOOST_CHECK_NO_THROW(options.find(MISSING_PHOTOMETRY_FLAG, false));

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(nominalBandList_test, PhotometryCatalogConfig_fixture) {

  // Given
  config_manager.registerConfiguration<PhotometryCatalogConfig>();
  config_manager.closeRegistration();
  
  // When
  config_manager.initialize(options_map);
  auto& result = config_manager.getConfiguration<PhotometryCatalogConfig>().getPhotometricBands();
  
  // Then
  BOOST_CHECK_EQUAL(result.size(), 2);
  BOOST_CHECK_EQUAL(result[0], "Filter1");
  BOOST_CHECK_EQUAL(result[1], "Filter2");

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(relativePath_test, PhotometryCatalogConfig_fixture) {

  // Given
  config_manager.registerConfiguration<PhotometryCatalogConfig>();
  config_manager.closeRegistration();
  options_map[FILTER_MAPPING_FILE].value() = boost::any(relative_filename.string());
  
  // When
  config_manager.initialize(options_map);
  auto& result = config_manager.getConfiguration<PhotometryCatalogConfig>().getPhotometricBands();
  
  // Then
  BOOST_CHECK_EQUAL(result.size(), 2);
  BOOST_CHECK_EQUAL(result[0], "Filter1");
  BOOST_CHECK_EQUAL(result[1], "Filter2");

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(absolutePath_test, PhotometryCatalogConfig_fixture) {

  // Given
  config_manager.registerConfiguration<PhotometryCatalogConfig>();
  config_manager.closeRegistration();
  options_map[FILTER_MAPPING_FILE].value() = boost::any(absolute_filename.string());
  
  // When
  config_manager.initialize(options_map);
  auto& result = config_manager.getConfiguration<PhotometryCatalogConfig>().getPhotometricBands();
  
  // Then
  BOOST_CHECK_EQUAL(result.size(), 2);
  BOOST_CHECK_EQUAL(result[0], "Filter1");
  BOOST_CHECK_EQUAL(result[1], "Filter2");

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(nominalPhotometryCatalog_test, PhotometryCatalogConfig_fixture) {

  // Given
  config_manager.registerConfiguration<PhotometryCatalogConfig>();
  config_manager.closeRegistration();
  
  // When
  config_manager.initialize(options_map);
  auto& result = config_manager.getConfiguration<CatalogConfig>().getCatalog();
  
  // Then
  BOOST_CHECK_EQUAL(result.size(), 3);
  BOOST_CHECK_EQUAL(result.find(1)->getAttribute<Photometry>()->find("Filter1")->flux,  1.1);
  BOOST_CHECK_EQUAL(result.find(1)->getAttribute<Photometry>()->find("Filter1")->error, 2.1);
  BOOST_CHECK_EQUAL(result.find(1)->getAttribute<Photometry>()->find("Filter1")->missing_photometry_flag, false);
  BOOST_CHECK_EQUAL(result.find(1)->getAttribute<Photometry>()->find("Filter2")->flux,  3.1);
  BOOST_CHECK_EQUAL(result.find(1)->getAttribute<Photometry>()->find("Filter2")->error, 4.1);
  BOOST_CHECK_EQUAL(result.find(1)->getAttribute<Photometry>()->find("Filter2")->missing_photometry_flag, false);
  BOOST_CHECK_EQUAL(result.find(2)->getAttribute<Photometry>()->find("Filter1")->flux,  1.2);
  BOOST_CHECK_EQUAL(result.find(2)->getAttribute<Photometry>()->find("Filter1")->error, 2.2);
  BOOST_CHECK_EQUAL(result.find(2)->getAttribute<Photometry>()->find("Filter1")->missing_photometry_flag, false);
  BOOST_CHECK_EQUAL(result.find(2)->getAttribute<Photometry>()->find("Filter2")->flux,  3.2);
  BOOST_CHECK_EQUAL(result.find(2)->getAttribute<Photometry>()->find("Filter2")->error, 4.2);
  BOOST_CHECK_EQUAL(result.find(2)->getAttribute<Photometry>()->find("Filter2")->missing_photometry_flag, false);
  BOOST_CHECK_EQUAL(result.find(3)->getAttribute<Photometry>()->find("Filter1")->flux,  1.3);
  BOOST_CHECK_EQUAL(result.find(3)->getAttribute<Photometry>()->find("Filter1")->error, 2.3);
  BOOST_CHECK_EQUAL(result.find(3)->getAttribute<Photometry>()->find("Filter1")->missing_photometry_flag, false);
  BOOST_CHECK_EQUAL(result.find(3)->getAttribute<Photometry>()->find("Filter2")->flux,  3.3);
  BOOST_CHECK_EQUAL(result.find(3)->getAttribute<Photometry>()->find("Filter2")->error, 4.3);
  BOOST_CHECK_EQUAL(result.find(3)->getAttribute<Photometry>()->find("Filter2")->missing_photometry_flag, false);

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(missingFile_test, PhotometryCatalogConfig_fixture) {

  // Given
  config_manager.registerConfiguration<PhotometryCatalogConfig>();
  config_manager.closeRegistration();
  
  // When
  options_map[FILTER_MAPPING_FILE].value() = boost::any(std::string{"missing.txt"});
  
  // Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(fileFormatError_test, PhotometryCatalogConfig_fixture) {

  // Given
  config_manager.registerConfiguration<PhotometryCatalogConfig>();
  config_manager.closeRegistration();
  
  // When
  options_map[FILTER_MAPPING_FILE].value() = boost::any(wrong_format_filename);
  
  // Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(excludeFilter_test, PhotometryCatalogConfig_fixture) {

  // Given
  config_manager.registerConfiguration<PhotometryCatalogConfig>();
  config_manager.closeRegistration();
  options_map[EXCLUDE_FILTER].as<std::vector<std::string>>().push_back("Filter1");
  
  // When
  config_manager.initialize(options_map);
  auto& result = config_manager.getConfiguration<PhotometryCatalogConfig>().getPhotometricBands();
  
  // Then
  BOOST_CHECK_EQUAL(result.size(), 1);
  BOOST_CHECK_EQUAL(result[0], "Filter2");
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(wrongExcludeFilter_test, PhotometryCatalogConfig_fixture) {

  // Given
  config_manager.registerConfiguration<PhotometryCatalogConfig>();
  config_manager.closeRegistration();
  
  // When
  options_map[EXCLUDE_FILTER].as<std::vector<std::string>>().push_back("Filter1");
  options_map[EXCLUDE_FILTER].as<std::vector<std::string>>().push_back("wrong");
  
  // Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(missingPhotometryFlag_test, PhotometryCatalogConfig_fixture) {

  // Given
  config_manager.registerConfiguration<PhotometryCatalogConfig>();
  config_manager.closeRegistration();
  
  // When
  options_map[MISSING_PHOTOMETRY_FLAG].value() = boost::any(1.2);
  config_manager.initialize(options_map);
  auto& result = config_manager.getConfiguration<CatalogConfig>().getCatalog();
  
  // Then
  BOOST_CHECK_EQUAL(result.size(), 3);
  BOOST_CHECK_EQUAL(result.find(1)->getAttribute<Photometry>()->find("Filter1")->flux,  1.1);
  BOOST_CHECK_EQUAL(result.find(1)->getAttribute<Photometry>()->find("Filter1")->error, 2.1);
  BOOST_CHECK_EQUAL(result.find(1)->getAttribute<Photometry>()->find("Filter1")->missing_photometry_flag, false);
  BOOST_CHECK_EQUAL(result.find(1)->getAttribute<Photometry>()->find("Filter2")->flux,  3.1);
  BOOST_CHECK_EQUAL(result.find(1)->getAttribute<Photometry>()->find("Filter2")->error, 4.1);
  BOOST_CHECK_EQUAL(result.find(1)->getAttribute<Photometry>()->find("Filter2")->missing_photometry_flag, false);
  BOOST_CHECK_EQUAL(result.find(2)->getAttribute<Photometry>()->find("Filter1")->flux,  1.2);
  BOOST_CHECK_EQUAL(result.find(2)->getAttribute<Photometry>()->find("Filter1")->error, 2.2);
  BOOST_CHECK_EQUAL(result.find(2)->getAttribute<Photometry>()->find("Filter1")->missing_photometry_flag, true);
  BOOST_CHECK_EQUAL(result.find(2)->getAttribute<Photometry>()->find("Filter2")->flux,  3.2);
  BOOST_CHECK_EQUAL(result.find(2)->getAttribute<Photometry>()->find("Filter2")->error, 4.2);
  BOOST_CHECK_EQUAL(result.find(2)->getAttribute<Photometry>()->find("Filter2")->missing_photometry_flag, false);
  BOOST_CHECK_EQUAL(result.find(3)->getAttribute<Photometry>()->find("Filter1")->flux,  1.3);
  BOOST_CHECK_EQUAL(result.find(3)->getAttribute<Photometry>()->find("Filter1")->error, 2.3);
  BOOST_CHECK_EQUAL(result.find(3)->getAttribute<Photometry>()->find("Filter1")->missing_photometry_flag, false);
  BOOST_CHECK_EQUAL(result.find(3)->getAttribute<Photometry>()->find("Filter2")->flux,  3.3);
  BOOST_CHECK_EQUAL(result.find(3)->getAttribute<Photometry>()->find("Filter2")->error, 4.3);
  BOOST_CHECK_EQUAL(result.find(3)->getAttribute<Photometry>()->find("Filter2")->missing_photometry_flag, false);

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


