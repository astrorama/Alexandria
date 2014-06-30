/** 
 * @file ChMatrix/serialization/tuple.h
 * @date May 16, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATRIX_SERIALIZATION_TUPLE_H
#define	CHMATRIX_SERIALIZATION_TUPLE_H

#include <tuple>
#include <type_traits>
#include <memory>
#include <boost/serialization/split_free.hpp>

namespace boost {
namespace serialization {

/// Class which saves in a boost serialization archive the elements of a tuple
/// in a recursive way. It uses two different ways to save the elements,
/// depending if their type has default constructor or not.
template<size_t N>
struct Save {
  
  /// Version of save for default constructible tuple elements. It just saves
  /// in the archive the element.
  template<typename Archive, typename... Args>
  static void save(Archive& ar, const std::tuple<Args...>& t, const unsigned int version,
                          typename std::enable_if<std::is_default_constructible<typename std::tuple_element<N-1, std::tuple<Args...>>::type>::value>::type* = 0) {
    ar << std::get<N-1>(t);
    Save<N-1>::save(ar, t, version);
  }
  
  /// Version of save for non default constructible tuple elements. It saves
  /// in the archive a pointer to the element, to enable the boost serialization
  /// non default constructor support. These objects must be read as pointers.
  template<typename Archive, typename... Args>
  static void save(Archive& ar, const std::tuple<Args...>& t, const unsigned int version,
                          typename std::enable_if<!std::is_default_constructible<typename std::tuple_element<N-1, std::tuple<Args...>>::type>::value>::type* = 0) {
    // Do NOT delete this pointer! It points in the element of the tuple and
    // the tuple will take care of the memory management
    typename std::remove_reference<decltype(std::get<N-1>(t))>::type* ptr = &std::get<N-1>(t);
    ar << ptr;
    Save<N-1>::save(ar, t, version);
  }
};

/// Class which defines the end of the recursion when saving the elements of
/// a tuple in a boost archive.
template<>
struct Save<0> {
  /// This method does nothing. It exists to break the recursion.
  template<typename Archive, typename... Args>
  static void save(Archive&, const std::tuple<Args...>&, const unsigned int) { }
};

/// Class which loads from a boost serialization archive the elements of a tuple
/// in a recursive way. It uses two different ways to load the elements,
/// depending if their type has default constructor or not. Note that non
/// default constructible elements must have a copy assignment operator.
template<size_t N>
struct Load {
  
  /// Version of load for default constructible tuple elements. It just loads
  /// from the archive the element into the default constructed element of the
  /// tuple.
  template<typename Archive, typename... Args>
  static void load(Archive& ar, std::tuple<Args...>& t, const unsigned int version,
                          typename std::enable_if<std::is_default_constructible<typename std::tuple_element<N-1, std::tuple<Args...>>::type>::value>::type* = 0) {
    ar >> std::get<N-1>(t);
    Load<N-1>::load(ar, t, version);
  }
  
  /// Version of load for non default constructible tuple elements. It reads
  /// from the archive a pointer to enable the boost non default constructor
  /// mechanisms and then it uses the copy assignment operator to move the
  /// just red object in the tuple.
  template<typename Archive, typename... Args>
  static void load(Archive& ar, std::tuple<Args...>& t, const unsigned int version,
                          typename std::enable_if<!std::is_default_constructible<typename std::tuple_element<N-1, std::tuple<Args...>>::type>::value>::type* = 0) {
    typedef typename std::remove_reference<decltype(std::get<N-1>(t))>::type ElementType;
    ElementType* ptr;
    ar >> ptr;
    // We use a unique_ptr to guarantee deletion of the pointer
    std::unique_ptr<ElementType> deleter {ptr};
    std::get<N-1>(t) = *deleter;
    Load<N-1>::load(ar, t, version);
  }
};

/// Class which defines the end of the recursion when loading the elements of
/// a tuple in a boost archive.
template<>
struct Load<0> {
  /// This method does nothing. It exists to break the recursion.
  template<typename Archive, typename... Args>
  static void load(Archive&, std::tuple<Args...>&, const unsigned int) { }
};

/// Method which saves a tuple instance to an archive. It uses the Save class
/// to recursively save all the tuple elements.
template<typename Archive, typename... Args>
void save(Archive& ar, const std::tuple<Args...>& t, const unsigned int version) {
  Save<sizeof...(Args)>::save(ar, t, version);
}

/// Method which loads a tuple instance to an archive. It uses the Load class
/// to recursively load all the tuple elements.
template<typename Archive, typename... Args>
void load(Archive& ar, std::tuple<Args...>& t, const unsigned int version) {
  Load<sizeof...(Args)>::load(ar, t, version);
}

/// Method which saves/loads a tuple instance to/from an archive. It uses the
/// split_free method to split the two actions in different methods.
template<typename Archive, typename... Args>
void serialize(Archive& ar, std::tuple<Args...>& t, const unsigned int version) {
  split_free(ar, t, version);
}

} /* end of namespace serialization */
} /* end of namespace boost */

#endif	/* CHMATRIX_SERIALIZATION_TUPLE_H */

