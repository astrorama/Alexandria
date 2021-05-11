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
 * @file src/lib/Cumulative.cpp
 * @date 01/11/18
 * @author fdubath
 */

#include "MathUtils/PDF/Cumulative.h"
#include "ElementsKernel/Exception.h"
#include "MathUtils/helpers/Solvers.h"
#include "XYDataset/XYDataset.h"
#include <cassert>
#include <cmath>
#include <cstdlib>  // for size_t

namespace Euclid {
namespace MathUtils {

Cumulative::Cumulative(Cumulative&& other)
    : m_x_sampling(std::move(other.m_x_sampling)), m_y_sampling(std::move(other.m_y_sampling)) {}

Cumulative& Cumulative::operator=(Cumulative&& other) {
  m_x_sampling = std::move(other.m_x_sampling);
  m_y_sampling = std::move(other.m_y_sampling);
  return *this;
}

Cumulative::Cumulative(const Cumulative& other) : m_x_sampling(other.m_x_sampling), m_y_sampling(other.m_y_sampling) {}

Cumulative& Cumulative ::operator=(const Cumulative& other) {
  m_x_sampling = other.m_x_sampling;
  m_y_sampling = other.m_y_sampling;
  return *this;
}

Cumulative::Cumulative(std::vector<double>& x_sampling, std::vector<double>& y_sampling)
    : m_x_sampling(x_sampling), m_y_sampling(y_sampling) {
  if (x_sampling.size() != y_sampling.size()) {
    throw Elements::Exception("Cumulative: X and Y sampling do not have the same length.");
  }
}

Cumulative::Cumulative(const XYDataset::XYDataset& sampling) : m_x_sampling{}, m_y_sampling{} {
  auto iter = sampling.begin();
  while (iter != sampling.end()) {
    m_x_sampling.push_back((*iter).first);
    m_y_sampling.push_back((*iter).second);
    ++iter;
  }
}

Cumulative Cumulative::fromPdf(const XYDataset::XYDataset& sampling) {
  std::vector<double> xs{};
  std::vector<double> ys{};
  auto                iter = sampling.begin();
  while (iter != sampling.end()) {
    xs.push_back((*iter).first);
    ys.push_back((*iter).second);
    ++iter;
  }
  return Cumulative::fromPdf(xs, ys);
}

Cumulative Cumulative::fromPdf(std::vector<double>& x_sampling, std::vector<double>& pdf_sampling) {
  double              total = 0.;
  std::vector<double> cumul{};
  auto                iter_pdf = pdf_sampling.cbegin();

  while (iter_pdf != pdf_sampling.cend()) {
    total += *(iter_pdf);
    cumul.push_back(total);
    ++iter_pdf;
  }

  return Cumulative(x_sampling, cumul);
}

void Cumulative::normalize() {
  double              total = m_y_sampling.back();
  std::vector<double> cumul{};
  auto                iter = m_y_sampling.begin();
  while (iter != m_y_sampling.end()) {
    cumul.push_back(*iter / total);
    ++iter;
  }

  m_y_sampling = std::move(cumul);
}

double Cumulative::findValue(double ratio, TrayPosition position) const {
  if (ratio > 1. || ratio < 0.) {
    throw Elements::Exception("Cumulative::findValue : ratio parameter must be in range [0,1]");
  }
  double value  = m_y_sampling.back() * ratio;
  auto   iter_x = m_x_sampling.cbegin();
  auto   iter_y = m_y_sampling.cbegin();
  while (iter_y != m_y_sampling.cend() && (*iter_y) < value) {
    ++iter_x;
    ++iter_y;
  }
  double begin_value = *iter_x;
  double tray        = *iter_y;
  while (iter_y != m_y_sampling.cend() && (*iter_y) == tray) {
    ++iter_x;
    ++iter_y;
  }

  double end_value = *(--iter_x);

  double result = 0;
  switch (position) {
  case TrayPosition::begin:
    result = begin_value;
    break;
  case TrayPosition::middle:
    result = 0.5 * (begin_value + end_value);
    break;
  case TrayPosition::end:
    result = end_value;
    break;
  }

  return result;
}

std::pair<double, double> Cumulative::findMinInterval(double rate) const {

  if (rate > 1. || rate <= 0.) {
    throw Elements::Exception("Cumulative::findMinInterval : rate parameter must be in range ]0,1]");
  }

  rate *= m_y_sampling.back();

  double first_correction = m_y_sampling.front();

  auto iter_1_x = m_x_sampling.cbegin();
  auto iter_2_x = ++(m_x_sampling.cbegin());
  auto iter_1_y = m_y_sampling.cbegin();
  auto iter_2_y = ++(m_y_sampling.cbegin());
  auto min_x    = m_x_sampling.cbegin();
  auto max_x    = --(m_x_sampling.cend());
  while (iter_1_x != m_x_sampling.cend()) {
    while (iter_2_x != m_x_sampling.cend() && (*iter_2_y - *iter_1_y + first_correction) < rate) {
      ++iter_2_x;
      ++iter_2_y;
    }
    if (iter_2_x == m_x_sampling.cend()) {
      break;
    }
    if ((*iter_2_x - *iter_1_x) <= (*max_x - *min_x)) {
      max_x = iter_2_x;
      min_x = iter_1_x;
    }
    ++iter_1_x;
    ++iter_1_y;
    first_correction = 0.;
  }

  return std::make_pair(*min_x, *max_x);
}

std::pair<double, double> Cumulative::findCenteredInterval(double rate) const {
  if (rate > 1. || rate <= 0.) {
    throw Elements::Exception("Cumulative::findCenteredInterval : rate parameter must be in range ]0,1]");
  }

  double min_rate = 0.5 - rate / 2.0;
  double max_rate = 0.5 + rate / 2.0;

  double min_x = findValue(min_rate, TrayPosition::end);
  double max_x = findValue(max_rate, TrayPosition::begin);

  return std::make_pair(min_x, max_x);
}

double inverseCumulative(const std::vector<double>& knots, const std::vector<double>& cdf, double p) {
  assert(p >= cdf.front() && p <= cdf.back());

  // Find segment
  std::size_t i = std::lower_bound(cdf.begin(), cdf.end(), p) - cdf.begin();
  if (i >= cdf.size())
    --i;

  // "Derive" the segment of the cdf to get the pdf
  const double p0 = 0., p1 = cdf[i + 1] - cdf[i];
  const double x0 = knots[i], x1 = knots[i + 1];

  // If both extremes are 0, then the interval has 0 probability.
  // If both extremes are the same, this is probably a discontinuity.
  // In those cases, return the lower bound, which might be at least defined (or has a probability of exactly p).
  if (p1 <= 0 || x1 == x0)
    return x0;

  // Linear interpolation of the pdf
  double a = (x1 - x0) / (p1 - p0);
  double b = x0 - a * p0;

  // The integration of the linear equation (for dx) is
  // y = a*x + b => y = a*x^2/2 + bx + c
  // We need to solve for x, since y is known (the target cumulative probability)
  double s0, s1;
  std::tie(s0, s1) = solveSquare(a / 2., b, 0., p);

  if (s0 >= x0 && s0 <= x1) {
    return s0;
  }
  return s1;
}

}  // namespace MathUtils
}  // namespace Euclid
