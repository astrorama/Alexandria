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

#include "SOM/NeighborhoodFunc.h"
#include <cmath>

namespace Euclid {
namespace SOM {
namespace NeighborhoodFunc {

Signature linearUnitDisk(double initial_radius) {
  double r_square = initial_radius * initial_radius;
  return [r_square](std::pair<std::size_t, std::size_t> bmu, std::pair<std::size_t, std::size_t> cell, std::size_t iteration,
                    std::size_t total_iterations) -> double {
    double iter_factor = 1.0 * (total_iterations - iteration) / total_iterations;
    iter_factor        = iter_factor * iter_factor;  // We compare the squared distances
    double x           = bmu.first - cell.first;
    double y           = bmu.second - cell.second;
    double dist_square = x * x + y * y;
    if (dist_square < r_square * iter_factor) {
      return 1.;
    } else {
      return 0.;
    }
  };
}

Signature kohonen(std::size_t x_size, std::size_t y_size, double sigma_cutoff_mult) {

  double                                       init_sigma = std::max(x_size, y_size) / 2.;
  std::tuple<std::size_t, std::size_t, double> sigma_buffer{0, 0, 0.};
  double                                       cutoff_mult_square = sigma_cutoff_mult * sigma_cutoff_mult;

  return [init_sigma, sigma_buffer, cutoff_mult_square](std::pair<std::size_t, std::size_t> bmu,
                                                        std::pair<std::size_t, std::size_t> cell, std::size_t iteration,
                                                        std::size_t total_iterations) mutable -> double {
    // If we have new iteration we recompute the sigma, otherwise we use the already
    // calculated one
    if (std::get<0>(sigma_buffer) != iteration || std::get<1>(sigma_buffer) != total_iterations) {
      std::get<0>(sigma_buffer) = iteration;
      std::get<1>(sigma_buffer) = total_iterations;
      double time_constant      = total_iterations / std::log(init_sigma);
      std::get<2>(sigma_buffer) = init_sigma * std::exp(-1. * iteration / time_constant);
    }
    double sigma_square = std::get<2>(sigma_buffer) * std::get<2>(sigma_buffer);

    double x           = static_cast<double>(bmu.first) - cell.first;
    double y           = static_cast<double>(bmu.second) - cell.second;
    double dist_square = x * x + y * y;

    if (dist_square < cutoff_mult_square * sigma_square) {
      return std::exp(-1. * dist_square / (2. * sigma_square));
    } else {
      return 0.;
    }
  };
}

}  // namespace NeighborhoodFunc
}  // namespace SOM
}  // namespace Euclid