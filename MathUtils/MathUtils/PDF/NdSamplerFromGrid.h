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
#include "NdArray/Operations.h"

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

/**
 * Helper function to generate a NdSampler from a GridContainer with a vector of vector of doubles as a cell manager.
 * It works similarly to createSamplerFromGrid, except that the cell content is considered an extra, implicit, axis.
 * @tparam GridAxes
 *  Grid axes
 * @tparam CellAxis
 *  Axis embedded into the cell
 * @details
 *  The compiler should be able to infer the axis types. Example:
 * \code{.cpp}
 * auto sampler = createSamplerFromGrid(grid);
 * \endcode
 *
 * @param grid
 *  The GridContainer
 * @param cell_axis
 *  User-defined knots for the embedded axis
 */
template <typename... GridAxes, typename CellAxis>
std::unique_ptr<NdSampler<GridAxes..., CellAxis>>
createSamplerFromGrid(const GridContainer::GridContainer<std::vector<std::vector<double>>, GridAxes...>& grid,
                      const std::vector<CellAxis>&                                                       cell_axis) {
  auto grid_knots = ExtractKnots<Euclid::_make_index_sequence<sizeof...(GridAxes)>>::extract(grid.getAxesTuple());
  auto pdf_shape  = ExtractKnots<Euclid::_make_index_sequence<sizeof...(GridAxes)>>::extractShape(grid.getAxesTuple());

  // Add one extra
  pdf_shape.push_back(cell_axis.size());
  auto knots = std::tuple_cat(grid_knots, std::make_tuple(cell_axis));

  // Build PDF considering the cell the last axis
  NdArray::NdArray<double> pdf(pdf_shape);
  std::size_t              pdf_i = 0;
  for (auto& cell : grid) {
    assert(cell.size() == cell_axis.size());
    for (auto& cv : cell) {
      auto coords    = NdArray::unravel_index(pdf_i++, pdf_shape);
      pdf.at(coords) = cv;
    }
  }

  return Euclid::make_unique<NdSampler<GridAxes..., CellAxis>>(std::move(knots), std::move(pdf));
}

/**
 * Helper function to generate a NdSampler from a GridContainer with a vector of vector of doubles as a cell manager.
 * It works similarly to createSamplerFromGrid, except that the cell content is considered an extra, implicit, axis.
 * Assumes the embedded axis to be discrete, with its knots being sequential between 0 and the size of the cell.
 *
 * @tparam GridAxes
 *  Grid axes
 */
template <typename... GridAxes>
std::unique_ptr<NdSampler<GridAxes..., std::size_t>>
createSamplerFromGrid(const GridContainer::GridContainer<std::vector<std::vector<double>>, GridAxes...>& grid) {
  auto&                    cell_ref = *grid.begin();
  std::vector<std::size_t> cell_axis(cell_ref.size());
  std::iota(cell_axis.begin(), cell_axis.end(), 0);
  return createSamplerFromGrid(grid, cell_axis);
}

}  // namespace MathUtils
}  // namespace Euclid

#endif  // _FUNCTIONUTILS_NDSAMPLERFROMGRID_H
