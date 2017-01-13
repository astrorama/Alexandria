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