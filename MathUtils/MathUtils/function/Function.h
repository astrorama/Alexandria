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
 * @file MathUtils/function/Function.h
 * @date February 18, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef MATHUTILS_FUNCTION_H
#define MATHUTILS_FUNCTION_H

#include "AlexandriaKernel/index_sequence.h"
#include "ElementsKernel/Exception.h"
#include <memory>
#include <vector>

namespace Euclid {
namespace MathUtils {

/**
 * @interface NAryFunctionImpl
 * @tparam Seq
 *  Sequence used to repeat N times the parameter to the operator ()
 */
template <typename Seq>
class NAryFunctionImpl {
public:
};

/**
 * @interface NAryFunctionImpl
 * @tparam Is
 * @details
 *  Specialization of NAryFunctionImpl that works over the concrete sequence std::index_sequence
 */
template <std::size_t... Is>
class NAryFunctionImpl<_index_sequence<Is...>> {
public:
  template <std::size_t>
  using Doubles = double;

  template <std::size_t>
  using Vectors = std::vector<double>;

  /// Default destructor
  virtual ~NAryFunctionImpl() = default;

  /**
   * Converts the values x1,...,xm from the input domain to the output domain.
   * @param x The value to convert
   * @return The value of the output domain
   */
  virtual double operator()(Doubles<Is>... xn) const = 0;

  /**
   * Operate over a set of input vectors, output a vector.
   * When a function is going to be evaluated over a grid, this can improve the performance since the
   * tight loop does not need to do indireections.
   * @param xs Set of input vectors
   * @param output Output vector. Concrete implementations must resize if needed.
   * @warning
   *    For unary functions, xs must be sorted. This allows better performance.
   */
  virtual void operator()(const Vectors<Is>&... xs, std::vector<double>& output) const {
    output.resize(std::get<0>(std::tuple<const Vectors<Is>&...>(xs...)).size());
    for (size_t i = 0; i < output.size(); ++i) {
      output[i] = (*this)(xs[i]...);
    }
  }
};

/**
 * @interface NAryFunction
 *
 * @brief Interface class representing a function with an arbitrary number of parameters
 *
 * @tparam N
 *  Number of parameters
 *
 * @details
 *  This class hides away NAryFunctionImpl, making easier to define a function
 *  with a given number of parameters: i.e. NAryFunction<5>
 *
 * @see Function
 *  For a detailed explanation of why `clone()` is defined here and not in NAryFunctionImpl
 */
template <std::size_t N>
class NAryFunction : public NAryFunctionImpl<_make_index_sequence<N>> {
public:
  /**
   * Creates a clone of the function object. All subclasses must implement this
   * method, to enable copying of Function objects when only a reference to the
   * Function class is available.
   * @return A copy of the Function object
   */
  virtual std::unique_ptr<NAryFunction> clone() const = 0;
};

/// Alias for an unary function
using Function = NAryFunction<1>;

/// Alias for a binary function
using BinaryFunction = NAryFunction<2>;

/// Alias for a ternary function
using TernaryFunction = NAryFunction<3>;

}  // namespace MathUtils
}  // end of namespace Euclid

#endif /* MATHUTILS_FUNCTION_H */
