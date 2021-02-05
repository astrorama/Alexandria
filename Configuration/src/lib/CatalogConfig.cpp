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
 * @file src/lib/CatalogConfig.icpp
 * @date 11/05/15
 * @author nikoapos
 */

#include "Configuration/CatalogConfig.h"
#include "AlexandriaKernel/memory_tools.h"
#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Logging.h"
#include "SourceCatalog/CatalogFromTable.h"
#include "Table/AsciiReader.h"
#include "Table/FitsReader.h"
#include <CCfits/CCfits>
#include <array>
#include <fstream>

namespace po = boost::program_options;
namespace fs = boost::filesystem;

namespace Euclid {
namespace Configuration {

static Elements::Logging logger = Elements::Logging::getLogger("CatalogConfig");

static const std::string INPUT_CATALOG_FILE{"input-catalog-file"};
static const std::string INPUT_CATALOG_FORMAT{"input-catalog-format"};
static const std::string SOURCE_ID_COLUMN_NAME{"source-id-column-name"};
static const std::string SOURCE_ID_COLUMN_INDEX{"source-id-column-index"};

CatalogConfig::CatalogConfig(long manager_id) : Configuration(manager_id) {}

auto CatalogConfig::getProgramOptions() -> std::map<std::string, OptionDescriptionList> {
  return {{"Input catalog options",
           {{INPUT_CATALOG_FILE.c_str(), po::value<std::string>()->required(), "The file containing the input catalog"},
            {INPUT_CATALOG_FORMAT.c_str(), po::value<std::string>()->default_value("AUTO"),
             "The format of the input catalog (AUTO, FITS or ASCII)"},
            {SOURCE_ID_COLUMN_NAME.c_str(), po::value<std::string>(), "The name of the column representing the source ID"},
            {SOURCE_ID_COLUMN_INDEX.c_str(), po::value<int>(), "The index of the column representing the source ID"}}}};
}

void CatalogConfig::preInitialize(const UserValues& args) {

  if (args.find(SOURCE_ID_COLUMN_NAME) != args.end() && args.find(SOURCE_ID_COLUMN_INDEX) != args.end()) {
    throw Elements::Exception() << "Options " << SOURCE_ID_COLUMN_NAME << " and " << SOURCE_ID_COLUMN_INDEX
                                << " are mutually exclusive";
  }

  if (args.find(SOURCE_ID_COLUMN_INDEX) != args.end() && args.at(SOURCE_ID_COLUMN_INDEX).as<int>() < 1) {
    throw Elements::Exception() << SOURCE_ID_COLUMN_INDEX << " must be a one-based "
                                << "index but was " << args.at(SOURCE_ID_COLUMN_INDEX).as<int>();
  }

  if (args.find(INPUT_CATALOG_FORMAT) != args.end() && args.at(INPUT_CATALOG_FORMAT).as<std::string>() != "AUTO" &&
      args.at(INPUT_CATALOG_FORMAT).as<std::string>() != "FITS" && args.at(INPUT_CATALOG_FORMAT).as<std::string>() != "ASCII") {
    throw Elements::Exception() << INPUT_CATALOG_FORMAT << "must be one of "
                                << "AUTO, FITS or ASCII, but was " << args.at(INPUT_CATALOG_FORMAT).as<std::string>();
  }
}

namespace {

fs::path getCatalogFileFromOptions(const Configuration::UserValues& args, const fs::path& base_dir) {
  fs::path catalog_file{args.at(INPUT_CATALOG_FILE).as<std::string>()};
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

enum class FormatType { FITS, ASCII };

FormatType autoDetectFormatType(fs::path file) {
  logger.info() << "Auto-detecting format of file " << file;
  FormatType result = FormatType::ASCII;
  {
    std::ifstream        in{file.string()};
    std::array<char, 80> first_header_array;
    in.read(first_header_array.data(), 80);
    in.close();
    std::string first_header_str{first_header_array.data()};
    if (first_header_str.compare(0, 9, "SIMPLE  =") == 0) {
      result = FormatType::FITS;
    }
  }
  logger.info() << "Detected " << (result == FormatType::FITS ? "FITS" : "ASCII") << " format";
  return result;
}

FormatType getFormatTypeFromOptions(const Configuration::UserValues& args, const fs::path& file) {
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

std::unique_ptr<Table::TableReader> getTableReaderImpl(bool fits_format, const boost::filesystem::path& filename) {
  if (fits_format) {
    return Euclid::make_unique<Table::FitsReader>(filename.native(), 1);
  } else {
    return Euclid::make_unique<Table::AsciiReader>(filename.native());
  }
}

std::string getIdColumnFromOptions(const Configuration::UserValues& args, const Table::ColumnInfo& column_info) {
  std::string id_column_name = "ID";
  if (args.find(SOURCE_ID_COLUMN_NAME) != args.end()) {
    id_column_name = args.at(SOURCE_ID_COLUMN_NAME).as<std::string>();
    if (column_info.find(id_column_name) == nullptr) {
      throw Elements::Exception() << "Input catalog file does not contain the "
                                  << "ID column with name " << id_column_name;
    }
  }
  if (args.find(SOURCE_ID_COLUMN_INDEX) != args.end()) {
    std::size_t index = args.at(SOURCE_ID_COLUMN_INDEX).as<int>();
    if (index > column_info.size()) {
      throw Elements::Exception() << SOURCE_ID_COLUMN_INDEX << " (" << index << ") is out of range (" << column_info.size() << ")";
    }
    id_column_name = column_info.getDescription(index - 1).name;
  }
  logger.info() << "Using ID column \"" << id_column_name << '"';
  return id_column_name;
}

}  // Anonymous namespace

void CatalogConfig::initialize(const UserValues& args) {
  m_filename       = getCatalogFileFromOptions(args, m_base_dir);
  m_fits_format    = getFormatTypeFromOptions(args, m_filename) == FormatType::FITS;
  m_column_info    = std::make_shared<Table::ColumnInfo>(getTableReaderImpl(m_fits_format, m_filename)->getInfo());
  m_id_column_name = getIdColumnFromOptions(args, *m_column_info);
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

std::unique_ptr<Table::TableReader> CatalogConfig::getTableReader() const {
  if (getCurrentState() < State::FINAL) {
    throw Elements::Exception() << "getTableReader() call to not finalized CatalogConfig";
  }
  return getTableReaderImpl(m_fits_format, m_filename);
}

std::shared_ptr<Table::ColumnInfo> CatalogConfig::getColumnInfo() const {
  if (getCurrentState() < State::INITIALIZED) {
    throw Elements::Exception() << "getColumnInfo() call to uninitialized CatalogConfig";
  }
  return m_column_info;
}

std::string CatalogConfig::getIdColumn() const {
  return m_id_column_name;
}

namespace {

class ConverterImpl {

public:
  ConverterImpl(std::shared_ptr<Table::ColumnInfo> column_info, const std::string& id_column_name,
                std::vector<std::shared_ptr<SourceCatalog::AttributeFromRow>> attribute_handlers)
      : m_converter(column_info, id_column_name, std::move(attribute_handlers)) {}

  SourceCatalog::Catalog operator()(const Table::Table& table) {
    return m_converter.createCatalog(table);
  }

private:
  SourceCatalog::CatalogFromTable m_converter;
};

}  // Anonymous namespace

CatalogConfig::TableToCatalogConverter CatalogConfig::getTableToCatalogConverter() const {
  if (getCurrentState() < State::FINAL) {
    throw Elements::Exception() << "getTableToCatalogConverter() call to not finalized CatalogConfig";
  }
  return ConverterImpl{m_column_info, m_id_column_name, m_attribute_handlers};
}

Table::Table CatalogConfig::readAsTable() const {
  if (getCurrentState() < State::FINAL) {
    throw Elements::Exception() << "getAsTable() call to not finalized CatalogConfig";
  }
  logger.info() << "Reading table from file " << m_filename;
  return getTableReader()->read();
}

SourceCatalog::Catalog CatalogConfig::readAsCatalog() const {
  if (getCurrentState() < State::FINAL) {
    throw Elements::Exception() << "getCatalog() call to not finalized CatalogConfig";
  }
  auto table     = readAsTable();
  auto converter = getTableToCatalogConverter();
  return converter(table);
}

const boost::filesystem::path& CatalogConfig::getFilename() const {
  if (getCurrentState() < State::INITIALIZED) {
    throw Elements::Exception() << "getFilename() call to not finalized CatalogConfig";
  }
  return m_filename;
}

}  // namespace Configuration
}  // namespace Euclid
