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
 * @file GridContainer/GridCellManagerTraits.h
 * @date May 13, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef GRIDCONTAINER_GRIDCELLMANAGERTRAITS_H
#define	GRIDCONTAINER_GRIDCELLMANAGERTRAITS_H

#include <vector>
#include <memory>

namespace Euclid {
namespace GridContainer {

/**
 * @class GridCellManagerTraits
 * 
 * @brief Class used by the GridContainer to access the different CellManagers
 * 
 * @details
 * To reduce the requirements of the different GridCellManager which are used by
 * the GridContainer to store the data, the GridContainer class does not directly access the
 * GridCellManager instances, but it uses this trait to redirect all the operations.
 * The default implementation of the trait simply redirects the operations,
 * but, if the API of a manager does not fit the trait, this default behavior
 * can be overridden by declaring a specialization of the trait.
 * 
 * @tparam GridCellManager the manager which keeps the GridContainer data
 */
template<typename GridCellManager>
struct GridCellManagerTraits {
  
  /// The type of the data kept by the GridCellManager
  typedef typename GridCellManager::data_type data_type;
  
  /// The iterator type which is used to iterate through the data kept in the
  /// cell manager
  typedef typename GridCellManager::iterator iterator;
  
  /**
   * Factory which creates a GridCellManager instance with the given number of
   * managed data, which all are set to a default value. The default
   * implementation will try to use a constructor with the size as parameter.
   * 
   * @param size The number of data the manager will contain
   * @return A unique_ptr to the newly constructed GridCellManager
   */
  static std::unique_ptr<GridCellManager> factory(size_t size);
  
  /**
   * Returns the number of data managed by the given GridCellManager. Defaults on
   * calling the constant version of method size() on the GridCellManager instance.
   * 
   * @param cell_manager The GridCellManager to get the size of
   * @return The number of data managed by the GridCellManager
   */
  static size_t size(const GridCellManager& cell_manager);
  
  /**
   * Returns an iterator pointing to the first element managed by the
   * GridCellManager. Defaults on calling the begin() method of the GridCellManager
   * instance.
   * 
   * @param cell_manager the cell manager
   * @return An iterator at the first element
   */
  static iterator begin(GridCellManager& cell_manager);
  
  /**
   * Returns an iterator pointing right after the last element managed by the
   * GridCellManager. Defaults on calling the end() method of the GridCellManager
   * instance.
   * 
   * @param cell_manager the GridCellManager
   * @return An iterator right after the last element
   */
  static iterator end(GridCellManager& cell_manager);
  
  /// Flag which indicates if the GridCellManager is boost serializable. By default
  /// it is set to false. Note that Grids which use CellManagers which have
  /// this flag set to false cannot be serialized.
  static const bool enable_boost_serialize = false;
  
}; // end of GridCellManagerTraits


/**
 * Specialization of the GridCellManagerTraits for vector CellManagers. It uses
 * all the default operations but it changes the serialization flag to true
 * to declare that vector GridCellManager%s can be serialized. Note that the type
 * T of the data managed has to also be serializable.
 * 
 * @tparam T the type of the data kept by the vector
 */
template<typename T>
struct GridCellManagerTraits<std::vector<T>> {
  
  /// The type of the data kept by the GridCellManager
  typedef T data_type;
  
  /// The iterator type which is used to iterate through the data kept in the
  /// cell manager
  typedef typename std::vector<T>::iterator iterator;
  
  /// Returns a vector containing "size" default constructed elements
  static std::unique_ptr<std::vector<T>> factory(size_t size);
  
  /// Returns the size of the vector
  static size_t size(const std::vector<T>& vector);
  
  /// Returns an iterator at the first element of the vector
  static iterator begin(std::vector<T>& vector);
  
  /// Returns an iterator right after the last element of the vector
  static iterator end(std::vector<T>& vector);
  
  /// Enables boost serialization of Grids using vector%s as GridCellManager%s
  static const bool enable_boost_serialize = true;
  
}; // end of GridCellManagerTraits vector specialization

} // end of namespace GridContainer
} // end of namespace Euclid

#include "GridContainer/_impl/GridCellManagerTraits.icpp"

#endif	/* GRIDCONTAINER_GRIDCELLMANAGERTRAITS_H */

