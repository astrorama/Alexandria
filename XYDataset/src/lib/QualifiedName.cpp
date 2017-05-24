/** 
 * @file src/lib/QualifiedName.cpp
 * @date May 19, 2014
 * @author Nikolaos Apostolakos
 */

#include <algorithm>
#include <boost/algorithm/string.hpp>
#include <ElementsKernel/Exception.h>
#include "XYDataset/QualifiedName.h"

namespace Euclid {
namespace XYDataset {

QualifiedName::QualifiedName(std::vector<std::string> groups, std::string name)
            : m_groups {std::move(groups)}, m_dataset_name {std::move(name)} {
  for (auto& group : m_groups) {
    if (group.empty() || group.find('/') != std::string::npos) {
      throw Elements::Exception() << "Invalid group name : \"" << group << "\""
          << " in qualified name : \"" << m_qualified_name.append(group).append("/") << "\"";
    }
    m_qualified_name.append(group).append("/");
  }
  if (m_dataset_name.empty() || m_dataset_name.find('/') != std::string::npos) {
    throw Elements::Exception() << "Invalid name : \"" << m_qualified_name.append(m_dataset_name) << "\"";
  }
  m_qualified_name.append(m_dataset_name);
}
            
std::vector<std::string> getGroups(const std::string& qualified_name) {
  std::vector<std::string> groups {};
  boost::split(groups, qualified_name, boost::is_any_of("/"));
  // The last one is the name, so we remove it
  groups.pop_back();
  return groups;
}
            
std::string getName(const std::string& qualified_name) {
  std::vector<std::string> groups {};
  boost::split(groups, qualified_name, boost::is_any_of("/"));
  return groups.back();
}

QualifiedName::QualifiedName(const std::string& qualified_name)
            : QualifiedName(getGroups(qualified_name), getName(qualified_name)) { }

const std::vector<std::string>& QualifiedName::groups() const {
  return m_groups;
}

const std::string& QualifiedName::datasetName() const {
  return m_dataset_name;
}

const std::string& QualifiedName::qualifiedName() const {
  return m_qualified_name;
}

bool QualifiedName::belongsInGroup(const QualifiedName& group) const {
  if (group.m_groups.size()+1 > this->m_groups.size()) {
    return false;
  }
  bool group_check = std::equal(group.m_groups.begin(), group.m_groups.end(), this->m_groups.begin());
  return group_check 
        ? group.m_dataset_name == this->m_groups.at(group.m_groups.size())
        : false;
}

size_t QualifiedName::hash() const {
  if (m_hash == 0) {
      std::hash<std::string> stringHash;
      m_hash = stringHash(qualifiedName());
    }
    return m_hash;
}

bool QualifiedName::operator<(const QualifiedName& other) const {
  size_t thisHash = this->hash();
  size_t otherHash = other.hash();
  if (thisHash != otherHash) {
    return thisHash < otherHash;
  } else{
    return this->qualifiedName() < other.qualifiedName();
  }
}

bool QualifiedName::operator==(const QualifiedName& other) const {
  size_t thisHash = this->hash();
  size_t otherHash = other.hash();
  if (thisHash != otherHash) {
    return false;
  } else{
    return this->qualifiedName() == other.qualifiedName();
  }
}

bool QualifiedName::operator!=(const QualifiedName& other) const {
  return !(*this == other);
}

std::ostream& operator<<(std::ostream& stream, const QualifiedName& qualified_name)
{
  stream << qualified_name.qualifiedName();
  return stream;
}

} // namespace XYDataset
} // end of namespace Euclid
