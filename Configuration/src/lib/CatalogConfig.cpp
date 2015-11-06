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
 * @file src/lib/CatalogConfig.icpp
 * @date 11/05/15
 * @author nikoapos
 */

#include <fstream>
#include <array>
#include <CCfits/CCfits>
#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Logging.h"
#include "Table/AsciiReader.h"
#include "Table/FitsReader.h"
#include "Configuration/CatalogConfig.h"
#include "SourceCatalog/CatalogFromTable.h"

namespace po = boost::program_options;
namespace fs = boost::filesystem;

namespace Euclid {
namespace Configuration {

static Elements::Logging logger = Elements::Logging::getLogger("CatalogConfig");

static const std::string INPUT_CATALOG_FILE {"input-catalog-file"};
static const std::string INPUT_CATALOG_FORMAT {"input-catalog-format"};
static const std::string SOURCE_ID_COLUMN_NAME {"source-id-column-name"};
static const std::string SOURCE_ID_COLUMN_INDEX {"source-id-column-index"};

CatalogConfig::CatalogConfig(long manager_id) : Configuration(manager_id) { }

auto CatalogConfig::getProgramOptions() -> std::map<std::string, OptionDescriptionList> {
  return {{"Input catalog options", {
    {INPUT_CATALOG_FILE.c_str(), po::value<std::string>()->required(),
        "The file containing the input catalog"},
    {INPUT_CATALOG_FORMAT.c_str(), po::value<std::string>(),
        "The format of the input catalog (FITS or ASCII)"},
    {SOURCE_ID_COLUMN_NAME.c_str(), po::value<std::string>(),
        "The name of the column representing the source ID"},
    {SOURCE_ID_COLUMN_INDEX.c_str(), po::value<int>(),
        "The index of the column representing the source ID"}
  }}};
}

void CatalogConfig::preInitialize(const UserValues& args) {
  
  if (args.find(SOURCE_ID_COLUMN_NAME) != args.end()
      && args.find(SOURCE_ID_COLUMN_INDEX) != args.end()) {
    throw Elements::Exception() << "Options " << SOURCE_ID_COLUMN_NAME 
        << " and " << SOURCE_ID_COLUMN_INDEX << " are mutually exclusive";
  }
  
  if (args.find(SOURCE_ID_COLUMN_INDEX) != args.end()
      && args.at(SOURCE_ID_COLUMN_INDEX).as<int>() < 1) {
    throw Elements::Exception() << SOURCE_ID_COLUMN_INDEX<< " must be a one-based "
        << "index but was " << args.at(SOURCE_ID_COLUMN_INDEX).as<int>();
  }
  
  if (args.find(INPUT_CATALOG_FORMAT) != args.end()
      && args.at(INPUT_CATALOG_FORMAT).as<std::string>() != "FITS"
      && args.at(INPUT_CATALOG_FORMAT).as<std::string>() != "ASCII") {
    throw Elements::Exception() << INPUT_CATALOG_FORMAT << "must be one of "
        << "FITS or ASCII, but was " << args.at(INPUT_CATALOG_FORMAT).as<std::string>();
  }
}

static fs::path getCatalogFileFromOptions(const Configuration::UserValues& args,
                                          const fs::path& base_dir) {
  fs::path catalog_file {args.at(INPUT_CATALOG_FILE).as<std::string>()};
  if (catalog_file.is_relative()) {
    catalog_file = base_dir / catalog_file;
  }
  if (!fs::exists(catalog_file)) {
    throw Elements::Exception() << "Input catalog file " << catalog_file << " does not exist";
  }
  if (fs::is_directory(catalog_file)) {
    throw Elements::Exception() << "Input catalog file " << catalog_file << " is not a file";
  }
  return catalog_file;
}

enum class FormatType {
  FITS, ASCII
};

static FormatType autoDetectFormatType(fs::path file) {
  logger.info() << "Auto-detecting format of file " << file;
  FormatType result = FormatType::ASCII;
  {
    std::ifstream in {file.string()};
    std::array<char, 80> first_header_array;
    in.read(first_header_array.data(), 80);
    in.close();
    std::string first_header_str {first_header_array.data()};
    if (first_header_str.compare(0, 9, "SIMPLE  =") == 0) {
      result = FormatType::FITS;
    }
  }
  logger.info() << "Detected " << (result == FormatType::FITS ? "FITS" : "ASCII") << " format";
  return result;
}

static FormatType getFormatTypeFromOptions(const Configuration::UserValues& args,
                                           const fs::path& file) {
  FormatType format;
  if (args.find(INPUT_CATALOG_FORMAT) == args.end()) {
    format = autoDetectFormatType(file);
  } else if (args.at(INPUT_CATALOG_FORMAT).as<std::string>().compare("FITS") == 0) {
    format = FormatType::FITS;
  } else {
    format = FormatType::ASCII;
  }
  return format;
}

static Table::Table readFitsTable(fs::path file) {
  CCfits::FITS fits {file.string()};
  return Table::FitsReader().read(fits.extension(1));
}

static Table::Table readAsciiTable(fs::path file) {
  std::ifstream in {file.string()};
  return Table::AsciiReader().read(in);
}

void CatalogConfig::initialize(const UserValues& args) {
  auto catalog_file = getCatalogFileFromOptions(args, m_base_dir);
  auto format = getFormatTypeFromOptions(args, catalog_file);
  logger.info() << "Reading table from file " << catalog_file;
  Table::Table table = (format == FormatType::FITS)
                       ? readFitsTable(catalog_file)
                       : readAsciiTable(catalog_file);
  m_table_ptr.reset(new Table::Table{std::move(table)});
}

static std::string getIdColumnFromOptions(const Configuration::UserValues& args,
                                          const Table::Table& table) {
  std::string id_column_name = "ID";
  if (args.find(SOURCE_ID_COLUMN_NAME) != args.end()) {
    id_column_name = args.at(SOURCE_ID_COLUMN_NAME).as<std::string>();
  }
  if (args.find(SOURCE_ID_COLUMN_INDEX) != args.end()) {
    int index = args.at(SOURCE_ID_COLUMN_INDEX).as<int>();
    id_column_name = table.getColumnInfo()->getName(index-1);
  }
  logger.info() << "Using ID column \"" << id_column_name << '"';
  return id_column_name;
}

void CatalogConfig::postInitialize(const UserValues& args) {
  auto& table = getAsTable();
  auto id_column_name = getIdColumnFromOptions(args, table);
  logger.info() << "Converting the table to a catalog";
  SourceCatalog::CatalogFromTable converter {table.getColumnInfo(), id_column_name,
                                             m_attribute_handlers};
  m_catalog_ptr.reset(new SourceCatalog::Catalog{converter.createCatalog(table)});
}

void CatalogConfig::setBaseDir(const fs::path& base_dir) {
  m_base_dir = base_dir;
}

void CatalogConfig::addAttributeHandler(std::shared_ptr<SourceCatalog::AttributeFromRow> handler) {
  m_attribute_handlers.push_back(handler);
}

const Table::Table& CatalogConfig::getAsTable() const {
  if (m_table_ptr == nullptr) {
    throw Elements::Exception() << "getAsTable() call to uninitialized CatalogConfig";
  }
  return *m_table_ptr;
}

const SourceCatalog::Catalog& CatalogConfig::getCatalog() const {
  if (m_catalog_ptr == nullptr) {
    throw Elements::Exception() << "getCatalog() call to uninitialized CatalogConfig";
  }
  return *m_catalog_ptr;
}

} // Configuration namespace
} // Euclid namespace



