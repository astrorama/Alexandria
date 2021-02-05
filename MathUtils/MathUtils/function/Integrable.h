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
 * @file MathUtils/function/Integrable.h
 * @date February 18, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef MATHUTILS_INTEGRABLE_H
#define MATHUTILS_INTEGRABLE_H

#include "MathUtils/function/Function.h"

namespace Euclid {
namespace MathUtils {

/**
 * @interface Integrable
 *
 * @brief Interface representing an integrable function
 *
 * @details
 * A function is integrable when there is a fast analytical way to calculate
 * its integral (as opposed to a numerical calculation). The implementations
 * of this interface should provide this calculation by implementing the
 * integrate() method.
 */
class Integrable : public Function {

public:
  /// Default destructor
  virtual ~Integrable() = default;

  /**
   * Calculates the integral of the function in the range [a,b].
   * @param a The lower bound of the integration
   * @param b The upper bound of the integration
   * @return The integral of the function in the range [a,b]
   */
  virtual double integrate(const double a, const double b) const = 0;
};

}  // namespace MathUtils
}  // end of namespace Euclid

#endif /* MATHUTILS_INTEGRABLE_H */
