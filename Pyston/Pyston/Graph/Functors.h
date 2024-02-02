/**
 * @copyright (C) 2012-2020 Euclid Science Ground Segment
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

#ifndef PYSTON_FUNCTORS_H
#define PYSTON_FUNCTORS_H

#include <cmath>

namespace Pyston {

/**
 * Convenience functor, used to attach a method for the unary '+' operator
 */
template <typename T>
struct Identity {
  T operator()(T value) const {
    return value;
  }
};

/**
 * This class helps defining templated-functors, very much alike
 * std::negate, but wrapping C calls that do not  have a corresponding
 * templated functor, and that receive a single parameter.
 * @tparam R
 *  Return type
 * @tparam T
 *  Parameter type
 * @tparam wrapped
 *  A pointer to the function being wrapped
 */
template <typename R, typename T, R (*wrapped)(T)>
struct UnaryWrapper {
  R operator()(T value) const {
    return wrapped(value);
  }
};

/**
 * Like UnaryWrapper, this class helps defining templated-functors that
 * receive two parameters, so it can be used as std::plus, std::multiplies and similar ones.
 * @tparam R
 *  Return type
 * @tparam T
 *  Parameter type. It is assumed both parameters are to be the same, since this is
 *  going to be used mostly to define operators
 * @tparam wrapped
 *  A pointer to the function being wrapped
 */
template <typename R, typename T, R (*wrapped)(T, T)>
struct BinaryWrapper {
  R operator()(T left, T right) const {
    return wrapped(left, right);
  }
};

/// Wraps the power function
template <typename T>
using Pow = BinaryWrapper<T, T, std::pow>;

/// Wraps the abs function
template <typename T>
using Abs = UnaryWrapper<T, T, std::abs>;

/// Wraps the round function
template <typename T>
using Round = UnaryWrapper<T, T, std::round>;

/// Wraps the exponential function
template <typename T>
using Exp = UnaryWrapper<T, T, std::exp>;

/// Wraps the exponential, base 2, function
template <typename T>
using Exp2 = UnaryWrapper<T, T, std::exp2>;

/// Wraps the log function
template <typename T>
using Log = UnaryWrapper<T, T, std::log>;

/// Wraps the log, base 2, function
template <typename T>
using Log2 = UnaryWrapper<T, T, std::log2>;

/// Wraps the log, base 10, function
template <typename T>
using Log10 = UnaryWrapper<T, T, std::log10>;

/// Wraps the square root function
template <typename T>
using Sqrt = UnaryWrapper<T, T, std::sqrt>;

/// Wraps the sin function
template <typename T>
using Sin = UnaryWrapper<T, T, std::sin>;

/// Wraps the cos function
template <typename T>
using Cos = UnaryWrapper<T, T, std::cos>;

/// Wraps the tan function
template <typename T>
using Tan = UnaryWrapper<T, T, std::tan>;

/// Wraps the arcsin function
template <typename T>
using ArcSin = UnaryWrapper<T, T, std::asin>;

/// Wraps the arcos function
template <typename T>
using ArcCos = UnaryWrapper<T, T, std::acos>;

/// Wraps the arctan function
template <typename T>
using ArcTan = UnaryWrapper<T, T, std::atan>;

/// Wraps the hyperbolic sin function
template <typename T>
using Sinh = UnaryWrapper<T, T, std::sinh>;

/// Wraps the hyperbolic cos function
template <typename T>
using Cosh = UnaryWrapper<T, T, std::cosh>;

/// Wraps the hyperbolic tan function
template <typename T>
using Tanh = UnaryWrapper<T, T, std::tanh>;

/// Wraps the hyperbolic arcsin function
template <typename T>
using ArcSinh = UnaryWrapper<T, T, std::asinh>;

/// Wraps the hyperbolic arccos function
template <typename T>
using ArcCosh = UnaryWrapper<T, T, std::acosh>;

/// Wraps the hyperbolic arctan function
template <typename T>
using ArcTanh = UnaryWrapper<T, T, std::atanh>;

/// Wraps atan2
template <typename T>
using ArcTan2 = BinaryWrapper<T, T, std::atan2>;

/// Wraps fmod
template <typename T>
using Fmod = BinaryWrapper<T, T, std::fmod>;

}  // namespace Pyston

#endif  // PYSTON_FUNCTORS_H
