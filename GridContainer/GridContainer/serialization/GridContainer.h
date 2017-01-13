/** 
 * 
 * @file GridContainer/serialization/GridContainer.h
 * @date May 17, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef GRIDCONTAINER_SERIALIZATION_GRIDCONTAINER_H
#define	GRIDCONTAINER_SERIALIZATION_GRIDCONTAINER_H

#include <type_traits>
#include <memory>
#include <boost/serialization/vector.hpp>
#include <boost/serialization/split_free.hpp>
#include "GridContainer/GridAxis.h"
#include "GridContainer/GridContainer.h"
#include "GridContainer/serialization/tuple.h"
#include "GridContainer/serialization/GridAxis.h"

namespace boost {
namespace serialization {

/// Method which saves a GridContainer instance to an archive. This version handles 
/// default constructible cell values.
template<class Archive, typename GridCellManager, typename... AxesTypes>
void save(Archive& ar, const Euclid::GridContainer::GridContainer<GridCellManager,AxesTypes...>& grid, const unsigned int,
               typename std::enable_if<std::is_default_constructible<typename Euclid::GridContainer::GridCellManagerTraits<GridCellManager>::data_type>::value>::type* = 0) {
  for (auto& cell : grid) {
    ar << cell;
  }
}

/// Method which saves a GridContainer instance to an archive. This version handles 
/// non-default constructible cell values.
template<class Archive, typename GridCellManager, typename... AxesTypes>
void save(Archive& ar, const Euclid::GridContainer::GridContainer<GridCellManager,AxesTypes...>& grid, const unsigned int,
               typename std::enable_if<!std::is_default_constructible<typename Euclid::GridContainer::GridCellManagerTraits<GridCellManager>::data_type>::value>::type* = 0) {
  for (auto& cell : grid) {
    // Do NOT delete this pointer! It points to the cell of the grid and the
    // grid will take care of the memory management
    typename std::remove_reference<decltype(cell)>::type* ptr = &cell;
    ar << ptr;
  }
}

/// Method which loads a GridContainer instance from an archive. This version handles 
/// default constructible cell values.
template<class Archive, typename GridCellManager, typename... AxesTypes>
void load(Archive& ar, Euclid::GridContainer::GridContainer<GridCellManager,AxesTypes...>& grid, const unsigned int,
               typename std::enable_if<std::is_default_constructible<typename Euclid::GridContainer::GridCellManagerTraits<GridCellManager>::data_type>::value>::type* = 0) {
  for (auto& cell : grid) {
    ar >> cell;
  }
}

/// Method which loads a GridContainer instance from an archive. This version handles 
/// non-default constructible cell values.
template<class Archive, typename GridCellManager, typename... AxesTypes>
void load(Archive& ar, Euclid::GridContainer::GridContainer<GridCellManager,AxesTypes...>& grid, const unsigned int,
               typename std::enable_if<!std::is_default_constructible<typename Euclid::GridContainer::GridCellManagerTraits<GridCellManager>::data_type>::value>::type* = 0) {
  for (auto& cell : grid) {
    typename Euclid::GridContainer::GridCellManagerTraits<GridCellManager>::data_type* ptr;
    ar >> ptr;
    // We use a unique_ptr to guarantee deletion of the pointer
    std::unique_ptr<typename Euclid::GridContainer::GridCellManagerTraits<GridCellManager>::data_type> deleter {ptr};
    cell = *deleter;
  }
}

/// Method which saves/loads a GridContainer instance to/from an archive. It does a
/// check that the GridCellManager of the GridContainer allows for boost serialization.
/// This check is done in compilation time. After the check the save/load action
/// is delegated to the save and load methods.
template<class Archive, typename GridCellManager, typename... AxesTypes>
void serialize(Archive& ar, Euclid::GridContainer::GridContainer<GridCellManager,AxesTypes...>& grid, const unsigned int version) {
  static_assert(Euclid::GridContainer::GridCellManagerTraits<GridCellManager>::enable_boost_serialize,
                "Boost serialization of GridContainer with unsupported GridCellManager");
  split_free(ar, grid, version);
}

/// Saves in the given archive all the data necessary for reconstructing the
/// given GridContainer by using its constructor. The data saved is the axes tuple.
/// The cell data are handled in the serialize method.
/// NOTE: Any changes in this method should be reflected in the
/// load_construct_data method.
template<class Archive, typename GridCellManager, typename... AxesTypes>
void save_construct_data(Archive& ar, const Euclid::GridContainer::GridContainer<GridCellManager,AxesTypes...>* t,
                                const unsigned int) {
  std::tuple<Euclid::GridContainer::GridAxis<AxesTypes>...> axes_tuple = t->getAxesTuple();
  ar << axes_tuple;
}

/// Helper method which constructs an GridAxis object with empty name and
/// zero knots.
template <typename T>
Euclid::GridContainer::GridAxis<T> emptyGridAxis() {
  return {"", {}};
}

/// Loads from the given archive all the data necessary for reconstructing a
/// GridContainer object and constructs a new one where the t pointer points. The
/// data red are the axes tuple and the GridCellManager.
/// NOTE: Any changes in this method should be reflected in the
/// save_construct_data method.
template<class Archive, typename GridCellManager, typename... AxesTypes>
void load_construct_data(Archive& ar, Euclid::GridContainer::GridContainer<GridCellManager,AxesTypes...>* t,
                                const unsigned int) {
  // We create a tuple containing empty GridAxis objects. These will be replaced
  // when we read from the stream with the real GridAxis objects. We have to do
  // that because the GridAxis does not have a default constructor.
  std::tuple<Euclid::GridContainer::GridAxis<AxesTypes>...> axes_tuple {(emptyGridAxis<AxesTypes>())...};
  ar >> axes_tuple;
  ::new(t) Euclid::GridContainer::GridContainer<GridCellManager,AxesTypes...>(axes_tuple);
}

} /* end of namespace serialization */
} /* end of namespace boost */

#endif	/* GRIDCONTAINER_SERIALIZATION_GRIDCONTAINER_H */

