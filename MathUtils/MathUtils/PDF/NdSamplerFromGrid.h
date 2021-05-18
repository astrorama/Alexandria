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

#ifndef _FUNCTIONUTILS_NDSAMPLERFROMGRID_H
#define _FUNCTIONUTILS_NDSAMPLERFROMGRID_H

#include "GridContainer/GridContainer.h"
#include "NdArray/NdArray.h"

namespace Euclid {
namespace MathUtils {

template <typename Seq>
struct ExtractKnots {};

template <std::size_t... Is>
struct ExtractKnots<Euclid::_index_sequence<Is...>> {
  template <typename... Axes>
  static std::tuple<std::vector<Axes>...> extract(const std::tuple<GridContainer::GridAxis<Axes>...>& axes) {
    return std::tuple<std::vector<Axes>...>{{std::get<Is>(axes).begin(), std::get<Is>(axes).end()}...};
  }

  template <typename... Axes>
  static std::vector<std::size_t> extractShape(const std::tuple<GridContainer::GridAxis<Axes>...>& axes) {
    return std::vector<std::size_t>{std::get<Is>(axes).size()...};
  }
};

/**
 * Helper function to generate a NdSampler from a GridContainer with a vector of double as a cell manager
 * @tparam Axes
 *  Grid axes
 * @details
 *  The compiler should be able to infer the axis types. Example:
 * \code{.cpp}
 * auto sampler = createSamplerFromGrid(grid);
 * \endcode
 */
template <typename... Axes>
std::unique_ptr<NdSampler<Axes...>> createSamplerFromGrid(const GridContainer::GridContainer<std::vector<double>, Axes...>& grid) {
  auto knots     = ExtractKnots<Euclid::_make_index_sequence<sizeof...(Axes)>>::extract(grid.getAxesTuple());
  auto pdf_shape = ExtractKnots<Euclid::_make_index_sequence<sizeof...(Axes)>>::extractShape(grid.getAxesTuple());
  NdArray::NdArray<double> pdf(pdf_shape, grid.begin(), grid.end());
  return Euclid::make_unique<NdSampler<Axes...>>(std::move(knots), std::move(pdf));
}

}  // namespace MathUtils
}  // namespace Euclid

#endif  // _FUNCTIONUTILS_NDSAMPLERFROMGRID_H
