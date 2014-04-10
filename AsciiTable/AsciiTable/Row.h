/** 
 * @file Row.h
 * @date April 8, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef ASCIITABLE_ROW_H
#define	ASCIITABLE_ROW_H

#include <memory>
#include <vector>
#include <string>
#include <iterator>
#include "AsciiTable/ColumnInfo.h"

namespace AsciiTable {

/**
 * @class Row
 * 
 * @brief Represents one row of a Table
 * 
 * @details
 * The Row is an immutable class which represents a single row of a Table. It
 * contains one cell for each column, which has a string value. The information
 * about the columns can be retrieved via a ColumnInfo object provided by the
 * getColumnInfo() method. The values of the cells cannot be the empty string,
 * neither a string containing whitespace characters, because these values
 * break the representation of the columns in the ASCII file.
 */
class Row {
  
public:
  
  typedef std::vector<std::string>::const_iterator const_iterator;
  
  /**
   * @brief
   * Constructs a Row with the given cell values and column info descriptor
   * @details
   * The number of values must match the number of columns, otherwise a
   * ElementsException is thrown. The column_info cannot be the nullptr and the
   * values of the cells cannot be the empty string or contain any whitespace
   * characters.
   * 
   * @param values The values of the row cells
   * @param column_info The information of the columns
   * @throws ElementsException
   *    if column_info is null
   * @throws ElementsException
   *    if the values vector have different size than the number of columns
   * @throws ElementsException
   *    if any of the cell values is the empty string
   * @throws ElementsException
   *    if any of the cell values contains whitespace characters
   */
  Row(std::vector<std::string> values, std::shared_ptr<ColumnInfo> column_info);
  
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
   * @throws ElementsKernel::ElementsException
   *    if the index is out of range
   */
  const std::string& operator[](const size_t index) const;
  
  /**
   * @brief
   * Returns the value of the row for the given column
   * 
   * @param column The name of the column
   * @return The value of the row for the column
   * @throws ElementsKernel::ElementsException
   *    if there is no column with such name
   */
  const std::string& operator[](const std::string& column) const;
  
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
  std::vector<std::string> m_values;
  std::shared_ptr<ColumnInfo> m_column_info;
};

}

#endif	/* ASCIITABLE_ROW_H */

