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

/*
 * @file TableReader.h
 * @author nikoapos
 */

#ifndef _TABLE_TABLEREADER_H
#define _TABLE_TABLEREADER_H

#include "Table/Table.h"

namespace Euclid {
namespace Table {

/**
 * @class TableReader
 *
 * @brief Interface for classes reading tables
 *
 * @details
 * Each TableReader implementation should behave like a stream to a table. It
 * must implement the methods getComment(), getInfo(), readImpl(), skip() and hasMoreRows().
 * See the documentation of these methods for more information of how to
 * implement them.
 *
 * Note that all TableReader implementations, as they are representing streams
 * to a single table, should not be able to be copied, something that is forced
 * by the TableReader interface. There is no such restriction for move operations.
 *
 */
class TableReader {

public:
  TableReader() = default;

  TableReader(TableReader&&) = default;
  TableReader& operator=(TableReader&&) = default;

  TableReader(const TableReader&) = delete;
  TableReader& operator=(const TableReader&) = delete;

  virtual ~TableReader() = default;

  /**
   * @return Returns the comment associated to the table
   */
  virtual std::string getComment() = 0;

  /**
   * @brief Returns the column information of the table
   * @details
   * The different implementations should try to implement this method in such
   * way so the full parsing of the table is not necessary and multiple calls
   * of this method do not trigger the reading again.
   * @return The table column information
   */
  virtual const ColumnInfo& getInfo() = 0;

  /**
   * @brief Reads next rows as a table
   * @details
   * If the given parameter is a number bigger than the rows left, the result is
   * a table with all of them (and size less than the parameter). If the parameter
   * is a negative number, the returned Table object contains all the remaining
   * rows. If the all the rows of the table have already been read, an exception
   * is thrown.
   * @param rows
   *    The number of rows to read
   * @return
   *    A Table object containing the rows read
   * @throws Elements::Exception
   *    If the reader has already read all the available rows
   */
  Table read(long rows = -1) {
    return readImpl(rows);
  }

  /**
   * @brief Skips next rows
   * @details
   * Implementations should implement this method so the next read() call will
   * ignore that many rows as the given parameter. If the given number is greater
   * or equal to the number of rows left, a consequent call of read() should
   * throw an exception and a call to hasMoreRows() should return false.
   * @param rows
   *    The number of rows to skip
   */
  virtual void skip(long rows) = 0;

  /**
   * @brief Checks if there are any rows left to read
   * @details
   * Implementations should implement this method to return true if there are
   * still rows not read using the read() method and false otherwise. If the
   * result of this method is true, a call to read() should successfully return
   * a table object, If the result of this method is false, a call th read()
   * will throw an Elements::Exception.
   * @return
   *    true if there are more rows to read
   */
  virtual bool hasMoreRows() = 0;

  /**
   * @brief Returns the number of rows left to read
   * @details
   * When using this method keep in mind that some formats (like ASCII) might
   * require to parse the full file.
   * @return
   *    The number of rows left to read
   */
  virtual std::size_t rowsLeft() = 0;

protected:
  /**
   * @brief Method to be implemented by subclasses for reading the table
   * @details
   * Implementations should implement this method to behave as described at the
   * documentation of the read() method.
   * @param rows
   *    The number of rows to read
   * @return
   *    A Table object containing the rows read
   * @throws Elements::Exception
   *    If the reader has already read all the available rows
   */
  virtual Table readImpl(long rows) = 0;
};

}  // namespace Table
}  // namespace Euclid

#endif /* _TABLE_TABLEREADER_H */
