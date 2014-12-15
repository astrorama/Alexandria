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

const std::vector<std::shared_ptr<Function>>& Piecewise::getFunctions() const {
  return m_functions;
}

double Piecewise::operator()(const double x) const {
  auto knotsBegin = m_knots.begin();
  if (x < *knotsBegin) {
    return 0;
  }
// The following line compares two doubles which are keys of the knots. This
// means that the much sticter bitewise equality must be used (and not equality
// of real representations). This pragma will hide the misidentified warning
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wfloat-equal"
  if (x == *knotsBegin) {
#pragma GCC diagnostic pop
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
// The following check tests if the two parameters are bitwise equal. A broader
// less string equality check (checking if they represent the same real number)
// cannot be performed without unecessary complication of the method interface
// because Piecewise is a generic usage class. For this reason only a bitwise
// equality check is performed and the rest equality cases will be handled by
// the rest of the code.
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wfloat-equal"
  if (x1 == x2) {
#pragma GCC diagnostic pop
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