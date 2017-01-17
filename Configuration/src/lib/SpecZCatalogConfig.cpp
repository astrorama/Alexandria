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
 * @file src/lib/SpecZCatalogConfig.cpp
 * @date 11/06/15
 * @author nikoapos
 */

#include "ElementsKernel/Exception.h"
#include "SourceCatalog/SourceAttributes/SpectroscopicRedshiftAttributeFromRow.h"
#include "Configuration/SpecZCatalogConfig.h"
#include "Configuration/CatalogConfig.h"

namespace po = boost::program_options;

namespace Euclid {
namespace Configuration {

static const std::string SPECZ_COLUMN_NAME {"spec-z-column-name"};
static const std::string SPECZ_COLUMN_INDEX {"spec-z-column-index"};
static const std::string SPECZ_ERR_COLUMN_NAME {"spec-z-err-column-name"};
static const std::string SPECZ_ERR_COLUMN_INDEX {"spec-z-err-column-index"};

SpecZCatalogConfig::SpecZCatalogConfig(long manager_id) : Configuration(manager_id) {
  declareDependency<CatalogConfig>();
}

auto SpecZCatalogConfig::getProgramOptions() -> std::map<std::string, OptionDescriptionList> {
  return {{"Input catalog options", {
    {SPECZ_COLUMN_NAME.c_str(), po::value<std::string>(),
        "The name of the column representing the spectroscopic redshift"},
    {SPECZ_COLUMN_INDEX.c_str(), po::value<int>(),
        "The 1-based index of the column representing the spectroscopic redshift"},
    {SPECZ_ERR_COLUMN_NAME.c_str(), po::value<std::string>(),
        "The name of the column representing spectroscopic redshift error"},
    {SPECZ_ERR_COLUMN_INDEX.c_str(), po::value<int>(),
        "The 1-based index of the column representing the spectroscopic redshift error"}
  }}};
}

void SpecZCatalogConfig::preInitialize(const UserValues& args) {
  if (args.find(SPECZ_COLUMN_NAME) != args.end() 
      && args.find(SPECZ_COLUMN_INDEX) != args.end()) {
    throw Elements::Exception() << "Options " << SPECZ_COLUMN_NAME << " and "
         << SPECZ_COLUMN_INDEX << " are mutually exclusive";
  }
  if (args.find(SPECZ_COLUMN_NAME) == args.end()
      && args.find(SPECZ_COLUMN_INDEX) == args.end()) {
     throw Elements::Exception() << "One of the options " << SPECZ_COLUMN_NAME
         << " and " << SPECZ_COLUMN_INDEX << " must be given";
  }
  if (args.find(SPECZ_COLUMN_INDEX) != args.end()
      && args.at(SPECZ_COLUMN_INDEX).as<int>() < 1) {
    throw Elements::Exception() << SPECZ_COLUMN_INDEX << " must be a one-based "
        << "index but was " << args.at(SPECZ_COLUMN_INDEX).as<int>();
  }
  if (args.find(SPECZ_ERR_COLUMN_NAME) != args.end() 
      && args.find(SPECZ_ERR_COLUMN_INDEX) != args.end()) {
    throw Elements::Exception() << "Options " << SPECZ_ERR_COLUMN_NAME << " and "
         << SPECZ_ERR_COLUMN_INDEX << " are mutually exclusive";
  }
  if (args.find(SPECZ_ERR_COLUMN_INDEX) != args.end()
      && args.at(SPECZ_ERR_COLUMN_INDEX).as<int>() < 1) {
    throw Elements::Exception() << SPECZ_ERR_COLUMN_INDEX << " must be a one-based "
        << "index but was " << args.at(SPECZ_ERR_COLUMN_INDEX).as<int>();
  }
}

static std::string getFluxColumnFromOptions(const Configuration::UserValues& args,
                                            const Table::ColumnInfo& column_info) {
  if (args.find(SPECZ_COLUMN_NAME) != args.end()) {
    std::string name  = args.at(SPECZ_COLUMN_NAME).as<std::string>();
    if (column_info.find(name) == nullptr) {
      throw Elements::Exception() << "Input catalog file does not contain the "
          << " SpecZ column with name " << name;
    }
    return name;
  } else {
    std::size_t index = args.at(SPECZ_COLUMN_INDEX).as<int>();
    if (index > column_info.size()) {
      throw Elements::Exception() << SPECZ_COLUMN_INDEX << " (" << index
          << ") is out of range (" << column_info.size() << ")";
    }
    return column_info.getDescription(index-1).name;
  }
}

static std::string getErrColumnFromOptions(const Configuration::UserValues& args,
                                            const Table::ColumnInfo& column_info) {
  if (args.find(SPECZ_ERR_COLUMN_NAME) != args.end()) {
    std::string name  = args.at(SPECZ_ERR_COLUMN_NAME).as<std::string>();
    if (column_info.find(name) == nullptr) {
      throw Elements::Exception() << "Input catalog file does not contain the "
          << " SpecZ error column with name " << name;
    }
    return name;
  } else {
    std::size_t index = args.at(SPECZ_ERR_COLUMN_INDEX).as<int>();
    if (index > column_info.size()) {
      throw Elements::Exception() << SPECZ_ERR_COLUMN_INDEX << " (" << index
          << ") is out of range (" << column_info.size() << ")";
    }
    return column_info.getDescription(index-1).name;
  }
}

void SpecZCatalogConfig::initialize(const UserValues& args) {
  auto column_info = getDependency<CatalogConfig>().getColumnInfo();
  
  std::string flux_column = getFluxColumnFromOptions(args, *column_info);
  
  std::shared_ptr<SourceCatalog::AttributeFromRow> handler_ptr {};
  
  if (args.find(SPECZ_ERR_COLUMN_NAME) == args.end()
      && args.find(SPECZ_ERR_COLUMN_INDEX) == args.end()) {
    handler_ptr.reset(new SourceCatalog::SpectroscopicRedshiftAttributeFromRow {column_info, flux_column});
  } else {
    std::string err_column = getErrColumnFromOptions(args, *column_info);
    handler_ptr.reset(new SourceCatalog::SpectroscopicRedshiftAttributeFromRow {column_info, flux_column, err_column});
  }
  
  getDependency<CatalogConfig>().addAttributeHandler(handler_ptr);
}

} // Configuration namespace
} // Euclid namespace



