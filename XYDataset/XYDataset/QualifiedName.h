/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
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
 * @file XYDataset/QualifiedName.h
 * @date May 19, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef PHZDATAMODEL_QUALIFIEDNAME_H
#define PHZDATAMODEL_QUALIFIEDNAME_H

#include <functional>
#include <iostream>
#include <string>
#include <vector>

#include "ElementsKernel/Export.h"

namespace Euclid {
namespace XYDataset {

/**
 * @class QualifiedName
 *
 * @brief Represents a name qualified with a set of groups
 *
 *
 * The QualifiedName class represents a name qualified with a set of groups.
 * The groups and the names are separated with the '/' character (eg
 * group1/group2/name). Note that the qualified name is assumed to be unique and
 * it can be used as identifier.
 *
 * The QualifiedName class provides a method for calculating its hash. The
 * "less than" and "equals" operators are implemented using this hash value as
 * much as possible. This means the QualifiedName can be used as a key in ordered
 * and unordered collections in an efficient way. Note that for favoring
 * performance, the ordering of the QualifiedNames is not alphabetical, but based
 * on the hash key. If the alphabetical ordering is important, then the provided
 * QualifiedName::AlphabeticalComparator can be used:
 *
 * \code
 * // This set will order the QualifiedNames based on their hash values
 * std::set<QualifiedName> hashOrderedSet {};
 *
 * // This set will order the QualifiedNames in alphabetical order of their
 * // qualified names
 * std::set<QualifiedName, QualifiedName::AlphabeticalComparator> alphabeticalSet {};
 * \endcode
 */
class ELEMENTS_API QualifiedName {

public:
  /**
   * @brief
   * Constructs a QualifiedName with the given group and name
   * @details
   * Both group and name cannot be empty and they cannot contain the '/'
   * character. In this case an Elements::Exception is thrown.
   *
   * @param groups One or more groups to qualify the name with
   * @param name The name
   * @throws Elements::Exception
   *    if any of the parameters is empty or contains the '/' character
   */
  QualifiedName(std::vector<std::string> groups, std::string name);

  /**
   * @brief
   * Constructs a QualifiedName object representing the given string
   * @details
   * The given string must follow the rules of a qualified name (groups and name
   * separated with the '/' character and no empty names allowed).
   * @throws Elements::Exception
   *    if the given string is an invalid qualified name
   */
  QualifiedName(const std::string&);  // cppcheck-suppress  noExplicitConstructor

  /**
   * @brief Copy constructor
   */
  QualifiedName(const QualifiedName&) = default;

  /**
   * @brief Copy assignment operator
   * @return A reference to the QualifiedName which was copied to
   */
  QualifiedName& operator=(const QualifiedName&) = default;

  /**
   * @brief Move constructor
   */
  QualifiedName(QualifiedName&&) = default;

  /**
   * @brief Move assignment operator
   * @return A reference to the QualifiedName in which was moved in
   */
  QualifiedName& operator=(QualifiedName&&) = default;

  /**
   * @brief Destructor
   */
  virtual ~QualifiedName() = default;

  /**
   * @brief Returns the groups qualifying the name
   * @return The groups qualifying the name
   */
  const std::vector<std::string>& groups() const;

  /**
   * @brief Returns the unqualified name
   * @return The unqualified name
   */
  const std::string& datasetName() const;

  /**
   * @brief Returns the qualified name as a string
   * @details
   * The qualified name is the combination of the groups and name
   * separated with the '/' character. For example: "group1/group2/name".
   * @return The qualified name as a string
   */
  const std::string& qualifiedName() const;

  /// Checks if the QualifiedName belongs in a given group
  bool belongsInGroup(const QualifiedName& group) const;

  /**
   * @brief Returns the hash value of the QualifiedName
   * @return The hash value
   */
  size_t hash() const;

  /**
   * @brief Compares this QualifiedName with the parameter
   * @details
   * The comparison is based on the hash values of the QualifiedNames (for performance
   * reasons). For alphabetical comparison the QualifiedName::alphabeticalComparator
   * can be used.
   * @param other The QualifiedName to compare with
   * @return
   */
  bool operator<(const QualifiedName& other) const;

  /**
   * @brief Checks if this QualifiedName is equal with the parameter
   * @details
   * Two QualifiedNames are considered equal if they have the same groups and name.
   * @param other The QualifiedName to compare with
   * @return true if the two QualifiedName are equal, false otherwise
   */
  bool operator==(const QualifiedName& other) const;

  /**
   * @brief Checks if this QualifiedName is not equal with the parameter
   * @details
   * Two QualifiedNames are considered equal if they have the same groups and name.
   * @param other The QualifiedName to compare with
   * @return true if the two QualifiedName are not equal, false otherwise
   */
  bool operator!=(const QualifiedName& other) const;

  /**
   * @class AlphabeticalComparator
   * @brief Provides alphabetical comparison for the QualifiedNames a and b
   * @param a The first QualifiedName to compare
   * @param b The second QualifiedName to compare
   * @return true if the a < b lexicographical, false otherwise
   */
  struct AlphabeticalComparator {
    bool operator()(const QualifiedName& a, const QualifiedName& b) const {
      if (a.qualifiedName().compare(b.qualifiedName()) < 0) {
        return true;
      } else {
        return false;
      }
    }
  };

private:
  std::vector<std::string> m_groups;
  std::string              m_dataset_name;
  std::string              m_qualified_name;
  mutable size_t           m_hash{0};

};  // class QualifiedName

/// Make the QualifiedName streamable
std::ostream& operator<<(std::ostream& stream, const QualifiedName& qualified_name);

}  // namespace XYDataset
}  // end of namespace Euclid

namespace std {

/**
 * @brief Hash operation for the Euclid::XYDataset::QualifiedName
 * @details
 * This method is implemented so no special hash functions need to be given as
 * template parameters to the unordered collections. It just redirects the call
 * to the QualifiedName function.
 * @param qualifiedName The QualifiedName to get the hash key for
 * @return The hash key of the QualifiedName
 */
template <>
struct hash<Euclid::XYDataset::QualifiedName> {
  size_t operator()(const Euclid::XYDataset::QualifiedName& qualifiedName) const {
    return qualifiedName.hash();
  }
};

}  // namespace std

#endif  // PHZDATAMODEL_QUALIFIEDNAME_H
