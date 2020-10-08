/*
 * Copyright (C) 2012-2020 Euclid Science Ground Segment
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
 * @file GridContainer/serialization/GridAxis.h
 * @date May 16, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef GRIDCONTAINER_SERIALIZATION_GRIDAXIS_H
#define GRIDCONTAINER_SERIALIZATION_GRIDAXIS_H

#include "GridContainer/GridAxis.h"
#include <boost/serialization/utility.hpp>
#include <memory>
#include <type_traits>

namespace boost {
namespace serialization {

/// Method which saves/loads an GridAxis instance to/from an archive. It
/// does nothing as everything is done with the data passed to the constructor.
template <typename Archive, typename T>
void serialize(Archive&, Euclid::GridContainer::GridAxis<T>&, const unsigned int) {
  // Nothing here as everything is done with the data passed to the constructor
}

/// Version of the saveType method for types which do have default constructors.
/// It saves the object t to the archive. The boost::serialization::serialize
/// method must be implemented for the type T.
template <typename Archive, typename T>
void saveType(Archive& ar, const T& t, typename std::enable_if<std::is_default_constructible<T>::value>::type* = 0) {
  ar << t;
}

/// Version of the saveType method for types which do not have default
/// constructor. It saves a pointer to the object t to the archive, so the
/// boost serialization for non-default constructor types is enabled. The
/// method boost::serialization::save_construct_data must be implemented for
/// the type T.
template <typename Archive, typename T>
void saveType(Archive& ar, const T& t, typename std::enable_if<!std::is_default_constructible<T>::value>::type* = 0) {
  const T* ptr = &t;
  ar << ptr;
}

/// Saves in the given archive all the data necessary for reconstructing the
/// given GridAxis object by using its constructor. The data saved are the
/// name of the axis, followed by the number of its knots, followed by the
/// value of each knot. The knot values must be boost serializable.
/// NOTE: Any changes in this method should be reflected in the
/// load_construct_data method.
template <typename Archive, typename T>
void save_construct_data(Archive& ar, const Euclid::GridContainer::GridAxis<T>* t, const unsigned int) {
  std::string name = t->name();
  ar << name;
  size_t size = t->size();
  ar << size;
  for (size_t i = 0; i < size; ++i) {
    saveType(ar, (*t)[i]);
  }
}

/// Version of the loadType method for types which do have default constructors.
/// It loads the object t from the archive. The boost::serialization::serialize
/// method must be implemented for the type T.
template <typename Archive, typename T>
T loadType(Archive& ar, typename std::enable_if<std::is_default_constructible<T>::value>::type* = 0) {
  T value;
  ar >> value;
  return value;
}

/// Version of the loadType method for types which do not have default
/// constructor. It loads a pointer to the object t from the archive and
/// it uses it to create the returned value. The method
/// boost::serialization::load_construct_data must be implemented for the type
/// T, which must also have a copy constructor.
template <typename Archive, typename T>
T loadType(Archive& ar, typename std::enable_if<!std::is_default_constructible<T>::value>::type* = 0) {
  T* ptr;
  ar >> ptr;
  // We use a unique_ptr to guarantee deletion of the pointer
  std::unique_ptr<T> deleter{ptr};
  T                  value{*deleter};
  return value;
}

/// Loads from the given archive all the data necessary for reconstructing an
/// GridAxis object and constructs a new one where the t pointer points. The
/// data red are the name of the axis, followed by the number of its knots,
/// followed by the value of each knot.
/// NOTE: Any changes in this method should be reflected in the
/// save_construct_data method.
template <typename Archive, typename T>
void load_construct_data(Archive& ar, Euclid::GridContainer::GridAxis<T>* t, const unsigned int) {
  std::string name;
  ar >> name;
  size_t size;
  ar >> size;
  std::vector<T> values;
  for (size_t i = 0; i < size; ++i) {
    T value = loadType<Archive, T>(ar);
    values.push_back(value);
  }
  ::new (t) Euclid::GridContainer::GridAxis<T>(name, values);
}

} /* end of namespace serialization */
} /* end of namespace boost */

#endif /* GRIDCONTAINER_SERIALIZATION_GRIDAXIS_H */
