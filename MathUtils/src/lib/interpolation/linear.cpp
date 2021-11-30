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
#include "MathUtils/function/Integrable.h"
#include "MathUtils/interpolation/interpolation.h"
#include <limits>

namespace Euclid {
namespace MathUtils {

class LinearInterpolator final : public Integrable {
public:
  LinearInterpolator(std::vector<double> knots, std::vector<double> coef0, std::vector<double> coef1)
      : m_knots(std::move(knots)), m_coef0(std::move(coef0)), m_coef1(std::move(coef1)){};

  virtual ~LinearInterpolator() = default;

  double operator()(double x) const override {
    auto knotsBegin = m_knots.begin();
    if (x < *knotsBegin) {
      return 0;
    }
    if (x == *knotsBegin) {
      return m_coef1.front() * x + m_coef0.front();
    }
    auto knotsEnd = m_knots.end();
    auto findX    = std::lower_bound(knotsBegin, knotsEnd, x);
    if (findX == knotsEnd) {
      return 0;
    }
    auto i = findX - knotsBegin - 1;
    return m_coef1[i] * x + m_coef0[i];
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
  const std::vector<double> m_knots, m_coef0, m_coef1;

  double antiderivative(int i, double x) const {
    return m_coef0[i] * x + m_coef1[i] * x * x / 2;
  }
};

std::unique_ptr<Function> linearInterpolation(const std::vector<double>& x, const std::vector<double>& y,
                                              bool extrapolate) {
  std::vector<double> coef0, coef1, knots(x);

  for (size_t i = 0; i < x.size() - 1; i++) {
    coef1.emplace_back((y[i + 1] - y[i]) / (x[i + 1] - x[i]));
    coef0.emplace_back(y[i] - coef1.back() * x[i]);
  }

  if (extrapolate) {
    knots.front() = std::numeric_limits<double>::lowest();
    knots.back()  = std::numeric_limits<double>::max();
  }

  return std::unique_ptr<Function>(new LinearInterpolator(std::move(knots), std::move(coef0), std::move(coef1)));
}

}  // namespace MathUtils
}  // end of namespace Euclid
