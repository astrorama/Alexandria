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
 * @file tests/src/CatalogConfig_test.cpp
 * @date 11/05/15
 * @author nikoapos
 */

#include <fstream>
#include <boost/test/unit_test.hpp>
#include <boost/filesystem.hpp>
#include <CCfits/CCfits>

#include "ElementsKernel/Temporary.h"
#include "Table/AsciiWriter.h"
#include "Table/FitsWriter.h"

#include "Configuration/CatalogConfig.h"
#include "ConfigManager_fixture.h"

using namespace Euclid::Table;
using namespace Euclid::Configuration;
using namespace Euclid::SourceCatalog;
namespace po = boost::program_options;
namespace fs = boost::filesystem;

static Table createTestTable() {
  std::vector<ColumnInfo::info_type> info_list {
    ColumnInfo::info_type {"Col1", typeid(std::int64_t)},
    ColumnInfo::info_type {"ID", typeid(std::int64_t)},
    ColumnInfo::info_type {"ID1", typeid(std::int64_t)},
    ColumnInfo::info_type {"ID2", typeid(std::int64_t)}
  };
  auto column_info = std::make_shared<ColumnInfo>(std::move(info_list));
  
  std::vector<Row> row_list {
    {{std::int64_t{10}, std::int64_t{20}, std::int64_t{30}, std::int64_t{40}}, column_info},
    {{std::int64_t{11}, std::int64_t{21}, std::int64_t{31}, std::int64_t{41}}, column_info},
    {{std::int64_t{12}, std::int64_t{22}, std::int64_t{32}, std::int64_t{42}}, column_info}
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

struct TestAttribute : public Attribute {
  TestAttribute(std::int64_t value) : value{value} {}
  std::int64_t value;
};

struct TestAttributeFromRow : public AttributeFromRow {
  std::unique_ptr<Attribute> createAttribute(const Euclid::Table::Row& row) override {
    return std::unique_ptr<Attribute>{new TestAttribute{boost::get<std::int64_t>(row["Col1"])}};
  }
};

struct TestAttributeHandlerConfig : public Configuration {
  TestAttributeHandlerConfig(long id) : Configuration(id) {
    declareDependency<CatalogConfig>();
  }
  void initialize(const UserValues&) override {
    getDependency<CatalogConfig>().addAttributeHandler(
                std::shared_ptr<AttributeFromRow>{new TestAttributeFromRow{}});
  }
};

struct CatalogConfig_fixture : public ConfigManager_fixture {
  
  const std::string INPUT_CATALOG_FILE {"input-catalog-file"};
  const std::string INPUT_CATALOG_FORMAT {"input-catalog-format"};
  const std::string SOURCE_ID_COLUMN_NAME {"source-id-column-name"};
  const std::string SOURCE_ID_COLUMN_INDEX {"source-id-column-index"};
  
  Table table = createTestTable();
  
  Elements::TempDir temp_dir;
  std::string fits_filename {"catalog.dat"};
  std::string ascii_filename {"catalog.txt"};
  fs::path relative_filename = fs::path{"relative"} / ascii_filename;
  fs::path absolute_filename = temp_dir.path() / "absolute" / ascii_filename;
  
  std::map<std::string, po::variable_value> options_map {};
  
  CatalogConfig_fixture() {
    
    {
      FitsWriter{(temp_dir.path()/fits_filename).string()}.setHduName("Test").addData(table);
    }
    {
      std::ofstream out {(temp_dir.path()/ascii_filename).string()};
      AsciiWriter(out).addData(table);
    }
    {
      fs::create_directories((temp_dir.path()/relative_filename).parent_path());
      std::ofstream out {(temp_dir.path()/relative_filename).string()};
      AsciiWriter(out).addData(table);
    }
    {
      fs::create_directories(absolute_filename.parent_path());
      std::ofstream out {absolute_filename.string()};
      AsciiWriter(out).addData(table);
    }
    
    config_manager.registerConfiguration<BaseDirConfig>();
    
    options_map["test-base-dir"].value() = boost::any(temp_dir.path().string());
    options_map[INPUT_CATALOG_FILE].value() = boost::any(ascii_filename);
    options_map[INPUT_CATALOG_FORMAT].value() = boost::any(std::string{"AUTO"});
  }
  
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (CatalogConfig_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getProgramOptions_test, CatalogConfig_fixture) {

  // Given
  config_manager.registerConfiguration<CatalogConfig>();
  
  // When
  auto options = config_manager.closeRegistration();
  
  // Then
  BOOST_CHECK_NO_THROW(options.find(INPUT_CATALOG_FILE, false));
  BOOST_CHECK_NO_THROW(options.find(INPUT_CATALOG_FORMAT, false));
  BOOST_CHECK_NO_THROW(options.find(SOURCE_ID_COLUMN_NAME, false));
  BOOST_CHECK_NO_THROW(options.find(SOURCE_ID_COLUMN_INDEX, false));

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(bothIdNameIndex_test, CatalogConfig_fixture) {
  
  // Given
  options_map[SOURCE_ID_COLUMN_NAME].value() = boost::any(std::string{"ID"});
  options_map[SOURCE_ID_COLUMN_INDEX].value() = boost::any(1);
  
  // When
  config_manager.registerConfiguration<CatalogConfig>();
  config_manager.closeRegistration();
  
  //Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(invalidIdIndex_test, CatalogConfig_fixture) {
  
  // Given
  options_map[SOURCE_ID_COLUMN_INDEX].value() = boost::any(0);
  
  // When
  config_manager.registerConfiguration<CatalogConfig>();
  config_manager.closeRegistration();
  
  //Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(invalidFormat_test, CatalogConfig_fixture) {
  
  // Given
  options_map[INPUT_CATALOG_FORMAT].value() = boost::any(std::string{"INVALID"});
  
  // When
  config_manager.registerConfiguration<CatalogConfig>();
  config_manager.closeRegistration();
  
  //Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(missingFile_test, CatalogConfig_fixture) {
  
  // Given
  config_manager.registerConfiguration<CatalogConfig>();
  config_manager.closeRegistration();
  
  // When
  options_map[INPUT_CATALOG_FILE].value() = boost::any(std::string{"missing"});
  
  //Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(wrongIdName_test, CatalogConfig_fixture) {
  
  // Given
  config_manager.registerConfiguration<CatalogConfig>();
  config_manager.closeRegistration();
  
  // When
  options_map[SOURCE_ID_COLUMN_NAME].value() = boost::any(std::string("Unknown"));
  
  //Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(wrongIdIndex_test, CatalogConfig_fixture) {
  
  // Given
  config_manager.registerConfiguration<CatalogConfig>();
  config_manager.closeRegistration();
  
  // When
  options_map[SOURCE_ID_COLUMN_INDEX].value() = boost::any(10);
  
  //Then
  BOOST_CHECK_THROW(config_manager.initialize(options_map), Elements::Exception);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ascii_test, CatalogConfig_fixture) {
  
  // Given
  config_manager.registerConfiguration<CatalogConfig>();
  config_manager.closeRegistration();
  options_map[INPUT_CATALOG_FILE].value() = boost::any(ascii_filename);
  options_map[INPUT_CATALOG_FORMAT].value() = boost::any(std::string{"ASCII"});
  
  // When
  config_manager.initialize(options_map);
  auto catalog = config_manager.getConfiguration<CatalogConfig>().getCatalog();
  
  //Then
  BOOST_CHECK_EQUAL(catalog.size(), 3);
  BOOST_CHECK(catalog.find(10) == nullptr);
  BOOST_CHECK(catalog.find(11) == nullptr);
  BOOST_CHECK(catalog.find(12) == nullptr);
  BOOST_CHECK(catalog.find(20) != nullptr);
  BOOST_CHECK(catalog.find(21) != nullptr);
  BOOST_CHECK(catalog.find(22) != nullptr);
  BOOST_CHECK(catalog.find(30) == nullptr);
  BOOST_CHECK(catalog.find(31) == nullptr);
  BOOST_CHECK(catalog.find(32) == nullptr);
  BOOST_CHECK(catalog.find(40) == nullptr);
  BOOST_CHECK(catalog.find(41) == nullptr);
  BOOST_CHECK(catalog.find(42) == nullptr);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(fits_test, CatalogConfig_fixture) {
  
  // Given
  config_manager.registerConfiguration<CatalogConfig>();
  config_manager.closeRegistration();
  options_map[INPUT_CATALOG_FILE].value() = boost::any(fits_filename);
  options_map[INPUT_CATALOG_FORMAT].value() = boost::any(std::string{"FITS"});
  
  // When
  config_manager.initialize(options_map);
  auto catalog = config_manager.getConfiguration<CatalogConfig>().getCatalog();
  
  //Then
  BOOST_CHECK_EQUAL(catalog.size(), 3);
  BOOST_CHECK(catalog.find(10) == nullptr);
  BOOST_CHECK(catalog.find(11) == nullptr);
  BOOST_CHECK(catalog.find(12) == nullptr);
  BOOST_CHECK(catalog.find(20) != nullptr);
  BOOST_CHECK(catalog.find(21) != nullptr);
  BOOST_CHECK(catalog.find(22) != nullptr);
  BOOST_CHECK(catalog.find(30) == nullptr);
  BOOST_CHECK(catalog.find(31) == nullptr);
  BOOST_CHECK(catalog.find(32) == nullptr);
  BOOST_CHECK(catalog.find(40) == nullptr);
  BOOST_CHECK(catalog.find(41) == nullptr);
  BOOST_CHECK(catalog.find(42) == nullptr);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(relativePath_test, CatalogConfig_fixture) {
  
  // Given
  config_manager.registerConfiguration<CatalogConfig>();
  config_manager.closeRegistration();
  options_map[INPUT_CATALOG_FILE].value() = boost::any(relative_filename.string());
  
  // When
  config_manager.initialize(options_map);
  auto catalog = config_manager.getConfiguration<CatalogConfig>().getCatalog();
  
  //Then
  BOOST_CHECK_EQUAL(catalog.size(), 3);
  BOOST_CHECK(catalog.find(10) == nullptr);
  BOOST_CHECK(catalog.find(11) == nullptr);
  BOOST_CHECK(catalog.find(12) == nullptr);
  BOOST_CHECK(catalog.find(20) != nullptr);
  BOOST_CHECK(catalog.find(21) != nullptr);
  BOOST_CHECK(catalog.find(22) != nullptr);
  BOOST_CHECK(catalog.find(30) == nullptr);
  BOOST_CHECK(catalog.find(31) == nullptr);
  BOOST_CHECK(catalog.find(32) == nullptr);
  BOOST_CHECK(catalog.find(40) == nullptr);
  BOOST_CHECK(catalog.find(41) == nullptr);
  BOOST_CHECK(catalog.find(42) == nullptr);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(absolutePath_test, CatalogConfig_fixture) {
  
  // Given
  config_manager.registerConfiguration<CatalogConfig>();
  config_manager.closeRegistration();
  options_map[INPUT_CATALOG_FILE].value() = boost::any(relative_filename.string());
  
  // When
  config_manager.initialize(options_map);
  auto catalog = config_manager.getConfiguration<CatalogConfig>().getCatalog();
  
  //Then
  BOOST_CHECK_EQUAL(catalog.size(), 3);
  BOOST_CHECK(catalog.find(10) == nullptr);
  BOOST_CHECK(catalog.find(11) == nullptr);
  BOOST_CHECK(catalog.find(12) == nullptr);
  BOOST_CHECK(catalog.find(20) != nullptr);
  BOOST_CHECK(catalog.find(21) != nullptr);
  BOOST_CHECK(catalog.find(22) != nullptr);
  BOOST_CHECK(catalog.find(30) == nullptr);
  BOOST_CHECK(catalog.find(31) == nullptr);
  BOOST_CHECK(catalog.find(32) == nullptr);
  BOOST_CHECK(catalog.find(40) == nullptr);
  BOOST_CHECK(catalog.find(41) == nullptr);
  BOOST_CHECK(catalog.find(42) == nullptr);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(idName_test, CatalogConfig_fixture) {
  
  // Given
  config_manager.registerConfiguration<CatalogConfig>();
  config_manager.closeRegistration();
  options_map[SOURCE_ID_COLUMN_NAME].value() = boost::any(std::string{"ID1"});
  
  // When
  config_manager.initialize(options_map);
  auto catalog = config_manager.getConfiguration<CatalogConfig>().getCatalog();
  
  //Then
  BOOST_CHECK_EQUAL(catalog.size(), 3);
  BOOST_CHECK(catalog.find(10) == nullptr);
  BOOST_CHECK(catalog.find(11) == nullptr);
  BOOST_CHECK(catalog.find(12) == nullptr);
  BOOST_CHECK(catalog.find(20) == nullptr);
  BOOST_CHECK(catalog.find(21) == nullptr);
  BOOST_CHECK(catalog.find(22) == nullptr);
  BOOST_CHECK(catalog.find(30) != nullptr);
  BOOST_CHECK(catalog.find(31) != nullptr);
  BOOST_CHECK(catalog.find(32) != nullptr);
  BOOST_CHECK(catalog.find(40) == nullptr);
  BOOST_CHECK(catalog.find(41) == nullptr);
  BOOST_CHECK(catalog.find(42) == nullptr);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(idIndex_test, CatalogConfig_fixture) {
  
  // Given
  config_manager.registerConfiguration<CatalogConfig>();
  config_manager.closeRegistration();
  options_map[SOURCE_ID_COLUMN_INDEX].value() = boost::any(4);
  
  // When
  config_manager.initialize(options_map);
  auto catalog = config_manager.getConfiguration<CatalogConfig>().getCatalog();
  
  //Then
  BOOST_CHECK_EQUAL(catalog.size(), 3);
  BOOST_CHECK(catalog.find(10) == nullptr);
  BOOST_CHECK(catalog.find(11) == nullptr);
  BOOST_CHECK(catalog.find(12) == nullptr);
  BOOST_CHECK(catalog.find(20) == nullptr);
  BOOST_CHECK(catalog.find(21) == nullptr);
  BOOST_CHECK(catalog.find(22) == nullptr);
  BOOST_CHECK(catalog.find(30) == nullptr);
  BOOST_CHECK(catalog.find(31) == nullptr);
  BOOST_CHECK(catalog.find(32) == nullptr);
  BOOST_CHECK(catalog.find(40) != nullptr);
  BOOST_CHECK(catalog.find(41) != nullptr);
  BOOST_CHECK(catalog.find(42) != nullptr);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(attributeHandler_test, CatalogConfig_fixture) {
  
  // Given
  config_manager.registerConfiguration<CatalogConfig>();
  config_manager.registerConfiguration<TestAttributeHandlerConfig>();
  config_manager.closeRegistration();
  
  // When
  config_manager.initialize(options_map);
  auto catalog = config_manager.getConfiguration<CatalogConfig>().getCatalog();
  
  //Then
  BOOST_CHECK_EQUAL(catalog.size(), 3);
  BOOST_CHECK_EQUAL(catalog.find(20)->getAttribute<TestAttribute>()->value, 10);
  BOOST_CHECK_EQUAL(catalog.find(21)->getAttribute<TestAttribute>()->value, 11);
  BOOST_CHECK_EQUAL(catalog.find(22)->getAttribute<TestAttribute>()->value, 12);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getColumnInfo_test, CatalogConfig_fixture) {
  
  // Given
  config_manager.registerConfiguration<CatalogConfig>();
  config_manager.registerConfiguration<TestAttributeHandlerConfig>();
  config_manager.closeRegistration();
  
  // When
  config_manager.initialize(options_map);
  auto& column_info = *config_manager.getConfiguration<CatalogConfig>().getColumnInfo();
  
  
  //Then
  BOOST_CHECK_EQUAL(column_info.size(), 4);
  BOOST_CHECK_EQUAL(column_info.getDescription(0).name, "Col1");
  BOOST_CHECK_EQUAL(column_info.getDescription(1).name, "ID");
  BOOST_CHECK_EQUAL(column_info.getDescription(2).name, "ID1");
  BOOST_CHECK_EQUAL(column_info.getDescription(3).name, "ID2");
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getTableReader_test, CatalogConfig_fixture) {
  
  // Given
  config_manager.registerConfiguration<CatalogConfig>();
  config_manager.registerConfiguration<TestAttributeHandlerConfig>();
  config_manager.closeRegistration();
  
  // When
  config_manager.initialize(options_map);
  auto reader = config_manager.getConfiguration<CatalogConfig>().getTableReader();
  auto table = reader->read();
  auto& column_info = *table.getColumnInfo();
  
  
  //Then
  BOOST_CHECK_EQUAL(column_info.size(), 4);
  BOOST_CHECK_EQUAL(column_info.getDescription(0).name, "Col1");
  BOOST_CHECK_EQUAL(column_info.getDescription(1).name, "ID");
  BOOST_CHECK_EQUAL(column_info.getDescription(2).name, "ID1");
  BOOST_CHECK_EQUAL(column_info.getDescription(3).name, "ID2");
  
  BOOST_CHECK_EQUAL(boost::get<std::int64_t>(table[0][0]), 10);
  BOOST_CHECK_EQUAL(boost::get<std::int64_t>(table[0][1]), 20);
  BOOST_CHECK_EQUAL(boost::get<std::int64_t>(table[0][2]), 30);
  BOOST_CHECK_EQUAL(boost::get<std::int64_t>(table[0][3]), 40);
  BOOST_CHECK_EQUAL(boost::get<std::int64_t>(table[1][0]), 11);
  BOOST_CHECK_EQUAL(boost::get<std::int64_t>(table[1][1]), 21);
  BOOST_CHECK_EQUAL(boost::get<std::int64_t>(table[1][2]), 31);
  BOOST_CHECK_EQUAL(boost::get<std::int64_t>(table[1][3]), 41);
  BOOST_CHECK_EQUAL(boost::get<std::int64_t>(table[2][0]), 12);
  BOOST_CHECK_EQUAL(boost::get<std::int64_t>(table[2][1]), 22);
  BOOST_CHECK_EQUAL(boost::get<std::int64_t>(table[2][2]), 32);
  BOOST_CHECK_EQUAL(boost::get<std::int64_t>(table[2][3]), 42);
  
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getTableToCatalogConverter_test, CatalogConfig_fixture) {
  
  // Given
  config_manager.registerConfiguration<CatalogConfig>();
  config_manager.registerConfiguration<TestAttributeHandlerConfig>();
  config_manager.closeRegistration();
  
  // When
  config_manager.initialize(options_map);
  auto reader = config_manager.getConfiguration<CatalogConfig>().getTableReader();
  auto table = reader->read();
  auto converter = config_manager.getConfiguration<CatalogConfig>().getTableToCatalogConverter();
  auto catalog = converter(table);
  
  //Then
  BOOST_CHECK_EQUAL(catalog.size(), 3);
  BOOST_CHECK_EQUAL(catalog.find(20)->getAttribute<TestAttribute>()->value, 10);
  BOOST_CHECK_EQUAL(catalog.find(21)->getAttribute<TestAttribute>()->value, 11);
  BOOST_CHECK_EQUAL(catalog.find(22)->getAttribute<TestAttribute>()->value, 12);
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


