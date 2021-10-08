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

#include "MathUtils/regression/LinearRegression.h"
#include <ElementsKernel/Exception.h>

namespace Euclid {
namespace MathUtils {

std::pair<double, double> linearRegression(const std::vector<double>& x, const std::vector<double>& y) {
  if (x.size() != y.size()) {
    throw Elements::Exception("linearRegression: x and y vectors must have the same size");
  }
  if (x.empty()) {
    throw Elements::Exception("linearRegression: Can not do a regression over empty vectors");
  }

  double mean_x = 0;
  double mean_y = 0;

  for (std::size_t index = 0; index < x.size(); ++index) {
    mean_x += x[index];
    mean_y += y[index];
  }

  mean_x /= x.size();
  mean_y /= x.size();

  double nom   = 0;
  double denom = 0;
  for (std::size_t index = 0; index < x.size(); ++index) {
    nom += (x[index] - mean_x) * (y[index] - mean_y);
    denom += (x[index] - mean_x) * (x[index] - mean_x);
  }

  double a = nom / denom;
  double b = mean_y - a * mean_x;

  return std::make_pair(a, b);
}

}  // namespace MathUtils
}  // namespace Euclid