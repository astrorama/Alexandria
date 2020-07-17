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
 * @file src/lib/ColumnInfo.cpp
 * @date April 7, 2014
 * @author Nikolaos Apostolakos
 */

#include <algorithm>
#include <set>
#include "ElementsKernel/Exception.h"
#include "Table/ColumnInfo.h"

namespace Euclid {
namespace Table {

ColumnInfo::ColumnInfo(std::vector<info_type> info_list)
        : m_info_list{std::move(info_list)} {
  if (m_info_list.empty()) {
    throw Elements::Exception() << "Empty info_list is not allowed";
  }
  std::set<std::string> set {};
  for (const auto& info : m_info_list) {
    const auto& name = info.name;
    if (!set.insert(name).second) {  // Check for duplicate names
      throw Elements::Exception() << "Duplicate column name " << name;
    }
  }
}

bool ColumnInfo::operator==(const ColumnInfo& other) const {
  if (this->m_info_list.size() != other.m_info_list.size()) {
    return false;
  }
  return std::equal(this->m_info_list.cbegin(), this->m_info_list.cend(), other.m_info_list.cbegin());
}

bool ColumnInfo::operator !=(const ColumnInfo& other) const {
  return !(*this == other);
}

std::size_t ColumnInfo::size() const {
  return m_info_list.size();
}

const ColumnDescription& ColumnInfo::getDescription(std::size_t index) const {
  if (index >= size()) {
    throw Elements::Exception("Index out of bounds");
  }
  return m_info_list[index];
}

const ColumnDescription& ColumnInfo::getDescription(const std::string& name) const {
  auto iter = std::find_if(m_info_list.begin(), m_info_list.end(),
                           [&name](const info_type& info) { return info.name == name; });
  if (iter == m_info_list.end()) {
    throw Elements::Exception() << "Column " << name << " does not exist";
  }
  return *iter;
}

std::unique_ptr<size_t> ColumnInfo::find(const std::string& name) const {
  auto begin = m_info_list.begin();
  auto end = m_info_list.end();
  auto iter = std::find_if(begin, end, [&name](const info_type& info){return info.name == name;});
  if (iter != end) {
    size_t index {static_cast<size_t>(std::distance(begin, iter))};
    return std::unique_ptr<size_t> {new size_t {index}};
  }
  return std::unique_ptr<size_t> {};
}

}
} // end of namespace Euclid
