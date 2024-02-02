/*
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
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

#include <algorithm>
#include <boost/algorithm/string.hpp>
#include <fstream>
#include <sstream>
#include <tuple>

#include "Configuration/PhotometricBandMappingConfig.h"
#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Logging.h"

namespace po = boost::program_options;
namespace fs = boost::filesystem;

namespace Euclid {
namespace Configuration {

static Elements::Logging logger = Elements::Logging::getLogger("PhotometricBandMappingConfig");

static const std::string FILTER_MAPPING_FILE{"filter-mapping-file"};
static const std::string EXCLUDE_FILTER{"exclude-filter"};

PhotometricBandMappingConfig::PhotometricBandMappingConfig(long manager_id) : Configuration(manager_id) {}

auto PhotometricBandMappingConfig::getProgramOptions() -> std::map<std::string, OptionDescriptionList> {
  return {
      {"Input catalog options",
       {{FILTER_MAPPING_FILE.c_str(), po::value<std::string>()->default_value("filter_mapping.txt"),
         "The file containing the photometry mapping of the catalog columns"},
        {EXCLUDE_FILTER.c_str(), po::value<std::vector<std::string>>()->default_value(std::vector<std::string>{}, ""),
         "A list of filters to ignore"}}}};
}

static fs::path getMappingFileFromOptions(const Configuration::UserValues& args, const fs::path& base_dir) {
  fs::path mapping_file{args.at(FILTER_MAPPING_FILE).as<std::string>()};
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

static std::tuple<PhotometricBandMappingConfig::MappingMap, PhotometricBandMappingConfig::UpperLimitThresholdMap,
                  PhotometricBandMappingConfig::ConvertFromMagMap>
parseFile(fs::path filename) {
  PhotometricBandMappingConfig::MappingMap             filter_name_mapping{};
  PhotometricBandMappingConfig::UpperLimitThresholdMap threshold_mapping{};
  PhotometricBandMappingConfig::ConvertFromMagMap      convert_from_mag_mapping{};
  std::ifstream                                        in{filename.string()};
  std::string                                          line;

  bool header_found             = false;
  int  filtr_column_index       = 0;
  int  flux_column_index        = 1;
  int  error_column_index       = 2;
  int  upper_limit_column_index = 3;
  int  convertion_column_index  = 4;

  std::vector<std::string> expected_column_name{"Filter", "Flux Column", "Error Column", "Upper Limit/error ratio",
                                                "Convert from MAG"};

  while (std::getline(in, line)) {
    boost::trim(line);
    if (line[0] == '#') {
      if (!header_found) {
        std::string trimmed_line = line.substr(1);
        boost::trim(trimmed_line);
        std::vector<int>         proposed_column_index{-1, -1, -1, -1, -1};
        std::vector<std::string> strs;
        boost::split(strs, trimmed_line, boost::is_any_of(","));

        for (size_t index = 0; index < expected_column_name.size(); ++index) {
          for (size_t index_string = 0; index_string < strs.size(); ++index_string) {
            std::string item = strs[index_string];
            boost::trim(item);
            if (item == expected_column_name[index]) {
              proposed_column_index[index] = index_string;
            }
          }
        }

        if (proposed_column_index[0] >= 0 && proposed_column_index[1] >= 0 && proposed_column_index[2] >= 0) {
          header_found             = true;
          filtr_column_index       = proposed_column_index[0];
          flux_column_index        = proposed_column_index[1];
          error_column_index       = proposed_column_index[2];
          upper_limit_column_index = proposed_column_index[3];
          convertion_column_index  = proposed_column_index[4];
        }
      }
      continue;
    }

    std::vector<std::string> cells;
    boost::split(cells, line, boost::is_any_of(" "));

    try {
      if (int(cells.size()) <= filtr_column_index || int(cells.size()) <= flux_column_index ||
          int(cells.size()) <= error_column_index) {
        throw Elements::Exception() << "File with missing values for the mandatory fields";
      }
      std::string filter_value = cells[filtr_column_index];
      boost::trim(filter_value);
      std::string flux_value = cells[flux_column_index];
      boost::trim(flux_value);
      std::string error_value = cells[error_column_index];
      boost::trim(error_value);

      filter_name_mapping.emplace_back(filter_value, std::make_pair(flux_value, error_value));

      if (upper_limit_column_index > 0 && int(cells.size()) > upper_limit_column_index &&
          cells[upper_limit_column_index] != "") {
        float n = std::stof(cells[upper_limit_column_index]);
        threshold_mapping.emplace_back(filter_value, n);
      } else {
        threshold_mapping.emplace_back(filter_value, 3.0);
      }

      if (convertion_column_index > 0 && int(cells.size()) > convertion_column_index &&
          cells[convertion_column_index] != "") {
        bool f = std::stoi(cells[convertion_column_index]);
        convert_from_mag_mapping.emplace_back(filter_value, f);
      } else {
        convert_from_mag_mapping.emplace_back(filter_value, false);
      }
    } catch (const std::exception& e) {
      logger.error() << "Syntax error in " << filename << ": " << line << " => " << e.what();
      ;
      throw Elements::Exception() << "Syntax error in " << filename << ": " << line << " => " << e.what();
    }
  }
  return std::make_tuple(filter_name_mapping, threshold_mapping, convert_from_mag_mapping);
}

void PhotometricBandMappingConfig::initialize(const UserValues& args) {

  // Parse the file with the mapping
  m_mapping_file               = getMappingFileFromOptions(args, m_base_dir);
  auto parsed                  = parseFile(m_mapping_file);
  auto all_filter_name_mapping = std::get<0>(parsed);
  auto all_threshold_mapping   = std::get<1>(parsed);
  auto all_convert_mapping     = std::get<2>(parsed);

  // Remove the filters which are marked to exclude
  auto                  exclude_vector = args.at(EXCLUDE_FILTER).as<std::vector<std::string>>();
  std::set<std::string> exclude_filters{exclude_vector.begin(), exclude_vector.end()};

  for (auto& pair : all_threshold_mapping) {
    if (exclude_filters.count(pair.first) == 0) {
      m_threshold_map.push_back(pair);
    }
  }

  for (auto& pair : all_convert_mapping) {
    if (exclude_filters.count(pair.first) == 0) {
      m_convert_from_mag_map.push_back(pair);
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
    std::stringstream wrong_filters{};
    for (auto& f : exclude_filters) {
      wrong_filters << f << " ";
    }
    throw Elements::Exception() << "Wrong " << EXCLUDE_FILTER << " option value(s) : " << wrong_filters.str();
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

const PhotometricBandMappingConfig::UpperLimitThresholdMap&
PhotometricBandMappingConfig::getUpperLimitThresholdMapping() {
  if (getCurrentState() < State::INITIALIZED) {
    throw Elements::Exception() << "getUpperLimitThresholdMapping() call to uninitialized "
                                << "PhotometricBandMappingConfig";
  }
  return m_threshold_map;
}

const PhotometricBandMappingConfig::ConvertFromMagMap& PhotometricBandMappingConfig::getConvertFromMagMapping() {
  if (getCurrentState() < State::INITIALIZED) {
    throw Elements::Exception() << "getConvertFromMagMapping() call to uninitialized "
                                << "PhotometricBandMappingConfig";
  }
  return m_convert_from_mag_map;
}

const fs::path PhotometricBandMappingConfig::getMappingFile() {
  if (getCurrentState() < State::INITIALIZED) {
    throw Elements::Exception() << "getMappingFile() call to uninitialized "
                                << "PhotometricBandMappingConfig";
  }
  return m_mapping_file;
}

}  // namespace Configuration
}  // namespace Euclid
