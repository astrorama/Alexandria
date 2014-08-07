/** 
 * @file GridContainer/serialization/GridContainer.h
 * @date May 17, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef GRIDCONTAINER_SERIALIZATION_GRIDCONTAINER_H
#define	GRIDCONTAINER_SERIALIZATION_GRIDCONTAINER_H

#include <type_traits>
#include <memory>
#include <boost/serialization/vector.hpp>
#include "GridContainer/GridAxis.h"
#include "GridContainer/GridContainer.h"
#include "GridContainer/serialization/tuple.h"
#include "GridContainer/serialization/GridAxis.h"

namespace boost {
namespace serialization {

/// Method which saves/loads a GridContainer instance to/from an archive. It does a
/// check that the GridCellManager of the GridContainer allows for boost serialization.
/// This check is done in compilation time.
template<class Archive, typename GridCellManager, typename... AxesTypes>
void serialize(Archive&, Grid::GridContainer<GridCellManager,AxesTypes...>&, const unsigned int) {
  static_assert(Grid::GridCellManagerTraits<GridCellManager>::enable_boost_serialize,
                "Boost serialization of GridContainer with unsupported GridCellManager");
}

/// Saves in the given archive all the data necessary for recunstructing the
/// given GridContainer by using its constructor. The data saved are the axes tuple
/// and a pointer to the GridCellManager.
/// NOTE: Any changes in this method should be reflected in the
/// load_construct_data method.
template<class Archive, typename GridCellManager, typename... AxesTypes>
void save_construct_data(Archive& ar, const Grid::GridContainer<GridCellManager,AxesTypes...>* t,
                                const unsigned int) {
  std::tuple<Grid::GridAxis<AxesTypes>...> axes_tuple = t->getAxesTuple();
  ar << axes_tuple;
  // Do NOT delete this pointer!!! It points to the GridCellManager of the grid
  const GridCellManager* cell_manager_ptr = &(t->getCellManager());
  ar << cell_manager_ptr;
}

/// Helper method which constructs an GridAxis object with empty name and
/// zero knots.
template <typename T>
Grid::GridAxis<T> emptyGridAxis() {
  return {"", {}};
}

/// Loads from the given archive all the data necessary for reconstructing a
/// GridContainer object and constructs a new one where the t pointer points. The
/// data red are the axes tuple and the GridCellManager.
/// NOTE: Any changes in this method should be reflected in the
/// save_construct_data method.
template<class Archive, typename GridCellManager, typename... AxesTypes>
void load_construct_data(Archive& ar, Grid::GridContainer<GridCellManager,AxesTypes...>* t,
                                const unsigned int) {
  // We create a tuple containing empty GridAxis objects. These will be replaced
  // when we read from the stream with the real GridAxis objects. We have to do
  // that because the GridAxis does not have a default constructor.
  std::tuple<Grid::GridAxis<AxesTypes>...> axes_tuple {(emptyGridAxis<AxesTypes>())...};
  ar >> axes_tuple;
  GridCellManager* cell_manager;
  ar >> cell_manager;
  std::unique_ptr<GridCellManager> ptr {cell_manager};
  ::new(t) Grid::GridContainer<GridCellManager,AxesTypes...>(std::move(ptr), axes_tuple);
}

} /* end of namespace serialization */
} /* end of namespace boost */

#endif	/* GRIDCONTAINER_SERIALIZATION_GRIDCONTAINER_H */

