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
 * @file Table/Row.h
 * @date April 8, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef TABLE_ROW_H
#define	TABLE_ROW_H

#include <memory>
#include <vector>
#include <string>
#include <iterator>
#include <boost/variant.hpp>

#include "ElementsKernel/Export.h"

#include "Table/ColumnInfo.h"
#include "NdArray/NdArray.h"

namespace std {

template <typename T>
std::ostream& operator<< (std::ostream& s, const std::vector<T>& v);

}

namespace Euclid {
namespace Table {

/**
 * @class Row
 *
 * @brief Represents one row of a Table
 *
 * @details
 * The Row is an immutable class which represents a single row of a Table. It
 * contains one cell for each column, which has a value of one of the types
 * defined in the cell_type boost::variant specialization. The information
 * about the columns can be retrieved via a ColumnInfo object provided by the
 * getColumnInfo() method. The values of the cells, in the case they are of
 * std::string type, they cannot be the empty string,
 * neither a string containing whitespace characters, because these values
 * break the representation of the columns in the ASCII file.
 */
class ELEMENTS_API Row {

public:

  /// The possible cell types
  typedef boost::variant<bool,
                         int32_t,
                         int64_t,
                         float,
                         double,
                         std::string,
                         std::vector<bool>,
                         std::vector<int32_t>,
                         std::vector<int64_t>,
                         std::vector<float>,
                         std::vector<double>,
                         NdArray::NdArray<bool>,
                         NdArray::NdArray<int32_t>,
                         NdArray::NdArray<int64_t>,
                         NdArray::NdArray<float>,
                         NdArray::NdArray<double>> cell_type;

  typedef std::vector<cell_type>::const_iterator const_iterator;

  /**
   * @brief
   * Constructs a Row with the given cell values and column info descriptor
   * @details
   * The number and type of the cells must match the ones of the columns, otherwise a
   * Elements::Exception is thrown. The column_info cannot be the nullptr and the
   * values of the cells cannot be the empty string or contain any whitespace
   * characters (if they are of type std::string).
   *
   * @param values The values of the row cells
   * @param column_info The information of the columns
   * @throws Elements::Exception
   *    if column_info is null
   * @throws Elements::Exception
   *    if the values vector have different size than the number of columns
   * @throws Elements::Exception
   *    if the values have different types than the columns
   * @throws Elements::Exception
   *    if any of the cell values is the empty string
   * @throws Elements::Exception
   *    if any of the cell values contains whitespace characters
   */
  Row(std::vector<cell_type> values, std::shared_ptr<ColumnInfo> column_info);

  /// Default destructor
  virtual ~Row() = default;

  /**
   * @brief
   * Returns a ColumnInfo object describing the columns of the Row
   *
   * @return the information about the columns
   */
  std::shared_ptr<ColumnInfo> getColumnInfo() const;

  /**
   * @brief
   * Returns the number of cells in the row
   *
   * @return the number of cells
   */
  size_t size() const;

  /**
   * @brief
   * Returns the value of the column with the given index (zero based)
   *
   * @param index The index of the column (zero based)
   * @return The value of the column
   * @throws Elements::Exception
   *    if the index is out of range
   */
  const cell_type& operator[](const size_t index) const;

  /**
   * @brief
   * Returns the value of the row for the given column
   *
   * @param column The name of the column
   * @return The value of the row for the column
   * @throws Elements::Exception
   *    if there is no column with such name
   */
  const cell_type& operator[](const std::string& column) const;

  /**
   * @brief
   * Returns a const iterator to the first cell of the row
   *
   * @return An iterator to the first cell
   */
  const_iterator begin() const;

  /**
   * @brief
   * Returns a const iterator to the past-the-end cell of the row
   *
   * @return An iterator to the cell past the end of the row
   */
  const_iterator end() const;

private:
  std::vector<cell_type> m_values;
  std::shared_ptr<ColumnInfo> m_column_info;
};

}
} // end of namespace Euclid

#endif	/* TABLE_ROW_H */

