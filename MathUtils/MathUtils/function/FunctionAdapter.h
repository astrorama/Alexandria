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
 * @file MathUtils/function/FunctionAdapter.h
 * @date November 2, 2015
 * @author Florian Dubath
 */

#ifndef MATHUTILS_FUNCTIONADAPTER_H_
#define MATHUTILS_FUNCTIONADAPTER_H_

#include "MathUtils/function/Function.h"
#include <functional>

namespace Euclid {
namespace MathUtils {

/**
 * @class FunctionAdapter
 *
 * @brief Adapt a std::function<double(double)> to the Function Interface.
 *
 * @details
 * In some case one need to wrap a std::function into the Function Interface.
 * This class provide this functionality. In particular it allows to build a
 * Function out of a Lamda expression.
 */
class FunctionAdapter : public Function {
public:
  /**
   * @brief Constructor
   *
   * @param function A std::function<double(double)> to be adapted as a Function.
   */
  explicit FunctionAdapter(std::function<double(double)> function);

  /// Default destructor
  virtual ~FunctionAdapter() = default;

  /**
   * Converts the value x from the input domain to the output domain by calling
   * the internal std::function<double(double)>.
   * @param x The value to convert
   * @return The value of the output domain
   */
  double operator()(const double x) const override;

  /**
   * Creates a clone of the function adapter object.
   * @return A copy of the FunctionAdapter object
   */
  std::unique_ptr<Function> clone() const override;

private:
  std::function<double(double)> m_function;
};

}  // namespace MathUtils
}  // namespace Euclid

#endif /* MATHUTILS_FUNCTIONADAPTER_H_ */
