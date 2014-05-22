/** 
 * @file QualifiedName.h
 * @date May 20, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef PHZDATAMODEL_SERIALIZATION_QUALIFIEDNAME_H
#define	PHZDATAMODEL_SERIALIZATION_QUALIFIEDNAME_H

#include <string>
#include <vector>
#include "XYDataset/QualifiedName.h"

namespace boost {
namespace serialization {

template<typename Archive>
void serialize(Archive&, XYDataset::QualifiedName&, const unsigned int) {
  // Nothing here. Everything is done in the constructor
}

template<typename Archive>
void save_construct_data(Archive& ar, const XYDataset::QualifiedName* t, const unsigned int) {
  std::vector<std::string> groups = t->groups();
  ar << groups;
  std::string name = t->name();
  ar << name;
}

template<typename Archive>
void load_construct_data(Archive& ar, XYDataset::QualifiedName* t, const unsigned int) {
  std::vector<std::string> groups;
  ar >> groups;
  std::string name;
  ar >> name;
  ::new(t) XYDataset::QualifiedName(std::move(groups), std::move(name));
}

} // end of namespace serialization
} // end of namespace boost

#endif	/* PHZDATAMODEL_SERIALIZATION_QUALIFIEDNAME_H */

