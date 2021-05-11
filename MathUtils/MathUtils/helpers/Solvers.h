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

#ifndef MATHUTILS_SOLVERS_H
#define MATHUTILS_SOLVERS_H

#include "ElementsKernel/Exception.h"
#include <tuple>

namespace Euclid {
namespace MathUtils {

/**
 * Solve x for y = a * x^2 + b * x + c
 * @return
 *  A pair with the two (or one) possible solution
 * @throw Elements::Exception
 *  If a == b == 0. (can not be solved)
 */
std::pair<double, double> solveSquare(double a, double b, double c, double y);

}  // namespace MathUtils
}  // namespace Euclid

#endif  // MATHUTILS_SOLVERS_H
