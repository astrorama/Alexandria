/*
 * Copyright (C) 2022 Euclid Science Ground Segment
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

#ifndef GRIDCONTAINER_SERIALIZATION_GRIDCONTAINER_H
#define GRIDCONTAINER_SERIALIZATION_GRIDCONTAINER_H

#include "GridContainer/GridCellManagerVectorOfVectors.h"
#include <boost/serialization/array.hpp>
#include <boost/serialization/collection_traits.hpp>
#include <boost/serialization/nvp.hpp>
#include <boost/serialization/serialization.hpp>

namespace boost {
namespace serialization {

template <class Archive, typename T>
void save(Archive& ar, const Euclid::GridContainer::VectorValueProxy<T>& value_proxy, const unsigned int) {
  size_t count = value_proxy.size();
  ar << BOOST_SERIALIZATION_NVP(count);
  if (count > 0) {
    ar << make_array<const T>(static_cast<const T*>(&value_proxy[0]), count);
  }
}

template <class Archive, typename T>
void load(Archive& ar, Euclid::GridContainer::VectorValueProxy<T>& value_proxy, const unsigned int) {
  size_t count;
  ar >> BOOST_SERIALIZATION_NVP(count);
  assert(count == value_proxy.size());
  T* ptr = &value_proxy[0];
  while (count-- > 0) {
    ar >> boost::serialization::make_nvp("item", *ptr++);
  }
}

template <class Archive, typename T>
void serialize(Archive& ar, Euclid::GridContainer::VectorValueProxy<T>& value_proxy, const unsigned int version) {
  split_free(ar, value_proxy, version);
}

}  // namespace serialization
}  // namespace boost

BOOST_SERIALIZATION_COLLECTION_TRAITS(Euclid::GridContainer::VectorValueProxy)

#endif  // GRIDCONTAINER_SERIALIZATION_GRIDCONTAINER_H
