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
 * @file src/lib/interpolation/linear.cpp
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#include "ElementsKernel/Exception.h"
#include "MathUtils/function/Piecewise.h"
#include "MathUtils/interpolation/interpolation.h"
#include <limits>

namespace Euclid {
namespace MathUtils {

class LinearInterpolator final : public PiecewiseBase {
public:
  LinearInterpolator(std::vector<double> knots, std::vector<double> coef0, std::vector<double> coef1)
      : PiecewiseBase(std::move(knots)), m_coef0(std::move(coef0)), m_coef1(std::move(coef1)){};

  virtual ~LinearInterpolator() = default;

  double operator()(double x) const override {
    auto i = findKnot(x);
    if (i < 0 || i >= static_cast<ssize_t>(m_knots.size())) {
      return 0;
    }
    if (i == 0) {
      return m_coef1.front() * x + m_coef0.front();
    }
    return m_coef1[i - 1] * x + m_coef0[i - 1];
  }

  void operator()(const std::vector<double>& xs, std::vector<double>& out) const override {
    out.resize(xs.size());
    // Find the first X that is within the range
    auto first_x = std::lower_bound(xs.begin(), xs.end(), m_knots.front());
    auto n_less  = first_x - xs.begin();

    // Opening 0s
    auto o = out.begin() + n_less;
    std::fill(out.begin(), o, 0.);

    // To avoid if within the loop, treat values exactly equal to the first knot here
    auto x = xs.begin() + n_less;
    while (x < xs.end() && *x == m_knots.front()) {
      *o = m_coef1.front() * *x + m_coef0.front();
      ++o, ++x;
    }
    if (x == xs.end()) {
      return;
    }

    // Interpolate values within range
    auto current_knot = std::lower_bound(m_knots.begin(), m_knots.end(), *x);
    while (o != out.end() && current_knot < m_knots.end()) {
      current_knot = std::find_if(current_knot, m_knots.end(), [x](double k) { return k >= *x; });
      auto i       = current_knot - m_knots.begin();
      *o           = m_coef1[i - 1] * *x + m_coef0[i - 1];
      ++o, ++x;
    }

    // Trailing 0s
    std::fill(o, out.end(), 0.);
  }

  std::unique_ptr<NAryFunction> clone() const override {
    return std::unique_ptr<NAryFunction>(new LinearInterpolator(m_knots, m_coef0, m_coef1));
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
  const std::vector<double> m_coef0, m_coef1;

  double antiderivative(int i, double x) const {
    return m_coef0[i] * x + m_coef1[i] * x * x / 2;
  }
};

std::unique_ptr<Function> linearInterpolation(const std::vector<double>& x, const std::vector<double>& y,
                                              bool extrapolate) {
  std::vector<double> coef0(x.size()), coef1(x.size()), knots(x);

  for (size_t i = 0; i < x.size() - 1; i++) {
    double dx = (x[i + 1] - x[i]);
    if (dx > 0) {
      coef1[i] = (y[i + 1] - y[i]) / dx;
      coef0[i] = y[i] - coef1[i] * x[i];
    }
  }

  if (extrapolate) {
    knots.front() = std::numeric_limits<double>::lowest();
    knots.back()  = std::numeric_limits<double>::max();
  }

  return std::unique_ptr<Function>(new LinearInterpolator(std::move(knots), std::move(coef0), std::move(coef1)));
}

}  // namespace MathUtils
}  // end of namespace Euclid
