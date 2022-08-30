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
 * @file NeighborhoodFunc.h
 * @author nikoapos
 */

#ifndef SOM_NEIGHBORHOODFUNC_H
#define SOM_NEIGHBORHOODFUNC_H

#include <ElementsKernel/Export.h>
#include <cmath>
#include <functional>

namespace Euclid {
namespace SOM {
namespace NeighborhoodFunc {

class LinearUnitDisk {
public:
  LinearUnitDisk(double initial_radius) : m_r_square(initial_radius * initial_radius){};

  double operator()(std::pair<std::size_t, std::size_t> bmu, std::pair<std::size_t, std::size_t> cell,
                    std::size_t iteration, std::size_t total_iterations);

private:
  double m_r_square;
};

class Kohonen {
public:
  Kohonen(std::size_t x_size, std::size_t y_size, double sigma_cutoff_mult);

  double operator()(std::pair<std::size_t, std::size_t> bmu, std::pair<std::size_t, std::size_t> cell,
                    std::size_t iteration, std::size_t total_iterations) {
    // If we have new iteration we recompute the sigma, otherwise we use the already
    // calculated one
    if (m_last_iteration != iteration || m_last_total != total_iterations) {
      m_last_iteration           = iteration;
      m_last_total               = total_iterations;
      const double time_constant = static_cast<double>(total_iterations) / m_sigma_log;
      const double sigma         = m_init_sigma * std::exp(-1. * static_cast<double>(iteration) / time_constant);
      m_sigma_square             = sigma * sigma;
    }

    const auto x           = static_cast<double>(static_cast<int>(bmu.first) - static_cast<int>(cell.first));
    const auto y           = static_cast<double>(static_cast<int>(bmu.second) - static_cast<int>(cell.second));
    const auto dist_square = x * x + y * y;

    if (dist_square < m_cutoff_mult_square * m_sigma_square) {
      return std::exp(-1. * dist_square / (2. * m_sigma_square));
    } else {
      return 0.;
    }
  }

private:
  const double m_init_sigma;
  const double m_sigma_log;
  const double m_cutoff_mult_square;
  std::size_t  m_last_iteration = 0;
  std::size_t  m_last_total     = 0;
  double       m_sigma_square   = 0.;
};

}  // namespace NeighborhoodFunc
}  // namespace SOM
}  // namespace Euclid

#endif /* SOM_NEIGHBORHOODFUNC_H */
