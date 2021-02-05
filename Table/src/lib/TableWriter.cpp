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
 * @file src/lib/TableWriter.cpp
 * @date 11/30/16
 * @author nikoapos
 */

#include "Table/TableWriter.h"
#include "ElementsKernel/Exception.h"

namespace Euclid {
namespace Table {

void TableWriter::addData(const Table& table) {
  auto& info = *table.getColumnInfo();
  if (m_column_info == nullptr) {
    m_column_info.reset(new ColumnInfo(info));
    init(table);
  } else if (*m_column_info != info) {
    throw Elements::Exception() << "Cannot append table with different columns";
  }
  append(table);
}

}  // namespace Table
}  // namespace Euclid
