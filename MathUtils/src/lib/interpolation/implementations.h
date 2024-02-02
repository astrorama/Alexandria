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
 * @file src/lib/interpolation/implementations.h
 * @date February 21, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef MATHUTILS_IMPLEMENTATIONS_H
#define MATHUTILS_IMPLEMENTATIONS_H

namespace Euclid {
namespace MathUtils {

/// Performs linear interpolation for the given set of data points
std::unique_ptr<Function> linearInterpolation(const std::vector<double>& x, const std::vector<double>& y,
                                              bool extrapolate);

/// Performs cubic spline interpolation for the given set of data points
std::unique_ptr<Function> splineInterpolation(const std::vector<double>& x, const std::vector<double>& y,
                                              bool extrapolate);

}  // namespace MathUtils
}  // end of namespace Euclid

#endif /* MATHUTILS_IMPLEMENTATIONS_H */
