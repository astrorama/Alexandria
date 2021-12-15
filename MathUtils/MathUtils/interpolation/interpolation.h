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
 * @file MathUtils/interpolation/interpolation.h
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef INTERPOLATION_H
#define INTERPOLATION_H

#include <array>
#include <memory>
#include <vector>

#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Export.h"

#include "MathUtils/function/Function.h"
#include "NdArray/NdArray.h"
#include "XYDataset/XYDataset.h"

namespace Euclid {
namespace MathUtils {

/// Enumeration of the different supported interpolation types
enum class InterpolationType { LINEAR, CUBIC_SPLINE };

struct InterpolationException : public Elements::Exception {
  using Elements::Exception::Exception;
};

/**
 * Returns a Function which performs interpolation for the given set of data
 * points. Duplicate (x,y) pairs are ignored and treated as a single one.
 * @param x The x values of the data points
 * @param y The y values of the data points
 * @param type The type of the interpolation to perform
 * @return A function representing the interpolation
 * @throws InterpolationException
 *    if the x and y vectors do not have the same size
 * @throws InterpolationException
 *    if there are decreasing x values
 * @throws InterpolationException
 *    if there are (X,Y) pairs with same X value but different Y value (step functions)
 */
ELEMENTS_API std::unique_ptr<Function> interpolate(const std::vector<double>& x, const std::vector<double>& y,
                                                   InterpolationType type, bool extrapolate = false);

/**
 * Returns a Function which performs interpolation for the data points of the
 * given dataset.
 * @param dataset The dataset containing the data points
 * @param type The type of the interpolation to perform
 * @return A function representing the interpolation
 * @throws InterpolationException
 *    if there are decreasing x values
 * @throws InterpolationException
 *    if there are (X,Y) pairs with same X value but different Y value (step functions)
 */
ELEMENTS_API std::unique_ptr<Function> interpolate(const Euclid::XYDataset::XYDataset& dataset, InterpolationType type,
                                                   bool extrapolate = false);

/**
 * Alias for an array of references to vectors of doubles
 * @tparam N Number of dimensions
 * @brief Used to pass the grid coordinates to interpn. Internally will make a copy of the required values.
 */
template <std::size_t N>
using Coordinates = std::array<std::vector<double>, N>;

/**
 * Returns a NAryFunction<N> which performs a multidimensional interpolation
 * @tparam N
 *  Dimensionality
 * @param grid
 *  Array containing the knots for each grid dimension. Note that the order must follow the same as the axes!
 *  the first coordinates corresponds to the axis 0, the second coordinates to the axis 1, and so on.
 * @param values
 *  Values at each grid point. Its shape must match the grid coordinates
 * @param type
 *  Interpolation type. Note that for N >= 2, only linear is supported right now
 * @param extrapolate
 *  If true, the values for points outside the grid will be extrapolated. If false,
 *  they will be 0.
 * @example
 *  For a grid of 3 dimensions, and 3 points on each dimension, `grid` must point to three
 *  vectors of size 3. The shape of values must be (3, 3, 3)
 */
template <std::size_t N>
ELEMENTS_API std::unique_ptr<NAryFunction<N>> interpn(const Coordinates<N>&           grid,
                                                      const NdArray::NdArray<double>& values, InterpolationType type,
                                                      bool extrapolate = false);

/**
 * Simple linear interpolation
 * @param x
 *  Target value
 * @param xp
 *  x samples
 * @param yp
 *  Function samples (yp = f(xp))
 * @param extrapolate
 *  If true, extrapolate
 * @return
 *  An approximation for f(x)
 */
ELEMENTS_API double simple_interpolation(double x, const std::vector<double>& xp, const std::vector<double>& yp,
                                         bool extrapolate = false);

ELEMENTS_API double simple_interpolation(double x, const std::array<double, 2>& xp, const std::array<double, 2>& yp,
                                         bool extrapolate = false) noexcept;

}  // namespace MathUtils
}  // end of namespace Euclid

#define INTERPOLATION_IMPL
#include "MathUtils/interpolation/_impl/interpolation.icpp"
#undef INTERPOLATION_IMPL

#endif /* INTERPOLATION_H */
