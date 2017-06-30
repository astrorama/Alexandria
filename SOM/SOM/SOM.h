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
 * @file SOM/SOM.h
 * @date 06/21/17
 * @author nikoapos
 */

#ifndef _SOM_SOM_H
#define _SOM_SOM_H

#include <vector>
#include <array>
#include <limits>
#include <type_traits>
#include "GridContainer/GridContainer.h"
#include "SOM/InitFunc.h"
#include "SOM/Distance.h"

namespace Euclid {
namespace SOM {

/**
 * @class SOM
 * @brief
 *
 */
template <std::size_t ND, typename DistFunc=Distance::L2<ND>>
class SOM {
  
  static_assert(std::is_base_of<Distance::Interface<ND>, DistFunc>::value,
          "DistFunc must be a subclass of the Distance::Interface<ND>");

public:
  
  using CellGridType = GridContainer::GridContainer<std::vector<std::array<double, ND>>, std::size_t, std::size_t>;
  using iterator = typename CellGridType::iterator;
  using const_iterator = typename CellGridType::const_iterator;
  
  SOM(std::size_t x, std::size_t y, InitFunc::Signature init_func=InitFunc::zero);

  /**
   * @brief Destructor
   */
  virtual ~SOM() = default;
  
  std::array<double, ND>& operator()(std::size_t x, std::size_t y);
  
  const std::array<double, ND>& operator()(std::size_t x, std::size_t y) const;
  
  const std::pair<std::size_t, std::size_t>& getSize() const;
  
  iterator begin();
  
  iterator end();
  
  const_iterator begin() const;
  
  const_iterator end() const;
  
  const_iterator cbegin();
  
  const_iterator cend();
  
  std::pair<std::size_t, std::size_t> findBMU(const std::array<double, ND>& input) const;
  
  std::pair<std::size_t, std::size_t> findBMU(const std::array<double, ND>& input,
                                              const std::array<double, ND>& uncertainties) const;
  
  template <typename InputType, typename WeightFunc>
  std::pair<std::size_t, std::size_t> findBMU(const InputType& input,
                                              WeightFunc weight_func) const;
  
  template <typename InputType, typename WeightFunc, typename UncertaintyFunc>
  std::pair<std::size_t, std::size_t> findBMU(const InputType& input,
                                              WeightFunc weight_func,
                                              UncertaintyFunc uncertainty_func) const;

private:
  
  CellGridType m_cells;
  std::pair<std::size_t, std::size_t> m_size;

}; /* End of SOM class */

} /* namespace SOM */
} /* namespace Euclid */

#include "SOM/_impl/SOM.icpp"

#endif
