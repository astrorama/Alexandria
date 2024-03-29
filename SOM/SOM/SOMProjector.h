/*
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
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

/*
 * @file SOMProjector.h
 * @author nikoapos
 */

#ifndef SOM_SOMPROJECTOR_H
#define SOM_SOMPROJECTOR_H

#include "GridContainer/GridContainer.h"
#include "SOM/SOM.h"
#include <functional>
#include <iterator>

namespace Euclid {
namespace SOM {
class SOMProjector {

public:
  template <typename T>
  using ProjectGrid = GridContainer::GridContainer<std::vector<T>, std::size_t, std::size_t>;

  template <typename T, typename DistFunc, typename InputIter, typename WeightFunc, typename AdderFunc>
  static ProjectGrid<T> project(const SOM<DistFunc>& som, InputIter begin, InputIter end, WeightFunc weight_func,
                                AdderFunc adder_func, const T& init_cell = T{});

  template <typename T, typename DistFunc, typename InputIter, typename WeightFunc, typename UncertaintyFunc,
            typename AdderFunc>
  static ProjectGrid<T> project(const SOM<DistFunc>& som, InputIter begin, InputIter end, WeightFunc weight_func,
                                UncertaintyFunc uncertainty_func, AdderFunc adder_func, const T& init_cell = T{});
};

}  // namespace SOM
}  // namespace Euclid

#include "SOM/_impl/SOMProjector.icpp"

#endif /* SOM_SOMPROJECTOR_H */
