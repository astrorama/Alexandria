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
 * @file MathUtils/interpolation/interpolation.h
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef INTERPOLATION_H
#define INTERPOLATION_H

#include <memory>
#include <vector>

#include "ElementsKernel/Export.h"
#include "ElementsKernel/Exception.h"

#include "XYDataset/XYDataset.h"
#include "MathUtils/function/Function.h"

namespace Euclid {
namespace MathUtils {

/// Enumeration of the different supported interpolation types
enum class InterpolationType {
  LINEAR, CUBIC_SPLINE
};

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
                                                   InterpolationType type, bool extrapolate=false);

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
                                                   bool extrapolate=false);

} // End of MathUtils
} // end of namespace Euclid

#endif  /* INTERPOLATION_H */
