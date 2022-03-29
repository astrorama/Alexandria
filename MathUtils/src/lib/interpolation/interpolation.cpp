/*
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
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

#include "MathUtils/interpolation/interpolation.h"
#include "ElementsKernel/Logging.h"
#include "MathUtils/function/FunctionAdapter.h"
#include "implementations.h"
#include <AlexandriaKernel/memory_tools.h>

namespace Euclid {
namespace MathUtils {

namespace {

Elements::Logging logger = Elements::Logging::getLogger("Interpolation");

}  // Anonymous namespace

std::unique_ptr<Function> interpolate(const std::vector<double>& x, const std::vector<double>& y,
                                      InterpolationType type, bool extrapolate) {

  if (x.size() != y.size()) {
    throw InterpolationException() << "Interpolation using vectors of incompatible "
                                   << "size: X=" << x.size() << ", Y=" << y.size();
  }

  if (x.size() == 1) {
    auto c = y.front();
    if (extrapolate) {
      return make_unique<FunctionAdapter>([c](double) { return c; });
    }
    auto sx = x.front();
    return make_unique<FunctionAdapter>([c, sx](double v) { return c * (v == sx); });
  }

  // We remove any duplicate lines and we check that we have only increasing
  // X values and no step functions
  std::vector<double> final_x;
  std::vector<double> final_y;

  final_x.reserve(x.size());
  final_y.reserve(x.size());

  final_x.emplace_back(x[0]);
  final_y.emplace_back(y[0]);
  for (std::size_t i = 1; i < x.size(); ++i) {
    if (x[i] == x[i - 1] && y[i] == y[i - 1]) {
      continue;
    }
    if (x[i] < x[i - 1]) {
      throw InterpolationException() << "Only increasing X values are supported "
                                     << "but found " << x[i] << " after " << x[i - 1];
    }
    final_x.emplace_back(x[i]);
    final_y.emplace_back(y[i]);
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
  if (dataset.size() == 1) {
    auto c = dataset.front();
    if (extrapolate) {
      return make_unique<FunctionAdapter>([c](double) { return c.second; });
    }
    return make_unique<FunctionAdapter>([c](double v) { return c.second * (v == c.first); });
  }

  std::vector<double> x;
  std::vector<double> y;
  x.reserve(dataset.size());
  y.reserve(dataset.size());
  for (auto& pair : dataset) {
    if (!x.empty()) {
      if (pair.first == x.back() && pair.second == y.back()) {
        continue;
      }
      if (pair.first < x.back()) {
        throw InterpolationException() << "Only increasing X values are supported "
                                       << "but found " << pair.first << " after " << x.back();
      }
    }
    x.emplace_back(pair.first);
    y.emplace_back(pair.second);
  }

  switch (type) {
  case InterpolationType::LINEAR:
    return linearInterpolation(x, y, extrapolate);
  case InterpolationType::CUBIC_SPLINE:
    return splineInterpolation(x, y, extrapolate);
  }
  return nullptr;
}

double simple_interpolation(double x, const std::vector<double>& xp, const std::vector<double>& yp, bool extrapolate) {
  if (xp.empty()) {
    throw InterpolationException() << "Can not interpolate an empty list of values";
  }
  if (xp.size() != yp.size()) {
    throw InterpolationException() << "Number of knots and number of values do not match";
  }
  if (xp.size() == 1) {
    return (extrapolate || xp.front() == x) ? yp.front() : 0.;
  }

  if ((x < xp.front() || x > xp.back()) && !extrapolate) {
    return 0;
  }

  auto        gt = std::upper_bound(xp.begin(), xp.end(), x);
  std::size_t i  = gt - xp.begin();
  if (i == 0) {
    ++i;
  }
  if (i == xp.size()) {
    if (!extrapolate && x > xp.back())
      return 0.;
    --i;
  }
  return simple_interpolation(x, xp[i - 1], xp[i], yp[i - 1], yp[i], extrapolate);
}

double simple_interpolation(double x, double x0, double x1, double y0, double y1, bool extrapolate) noexcept {
  // Looks convolved, but this avoids branching
  double within = ((x >= x0) & (x <= x1)) | extrapolate;
  double coef1  = (y1 - y0) / (x1 - x0);
  double coef0  = y0 - coef1 * x0;
  return within * (coef0 + coef1 * x);
}

}  // namespace MathUtils
}  // end of namespace Euclid
