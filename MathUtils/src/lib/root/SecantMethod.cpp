/*
 * Copyright (C) 2022 Euclid Science Ground Segment
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

#include "MathUtils/root/SecantMethod.h"

namespace Euclid {
namespace MathUtils {

std::pair<double, SecantEndReason> secantMethod(const Function& func, double x0, double x1,
                                                const SecantParams& params) {
  for (std::size_t i = 0; i < params.max_iter; ++i) {
    double y1 = func(x1);
    if (y1 == 0.) {
      return std::make_pair(x1, SecantEndReason::SUCCESS);
    } else if (std::abs(y1) < params.atol) {
      return std::make_pair(x1, SecantEndReason::TOLERANCE);
    }

    double y0 = func(x0);
    double x2 = x1 - y1 * ((x1 - x0) / (y1 - y0));

    if (x2 <= params.min) {
      return std::make_pair(params.min, SecantEndReason::FAILED);
    }
    if (x2 >= params.max) {
      return std::make_pair(params.max, SecantEndReason::FAILED);
    }
    x0 = x1;
    x1 = x2;
  }
  return std::make_pair(x0, SecantEndReason::MAX_ITER);
}

}  // namespace MathUtils
}  // namespace Euclid
