/** 
 * @file GridContainer/serialize.h
 * @date May 19, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef GRIDCONTAINER_SERIALIZE_H
#define	GRIDCONTAINER_SERIALIZE_H

#include <iostream>
#include <memory>
#include <boost/archive/binary_iarchive.hpp>
#include <boost/archive/binary_oarchive.hpp>
#include "GridContainer/GridContainer.h"
#include "GridContainer/serialization/GridContainer.h"

namespace Grid {

/**
 * @brief Exports to the given output stream the given grid
 * @details
 * The current implementation uses boost serialization and it requires that
 * the GridCellManager and all the axes values are serializable. Also the
 * GridCellManagerTraits specialization for the specific GridCellManager must have the
 * enable_boost_serialize flag set to true.
 * 
 * Note that if any of the required types is not boost serializable, compilation
 * of this method will fail. Non serializable grids of this type can still 
 * be used if there is no call to this method.
 * 
 * @tparam GridCellManager the type of the cell manager of the GridContainer
 * @tparam AxesTypes the types of the GridContainer axes knot values
 * @param out The stream to write the grid in
 * @param grid The grid to export
 */
template<typename GridCellManager, typename... AxesTypes>
void gridBinaryExport(std::ostream& out, const GridContainer<GridCellManager, AxesTypes...>& grid) {
  // Do NOT delete this pointer!!! It  points to the actual grid
  const GridContainer<GridCellManager, AxesTypes...>* ptr = &grid;
  boost::archive::binary_oarchive boa {out};
  boa << ptr;
}

/**
 * @brief Imports from the given stream a grid
 * @details
 * The current implementation uses boost serialization and it requires that
 * the GridCellManager and all the axes values are serializable. Also the
 * GridCellManagerTraits specialization for the specific GridCellManager must have the
 * enable_boost_serialize flag set to true.
 * 
 * Note that if any of the required types is not boost serializable, compilation
 * of this method will fail. Non serializable grids of this type can still 
 * be used if there is no call to this method.
 * 
 * @tparam GridCellManager the type of the cell manager of the GridContainer
 * @tparam AxesTypes the types of the GridContainer axes knot values
 * @param in The stream to read the grid from
 * @return The grid red from the stream
 */
template<typename GridCellManager, typename... AxesTypes>
GridContainer<GridCellManager, AxesTypes...> gridBinaryImport(std::istream& in) {
  boost::archive::binary_iarchive bia {in};
  // Do NOT delete manually this pointer. It is wrapped with a unique_ptr later.
  GridContainer<GridCellManager, AxesTypes...>* ptr;
  bia >> ptr;
  std::unique_ptr<GridContainer<GridCellManager, AxesTypes...>> matr_ptr {ptr};
  // We move out to the result the grid pointed by the pointer. The unique_ptr
  // will delete the (now empty) pointed object
  return std::move(*matr_ptr);
}

} // end of namespace Grid

#endif	/* GRIDCONTAINER_SERIALIZE_H */

