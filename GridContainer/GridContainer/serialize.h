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
#include <boost/filesystem.hpp>
#include "GridContainer/GridContainer.h"
#include "GridContainer/serialization/GridContainer.h"

namespace Euclid {
namespace GridContainer {

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
 * @tparam GridType the type of the grid to read from the stream
 * @param in The stream to read the grid from
 * @return The grid red from the stream
 */
template<typename GridType>
GridType gridBinaryImport(std::istream& in) {
  boost::archive::binary_iarchive bia {in};
  // Do NOT delete manually this pointer. It is wrapped with a unique_ptr later.
  GridType* ptr;
  bia >> ptr;
  std::unique_ptr<GridType> matr_ptr {ptr};
  // We move out to the result the grid pointed by the pointer. The unique_ptr
  // will delete the (now empty) pointed object
  return std::move(*matr_ptr);
}

/**
 * @brief Exports a Grid as a FITS file
 * @details
 * The grid cell values are stored in an array HDU. Grids with cell types which
 * are not one of the default FITS array types are not supported (compilation
 * will fail). The name of this HDU is the name given with the parameter hdu_name.
 * 
 * The array HDU is followed with one binary table HDU per grid axis, where the
 * axes knot values are stored. The names of these HDUs are following the
 * format: <AXISNAME>_<hdu_name>, where the hdu_name is the one of the array HDU.
 * Note that the axes knots must be of one of the default FITS binary table types.
 * This behavior can be extended by specializing the GridAxisValueFitsHelper
 * template (this is already done for the XYDataset::QualifiedName).
 * 
 * If the FITS file does not already exist, this method will create it. If it
 * exists, the grid related HDUs will be appended to the file. Note that if the
 * FITS file is being created, the primary HDU is left empty and the array HDU
 * with the grid data is the first extension.
 * 
 * @param filename The FITS file to store the grid
 * @param hdu_name The name of the array HDU
 * @param grid The grid to store
 */
template<typename GridCellManager, typename... AxesTypes>
void gridFitsExport(const boost::filesystem::path& filename,
                    const std::string& hdu_name,
                    const GridContainer<GridCellManager, AxesTypes...>& grid);

/**
 * @brief Imports a Grid from a FITS file
 * @details
 * The FITS file must follow the format as described in the gridFitsExport()
 * documentation. The given HDU index is the index of the array HDU with the
 * grid data.
 * 
 * @param filename The FITS file containing the grid
 * @param hdu_index The index of the array HDU with the grid data
 * @return The grid
 */
template<typename GridType>
GridType gridFitsImport(const boost::filesystem::path& filename, int hdu_index);

} // end of namespace GridContainer
} // end of namespace Euclid

#include "GridContainer/_impl/FitsSerialize.icpp"

#endif	/* GRIDCONTAINER_SERIALIZE_H */

