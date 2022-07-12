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
 * @file MathUtils/function/Differentiable.h
 * @date February 18, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef MATHUTILS_DIFFERENTIABLE_H
#define MATHUTILS_DIFFERENTIABLE_H

#include <memory>

#include "ElementsKernel/Export.h"

#include "MathUtils/function/Integrable.h"

namespace Euclid {
namespace MathUtils {

/**
 * @interface Differentiable
 *
 * @brief Interface representing a differentiable function
 *
 * @details
 * A function is differentiable if its derivative and indefinite integrals can
 * be calculated in a fast, analytical way. The implementations of this
 * interface should implement the derivative() and indefiniteIntegral() functions
 * accordingly. Note that the Differentiable class implements the Integrable
 * interface by using the indefiniteIntegral().
 */
class ELEMENTS_API Differentiable : public Integrable {
public:
  /// Default destructor
  virtual ~Differentiable() = default;

  /// Returns a Function representing the derivative
  virtual std::shared_ptr<Function> derivative() const = 0;

  /// Returns a Function representing the indefiniteIntegral
  virtual std::shared_ptr<Function> indefiniteIntegral() const = 0;

  /**
   * Calculates the integral in the range [x1,x2], by using the indefinite
   * integral.
   * @param x1 The lower bound of the integration
   * @param x2 The upper bound of the integration
   * @return The integral in the range [x1,x2]
   */
  double integrate(const double x1, const double x2) const final;
};

}  // namespace MathUtils
}  // end of namespace Euclid

#endif /* MATHUTILS_DIFFERENTIABLE_H */
