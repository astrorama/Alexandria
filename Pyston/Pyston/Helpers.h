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

#ifndef PYSTON_HELPERS_H
#define PYSTON_HELPERS_H

#include "Pyston/Graph/Cast.h"
#include "Pyston/Graph/Function.h"
#include <boost/python.hpp>
#include <memory>

namespace Pyston {

template <typename Signature>
struct makeFunctionHelper;

/**
 * Create a function factory for functions that expect a context
 */
template <typename R, typename... Args>
struct makeFunctionHelper<R(const Context&, Args...)> {
  static boost::python::object make(const std::string& repr, std::function<R(const Context&, Args...)> functor) {
    return boost::python::make_function(
        FunctionFactory<R(Args...)>(repr, functor), boost::python::default_call_policies(),
        boost::mpl::vector<std::shared_ptr<Node<R>>, const std::shared_ptr<Node<Args>>&...>());
  }
};

/**
 * Create a function factory for functions that do *not* expect a context, wrapping them
 * into a lambda expression that just ignores it
 */
template <typename R, typename... Args>
struct makeFunctionHelper<R(Args...)> {
  static boost::python::object make(const std::string& repr, std::function<R(Args...)> functor) {
    auto wrapped = [functor](const Context&, Args... args) { return functor(args...); };
    return boost::python::make_function(
        FunctionFactory<R(Args...)>(repr, wrapped), boost::python::default_call_policies(),
        boost::mpl::vector<std::shared_ptr<Node<R>>, const std::shared_ptr<Node<Args>>&...>());
  }
};

template <typename Signature>
struct makeBinaryFunctionHelper;

/**
 * Function factory specifically for binary functions, with the additional option to reverse
 * them
 * @tparam R
 *  Return type
 * @tparam T
 *  Type of the parameter
 */
template <typename R, typename T>
struct makeBinaryFunctionHelper<R(T, T)> {

  static boost::python::object make(const std::string& repr, std::function<R(T, T)> functor, bool reversed) {
    FunctionFactory<R(T, T)> factory(repr, [functor](const Context&, T l, T r) { return functor(l, r); });

    return boost::python::make_function(
        [factory, reversed](const std::shared_ptr<Node<T>>& left, const std::shared_ptr<Node<T>>& right) {
          if (reversed)
            return factory(right, left);
          return factory(left, right);
        },
        boost::python::default_call_policies(),
        boost::mpl::vector<std::shared_ptr<Node<R>>, const std::shared_ptr<Node<T>>&,
                           const std::shared_ptr<Node<T>>&>());
  }
};

/**
 * @details
 *  boost::python seems to have some trouble attaching functors as methods
 *  to python objects, so it requires some massaging in order to figure out the signature,
 *  keep the reference alive, etc.
 *  Since the code is a bit convolved, we isolate it here to make it easier to use
 * @tparam Signature
 *  Signature of the functor
 * @param repr
 *  Literal representation of the node, for pretty-printing
 * @param functor
 *  Functor to insert
 * @return
 *  A callable python object
 */
template <typename Signature>
static boost::python::object makeFunction(const std::string& repr, std::function<Signature> functor) {
  return makeFunctionHelper<Signature>::make(repr, functor);
}

/**
 * @details
 *  Special case that allows to create calls to binary functions, supporting the reversal
 *  or arguments if needed, which is the case for methods like __rmul__, __rpow__ and similar
 *  The functor can only receive parameters of the same type. Any required casting will
 *  be done by NodeConverter
 * @tparam Signature
 *  Signature of the functor that receives two parameters *of the same type*
 * @param repr
 *  Literal representation of the node, for pretty-printing
 * @param functor
 *  Functor to insert
 * @return
 *  A callable python object
 */
template <typename Signature>
static boost::python::object makeBinaryFunction(const std::string& repr, std::function<Signature> functor,
                                                bool reversed = false) {
  return makeBinaryFunctionHelper<Signature>::make(repr, functor, reversed);
}

}  // namespace Pyston

#endif  // PYSTON_HELPERS_H
