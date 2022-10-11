/**
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
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
 * @file src/lib/Row.cpp
 * @date April 8, 2014
 * @author Nikolaos Apostolakos
 */

#include "Table/Row.h"
#include "AlexandriaKernel/RegexHelper.h"
#include "ElementsKernel/Exception.h"
#include <algorithm>
#include <boost/algorithm/string/join.hpp>

#if BOOST_VERSION < 105600
#include <boost/units/detail/utility.hpp>
using boost::units::detail::demangle;
#else
using boost::core::demangle;
#endif

namespace Euclid {
namespace Table {

struct StreamCellVisitor : public boost::static_visitor<void> {

  explicit StreamCellVisitor(std::ostream& s) : m_stream(s) {}

  template <typename T>
  void operator()(const std::vector<T>& v) const {
    auto it = v.begin();
    if (it != v.end()) {
      m_stream << *it;
      ++it;
    }
    while (it != v.end()) {
      m_stream << ',' << *it;
      ++it;
    }
  }

  template <typename T>
  void operator()(const T& val) const {
    m_stream << val;
  }

  std::ostream& m_stream;
};

std::ostream& operator<<(std::ostream& s, const cell_stream_adaptor& cell) {
  StreamCellVisitor visitor{s};
  boost::apply_visitor(visitor, cell.m_cell);
  return s;
}

Row::Row(std::vector<cell_type> values, std::shared_ptr<ColumnInfo> column_info)
    : m_values(std::move(values)), m_column_info{column_info} {
  if (!m_column_info) {
    throw Elements::Exception() << "Row construction with nullptr column_info";
  }
  if (m_values.size() != m_column_info->size()) {
    throw Elements::Exception() << "Wrong number of row values (" << m_values.size() << " instead of "
                                << m_column_info->size();
  }
  for (std::size_t i = 0; i < m_values.size(); ++i) {
    auto& value_type  = m_values[i].type();
    auto& column_type = column_info->getDescription(i).type;
    if (std::type_index{value_type} != column_type) {
      auto& column_name = column_info->getDescription(i).name;
      throw Elements::Exception() << "Incompatible cell type for " << column_name << ": expected "
                                  << demangle(column_type.name()) << ", got " << demangle(value_type.name());
    }
  }
  static const regex::regex vertical_whitespace{".*[\\n\\v\\f\\r].*"};  // Checks if input contains any whitespace
                                                                        // characters
  for (auto cell : m_values) {
    if (cell.type() == typeid(std::string)) {
      std::string value = boost::get<std::string>(cell);
      if (value.empty()) {
        throw Elements::Exception() << "Empty string cell values are not allowed";
      }
      if (regex_match(value, vertical_whitespace)) {
        throw Elements::Exception() << "Cell value '" << value << "' contains "
                                    << "vertical whitespace characters";
      }
    }
  }
}

std::shared_ptr<ColumnInfo> Row::getColumnInfo() const {
  return m_column_info;
}

size_t Row::size() const {
  return m_values.size();
}

const Row::cell_type& Row::operator[](const size_t index) const {
  if (index >= m_values.size()) {
    throw Elements::Exception("Index out of bounds");
  }
  return m_values[index];
}

const Row::cell_type& Row::operator[](const std::string& column) const {
  auto index = m_column_info->find(column);
  if (!index) {
    throw Elements::Exception() << "Row does not contain column with name " << column;
  }
  return m_values[*index];
}

Row::const_iterator Row::begin() const {
  return m_values.cbegin();
}

Row::const_iterator Row::end() const {
  return m_values.cend();
}

}  // namespace Table
}  // end of namespace Euclid
