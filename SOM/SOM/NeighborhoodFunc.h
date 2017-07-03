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

/* 
 * @file NeighborhoodFunc.h
 * @author nikoapos
 */

#ifndef SOM_NEIGHBORHOODFUNC_H
#define SOM_NEIGHBORHOODFUNC_H

#include <functional>

namespace Euclid {
namespace SOM {
namespace NeighborhoodFunc {

using Signature = std::function<double(std::pair<std::size_t, std::size_t> bmu,
                                       std::pair<std::size_t, std::size_t> cell,
                                       std::size_t iteration, std::size_t total_iterations)>;

Signature unitDisk(double initial_radius) {
  double r_square = initial_radius * initial_radius;
  return [r_square](std::pair<std::size_t, std::size_t> bmu,
                    std::pair<std::size_t, std::size_t> cell,
                    std::size_t iteration, std::size_t total_iterations) -> double {
    double iter_factor = 1.0 * (total_iterations - iteration) / total_iterations;
    iter_factor = iter_factor * iter_factor; // We compare the squared distances
    double x = bmu.first - cell.first;
    double y = bmu.second - cell.second;
    double dist_square = x * x + y * y;
    if (dist_square < r_square * iter_factor) {
      return 1.;
    } else {
      return 0.;
    }
  };
}

}
}
}

#endif /* SOM_NEIGHBORHOODFUNC_H */

