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

/**
 * @file MathUtils/src/lib/numericalDifferentiation/CentralDifference.cpp
 * @date January 09, 2020
 * @author Alejandro Alvarez Ayllon
 */

#include "MathUtils/numericalDifferentiation/FiniteDifference.h"
#include <cmath>
#include <limits>

namespace Euclid {
namespace MathUtils {

static double guess_h(double initial_h, double x) {
  volatile double xh = x + initial_h;
  volatile double h = xh - x;
  if (h == 0) {
    h = std::nextafter(x, std::numeric_limits<double>::max()) - x;
  }
  return h;
}

double derivative(const Function& f, const double x) {
  double h = std::sqrt(std::numeric_limits<double>::epsilon()) * 2;
  h = guess_h(h, x);

  double yh = f(x + h);
  double y0 = f(x);
  return (yh - y0) / h;
}

double derivative2nd(const Function& f, const double x) {
  double h = std::sqrt(std::sqrt(std::numeric_limits<double>::epsilon())) * 2;
  h = guess_h(h, x);

  double ymh = f(x - h);
  double y = f(x);
  double yph = f(x + h);

  return (yph - 2 * y + ymh) / (h * h);
}

} // end namespace MathUtils
} // end namespace Euclid
