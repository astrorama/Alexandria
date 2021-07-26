/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
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
 * @file GridContainer/GridIndexHelper.h
 * @date May 15, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef GRIDCONTAINER_GRIDINDEXHELPER_H
#define GRIDCONTAINER_GRIDINDEXHELPER_H

#include "GridContainer/GridAxis.h"
#include "GridContainer/_impl/GridConstructionHelper.h"
#include <tuple>
#include <vector>

namespace Euclid {
namespace GridContainer {

/**
 * @class GridIndexHelper
 *
 * @brief Helper class for converting multi-dimensional grid coordinates to
 * the index of a long data array and vice versa
 *
 * @details
 * The assumption for the mapping is that the first axis is assumed to vary the
 * fastest and the last the slowest. All indices and coordinates are zero
 * based (start from zero). This class exists mainly to be
 * used internally for the GridContainer iterator operations, but it is considered
 * part of the public interface of the GridContainer module and can be used by
 * any class which wants to perform such conversions. Use of this class in
 * such cases is recommended for performance reasons.
 *
 * @tparam AxesTypes The types of the GridContainer axes
 */
template <typename... AxesTypes>
class GridIndexHelper {

public:
  /**
   * Constructs a new GridIndexHelper instance for making conversions for
   * a GridContainer with the given axes. For avoiding the long template syntax
   * consider using the makeGridIndexHelper() factory method instead.
   *
   * @param axes_tuple The information about the axes of the GridContainer
   */
  explicit GridIndexHelper(const std::tuple<GridAxis<AxesTypes>...>& axes_tuple);

  /// Default move constructor and assignment operator
  GridIndexHelper(GridIndexHelper<AxesTypes...>&&) = default;
  GridIndexHelper& operator=(GridIndexHelper<AxesTypes...>&&) = default;

  /// Default destructor
  virtual ~GridIndexHelper() = default;

  /**
   * Returns the coordinate of the GridContainer axis with the given index which
   * corresponds to the given index of a one dimensional array containing all
   * the GridContainer elements.
   *
   * @param axis The axis to get the index for
   * @param array_index The index of the one dimensional array
   * @return the coordinate of the axis
   */
  size_t axisIndex(size_t axis, size_t array_index) const;

  /**
   * Returns the index of a one dimensional array which corresponds to the
   * given GridContainer coordinates. This method does not perform any bound checks.
   *
   * @param coords The GridContainer coordinates
   * @return the one dimensional array index
   */
  size_t totalIndex(decltype(std::declval<GridAxis<AxesTypes>>().size())... coords) const;

  /**
   * Returns the index of a one dimensional array which corresponds to the
   * given GridContainer coordinates. This method performs bound checks.
   *
   * @param coords The GridContainer coordinates
   * @return the one dimensional array index
   * @throws Elements::Exception
   *    if any coordinate is out of bound
   */
  size_t totalIndexChecked(decltype(std::declval<GridAxis<AxesTypes>>().size())... coords) const;

  /// Checks if any of the given coordinates is fixed and not zero
  template <typename Coord>
  void checkAllFixedAreZero(const std::map<size_t, size_t>& fixed_indices, Coord coord) const;

  /// Checks if any of the given coordinates is fixed and not zero
  template <typename Coord, typename... RestCoords>
  void checkAllFixedAreZero(const std::map<size_t, size_t>& fixed_indices, Coord coord,
                            RestCoords... rest_coords) const;

  std::vector<size_t>      m_axes_sizes;
  std::vector<size_t>      m_axes_index_factors;
  std::vector<std::string> m_axes_names;
};

/**
 * Factory method for simplifying the creation of GridIndexHelper instances.
 * It is equivalent with using the constructor by specifying the AxesTypes
 * template parameters.
 *
 * @tparam AxesTypes the types of the GridContainer axes
 * @param axes_tuple the information of the GridContainer axes
 * @return The GridIndexHelper instance
 */
template <typename... AxesTypes>
GridIndexHelper<AxesTypes...> makeGridIndexHelper(const std::tuple<GridAxis<AxesTypes>...>& axes_tuple) {
  return GridIndexHelper<AxesTypes...>(axes_tuple);
}

}  // end of namespace GridContainer
}  // end of namespace Euclid

#include "GridContainer/_impl/GridIndexHelper.icpp"

#endif /* GRIDCONTAINER_GRIDINDEXHELPER_H */
