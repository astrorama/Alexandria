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
 * @file MathUtils/src/lib/numericalIntegration/SimpsonsRule.cpp
 * @date July 2, 2015
 * @author Florian Dubath
 */

#include "MathUtils/numericalIntegration/SimpsonsRule.h"
#include "ElementsKernel/Exception.h"
#include <cmath>

namespace Euclid {
namespace MathUtils {

double SimpsonsRule::operator()(const Function& function, double min, double max, int order) {
  if (order < 3) {
    throw Elements::Exception() << "Simpson's Rule integration is define only for order bigger than 2";
  }

  int    N = pow(2, order);
  double h = (max - min) / N;

  double partial_sum = 0;
  for (int i = 3; i < N - 2; i++) {
    partial_sum += function(min + i * h);
  }

  partial_sum += 0.375 * (function(min) + function(max));
  partial_sum += 7. * (function(min + h) + function(max - h)) / 6.;
  partial_sum += 23. * (function(min + 2. * h) + function(max - 2 * h)) / 24.;

  return partial_sum * h;
}

double SimpsonsRule::operator()(const Function& function, double min, double max, double previous_value, int order) {
  if (order < 4) {
    throw Elements::Exception() << "Simpson's Rule integration with recursion is define only for order bigger than 3";
  }

  int    N = pow(2, order);
  double h = (max - min) / N;

  double partial_sum = 0;

  for (int j = 1; j < N / 2 - 1; j++) {
    int i = 2 * j + 1;
    partial_sum += function(min + i * h);
  }

  partial_sum += 7. * (function(min + h) + function(max - h)) / 6.;
  partial_sum -= 5. * (function(min + 2. * h) + function(max - 2. * h)) / 24.;
  partial_sum += (function(min + 4. * h) + function(max - 4. * h)) / 24.;
  return partial_sum * h + previous_value / 2.;
}

}  // namespace MathUtils
}  // end of namespace Euclid
