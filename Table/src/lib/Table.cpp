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
 * @file src/lib/Table.cpp
 * @date April 9, 2014
 * @author Nikolaos Apostolakos
 */

#include "ElementsKernel/Exception.h"
#include "Table/Table.h"

namespace Euclid {
namespace Table {

Table::Table(std::vector<Row> row_list) : m_row_list {std::move(row_list)} ,
                                          m_column_info {} {
  // Check we have some rows
  if (m_row_list.empty()) {
    throw Elements::Exception() << "Construction of empty tables is not allowed";
  }
  // We cannot initialize the m_column_info before this point because we must
  // be sure the row list is not empty
  m_column_info = m_row_list[0].getColumnInfo();
  // Check that all the rows have the same column info
  for (auto row : m_row_list) {
    if (*row.getColumnInfo() != *m_column_info) {
      throw Elements::Exception() << "Construction of table from rows with different "
                                << "columns is not allowed";
    }
  }
}

std::shared_ptr<ColumnInfo> Table::getColumnInfo() const {
  return m_column_info;
}

std::size_t Table::size() const {
  return m_row_list.size();
}

const Row& Table::operator [](std::size_t index) const {
  if (index >= m_row_list.size()) {
    throw Elements::Exception("Index out of bounds");
  }
  return m_row_list[index];
}

Table::const_iterator Table::begin() const {
  return m_row_list.cbegin();
}

Table::const_iterator Table::end() const {
  return m_row_list.cend();
}

}
} // end of namespace Euclid
