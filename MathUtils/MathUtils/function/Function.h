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
 * @file MathUtils/function/Function.h
 * @date February 18, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef MATHUTILS_FUNCTION_H
#define MATHUTILS_FUNCTION_H

#include "ElementsKernel/Exception.h"
#include <memory>

namespace Euclid {
namespace MathUtils {

/**
 * @interface Function
 *
 * @brief Interface class representing a function
 *
 * @details
 * A function is an object which can convert a value from domain X to a value
 * of domain Y. This interface is the root of a hierarchy of classes which
 * perform such conversions, with the parenthesis operator. Because this class
 * is designed for inheritance, it requires the implementation of the clone()
 * method for copying functions when a reference of type Function is used.
 */
class Function {

public:
  /// Default destructor
  virtual ~Function() = default;

  /**
   * Converts the value x from the input domain to the output domain.
   * @param x The value to convert
   * @return The value of the output domain
   */
  virtual double operator()(const double x) const = 0;

  /**
   * Creates a clone of the function object. All subclasses must implement this
   * method, to enable copying of Function objects when only a reference to the
   * Function class is available.
   * @return A copy of the Function object
   */
  virtual std::unique_ptr<Function> clone() const = 0;
};

}  // namespace MathUtils
}  // end of namespace Euclid

#endif /* MATHUTILS_FUNCTION_H */
