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
#include <cmath>

namespace Euclid {
namespace MathUtils {

SecantReturn secantMethod(const Function& func, double x0, double x1, const SecantParams& params) {
  SecantReturn ret{x0, SecantEndReason::SUCCESS, 0};

  double y0 = func(x0);

  if (!std::isfinite(y0)) {
    return {x0, SecantEndReason::VALUE_ERROR, 0};
  }

  for (ret.iterations = 0; ret.iterations < params.max_iter; ++ret.iterations) {
    if (std::abs(y0) <= params.atol) {
      break;
    }

    double y1 = func(x1);
    if (!std::isfinite(y1)) {
      ret.reason = SecantEndReason::VALUE_ERROR;
      break;
    }
    if (y1 == y0) {
      ret.reason = SecantEndReason::GRADIENT;
      break;
    }

    double x2 = x1 - y1 * ((x1 - x0) / (y1 - y0));

    if (x2 <= params.min) {
      ret.root   = params.min;
      ret.reason = SecantEndReason::OUT_OF_BOUNDS;
      break;
    } else if (x2 >= params.max) {
      ret.root   = params.max;
      ret.reason = SecantEndReason::OUT_OF_BOUNDS;
      break;
    }
    x0       = x1;
    x1       = x2;
    y0       = y1;
    ret.root = x0;
  }
  return ret;
}

}  // namespace MathUtils
}  // namespace Euclid
