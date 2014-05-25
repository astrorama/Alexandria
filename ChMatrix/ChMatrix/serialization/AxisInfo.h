/** 
 * @file AxisInfo.h
 * @date May 16, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATRIX_SERIALIZATION_AXISINFO_H
#define	CHMATRIX_SERIALIZATION_AXISINFO_H

#include <type_traits>
#include <boost/serialization/utility.hpp>
#include "ChMatrix/AxisInfo.h"

namespace boost {
namespace serialization {

template<typename Archive, typename T>
void serialize(Archive&, ChMatrix::AxisInfo<T>&, const unsigned int) {
  // Nothing here as everything is done with the data passed to the constructor
}

template<typename Archive, typename T>
void saveType(Archive& ar, const T& t, typename std::enable_if<std::is_default_constructible<T>::value>::type* = 0) {
  ar << t;
}

template<typename Archive, typename T>
void saveType(Archive& ar, const T& t, typename std::enable_if<!std::is_default_constructible<T>::value>::type* = 0) {
  const T* ptr = &t;
  ar << ptr;
}

template<typename Archive, typename T>
void save_construct_data(Archive& ar, const ChMatrix::AxisInfo<T>* t,
                                const unsigned int) {
  std::string name = t->name();
  ar << name;
  size_t size = t->size();
  ar << size;
  for (size_t i=0; i<size; ++i) {
    saveType(ar, (*t)[i]);
  }
}

template<typename Archive, typename T>
T loadType(Archive& ar, typename std::enable_if<std::is_default_constructible<T>::value>::type* = 0) {
  T value;
  ar >> value;
  return value;
}

template<typename Archive, typename T>
T loadType(Archive& ar, typename std::enable_if<!std::is_default_constructible<T>::value>::type* = 0) {
  T* ptr;
  ar >> ptr;
  T value {*ptr};
  delete ptr;
  return value;
}

template<typename Archive, typename T>
void load_construct_data(Archive& ar, ChMatrix::AxisInfo<T>* t,
                                const unsigned int) {
  std::string name;
  ar >> name;
  size_t size;
  ar >> size;
  std::vector<T> values;
  for (size_t i=0; i<size; ++i) {
    T value = loadType<Archive, T>(ar);
    values.push_back(value);
  }
  ::new(t) ChMatrix::AxisInfo<T>(name, values);
}

} /* end of namespace serialization */
} /* end of namespace boost */

#endif	/* CHMATRIX_SERIALIZATION_AXISINFO_H */

