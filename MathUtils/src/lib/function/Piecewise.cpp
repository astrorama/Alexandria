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
 * @file src/lib/function/Piecewise.cpp
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#include <algorithm>
#include "ElementsKernel/Exception.h"
#include "MathUtils/function/Piecewise.h"
#include "MathUtils/function/function_tools.h"

namespace Euclid {
namespace MathUtils {

Piecewise::Piecewise(std::vector<double> knots, std::vector<std::shared_ptr<Function> > functions)
                    : m_knots{std::move(knots)} {
  if (m_knots.size() - functions.size() != 1) {
    throw Elements::Exception() << "Invalid number of knots(" << m_knots.size()
                              << ")-functions(" << m_functions.size() << ")";
  }

  m_functions.reserve(functions.size());
  std::transform(functions.begin(), functions.end(), std::back_inserter(m_functions),
                 [](std::shared_ptr<Function>& f) { return f->clone(); });

  auto knotsIter = m_knots.begin();
  while (++knotsIter != m_knots.end()) {
    if (*knotsIter <= *(knotsIter-1)) {
      throw Elements::Exception("knots must be strictly increasing");
    }
  }
}

Piecewise::Piecewise(std::vector<double> knots, std::vector<std::unique_ptr<Function>>&& functions)
                    : m_knots{std::move(knots)}, m_functions{std::move(functions)} {
  if (m_knots.size() - m_functions.size() != 1) {
    throw Elements::Exception() << "Invalid number of knots(" << m_knots.size()
                                << ")-functions(" << m_functions.size() << ")";
  }
  auto knotsIter = m_knots.begin();
  while (++knotsIter != m_knots.end()) {
    if (*knotsIter <= *(knotsIter-1)) {
      throw Elements::Exception("knots must be strictly increasing");
    }
  }
}

const std::vector<double>& Piecewise::getKnots() const {
  return m_knots;
}

const std::vector<std::unique_ptr<Function>>& Piecewise::getFunctions() const {
  return m_functions;
}

double Piecewise::operator()(const double x) const {
  auto knotsBegin = m_knots.begin();
  if (x < *knotsBegin) {
    return 0;
  }
  if (x == *knotsBegin) {
    return (*m_functions[0])(x);
  }
  auto knotsEnd = m_knots.end();
  auto findX = std::lower_bound(knotsBegin, knotsEnd, x);
  if (findX == knotsEnd) {
    return 0;
  }
  return (*m_functions[findX-knotsBegin-1])(x);
}

std::unique_ptr<Function> Piecewise::clone() const {
  std::vector<std::unique_ptr<Function>> cloned_functions;
  cloned_functions.reserve(m_functions.size());
  for (auto& f: m_functions) {
    cloned_functions.emplace_back(f->clone());
  }
  return std::unique_ptr<Function> {new Piecewise(m_knots, std::move(cloned_functions))};
}

double Piecewise::integrate(const double x1, const double x2) const {
  if (x1 == x2) {
    return 0;
  }
  int direction = 1;
  double min = x1;
  double max = x2;
  if (min > max) {
    direction = -1;
    min = x2;
    max = x1;
  }
  double result = 0;
  auto knotIter = std::upper_bound(m_knots.begin(), m_knots.end(), min);
  if (knotIter != m_knots.begin()) {
    --knotIter;
  }
  auto functionIter = m_functions.begin() + (knotIter - m_knots.begin());
  while (++knotIter != m_knots.end()) {
    auto prevKnotIter = knotIter - 1;
    if (max <= *prevKnotIter) {
      break;
    }
    if (min < *knotIter) {
      double down = (min > *prevKnotIter) ? min : *prevKnotIter;
      double up = (max < *knotIter) ? max : *knotIter;
      result += Euclid::MathUtils::integrate(**functionIter, down, up);
    }
    ++functionIter;
  }
  return direction * result;
}

} // End of MathUtils
} // end of namespace Euclid
