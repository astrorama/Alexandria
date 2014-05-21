/** 
 * @file QualifiedName.cpp
 * @date May 19, 2014
 * @author Nikolaos Apostolakos
 */

#include <ElementsKernel/ElementsException.h>
#include "XYDataset/QualifiedName.h"

namespace XYDataset {

QualifiedName::QualifiedName(std::vector<std::string> groups, std::string name)
    : m_groups {std::move(groups)}, m_name {std::move(name)} {
  for (auto& group : m_groups) {
    if (group.empty() || group.find('/') != std::string::npos) {
      throw ElementsException() << "Invalid group name " << group;
    }
    m_qualified_name.append(group).append("/");
  }
  if (m_name.empty() || m_name.find('/') != std::string::npos) {
    throw ElementsException() << "Invalid name " << m_name;
  }
  m_qualified_name.append(m_name);
}

const std::vector<std::string>& QualifiedName::groups() const {
  return m_groups;
}

const std::string& QualifiedName::name() const {
  return m_name;
}

const std::string& QualifiedName::qualifiedName() const {
  return m_qualified_name;
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

} // namespace XYDataset
