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

#ifndef _FUNCTIONUTILS_LINEARREGRESSION_H
#define _FUNCTIONUTILS_LINEARREGRESSION_H

#include <utility>  // for std::pair
#include <vector>   // for std::vector

namespace Euclid {
namespace MathUtils {

/**
 * Computes factors a and b such that  y = a * x + b
 * @param x Independent variable
 * @param y Dependent variable
 * @return The factors (a, b)
 */
std::pair<double, double> linearRegression(const std::vector<double>& x, const std::vector<double>& y);

}  // namespace MathUtils
}  // namespace Euclid

#endif  // _FUNCTIONUTILS_LINEARREGRESSION_H
