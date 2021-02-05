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

/**
 * @file src/lib/interpolation/linear.cpp
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#include "ElementsKernel/Exception.h"
#include "MathUtils/function/Piecewise.h"
#include "MathUtils/function/Polynomial.h"
#include "MathUtils/interpolation/interpolation.h"
#include <limits>

namespace Euclid {
namespace MathUtils {

std::unique_ptr<Function> linearInterpolation(const std::vector<double>& x, const std::vector<double>& y, bool extrapolate) {
  std::vector<std::shared_ptr<Function>> functions{};
  for (size_t i = 0; i < x.size() - 1; i++) {
    double coef1 = (y[i + 1] - y[i]) / (x[i + 1] - x[i]);
    double coef0 = y[i] - coef1 * x[i];
    functions.push_back(std::shared_ptr<Function>(new Polynomial{{coef0, coef1}}));
  }

  if (extrapolate) {
    std::vector<double> x_copy(x);
    x_copy.front() = std::numeric_limits<double>::lowest();
    x_copy.back()  = std::numeric_limits<double>::max();
    return std::unique_ptr<Function>(new Piecewise{x_copy, std::move(functions)});
  }

  return std::unique_ptr<Function>(new Piecewise{x, std::move(functions)});
}

}  // namespace MathUtils
}  // end of namespace Euclid
