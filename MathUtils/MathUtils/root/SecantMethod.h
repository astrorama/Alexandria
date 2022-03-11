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

#ifndef _FUNCTIONUTILS_SECANTMETHOD_H
#define _FUNCTIONUTILS_SECANTMETHOD_H

#include "MathUtils/function/Function.h"
#include <limits>

namespace Euclid {
namespace MathUtils {

enum class SecantEndReason { SUCCESS, MAX_ITER, GRADIENT, OUT_OF_BOUNDS, VALUE_ERROR };

struct SecantParams {
  std::size_t max_iter = 1000;
  double      atol     = 1e-8;
  double      min      = -std::numeric_limits<double>::infinity();
  double      max      = std::numeric_limits<double>::infinity();
};

struct SecantReturn {
  double          root;
  SecantEndReason reason;
  std::size_t     iterations;
};

SecantReturn secantMethod(const Function& func, double x0, double x1, const SecantParams& params = SecantParams{});

}  // namespace MathUtils
}  // namespace Euclid

#endif  // _FUNCTIONUTILS_SECANTMETHOD_H