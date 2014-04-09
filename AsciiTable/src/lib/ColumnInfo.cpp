/** 
 * @file ColumnInfo.cpp
 * @date April 7, 2014
 * @author Nikolaos Apostolakos
 */

#include <algorithm>
#include <iterator>
#include <set>
#include "ElementsKernel/ElementsException.h"
#include "AsciiTable/ColumnInfo.h"

namespace AsciiTable {

ColumnInfo::ColumnInfo(std::vector<std::string> name_list)
        : m_name_list{std::move(name_list)} {
  // We use a set to check for duplicate column names
  std::set<std::string> set {};
  for (auto name : m_name_list) {
    if (!set.insert(name).second) {
      throw ElementsException() << "Duplicate column name " << name;
    }
  }
}

bool ColumnInfo::operator==(const ColumnInfo& other) const {
  if (this->m_name_list.size() != other.m_name_list.size()) {
    return false;
  }
  return std::equal(this->m_name_list.cbegin(), this->m_name_list.cend(), other.m_name_list.cbegin());
}

bool ColumnInfo::operator !=(const ColumnInfo& other) const {
  return !(*this == other);
}

std::size_t ColumnInfo::size() const {
  return m_name_list.size();
}

std::unique_ptr<std::string> ColumnInfo::getName(std::size_t index) const {
  if (index < size()) {
    return std::unique_ptr<std::string> {new std::string {m_name_list[index]}};
  }
  return std::unique_ptr<std::string> {};
}

std::unique_ptr<size_t> ColumnInfo::getIndex(const std::string& name) const {
  auto begin = m_name_list.begin();
  auto end = m_name_list.end();
  auto iter = std::find(begin, end, name);
  if (iter != end) {
    size_t index {static_cast<size_t>(std::distance(begin, iter))};
    return std::unique_ptr<size_t> {new size_t {index}}; 
  }
  return std::unique_ptr<size_t> {};
}


}