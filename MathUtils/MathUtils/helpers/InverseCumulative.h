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

/**
 * Model an inverse cumulative, used to sample a value given a PDF
 * @tparam TKnot
 *  Knot type, may be discrete or continuous
 * @tparam E
 *  Used by the discrete and continuous specializations.
 * @details
 *  The PDF is linearly interpolated. This implies that the CDF
 *  is computed deriving analytically each segment into a quadratic function.
 */
template <typename TKnot, typename E = void>
class InverseCumulative {

  /**
   * Constructor
   * @param knots
   *    PDF knots. For continuous distributions, they must be in order.
   *    Discrete distributions do not need to be sorted.
   * @param pdf
   *    Distribution PDF
   */
  InverseCumulative(std::vector<TKnot> knots, std::vector<double> pdf);

  /**
   * Return the first value where the CDF has a value >= p
   * For continuous distributions each segment of the PDF is assumed to be linearly interpolated,
   * so the integral of the PDF is used to interpolate the knot value.
   */
  TKnot operator()(double p) const;
};

}  // namespace MathUtils
}  // namespace Euclid

#define INVERSE_CUMULATIVE_IMPL
#include "MathUtils/helpers/_impl/InverseCumulative.icpp"
#undef INVERSE_CUMULATIVE_IMPL

#endif  // MATHUTILS_INV_CUMULATIVE_H
