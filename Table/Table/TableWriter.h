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
 * @file Table/TableWriter.h
 * @date 11/30/16
 * @author nikoapos
 */

#ifndef _TABLE_TABLEWRITER_H
#define _TABLE_TABLEWRITER_H

#include "Table/Table.h"
#include <memory>
#include <string>

namespace Euclid {
namespace Table {

/**
 * @class TableWriter
 *
 * @brief Interface for classes writing tables
 *
 * @details
 * Each TableWriter implementation should behave like a stream writing a table.
 * It must implement the methods addComment(), init() and append(). See the
 * documentation of these methods for more information of how to implement them.
 *
 * Note that all TableWriter implementations, as they are representing streams
 * to a single table, should not be able to be copied, something that is forced
 * by the TableWriter interface. There is no such restriction for move operations.
 */
class TableWriter {
public:
  TableWriter() = default;

  TableWriter(TableWriter&&) = default;
  TableWriter& operator=(TableWriter&&) = default;

  TableWriter(const TableWriter&) = delete;
  TableWriter& operator=(const TableWriter&) = delete;

  virtual ~TableWriter() = default;

  /**
   * @brief Adds a comment to the output table
   * @details
   * The different implementations should implement this method to write the
   * comment to the output stream. The behavior of this method after data have
   * been already been added is up to the specific implementation, which can
   * either allow for the addition of the comment (if the format supports such
   * action) or throw an exception. Users of the generic interface should not
   * call this method after the addData() has been called.
   * @param comment
   *    The comment to add
   * @throws Elements::Exception
   *    If data have been already been added and the implementation does not
   *    support further comments addition
   */
  virtual void addComment(const std::string& comment) = 0;

  /**
   * @brief Appends the contents of the given table to the output
   * @details
   * The first time this method is called defines the columns of the output. Any
   * subsequent calls must be done with tables which match exactly these column
   * names and types. When the call ends, the given data should be already written
   * to the underlying stream or file.
   * @param table
   *    The table containing the rows to write
   * @throws Elements::Exception
   *    If the given table has different columns than one used at a previous
   *    call of the addData() method.
   */
  void addData(const Table& table);

protected:
  /**
   * @brief Initializes the output header based on the given table columns
   * @details
   * This method will be called the first time the addData() is called, before
   * the append() call. The specific implementations should update their output
   * with the column information of the table.
   * @param table
   *    The table to get the column information from
   */
  virtual void init(const Table& table) = 0;

  /**
   * @brief Appends to the output the contents of the given table
   * @details
   * The specific implementations should implement this method to append to the
   * output all the rows of the given table. This method can assume that the init()
   * has already been called. The given table is guaranteed to have the same
   * columns with the one the init() has been called with, so no extra checks
   * are necessary. When the call ends, the given data should be already written
   * to the output.
   * @param table
   *    The table containing the rows to write
   */
  virtual void append(const Table& table) = 0;

private:
  std::unique_ptr<ColumnInfo> m_column_info{nullptr};
};  // End of TableWriter class

}  // namespace Table
}  // namespace Euclid

#endif
