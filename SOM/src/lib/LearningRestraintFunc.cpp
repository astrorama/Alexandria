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

#include "SOM/LearningRestraintFunc.h"
#include <cmath>

namespace Euclid {
namespace SOM {
namespace LearningRestraintFunc {

Signature linear() {
  return [](std::size_t iteration, std::size_t total_iterations) -> double {
    return 1.0 * (total_iterations - iteration) / total_iterations;
  };
}

Signature exponentialDecay(double initial_rate) {
  return [initial_rate](std::size_t iteration, std::size_t total_iterations) -> double {
    return initial_rate * std::exp(-1. * iteration / total_iterations);
  };
}

}  // namespace LearningRestraintFunc
}  // namespace SOM
}  // namespace Euclid
