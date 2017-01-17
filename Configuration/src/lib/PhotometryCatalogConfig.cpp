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
 * @file src/lib/PhotometryCatalogConfig.cpp
 * @date 11/06/15
 * @author nikoapos
 */
#include "SourceCatalog/SourceAttributes/PhotometryAttributeFromRow.h"
#include "Configuration/CatalogConfig.h"
#include "Configuration/PhotometricBandMappingConfig.h"
#include "Configuration/PhotometryCatalogConfig.h"

namespace po = boost::program_options;
namespace fs = boost::filesystem;

namespace Euclid {
namespace Configuration {

static const std::string MISSING_PHOTOMETRY_FLAG {"missing-photometry-flag"};

PhotometryCatalogConfig::PhotometryCatalogConfig(long manager_id) : Configuration(manager_id) {
  declareDependency<CatalogConfig>();
  declareDependency<PhotometricBandMappingConfig>();
}

auto PhotometryCatalogConfig::getProgramOptions() -> std::map<std::string, OptionDescriptionList> {
  return {{"Input catalog options", {
    {MISSING_PHOTOMETRY_FLAG.c_str(), po::value<double>()->default_value(-99.),
        "It is a flag value for missing flux for a source"}
  }}};
}

void PhotometryCatalogConfig::initialize(const UserValues& args) {
  
  double missing_photo_flag = args.at(MISSING_PHOTOMETRY_FLAG).as<double>();

  auto filter_name_mapping = getDependency<PhotometricBandMappingConfig>().getPhotometricBandMapping();
  auto column_info = getDependency<CatalogConfig>().getColumnInfo();
  
  // Add the row handler to parse the photometries
  std::shared_ptr<SourceCatalog::AttributeFromRow> handler_ptr {
    new SourceCatalog::PhotometryAttributeFromRow {column_info,
                                                   std::move(filter_name_mapping),
                                                   missing_photo_flag}
  };
  getDependency<CatalogConfig>().addAttributeHandler(std::move(handler_ptr));
}

} // Configuration namespace
} // Euclid namespace



