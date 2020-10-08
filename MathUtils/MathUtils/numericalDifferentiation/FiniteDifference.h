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
 * @file MathUtils/numericalDifferentiation/CentralDifference.h
 * @date January 09, 2020
 * @author Alejandro Alvarez Ayllon
 */

#ifndef MATHUTILS_MATHUTILS_NUMERICALDIFFERENTIATION_FINITEDIFFERENCE_H_
#define MATHUTILS_MATHUTILS_NUMERICALDIFFERENTIATION_FINITEDIFFERENCE_H_

#include "MathUtils/function/Function.h"

namespace Euclid {
namespace MathUtils {

/**
 * Derivative using finite differences:
 *  \f$ f'(x) = \frac{f(x+h) - f(x)}{h} \f$
 * @note
 *  h is computed automatically following the same approach as boost numeric differentiation:
 *  \f$ h =(x + \sqrt{\epsilon} * 2)  - x \f$
 *  This guarantees that xh is representable using floating point (since (x + h) - x is *not* necessarily equal to h)
 *  If h happens to be 0, std::nextafter is called
 * @param f
 *  The Function to derive
 * @param x
 *  The point where to do the derivation
 * @return
 *  An approximation of f'(x)
 */
double derivative(const Function& f, const double x);

/**
 * Second derivative using finite differences:
 *  \f$ f''(x) = \frac{f(x+h) - 2f(x) + f(x - h)}{h^2} \f$
 * @note
 *  h is computed automatically as follows:
 *  \f$ h =(x + \sqrt[4]{\epsilon} * 2) - x \f$
 *  This guarantees that xh is representable using floating point (since (x + h) - x is *not* necessarily equal to h)
 *  If h happens to be 0, std::nextafter is called
 * @param f
 *  The Function to derive
 * @param x
 *  The point where to do the derivation
 * @return
 *  An approximation of f''(x)
 */
double derivative2nd(const Function& f, const double x);

}  // end namespace MathUtils
}  // end namespace Euclid

#endif  // MATHUTILS_MATHUTILS_NUMERICALDIFFERENTIATION_FINITEDIFFERENCE_H_
