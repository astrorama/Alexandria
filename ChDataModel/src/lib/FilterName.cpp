/** 
 * @file FilterName.cpp
 * @date January 17, 2014
 * @author Nikolaos Apostolakos
 */

#include "ChDataModel/FilterName.h"

namespace ChDataModel {

FilterName::FilterName(const std::string& group, const std::string& name)
    : m_group {group}, m_name {name} { }

const std::string& FilterName::group() const {
  return m_group;
}

const std::string& FilterName::name() const {
  return m_name;
}

const std::string& FilterName::qualifiedName() const {
  if (m_qual_name.empty()) {
    std::string temp {m_group};
    temp.append("/").append(m_name);
    m_qual_name = temp;
  }
  return m_qual_name;
}

size_t FilterName::hash() const {
  if (m_hash == 0) {
      std::hash<std::string> stringHash;
      m_hash = stringHash(qualifiedName());
    }
    return m_hash;
}

bool FilterName::operator<(const FilterName& other) const {
  size_t thisHash = this->hash();
  size_t otherHash = other.hash();
  if (thisHash != otherHash) {
    return thisHash < otherHash;
  } else{
    return this->qualifiedName() < other.qualifiedName();
  }
}

bool FilterName::operator==(const FilterName& other) const {
  size_t thisHash = this->hash();
  size_t otherHash = other.hash();
  if (thisHash != otherHash) {
    return false;
  } else{
    return this->qualifiedName() == other.qualifiedName();
  }
}

} // namespace ChDataModel

namespace std {

template <>
struct hash<ChDataModel::FilterName> {
  size_t operator()(const ChDataModel::FilterName& filterName) const {
    return filterName.hash();
  }
};

} // namespace std