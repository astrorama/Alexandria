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
 * @file Table/ColumnDescription.h
 * @date 09/06/16
 * @author nikoapos
 */

#ifndef _TABLE_COLUMNDESCRIPTION_H
#define _TABLE_COLUMNDESCRIPTION_H

#include <functional>
#include <iomanip>
#include <ostream>
#include <string>
#include <typeindex>

namespace Euclid {
namespace Table {

/**
 * @class ColumnDescription
 *
 * @brief Contains the description of a specific column of a Table
 *
 * @details
 * Each table column is described by the following:
 * - name : The name of the column
 * - type : The type of its data
 * - unit : The unit in which the data are expressed
 * - description : A string describing the column
 *
 * The access to the above is done by directly accessing the public members of
 * the ColumnDescription class.
 *
 * The ColumnDescription implements the comparison operators by checking only
 * the name, type and unit and by ignoring the description text.
 */
class ColumnDescription {

public:
  /// Constructs a new ColumnDescription instance
  /// @throws Elements::Exception
  ///     if the name is the empty string or if it contains whitespaces
  // cppcheck-suppress  noExplicitConstructor
  ColumnDescription(std::string name, std::type_index type = typeid(std::string), std::string unit = "",
                    std::string description = "");

  // cppcheck-suppress  noExplicitConstructor
  ColumnDescription(std::string name, std::type_index type, std::size_t size, std::string unit = "",
                    std::string description = "");

  ColumnDescription(const ColumnDescription&) = default;
  ColumnDescription(ColumnDescription&&)      = default;
  ColumnDescription& operator=(const ColumnDescription&) = default;
  ColumnDescription& operator=(ColumnDescription&&) = default;

  /// Returns true if the two ColumnDescriptions do not describe the same column
  bool operator!=(const ColumnDescription& other) const {
    return !(*this == other);  // Reuse equals operator
  }

  /// Returns true if the two ColumnDescriptions describe the same column
  /// (ignoring the description text)
  bool operator==(const ColumnDescription& other) const {
    return name == other.name && type == other.type && unit == other.unit;
  }

  std::string     name;
  std::type_index type;
  std::string     unit;
  std::string     description;
  std::size_t     size;

}; /* End of ColumnDescription class */

} /* namespace Table */
} /* namespace Euclid */

#endif
