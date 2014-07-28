/** 
 * @file src/lib/function/Piecewise.cpp
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#include <algorithm>
#include "ElementsKernel/ElementsException.h"
#include "ChMath/function/Piecewise.h"
#include "ChMath/function/function_tools.h"

namespace ChMath {

Piecewise::Piecewise(std::vector<double> knots, std::vector<std::shared_ptr<Function> > functions)
                    : m_knots{std::move(knots)}, m_functions{std::move(functions)} {
  if (m_knots.size() - m_functions.size() != 1) {
    throw ElementsException() << "Invalid number of knots(" << m_knots.size()
                              << ")-functions(" << m_functions.size() << ")";
  }
  auto knotsIter = m_knots.begin();
  while (++knotsIter != m_knots.end()) {
    if (*knotsIter <= *(knotsIter-1)) {
      throw ElementsException("knots must be strictly increasing");
    }
  }
}
                    
const std::vector<double>& Piecewise::getKnots() const {
  return m_knots;
}

const std::vector<std::shared_ptr<Function>>& Piecewise::getFunctions() const {
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
  return std::unique_ptr<Function> {new Piecewise(m_knots, m_functions)};
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
      result += ChMath::integrate(**functionIter, down, up);
    }
    ++functionIter;
  }
  return direction * result;
}

} // End of ChMath