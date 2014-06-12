/** 
 * @file Table.h
 * @date April 9, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHTABLE_TABLE_H
#define	CHTABLE_TABLE_H

#include <memory>
#include <vector>
#include "ChTable/ColumnInfo.h"
#include "ChTable/Row.h"

namespace ChTable {

/**
 * @class Table
 * 
 * @brief Represents an ASCII table
 * 
 * @details
 * The Table is an immutable class which represents an ASCII table. It contains
 * a list of Rows, which all have the same columns. Note that because the Table
 * is immutable instances without rows are not allowed.
 */
class Table {
  
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
   * @throws ElementsException
   *    if the given list is empty
   * @throws ElementsException
   *    if not all the rows have the same columns
   */
  Table(std::vector<Row> row_list);
  
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
   * @throws ElementsException
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
  std::vector<Row> m_row_list;
  std::shared_ptr<ColumnInfo> m_column_info;
};

}

#endif	/* CHTABLE_TABLE_H */

