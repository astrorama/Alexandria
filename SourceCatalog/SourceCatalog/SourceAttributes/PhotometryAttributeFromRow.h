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
 * @file SourceCatalog/SourceAttributes/PhotometryAttributeFromRow.h
 *
 * @date Apr 17, 2014
 * @author Pierre Dubath
 */

#ifndef PHOTOMETRYATTRIBUTEFROMROW_H_
#define PHOTOMETRYATTRIBUTEFROMROW_H_
#include <map>
#include <memory>
#include <string>
#include <utility>
#include <vector>

#include "ElementsKernel/Export.h"

#include "SourceCatalog/AttributeFromRow.h"
#include "SourceCatalog/Catalog.h"
#include "Table/Table.h"

namespace Euclid {
namespace SourceCatalog {

/**
 * @class PhotometryAttributeFromRow
 * @brief Implementation of the AttributeFromRow for a photometry attribute.
 * This class implements the createAttribute method that must be used to
 * create Photometry objects.
 *
 */
class ELEMENTS_API PhotometryAttributeFromRow : public AttributeFromRow {
public:
  /**
   * @brief Create a PhotometryAttributeFromRow object
   *
   * @details Create a PhotometryAttributeFromRow object, setting up the rule for building
   * PhotometryAttribute from table rows. The filter_name_mapping provides the correspondence
   * between the filterName (string) and the names used for the Table columns. These names (of
   * the flux and the error columns) are searched in the columnInfo of the Table and a new
   * mapping between the filterName and the indices of the flux and of the error columns is built.
   * The user must provide this mapping between the filterName (which are then used throughout the
   * processing) and the column names which comes from the input photometric (ASCII or FITS) catalog.
   *
   * @param column_info_ptr
   *    describes the columns of the Table providing in particular the require column names
   *
   * @param filter_name_mapping
   *    supplies the mapping between the filter name (std::string) and the Table column names,
   *    both for the flux and for the error columns
   *
   * @param has_missing_photometry
   *    If true the attribute accept values indicating that the photometry is missing
   *
   * @param missing_photometry_flag
   *    provides the value of the flag when no data is available
   *
   *
   * @param has_upper_limit
   *    if true the attribute accept values indicating that the flux is an upper limit and not an actual value
   *
   * @exception
   *  An exception is thrown if the names provided in the mapping are not present in the columnInfo.
   */
  PhotometryAttributeFromRow(
      std::shared_ptr<Euclid::Table::ColumnInfo>                                      column_info_ptr,
      const std::vector<std::pair<std::string, std::pair<std::string, std::string>>>& filter_name_mapping,
      const bool missing_photometry_enabled, const double missing_photometry_flag, const bool upper_limit_enabled,
      const std::vector<std::pair<std::string, float>> n_map, const double n_upper_limit_flag,
      const std::vector<std::pair<std::string, bool>> convert_from_mag = {});

  virtual ~PhotometryAttributeFromRow();

  /**
   * @brief Create a photometricAttribute from a Table row
   * @details Create a photometricAttribute from a Table row using the mapping included in this object
   * @param row A Table row
   * @return A unique pointer to a (Photometry) Attribute
   */
  std::unique_ptr<Attribute> createAttribute(const Euclid::Table::Row& row) override;

  std::pair<double, double> convertFromMag(const double mag, const double mag_err) const;

private:
  /*
   * Map the correspondence between the filterName and the indexes used in the Table columns
   */
  std::vector<std::pair<size_t, size_t>> m_table_index_vector;

  /*
   * Pointer to the shared filter name vector
   */
  std::shared_ptr<std::vector<std::string>> m_filter_name_vector_ptr;

  bool m_missing_photometry_enabled;

  /*
   * Flag value for missing photometry data
   */
  double m_missing_photometry_flag;

  bool m_upper_limit_enabled;

  std::vector<std::pair<std::string, float>> m_n_map;

  double m_n_upper_limit_flag;

  std::vector<std::pair<std::string, bool>> m_convert_from_mag;
};

}  // namespace SourceCatalog
}  // end of namespace Euclid

#endif  // PHOTOMETRYATTRIBUTEFROMROW_H_
