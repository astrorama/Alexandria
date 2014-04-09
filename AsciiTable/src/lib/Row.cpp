/** 
 * @file Row.cpp
 * @date April 8, 2014
 * @author Nikolaos Apostolakos
 */

#include "ElementsKernel/ElementsException.h"
#include "AsciiTable/Row.h"

namespace AsciiTable {

Row::Row(std::vector<std::string> values, std::shared_ptr<ColumnInfo> column_info)
        : m_values{std::move(values)}, m_column_info{column_info} {
  // Check that the column_info is not null
  if (!m_column_info) {
    throw ElementsException() << "Row construction with nullptr column_info";
  }
  // We check that the values vector has correct size
  if (m_values.size() != m_column_info->size()) {
    throw ElementsException() << "Wrong number of row values (" << m_values.size()
                              << " instead of " << m_column_info->size();
  }
}

size_t Row::size() const {
  return m_values.size();
}

const std::string& Row::operator [](const size_t index) const {
  if (index >= m_values.size()) {
    throw ElementsException("Index out of bounds");
  }
  return m_values[index];
}

const std::string& Row::operator [](const std::string& column) const {
  auto index = m_column_info->getIndex(column);
  if (!index) {
    throw ElementsException() << "Row does not contain column with name " << column;
  }
  return m_values[*index];
}

Row::const_iterator Row::begin() const {
  return m_values.cbegin();
}

Row::const_iterator Row::end() const {
  return m_values.cend();
}

}