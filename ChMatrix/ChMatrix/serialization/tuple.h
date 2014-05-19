/** 
 * @file tuple.h
 * @date May 16, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATRIX_SERIALIZATION_TUPLE_H
#define	CHMATRIX_SERIALIZATION_TUPLE_H

#include <tuple>
#include <type_traits>
#include <memory>
#include <boost/serialization/split_free.hpp>
#include <boost/shared_ptr.hpp>
#include <boost/serialization/shared_ptr.hpp>

#include <iostream>

namespace boost {
namespace serialization {

template<size_t N>
struct Save {
  
  template<typename Archive, typename... Args>
  static void save(Archive& ar, const std::tuple<Args...>& t, const unsigned int version,
                          typename std::enable_if<std::is_default_constructible<typename std::tuple_element<N-1, std::tuple<Args...>>::type>::value>::type* = 0) {
    ar << std::get<N-1>(t);
    Save<N-1>::save(ar, t, version);
  }
  
  template<typename Archive, typename... Args>
  static void save(Archive& ar, const std::tuple<Args...>& t, const unsigned int version,
                          typename std::enable_if<!std::is_default_constructible<typename std::tuple_element<N-1, std::tuple<Args...>>::type>::value>::type* = 0) {
    // Here we have an element of the tuple which is not default constructible.
    // This means we have to load it as a pointer. To not have memory leaks we
    // store it as a boost::shared_ptr (STL pointers are not supported by boost
    // serialization) so we can read from the stream a shared_ptr. Note that we
    // create a new object in the heap by using the copy constructor. This object
    // will be deleted after this method exits, but the one in the tuple will not.
    boost::shared_ptr<typename std::tuple_element<N-1, std::tuple<Args...>>::type> ptr {new typename std::tuple_element<N-1, std::tuple<Args...>>::type(std::get<N-1>(t))};
    ar << ptr;
    Save<N-1>::save(ar, t, version);
  }
};

template<>
struct Save<0> {
  template<typename Archive, typename... Args>
  static void save(Archive&, const std::tuple<Args...>&, const unsigned int) { }
};

template<size_t N>
struct Load {
  
  template<typename Archive, typename... Args>
  static void load(Archive& ar, std::tuple<Args...>& t, const unsigned int version,
                          typename std::enable_if<std::is_default_constructible<typename std::tuple_element<N-1, std::tuple<Args...>>::type>::value>::type* = 0) {
    ar >> std::get<N-1>(t);
    Load<N-1>::load(ar, t, version);
  }
  
  template<typename Archive, typename... Args>
  static void load(Archive& ar, std::tuple<Args...>& t, const unsigned int version,
                          typename std::enable_if<!std::is_default_constructible<typename std::tuple_element<N-1, std::tuple<Args...>>::type>::value>::type* = 0) {
    // We read the object in a shared_ptr and then we copy it in the tuple. The
    // shared_ptr will delete the extra copy in the heap.
    boost::shared_ptr<typename std::tuple_element<N-1, std::tuple<Args...>>::type> ptr;
    ar >> ptr;
    std::get<N-1>(t) = *ptr;
    Load<N-1>::load(ar, t, version);
  }
};

template<>
struct Load<0> {
  template<typename Archive, typename... Args>
  static void load(Archive&, std::tuple<Args...>&, const unsigned int) { }
};

template<typename Archive, typename... Args>
void save(Archive& ar, const std::tuple<Args...>& t, const unsigned int version) {
  Save<sizeof...(Args)>::save(ar, t, version);
}

template<typename Archive, typename... Args>
void load(Archive& ar, std::tuple<Args...>& t, const unsigned int version) {
  Load<sizeof...(Args)>::load(ar, t, version);
}

template<typename Archive, typename... Args>
void serialize(Archive& ar, std::tuple<Args...>& t, const unsigned int version) {
  split_free(ar, t, version);
}

} /* end of namespace serialization */
} /* end of namespace boost */

#endif	/* CHMATRIX_SERIALIZATION_TUPLE_H */

