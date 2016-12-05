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
#include "Table/FitsReaderOld.h"
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
    {INPUT_CATALOG_FORMAT.c_str(), po::value<std::string>()->default_value("AUTO"),
        "The format of the input catalog (AUTO, FITS or ASCII)"},
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
      && args.at(INPUT_CATALOG_FORMAT).as<std::string>() != "AUTO"
      && args.at(INPUT_CATALOG_FORMAT).as<std::string>() != "FITS"
      && args.at(INPUT_CATALOG_FORMAT).as<std::string>() != "ASCII") {
    throw Elements::Exception() << INPUT_CATALOG_FORMAT << "must be one of "
        << "AUTO, FITS or ASCII, but was " << args.at(INPUT_CATALOG_FORMAT).as<std::string>();
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
  AUTO, FITS, ASCII
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
  if (args.at(INPUT_CATALOG_FORMAT).as<std::string>().compare("AUTO") == 0) {
    format = autoDetectFormatType(file);
  } else if (args.at(INPUT_CATALOG_FORMAT).as<std::string>().compare("FITS") == 0) {
    format = FormatType::FITS;
  } else {
    format = FormatType::ASCII;
  }
  return format;
}

static Table::Table readFitsTable(fs::path file) {
  try {
    CCfits::FITS fits {file.string()};
    return Table::FitsReaderOld().read(fits.extension(1));
  } catch (CCfits::FitsException ex) {
    throw Elements::Exception() << "Error while reading file " << file
                                << ": " << ex.message();
  }
}

static Table::Table readAsciiTable(fs::path file) {
  std::ifstream in {file.string()};
  return Table::AsciiReader(in).read();
}

void CatalogConfig::initialize(const UserValues& args) {
  m_filename = getCatalogFileFromOptions(args, m_base_dir);
  auto format = getFormatTypeFromOptions(args, m_filename);
  logger.info() << "Reading table from file " << m_filename;
  Table::Table table = (format == FormatType::FITS)
                       ? readFitsTable(m_filename)
                       : readAsciiTable(m_filename);
  m_table_ptr.reset(new Table::Table{std::move(table)});
}

static std::string getIdColumnFromOptions(const Configuration::UserValues& args,
                                          const Table::Table& table) {
  std::string id_column_name = "ID";
  if (args.find(SOURCE_ID_COLUMN_NAME) != args.end()) {
    id_column_name = args.at(SOURCE_ID_COLUMN_NAME).as<std::string>();
    if (table.getColumnInfo()->find(id_column_name) == nullptr) {
      throw Elements::Exception() << "Input catalog file does not contain the "
          << "ID column with name " << id_column_name;
    }
  }
  if (args.find(SOURCE_ID_COLUMN_INDEX) != args.end()) {
    std::size_t index = args.at(SOURCE_ID_COLUMN_INDEX).as<int>();
    if (index > table.getColumnInfo()->size()) {
      throw Elements::Exception() << SOURCE_ID_COLUMN_INDEX << " (" << index
          << ") is out of range (" << table.getColumnInfo()->size() << ")";
    }
    id_column_name = table.getColumnInfo()->getDescription(index-1).name;
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
  if (getCurrentState() >= State::INITIALIZED) {
    throw Elements::Exception() << "setBaseDir() call to initialized CatalogConfig";
  }
  m_base_dir = base_dir;
}

void CatalogConfig::addAttributeHandler(std::shared_ptr<SourceCatalog::AttributeFromRow> handler) {
  if (getCurrentState() >= State::FINAL) {
    throw Elements::Exception() << "addAttributeHandler() call to finalized CatalogConfig";
  }
  m_attribute_handlers.push_back(handler);
}

const Table::Table& CatalogConfig::getAsTable() const {
  if (getCurrentState() < State::INITIALIZED) {
    throw Elements::Exception() << "getAsTable() call to uninitialized CatalogConfig";
  }
  return *m_table_ptr;
}

const SourceCatalog::Catalog& CatalogConfig::getCatalog() const {
  if (getCurrentState() < State::FINAL) {
    throw Elements::Exception() << "getCatalog() call to not finalized CatalogConfig";
  }
  return *m_catalog_ptr;
}

const boost::filesystem::path& CatalogConfig::getFilename() const {
  if (getCurrentState() < State::INITIALIZED) {
    throw Elements::Exception() << "getFilename() call to not finalized CatalogConfig";
  }
  return m_filename;
}

} // Configuration namespace
} // Euclid namespace



