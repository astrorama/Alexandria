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

#include "MathUtils/helpers/InverseCumulative.h"
#include "MathUtils/helpers/Solvers.h"
#include <algorithm>
#include <cassert>

namespace Euclid {
namespace MathUtils {

InverseCumulative::InverseCumulative(std::vector<double> knots, std::vector<double> pdf)
    : m_knots(std::move(knots)), m_pdf(std::move(pdf)), m_cdf(m_pdf.size()) {
  if (m_knots.size() != m_knots.size()) {
    throw Elements::Exception() << "PDF and knots dimensionality do not match: " << m_knots.size() << " != " << knots.size();
  }

  m_cdf[0] = m_pdf[0];
  for (std::size_t i = 1; i < m_cdf.size(); ++i) {
    m_cdf[i] = (m_knots[i] - m_knots[i - 1]) * (m_pdf[i] + m_pdf[i - 1]) / 2.;
    m_cdf[i] += m_cdf[i - 1];
  }
  m_min   = m_cdf.front();
  m_range = m_cdf.back() - m_min;
}

double InverseCumulative::operator()(double p) const {
  if (p < 0. || p > 1.) {
    throw Elements::Exception() << "Cumulative::findInterpolatedValue : p parameter must be in the range [0,1]";
  }

  const double unnormed_p = p * m_range + m_min;

  // Find segment
  if (unnormed_p <= m_cdf.front())
    return m_knots.front();
  if (unnormed_p >= m_cdf.back())
    return m_knots.back();

  std::size_t i = std::upper_bound(m_cdf.begin(), m_cdf.end(), unnormed_p) - m_cdf.begin() - 1;

  const double x0 = m_knots[i], x1 = m_knots[i + 1];
  const double cdf0 = m_cdf[i], cdf1 = m_cdf[i + 1];
  const double p0 = m_pdf[i], p1 = m_pdf[i + 1];

  // If p0 == p1 we are on a uniform area
  if (p0 == p1) {
    return (x1 - x0) * p + x0;
  }

  // If both cdf are the same, then the interval has 0 probability.
  // If both x are the same, this is probably a discontinuity.
  // In those cases, return the lower bound, which might be at least defined (or has a probability of exactly p).
  if (x1 == x0 || cdf0 == cdf1 || cdf0 >= unnormed_p) {
    return x0;
  }

  // Since we assume a linear interpolation, we know that
  // p0 = a * x0 + b
  // p1 = a * x1 + b
  // So we can solve for a and b
  const double a = (p1 - p0) / (x1 - x0);
  const double b = p0 - a * x0;

  assert(std::abs(a * x0 + b - p0) < 1e-8);
  assert(std::abs(a * x1 + b - p1) < 1e-8);

  // The CDF is the integral, so we also know that
  // cdf0 = a/2 * x0^2 + b * x0 + c
  // cdf1 = a/2 * x1^2 + b * x1 + c
  // We already know a and b, so it is easy to solve for c
  const double c = cdf0 - (a / 2.) * (x0 * x0) - b * x0;

  // Double check that the equation passes through the CDF at the limits
  assert(std::abs((a / 2.) * (x0 * x0) + b * x0 + c - cdf0) < 1e-8);
  assert(std::abs((a / 2) * (x1 * x1) + b * x1 + c - cdf1) < 1e-8);

  // We have the equation, so we now need to solve x for p
  double s0, s1;
  std::tie(s0, s1) = solveSquare(a / 2, b, c, unnormed_p);

  // Pick the possible result that lies within [x0, x1]
  if (s0 >= x0 - 1e-8 && s0 <= x1 + 1e-8) {
    return s0;
  }
  assert(s1 >= x0 - 1e-8 && s1 <= x1 + 1e-8);
  return s1;
}

}  // namespace MathUtils
}  // namespace Euclid