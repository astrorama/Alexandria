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

#include "SOM/NeighborhoodFunc.h"
#include <algorithm>  // std::max
#include <cmath>

namespace Euclid {
namespace SOM {
namespace NeighborhoodFunc {

double LinearUnitDisk::operator()(std::pair<std::size_t, std::size_t> bmu, std::pair<std::size_t, std::size_t> cell,
                                  std::size_t iteration, std::size_t total_iterations) {
  double iter_factor = 1.0 * static_cast<double>(total_iterations - iteration) / static_cast<double>(total_iterations);
  iter_factor        = iter_factor * iter_factor;  // We compare the squared distances
  auto   x           = static_cast<double>(bmu.first - cell.first);
  auto   y           = static_cast<double>(bmu.second - cell.second);
  double dist_square = x * x + y * y;
  if (dist_square < m_r_square * iter_factor) {
    return 1.;
  } else {
    return 0.;
  }
}

Kohonen::Kohonen(std::size_t x_size, std::size_t y_size, double sigma_cutoff_mult)
    : m_init_sigma(static_cast<double>(std::max(x_size, y_size)) / 2.)
    , m_sigma_log(std::log(m_init_sigma))
    , m_cutoff_mult_square{sigma_cutoff_mult * sigma_cutoff_mult} {}

}  // namespace NeighborhoodFunc
}  // namespace SOM
}  // namespace Euclid
