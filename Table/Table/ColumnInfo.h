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
 * @file Table/ColumnInfo.h
 * @date April 7, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef TABLE_COLUMNINFO_H
#define	TABLE_COLUMNINFO_H

#include <string>
#include <vector>
#include <memory>
#include <typeindex>
#include <utility>

#include "ElementsKernel/Export.h"

#include "Table/ColumnDescription.h"

namespace Euclid {
namespace Table {

/**
 * @class ColumnInfo
 *
 * @brief Provides information about the columns of a Table
 *
 * @details
 * The ColumnInfo is an immutable class which provides information about the
 * columns of a Table. This class can be used for retrieving the
 * ColumnDescription of a column using its index (zero based) and for searching
 * a column with a specific name. The names of the columns must by unique.
 */
class ELEMENTS_API ColumnInfo {

public:

  using info_type = ColumnDescription;

  /**
   * @brief
   * Constructs a ColumnInfo representing the given column names and types
   * @details
   * The order of the columns is assumed to be the same with their order in the
   * passed vector. Because the ColumnInfo is immutable the info_list cannot
   * be empty.
   *
   * Note that the info_list is passed by value to allow the caller to optimize
   * for performance, meaning that the constructor will take advantage of move
   * semantics if the passed object is an rvalue.
   *
   * @param info_list A vector containing the descriptions of the columns
   * @throws Elements::Exception
   *    if the info_list is empty
   * @throws Elements::Exception
   *    if the info_list contains duplicate name entries
   */
  explicit ColumnInfo(std::vector<info_type> info_list);

  /// Default destructor
  virtual ~ColumnInfo() = default;

  /**
   * @brief
   * Returns true if this ColumnInfo represents the same columns with the given one
   *
   * @param other the ColumnInfo to compare with
   * @return true if the two ColumnInfos represent the same columns, false otherwise
   */
  bool operator==(const ColumnInfo& other) const;

  /**
   * @brief
   * Returns false if this ColumnInfo represents the same columns with the given one
   *
   * @param other the ColumnInfo to compare with
   * @return false if the two ColumnInfos represent the same columns, true otherwise
   */
  bool operator!=(const ColumnInfo& other) const;

  /**
   * @brief
   * Returns the number of columns represented by this ColumnInfo
   *
   * @return the number of columns
   */
  std::size_t size() const;

  /**
   * @brief
   * Returns the description of the column with the given index or throws an
   * exception if the index is bigger than the size of the ColumnInfo
   *
   * @param index The index to search for
   * @return The description of the column
   * @throws Elements::Exception
   *    if the index is out of bounds
   */
  const ColumnDescription& getDescription(std::size_t index) const;

  /**
   * @brief
   * Returns the description of the column with the given name or throws an
   * exception if column does not exist
   *
   * @param name The name to search for
   * @return The description of the column
   * @throws Elements::Exception
   *    if the index is out of bounds
   */
  const ColumnDescription& getDescription(const std::string& name) const;

  /**
   * @brief
   * Returns the index of a column, given the name of it, or nullptr if there is
   * no column with this name
   *
   * @param name The name to search for
   * @return The index of the column or nullptr if there is no such column
   */
  std::unique_ptr<std::size_t> find(const std::string& name) const;

private:
  std::vector<info_type> m_info_list;

};

}
} // end of namespace Euclid

#endif	/* TABLE_COLUMNINFO_H */

