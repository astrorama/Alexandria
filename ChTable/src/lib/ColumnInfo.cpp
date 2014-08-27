/** 
 * @file src/lib/ColumnInfo.cpp
 * @date April 7, 2014
 * @author Nikolaos Apostolakos
 */

#include <algorithm>
#include <set>
// The std regex library is not fully implemented in GCC 4.8. The following lines
// make use of the BOOST library and can be modified if GCC 4.9 will be used in
// the future.
// #include <regex>
#include <boost/regex.hpp>
using boost::regex;
using boost::regex_match;
#include "ElementsKernel/Exception.h"
#include "ChTable/ColumnInfo.h"

namespace Euclid {
namespace ChTable {

ColumnInfo::ColumnInfo(std::vector<info_type> info_list)
        : m_info_list{std::move(info_list)} {
  if (m_info_list.empty()) {
    throw Elements::Exception() << "Empty info_list is not allowed";
  }
  std::set<std::string> set {};
  regex whitespace {".*\\s.*"}; // Checks if input contains any whitespace characters
  for (const auto& info_pair : m_info_list) {
    const auto& name = info_pair.first;
    if (name.empty()) {
      throw Elements::Exception() << "Empty string column names are not allowed";
    }
    if (regex_match(name, whitespace)) {
      throw Elements::Exception() << "Column name '" << name << "' contains "
                                << "whitespace characters";
    }
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

const std::string& ColumnInfo::getName(std::size_t index) const {
  if (index >= size()) {
    throw Elements::Exception("Index out of bounds");
  }
  return m_info_list[index].first;
}

const std::type_index& ColumnInfo::getType(std::size_t index) const {
  if (index >= size()) {
    throw Elements::Exception("Index out of bounds");
  }
  return m_info_list[index].second;
}

std::unique_ptr<size_t> ColumnInfo::find(const std::string& name) const {
  auto begin = m_info_list.begin();
  auto end = m_info_list.end();
  auto iter = std::find_if(begin, end, [&name](const info_type& pair){return pair.first == name;});
  if (iter != end) {
    size_t index {static_cast<size_t>(std::distance(begin, iter))};
    return std::unique_ptr<size_t> {new size_t {index}}; 
  }
  return std::unique_ptr<size_t> {};
}

}
} // end of namespace Euclid