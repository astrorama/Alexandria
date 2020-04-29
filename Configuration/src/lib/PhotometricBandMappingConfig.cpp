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
 * @file src/lib/PhotometricBandMappingConfig.cpp
 * @date 11/11/15
 * @author nikoapos
 */

#include <fstream>
#include <algorithm>
#include <sstream>
#include <boost/regex.hpp>
using boost::regex;
using boost::regex_match;
using boost::smatch;
#include <boost/algorithm/string.hpp>

#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Logging.h"
#include "Configuration/PhotometricBandMappingConfig.h"

namespace po = boost::program_options;
namespace fs = boost::filesystem;

namespace Euclid {
namespace Configuration {

static Elements::Logging logger = Elements::Logging::getLogger("PhotometricBandMappingConfig");

static const std::string FILTER_MAPPING_FILE {"filter-mapping-file"};
static const std::string EXCLUDE_FILTER {"exclude-filter"};

PhotometricBandMappingConfig::PhotometricBandMappingConfig(long manager_id) 
        : Configuration(manager_id) { }

auto PhotometricBandMappingConfig::getProgramOptions() -> std::map<std::string, OptionDescriptionList> {
  return {{"Input catalog options", {
    {FILTER_MAPPING_FILE.c_str(), po::value<std::string>()->default_value("filter_mapping.txt"),
        "The file containing the photometry mapping of the catalog columns"},
    {EXCLUDE_FILTER.c_str(), po::value<std::vector<std::string>>()->default_value(std::vector<std::string>{}, ""),
        "A list of filters to ignore"}
  }}};
}

static fs::path getMappingFileFromOptions(const Configuration::UserValues& args,
                                          const fs::path& base_dir) {
  fs::path mapping_file {args.at(FILTER_MAPPING_FILE).as<std::string>()};
  if (mapping_file.is_relative()) {
    mapping_file = base_dir / mapping_file;
  }
  if (!fs::exists(mapping_file)) {
    throw Elements::Exception() << "Photometry mapping file " << mapping_file << " does not exist";
  }
  if (fs::is_directory(mapping_file)) {
    throw Elements::Exception() << "Photometry mapping file " << mapping_file << " is not a file";
  }
  return mapping_file;
}

static std::pair<PhotometricBandMappingConfig::MappingMap, PhotometricBandMappingConfig::UpperLimitThresholdMap> parseFile(fs::path filename) {
  PhotometricBandMappingConfig::MappingMap filter_name_mapping {};
  PhotometricBandMappingConfig::UpperLimitThresholdMap threshold_mapping{};
  std::ifstream in {filename.string()};
  std::string line;
  regex expr {"\\s*([^\\s#]+)\\s+([^\\s#]+)\\s+([^\\s#]+)(\\s+[^\\s#]+\\s*$)?"};
  while (std::getline(in, line)) {
    boost::trim(line);
    if (line[0] == '#') {
      continue;
    }
    smatch match_res;
    if (!regex_match(line, match_res, expr)) {
      logger.error() << "Syntax error in " << filename << ": " << line;
      throw Elements::Exception() << "Syntax error in " << filename << ": " << line;
    }
    filter_name_mapping.emplace_back(match_res.str(1), std::make_pair(match_res.str(2), match_res.str(3)));

    try{
      float n=std::stof(match_res.str(4));
      threshold_mapping.emplace_back(match_res.str(1), n);
    } catch (std::invalid_argument&){
      threshold_mapping.emplace_back(match_res.str(1), 1.0);
    }
  }
  return std::make_pair(filter_name_mapping,threshold_mapping);
}

void PhotometricBandMappingConfig::initialize(const UserValues& args) {
  
  // Parse the file with the mapping
  auto filename = getMappingFileFromOptions(args, m_base_dir);
  auto parsed = parseFile(filename);
  auto all_filter_name_mapping = parsed.first;
  auto all_threshold_mapping = parsed.second;
  
  // Remove the filters which are marked to exclude
  auto exclude_vector = args.at(EXCLUDE_FILTER).as<std::vector<std::string>>();
  std::set<std::string> exclude_filters {exclude_vector.begin(), exclude_vector.end()};

  for (auto& pair : all_threshold_mapping) {
    if (exclude_filters.count(pair.first) <= 0) {
      m_threshold_map.push_back(pair);
    }
  }

  for (auto& pair : all_filter_name_mapping) {
    if (exclude_filters.count(pair.first) > 0) {
      exclude_filters.erase(pair.first);
    } else {
      m_mapping_map.push_back(pair);
    }
  }


  if (!exclude_filters.empty()) {
    std::stringstream wrong_filters {};
    for (auto& f : exclude_filters) {
      wrong_filters << f << " ";
    }
    throw Elements::Exception() << "Wrong " << EXCLUDE_FILTER << " option value(s) : "
                                << wrong_filters.str();
  }
  
}

void PhotometricBandMappingConfig::setBaseDir(const boost::filesystem::path& base_dir) {
  if (getCurrentState() >= State::INITIALIZED) {
    throw Elements::Exception() << "setBaseDir() call to initialized PhotometricBandMappingConfig";
  }
  m_base_dir = base_dir;
}

const PhotometricBandMappingConfig::MappingMap& PhotometricBandMappingConfig::getPhotometricBandMapping() {
  if (getCurrentState() < State::INITIALIZED) {
    throw Elements::Exception() << "getPhotometricBandMapping() call to uninitialized "
                                << "PhotometricBandMappingConfig";
  }
  return m_mapping_map;
}


const PhotometricBandMappingConfig::UpperLimitThresholdMap& PhotometricBandMappingConfig::getUpperLimitThresholdMapping() {
  if (getCurrentState() < State::INITIALIZED) {
     throw Elements::Exception() << "getUpperLimitThresholdMapping() call to uninitialized "
                                 << "PhotometricBandMappingConfig";
   }
   return m_threshold_map;
}

} // Configuration namespace
} // Euclid namespace



