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

/**
 * @file SOM/SOM.h
 * @date 06/21/17
 * @author nikoapos
 */

#ifndef _SOM_SOM_H
#define _SOM_SOM_H

#include "GridContainer/GridCellManagerVectorOfVectors.h"
#include "GridContainer/GridContainer.h"
#include "SOM/Distance.h"
#include "SOM/InitFunc.h"
#include <array>
#include <limits>
#include <tuple>
#include <type_traits>
#include <vector>

namespace Euclid {
namespace SOM {

/**
 * @class SOM
 * @brief
 *
 */
template <typename DistFunc = Distance::L2>
class SOM {

  static_assert(std::is_base_of<Distance::Interface, DistFunc>::value,
                "DistFunc must be a subclass of the Distance::Interface");

public:
  using GridCellManager = GridContainer::GridCellManagerVectorOfVectors<double>;
  using CellGridType    = GridContainer::GridContainer<GridCellManager, std::size_t, std::size_t>;
  using iterator        = typename CellGridType::iterator;
  using const_iterator  = typename CellGridType::const_iterator;
  using reference_type  = typename CellGridType::reference_type;

  SOM(std::size_t nd, std::size_t x, std::size_t y, InitFunc::Signature init_func = InitFunc::zero);

  SOM(SOM<DistFunc>&&) = default;
  SOM& operator=(SOM<DistFunc>&&) = default;

  /**
   * @brief Destructor
   */
  virtual ~SOM() = default;

  reference_type operator()(std::size_t x, std::size_t y);

  const reference_type operator()(std::size_t x, std::size_t y) const;

  const std::pair<std::size_t, std::size_t>& getSize() const;

  std::size_t getDimensions() const;

  iterator begin();

  iterator end();

  const_iterator begin() const;

  const_iterator end() const;

  const_iterator cbegin();

  const_iterator cend();

  std::tuple<std::size_t, std::size_t, double> findBMU(const std::vector<double>& input) const;

  std::tuple<std::size_t, std::size_t, double> findBMU(const std::vector<double>& input,
                                                       const std::vector<double>& uncertainties) const;

  template <typename InputType, typename WeightFunc>
  std::tuple<std::size_t, std::size_t, double> findBMU(const InputType& input, WeightFunc weight_func) const;

  template <typename InputType, typename WeightFunc, typename UncertaintyFunc>
  std::tuple<std::size_t, std::size_t, double> findBMU(const InputType& input, WeightFunc weight_func,
                                                       UncertaintyFunc uncertainty_func) const;

private:
  std::size_t                         m_dimensions;
  CellGridType                        m_cells;
  std::pair<std::size_t, std::size_t> m_size;

}; /* End of SOM class */

} /* namespace SOM */
} /* namespace Euclid */

#include "SOM/_impl/SOM.icpp"

#endif
