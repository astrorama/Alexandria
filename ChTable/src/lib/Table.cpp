/** 
 * @file src/lib/Table.cpp
 * @date April 9, 2014
 * @author Nikolaos Apostolakos
 */

#include "ElementsKernel/ElementsException.h"
#include "ChTable/Table.h"

namespace Euclid {
namespace ChTable {

Table::Table(std::vector<Row> row_list) : m_row_list {std::move(row_list)} ,
                                          m_column_info {} {
  // Check we have some rows
  if (m_row_list.empty()) {
    throw ElementsException() << "Construction of empty tables is not allowed";
  }
  // We cannot initialize the m_column_info before this point because we must
  // be sure the row list is not empty
  m_column_info = m_row_list[0].getColumnInfo();
  // Check that all the rows have the same column info
  for (auto row : m_row_list) {
    if (*row.getColumnInfo() != *m_column_info) {
      throw ElementsException() << "Construction of table from rows with different "
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
    throw ElementsException("Index out of bounds");
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