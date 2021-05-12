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

#ifndef MATHUTILS_INV_CUMULATIVE_H
#define MATHUTILS_INV_CUMULATIVE_H

#include "ElementsKernel/Exception.h"
#include <vector>

namespace Euclid {
namespace MathUtils {

class InverseCumulative {
public:
  InverseCumulative(std::vector<double> knots, std::vector<double> pdf);

  double operator()(double p) const;

private:
  std::vector<double> m_knots, m_pdf, m_cdf;
  double              m_min, m_range;
};

}  // namespace MathUtils
}  // namespace Euclid

#endif  // MATHUTILS_INV_CUMULATIVE_H
