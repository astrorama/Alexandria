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

#ifndef XYDATASET_SERIALIZE_H
#define XYDATASET_SERIALIZE_H

#include "XYDataset/QualifiedName.h"
#include <boost/serialization/string.hpp>
#include <boost/serialization/vector.hpp>
#include <string>
#include <vector>

namespace boost {
namespace serialization {

/**
 * @brief Serialize/deserialize function.
 *
 * @details
 * Everything is done in the constructor. Nothing here.
 *
 */
template <typename Archive>
void serialize(Archive&, Euclid::XYDataset::QualifiedName&, const unsigned int) {
  // Nothing here. Everything is done in the constructor
}

/**
 * @brief Save the data to be used by the constructor.
 *
 * @details
 * Stores the Groups vector then the (unqualified)name.
 *
 */
template <typename Archive>
void save_construct_data(Archive& ar, const Euclid::XYDataset::QualifiedName* t, const unsigned int) {
  std::vector<std::string> groups = t->groups();
  ar << groups;
  std::string name = t->datasetName();
  ar << name;
}

/**
 * @brief Get constructor data and instantiate the object.
 *
 * @details
 * Reads the Groups vector then the (unqualified)name.
 *
 */
template <typename Archive>
void load_construct_data(Archive& ar, Euclid::XYDataset::QualifiedName* t, const unsigned int) {
  std::vector<std::string> groups;
  ar >> groups;
  std::string name;
  ar >> name;
  ::new (t) Euclid::XYDataset::QualifiedName(std::move(groups), std::move(name));
}

}  // namespace serialization
}  // namespace boost

#endif  // XYDATASET_SERIALIZE_H
