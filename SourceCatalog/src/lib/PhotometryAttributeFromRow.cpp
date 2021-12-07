/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
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
 * @file src/lib/PhotometryAttributeFromRow.cpp
 *
 * @date Apr 17, 2014
 * @author dubath
 */

#include "SourceCatalog/SourceAttributes/PhotometryAttributeFromRow.h"
#include "ElementsKernel/Real.h"
#include <cmath>
#include <typeindex>

#include "../../SourceCatalog/PhotometryParsingException.h"
#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Real.h"
#include "Table/CastVisitor.h"

namespace Euclid {
namespace SourceCatalog {

PhotometryAttributeFromRow::PhotometryAttributeFromRow(
    std::shared_ptr<Euclid::Table::ColumnInfo>                                      column_info_ptr,
    const std::vector<std::pair<std::string, std::pair<std::string, std::string>>>& filter_name_mapping,
    const bool missing_photometry_enabled, const double missing_photometry_flag, const bool upper_limit_enabled,
    const std::vector<std::pair<std::string, float>>& n_map, const double n_upper_limit_flag,
    const std::vector<std::pair<std::string, bool>>& convert_from_mag)
    : m_missing_photometry_enabled(missing_photometry_enabled)
    , m_missing_photometry_flag(missing_photometry_flag)
    , m_upper_limit_enabled(upper_limit_enabled)
    , m_n_map(n_map)
    , m_n_upper_limit_flag(n_upper_limit_flag)
    , m_convert_from_mag(convert_from_mag) {

  std::unique_ptr<size_t> flux_column_index_ptr;
  std::unique_ptr<size_t> error_column_index_ptr;

  for (auto filter_name_pair : filter_name_mapping) {
    flux_column_index_ptr  = column_info_ptr->find(filter_name_pair.second.first);
    error_column_index_ptr = column_info_ptr->find(filter_name_pair.second.second);

    if (flux_column_index_ptr == nullptr) {
      throw Elements::Exception() << "Column info does not have the flux column " << filter_name_pair.second.first;
    }
    if (error_column_index_ptr == nullptr) {
      throw Elements::Exception() << "Column info does not have the flux error column "
                                  << filter_name_pair.second.second;
    }
    m_table_index_vector.push_back(std::make_pair(*(flux_column_index_ptr), *(error_column_index_ptr)));
  }

  // create and filled the shared pointer to the filter name vector
  m_filter_name_vector_ptr = std::make_shared<std::vector<std::string>>();
  for (auto a_filter_name_map : filter_name_mapping) {
    m_filter_name_vector_ptr->push_back(a_filter_name_map.first);
  }

  // default the m_convert_from_mag
  if (m_convert_from_mag.size() != m_n_map.size()) {
    m_convert_from_mag = std::vector<std::pair<std::string, bool>>();
    for (auto m_n_pair : m_n_map) {
      m_convert_from_mag.push_back(std::make_pair(m_n_pair.first, false));
    }
  }
}

PhotometryAttributeFromRow::~PhotometryAttributeFromRow() {}

std::pair<double, double> PhotometryAttributeFromRow::convertFromMag(const double mag, const double mag_err) const {

  if (Elements::isEqual(mag, m_missing_photometry_flag) || std::isnan(mag)) {
    return std::make_pair(m_missing_photometry_flag, 0);
  } else {
    // check if the error is a flag
    bool is_flag = Elements::isEqual(mag_err, m_n_upper_limit_flag);

    // compute the flux and the error
    double flux = 3.631e9 * std::pow(10, -0.4 * mag);
    // with this formula the sign of mag_err is forwarded to the flux_err
    double flux_err = is_flag ? m_n_upper_limit_flag : 0.4 * flux * mag_err * std::log(10);

    return std::make_pair(flux, flux_err);
  }
}

static std::string getContextDescription(bool missing_photometry_enabled, bool upper_limit_enabled) {
  std::string setup_desc("with ");
  if (missing_photometry_enabled && upper_limit_enabled) {
    setup_desc += "'missing data' and 'upper limit' enabled";
  } else if (missing_photometry_enabled) {
    setup_desc += "'missing data' and 'upper limit' disabled";
  } else if (upper_limit_enabled) {
    setup_desc += "'missing data' disabled and 'upper limit' enabled";
  } else {
    setup_desc += "'missing data' and 'upper limit' disabled";
  }
  return setup_desc;
}

std::unique_ptr<Attribute> PhotometryAttributeFromRow::createAttribute(const Euclid::Table::Row& row) {
  std::vector<FluxErrorPair> photometry_vector{};

  auto context_desc = getContextDescription(m_missing_photometry_enabled, m_upper_limit_enabled);

  auto n_threshod_iter       = m_n_map.begin();
  auto convert_from_mag_iter = m_convert_from_mag.begin();
  for (auto& filter_index_pair : m_table_index_vector) {
    Euclid::Table::Row::cell_type flux_cell  = row[filter_index_pair.first];
    Euclid::Table::Row::cell_type error_cell = row[filter_index_pair.second];

    double flux  = boost::apply_visitor(Table::CastVisitor<double>{}, flux_cell);
    double error = boost::apply_visitor(Table::CastVisitor<double>{}, error_cell);

    if (convert_from_mag_iter->second) {
      auto converted = convertFromMag(flux, error);
      flux           = converted.first;
      error          = converted.second;
    }

    bool upper_limit = false;
    if (std::isinf(flux)) {
      throw SourceCatalog::PhotometryParsingException("Infinite flux encountered when parsing the Photometry",
                                                      context_desc.c_str(), flux, error);
    }

    bool missing_data = std::isnan(flux) | std::isnan(error) |
                        (m_missing_photometry_enabled && Elements::isEqual(flux, m_missing_photometry_flag));

    if (m_missing_photometry_enabled && missing_data) {
      error = 0.;
    } else if (!m_missing_photometry_enabled && missing_data) {
      throw SourceCatalog::PhotometryParsingException("NAN flux encountered when parsing the Photometry ",
                                                      context_desc.c_str(), flux, error);
    } else if (m_upper_limit_enabled) {
      /** Upper limit enabled **/
      if (error == 0.) {
        throw SourceCatalog::PhotometryParsingException("Zero error encountered when parsing the Photometry",
                                                        context_desc.c_str(), flux, error);
      }
      if (error < 0) {
        /** Actual upper limit **/
        if (Elements::isEqual(error, m_n_upper_limit_flag)) {
          error = flux / n_threshod_iter->second;
        }
        upper_limit = true;
        if (flux <= 0) {
          throw SourceCatalog::PhotometryParsingException(
              "Negative or Zero flux encountered when parsing the Photometry", context_desc.c_str(), flux, error);
        }

        error = std::abs(error);
      }
    } else {
      /** Upper limit disabled **/
      if (error <= 0) {
        throw SourceCatalog::PhotometryParsingException(
            "Negative or Zero error encountered when parsing the Photometry", context_desc.c_str(), flux, error);
      }
    }

    photometry_vector.push_back(FluxErrorPair{flux, error, missing_data, upper_limit});
    ++n_threshod_iter;
    ++convert_from_mag_iter;
  }  // Eof for

  std::unique_ptr<Attribute> photometry_ptr{new Photometry{m_filter_name_vector_ptr, photometry_vector}};

  return photometry_ptr;
}

}  // namespace SourceCatalog
}  // end of namespace Euclid
