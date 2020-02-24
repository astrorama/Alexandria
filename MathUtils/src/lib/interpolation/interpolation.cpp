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
 * @file src/lib/interpolation/interpolation.cpp
 * @date February 21, 2014
 * @author Nikolaos Apostolakos
 */

#include "ElementsKernel/Logging.h"
#include "MathUtils/interpolation/interpolation.h"
#include "implementations.h"

namespace Euclid {
namespace MathUtils {

namespace {

Elements::Logging logger = Elements::Logging::getLogger("Interpolation");

} // Anonymous namespace

std::unique_ptr<Function> interpolate(const std::vector<double>& x, const std::vector<double>& y,
                                      InterpolationType type, bool extrapolate) {

  if (x.size() != y.size()) {
    throw InterpolationException() << "Interpolation using vectors of incompatible "
            << "size: X=" << x.size() << ", Y=" << y.size();
  }

  // We remove any duplicate lines and we check that we have only increasing
  // X values and no step functions
  std::vector<double> final_x {};
  std::vector<double> final_y {};
  final_x.push_back(x[0]);
  final_y.push_back(y[0]);
  for (std::size_t i = 1; i < x.size(); ++i) {
    if (x[i] == x[i-1]) {
      if (y[i] == y[i-1]) {
        logger.warn() << "Ignoring duplicate pair (" << x[i] << ", " << y[i]
                << ") during interpolation";
        continue;
      } else {
        throw InterpolationException() << "Interpolation of step functions is not "
                << "supported. Entries: (" << x[i] << ", " << y[i] << ") and ("
                << x[i-1] << ", " << y[i-1] << ")";
      }
    }
    if (x[i] < x[i-1]) {
      throw InterpolationException() << "Only increasing X values are supported "
              << "but found " << x[i] << " after " << x[i-1];
    }
  final_x.push_back(x[i]);
  final_y.push_back(y[i]);
  }

  switch (type) {
  case InterpolationType::LINEAR:
    return linearInterpolation(final_x, final_y, extrapolate);
  case InterpolationType::CUBIC_SPLINE:
    return splineInterpolation(final_x, final_y, extrapolate);
  }
  return nullptr;
}

std::unique_ptr<Function> interpolate(const Euclid::XYDataset::XYDataset& dataset, InterpolationType type,
                                      bool extrapolate) {
  std::vector<double> x {};
  std::vector<double> y {};
  for (auto& pair : dataset) {
    x.push_back(pair.first);
    y.push_back(pair.second);
  }
  return interpolate(x, y, type, extrapolate);
}

} // End of MathUtils
} // end of namespace Euclid