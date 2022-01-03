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

#ifndef MATHUTILS_GRIDINTERPOLATION_H
#define MATHUTILS_GRIDINTERPOLATION_H

#include "NdArray/NdArray.h"
#include <tuple>
#include <vector>

namespace Euclid {
namespace MathUtils {

/**
 * Interpolate on a grid with arbitrary knot types (discrete or continuous)
 * @tparam AxisType
 *  List of axes types. Their order corresponds to the order of the axes on the NdArray with the grid values.
 *  For instance, values.at(0,1,2) corresponds to the position on the grid defined by the knot 0 of the first
 *  axis, the knot 1 of the second axis, and the knot 2 of the third axis.
 *
 * @details
 *  Example of usage:
 *
 * \code{.cpp}
 * // First and second axes are continuous, third one is discrete
 * InterpN<double, double, MyEnum> interp(...);
 * double interpolated = interp(0.5, 1.48, MyEnum::A)
 * \endcode
 *
 * @warning
 *  For discrete dimensions, even if extrapolate is true, undefined bins will be considered to have a value of 0.
 *
 * @warning
 *  For integer dimensions, values are expected to start at 0 and be strictly incremental. This is a compromise to
 *  improve the sampling performance (direct access to an array instead of a search)
 */
template <typename... AxisType>
class InterpN {
public:
  /**
   * Constructor
   * @param grid
   *    Knots defining the grid
   * @param values
   *    Grid values
   * @param extrapolate
   *    If true, values will be extrapolated on continuous dimensions
   * @warning
   *    The memory layout of values is expected to follow the same as GridContainer: the faster changing axis (the last)
   *    corresponds to the first grid axis
   */
  InterpN(const std::tuple<std::vector<AxisType>...>& grid, const NdArray::NdArray<double>& values, bool extrapolate);

  /**
   * Destructor
   */
  ~InterpN() = default;

  /**
   * Interpolate the value for the given parameters
   */
  double operator()(AxisType... args) const;
};

}  // namespace MathUtils
}  // namespace Euclid

#define GRIDINTERPOLATION_IMPL
#include "MathUtils/interpolation/_impl/GridInterpolation.icpp"
#undef GRIDINTERPOLATION_IMPL

#endif  // MATHUTILS_GRIDINTERPOLATION_H
