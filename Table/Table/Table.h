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
 * @file Table/Table.h
 * @date April 9, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef TABLE_TABLE_H
#define TABLE_TABLE_H

#include <memory>
#include <vector>

#include "ElementsKernel/Export.h"

#include "Table/ColumnInfo.h"
#include "Table/Row.h"

namespace Euclid {
namespace Table {

/**
 * @class Table
 *
 * @brief Represents a table
 *
 * @details
 * The Table is an immutable class which represents a table. It contains
 * a list of Rows, which all have the same columns. Note that because the Table
 * is immutable instances without rows are not allowed.
 */
class ELEMENTS_API Table {

public:
  typedef std::vector<Row>::const_iterator const_iterator;

  /**
   * @brief
   * Constructs a Table with the given rows
   * @details
   * The given row_list, which cannot be empty, must contain Rows which have the
   * same ColumnInfo. Rows with different columns are not allowed.
   *
   * @param row_list The rows of the table
   * @throws Elements::Exception
   *    if the given list is empty
   * @throws Elements::Exception
   *    if not all the rows have the same columns
   */
  explicit Table(std::vector<Row> row_list);

  /**
   * @brief
   * Construct an empty Table with associated metadata
   * @param column_info
   */
  explicit Table(std::shared_ptr<ColumnInfo> column_info);

  /// Default destructor
  virtual ~Table() = default;

  /**
   * @brief
   * Returns a ColumnInfo object describing the columns of the table
   *
   * @return the information about the columns
   */
  std::shared_ptr<ColumnInfo> getColumnInfo() const;

  /**
   * @brief
   * Returns the number of rows in the table
   * @return the number of rows
   */
  std::size_t size() const;

  /**
   * @brief
   * Returns the row with the given index (zero based)
   *
   * @param index The index of the row (zero based)
   * @return The row
   * @throws Elements::Exception
   *    if the index is out of range
   */
  const Row& operator[](std::size_t index) const;

  /**
   * @brief
   * Returns a const iterator to the first row
   *
   * @return An iterator to the first row
   */
  const_iterator begin() const;

  /**
   * @brief
   * Returns a const iterator to the past-the-end row
   *
   * @return An iterator to the past-the-end row
   */
  const_iterator end() const;

private:
  std::vector<Row>            m_row_list;
  std::shared_ptr<ColumnInfo> m_column_info;
};

}  // namespace Table
}  // end of namespace Euclid

#endif /* TABLE_TABLE_H */
