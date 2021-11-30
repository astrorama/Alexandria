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
 * @file src/lib/interpolation/spline.cpp
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#include "ElementsKernel/Exception.h"
#include "MathUtils/function/Piecewise.h"
#include "MathUtils/interpolation/interpolation.h"
#include <limits>

namespace Euclid {
namespace MathUtils {

class CubicInterpolator final : public PiecewiseBase {
public:
  CubicInterpolator(std::vector<double> knots, std::vector<double> coef0, std::vector<double> coef1,
                    std::vector<double> coef2, std::vector<double> coef3)
      : PiecewiseBase(std::move(knots))
      , m_coef0(std::move(coef0))
      , m_coef1(std::move(coef1))
      , m_coef2(std::move(coef2))
      , m_coef3(std::move(coef3)) {}

  virtual ~CubicInterpolator() = default;

  double operator()(double x) const override {
    auto knotsBegin = m_knots.begin();
    if (x < *knotsBegin) {
      return 0;
    }
    if (x == *knotsBegin) {
      return m_coef3.front() * x * x * x + m_coef2.front() * x * x + m_coef1.front() * x + m_coef0.front();
    }
    auto knotsEnd = m_knots.end();
    auto findX    = std::lower_bound(knotsBegin, knotsEnd, x);
    if (findX == knotsEnd) {
      return 0;
    }
    auto i = findX - knotsBegin - 1;
    return m_coef3[i] * x * x * x + m_coef2[i] * x * x + m_coef1[i] * x + m_coef0[i];
  }

  std::unique_ptr<NAryFunction> clone() const override {
    return std::unique_ptr<NAryFunction>(new CubicInterpolator(m_knots, m_coef0, m_coef1, m_coef2, m_coef3));
  }

  double integrate(const double a, const double b) const override {
    if (a == b) {
      return 0;
    }
    int    direction = 1;
    double min       = a;
    double max       = b;
    if (min > max) {
      direction = -1;
      min       = b;
      max       = a;
    }
    double result   = 0;
    auto   knotIter = std::upper_bound(m_knots.begin(), m_knots.end(), min);
    if (knotIter != m_knots.begin()) {
      --knotIter;
    }
    auto i = knotIter - m_knots.begin();
    while (++knotIter != m_knots.end()) {
      auto prevKnotIter = knotIter - 1;
      if (max <= *prevKnotIter) {
        break;
      }
      if (min < *knotIter) {
        double down = (min > *prevKnotIter) ? min : *prevKnotIter;
        double up   = (max < *knotIter) ? max : *knotIter;
        result += antiderivative(i, up) - antiderivative(i, down);
      }
      ++i;
    }
    return direction * result;
  }

private:
  std::vector<double> m_coef0, m_coef1, m_coef2, m_coef3;

  double antiderivative(int i, double x) const {
    double x2 = x * x;
    return m_coef0[i] * x + m_coef1[i] * x2 / 2. + m_coef2[i] * x2 * x / 3. + m_coef3[i] * x2 * x2 / 4.;
  }
};

std::unique_ptr<Function> splineInterpolation(const std::vector<double>& x, const std::vector<double>& y,
                                              bool extrapolate) {
  std::vector<double> knots(x);

  // Number of intervals
  int n = x.size() - 1;

  // Differences between knot points
  std::vector<double> h(n, 0.);
  for (int i = 0; i < n; i++)
    h[i] = x[i + 1] - x[i];

  std::vector<double> mu(n, 0.);
  std::vector<double> z(n + 1, 0.);
  for (int i = 1; i < n; ++i) {
    double g = 2. * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1];
    mu[i]    = h[i] / g;
    z[i]     = (3. * (y[i + 1] * h[i - 1] - y[i] * (x[i + 1] - x[i - 1]) + y[i - 1] * h[i]) / (h[i - 1] * h[i]) -
            h[i - 1] * z[i - 1]) /
           g;
  }

  // cubic spline coefficients
  std::vector<double> coef0(n, 0.);
  std::vector<double> coef1(n, 0.);
  std::vector<double> coef2(n + 1, 0.);
  std::vector<double> coef3(n, 0.);

  z[n]     = 0.;
  coef2[n] = 0.;

  for (int j = n - 1; j >= 0; j--) {
    coef0[j] = y[j];
    coef2[j] = z[j] - mu[j] * coef2[j + 1];
    coef1[j] = (y[j + 1] - y[j]) / h[j] - h[j] * (coef2[j + 1] + 2. * coef2[j]) / 3.;
    coef3[j] = (coef2[j + 1] - coef2[j]) / (3. * h[j]);
  }

  // The above were taken from SplineInterpolator from Apache commons math. These
  // polynomials need to be shifted by -x[i] in our case.
  for (int i = 0; i < n; i++) {
    double x_1 = -x[i];
    double x_2 = x_1 * x_1;
    double x_3 = x_1 * x_2;
    coef0[i]   = coef0[i] + coef1[i] * x_1 + coef2[i] * x_2 + coef3[i] * x_3;
    coef1[i]   = coef1[i] + 2. * coef2[i] * x_1 + 3. * coef3[i] * x_2;
    coef2[i]   = coef2[i] + 3. * coef3[i] * x_1;
    // d[i] keeps the same value
  }

  if (extrapolate) {
    knots.front() = std::numeric_limits<double>::lowest();
    knots.back()  = std::numeric_limits<double>::max();
  }

  return std::unique_ptr<Function>(
      new CubicInterpolator(std::move(knots), std::move(coef0), std::move(coef1), std::move(coef2), std::move(coef3)));
}

}  // namespace MathUtils
}  // end of namespace Euclid
