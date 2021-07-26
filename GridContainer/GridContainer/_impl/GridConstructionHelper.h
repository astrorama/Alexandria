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
 * @file GridContainer/_impl/GridConstructionHelper.h
 * @date May 13, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef GRIDCONTAINER_GRIDCONSTRUCTIONHELPER_H
#define GRIDCONTAINER_GRIDCONSTRUCTIONHELPER_H

#include "GridContainer/GridAxis.h"
#include "TemplateLoopCounter.h"
#include <map>
#include <tuple>
#include <type_traits>
#include <vector>

namespace Euclid {
namespace GridContainer {

/**
 * @class GridConstructionHelper
 *
 * @brief GridContainer construction helper class
 *
 * @brief
 * The GridConstructionHelper is a helper class, which provides functions
 * which use iteration over variadic templates to construct some collections
 * required during the construction of the GridContainer class. It is meant to be
 * used by the GridContainer constructor. For a helper class with similar behavior
 * to be used outside the GridContainer class see the GridIndexHelper class.
 *
 * @tparam Axes the types of the axes
 */
template <typename... Axes>
class GridConstructionHelper {
public:
  /**
   * @brief
   * Creates a vector which contains the sizes of the given axes
   * @details
   * Note that this method is using variadic template iteration by using the
   * second parameter (TemplateLoopCounter). To initiate the iteration the
   * counter must be equal with the number of axes in the tuple.
   *
   * @tparam I the index of the axis until which the results are calculated
   * @param axes A tuple containing the GridAxis objects describing the axes
   * @return A vector containing the sizes of the axes
   */
  template <int I>
  static std::vector<size_t> createAxesSizesVector(const std::tuple<GridAxis<Axes>...>& axes,
                                                   const TemplateLoopCounter<I>&) {
    std::vector<size_t> result{createAxesSizesVector(axes, TemplateLoopCounter<I - 1>{})};
    result.push_back(std::get<I - 1>(axes).size());
    return result;
  }

  /// Method which terminates the iteration when creating the axes sizes vector
  static std::vector<size_t> createAxesSizesVector(const std::tuple<GridAxis<Axes>...>&,
                                                   const TemplateLoopCounter<0>&) {
    return std::vector<size_t>{};
  }

  /**
   * @brief
   * Creates a vector which contains the names of the given axes
   * @details
   * Note that this method is using variadic template iteration by using the
   * second parameter (TemplateLoopCounter). To initiate the iteration the
   * counter must be equal with the number of axes in the tuple.
   *
   * @tparam I the index of the axis until which the results are calculated
   * @param axes A tuple containing the GridAxis objects describing the axes
   * @return A vector containing the names of the axes
   */
  template <int I>
  static std::vector<std::string> createAxesNamesVector(const std::tuple<GridAxis<Axes>...>& axes,
                                                        const TemplateLoopCounter<I>&) {
    std::vector<std::string> result{createAxesNamesVector(axes, TemplateLoopCounter<I - 1>{})};
    result.push_back(std::get<I - 1>(axes).name());
    return result;
  }

  /// Method which terminates the iteration when creating the axes names vector
  static std::vector<std::string> createAxesNamesVector(const std::tuple<GridAxis<Axes>...>&,
                                                        const TemplateLoopCounter<0>&) {
    return std::vector<std::string>{};
  }

  /**
   * @brief
   * Returns the index factor of an axis
   * @details
   * The index factor of an axis is the step needed to be done in the single
   * dimensional array to move to the next element of the axis. It is equal
   * to the multiplication of the sizes of all the axes which have faster
   * iteration rate. Its purpose is to facilitate the conversion of multi-
   * dimensional coordinates to the index of a long array.
   *
   * @tparam I the index of the axis to get the factor for
   * @param axes The axes to use for the calculation
   * @return The index factor of the Ith axis
   */
  template <int I>
  static size_t getAxisIndexFactor(const std::tuple<GridAxis<Axes>...>& axes, const TemplateLoopCounter<I>&) {
    return std::get<I>(axes).size() * getAxisIndexFactor(axes, TemplateLoopCounter<I - 1>{});
  }

  /// Method which terminates the iteration when calculating the axis index factors
  static size_t getAxisIndexFactor(const std::tuple<GridAxis<Axes>...>&, const TemplateLoopCounter<-1>&) {
    return 1;
  }

  /**
   * @brief
   * Creates a vector which contains the index factors of the given axes
   * @details
   * For an explanation of the index factor see the documentation of the
   * getAxisIndexFactor method. The returned vector has size one bigger than
   * the number of axes. The last element contains the total size of the
   * required single dimensional array to keep the data.
   * Note that this method is using variadic template iteration by using the
   * second parameter (TemplateLoopCounter). To initiate the iteration the
   * counter must be equal with the number of axes in the tuple.
   *
   * @tparam I the index of the axis until which the results are calculated
   * @param axes A tuple containing the GridAxis objects describing the axes
   * @return A vector containing the index factors of the axes
   */
  template <int I>
  static std::vector<size_t> createAxisIndexFactorVector(const std::tuple<GridAxis<Axes>...>& axes,
                                                         const TemplateLoopCounter<I>&) {
    std::vector<size_t> result{createAxisIndexFactorVector(axes, TemplateLoopCounter<I - 1>{})};
    result.push_back(getAxisIndexFactor(axes, TemplateLoopCounter<I - 1>{}));
    return result;
  }

  /// Method which terminates the iteration when creating the axes index factors
  static std::vector<size_t> createAxisIndexFactorVector(const std::tuple<GridAxis<Axes>...>&,
                                                         const TemplateLoopCounter<0>&) {
    return std::vector<size_t>{1};
  }

  template <int I>
  static void findAndFixAxis(std::tuple<GridAxis<Axes>...>& axes_tuple, size_t axis, size_t index,
                             const TemplateLoopCounter<I>&) {
    if (axis == I) {
      auto&                                                    old_axis = std::get<I>(axes_tuple);
      typename std::remove_reference<decltype(old_axis)>::type new_axis{old_axis.name(), {old_axis[index]}};
      std::get<I>(axes_tuple) = std::move(new_axis);
      return;
    }
    findAndFixAxis(axes_tuple, axis, index, TemplateLoopCounter<I + 1>{});
  }

  static void findAndFixAxis(std::tuple<GridAxis<Axes>...>&, size_t, size_t,
                             const TemplateLoopCounter<sizeof...(Axes)>&) {
    // does nothing
  }

  template <typename IterType, int I>
  static void fixIteratorAxes(IterType& iter, std::map<size_t, size_t> fix_indices, const TemplateLoopCounter<I>&) {
    auto fix_pair = fix_indices.find(I);
    if (fix_pair != fix_indices.end()) {
      iter.template fixAxisByIndex<I>(fix_pair->second);
    }
    fixIteratorAxes(iter, fix_indices, TemplateLoopCounter<I + 1>{});
  }

  template <typename IterType>
  static void fixIteratorAxes(IterType&, std::map<size_t, size_t>, const TemplateLoopCounter<sizeof...(Axes)>&) {
    // does nothing
  }
};

}  // end of namespace GridContainer
}  // end of namespace Euclid

#endif /* GRIDCONTAINER_GRIDCONSTRUCTIONHELPER_H */
