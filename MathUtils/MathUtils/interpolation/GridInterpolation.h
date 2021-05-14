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

template <typename... AxisType>
class InterpN {
public:
  InterpN(const std::tuple<std::vector<AxisType>...>& grid, const NdArray::NdArray<double>& values, bool extrapolate);

  ~InterpN() = default;

  double operator()(AxisType... args) const;
};

}  // namespace MathUtils
}  // namespace Euclid

#define GRIDINTERPOLATION_IMPL
#include "MathUtils/interpolation/_impl/GridInterpolation.icpp"
#undef GRIDINTERPOLATION_IMPL

#endif  // MATHUTILS_GRIDINTERPOLATION_H
