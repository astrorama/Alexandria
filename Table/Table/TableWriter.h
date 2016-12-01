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

#include <string>
#include <memory>
#include "Table/Table.h"

namespace Euclid {
namespace Table {

/**
 * @class TableWriter
 * @brief
 *
 */
class TableWriter {

public:
  
  TableWriter() = default;
  
  TableWriter(TableWriter&&) = default;
  TableWriter& operator=(TableWriter&&) = default;
  
  TableWriter(const TableWriter&) = delete;
  TableWriter& operator=(const TableWriter&) = delete;

  virtual ~TableWriter() = default;
  
  virtual void addComment(const std::string&) = 0;

  virtual void addData(const Table& table) final;

protected:
  
  virtual void init(const Table& table) = 0;
  
  virtual void append(const Table& table) = 0;

private:
  
  std::unique_ptr<ColumnInfo> m_column_info {nullptr};

}; // End of TableWriter class

} // namespace Table
} // namespace Euclid


#endif
