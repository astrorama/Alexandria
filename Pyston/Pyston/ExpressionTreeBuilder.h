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

#ifndef PYSTON_EXPRESSIONTREEBUILDER_H
#define PYSTON_EXPRESSIONTREEBUILDER_H

#include <boost/python/list.hpp>
#include <boost/python/object.hpp>
#include <boost/python/object/add_to_namespace.hpp>
#include <boost/python/tuple.hpp>
#include <functional>
#include <tuple>

#include "Pyston/Exceptions.h"
#include "Pyston/ExpressionTree.h"
#include "Pyston/GIL.h"
#include "Pyston/Graph/AttributeSet.h"
#include "Pyston/Graph/Placeholder.h"
#include "Pyston/Helpers.h"

namespace Pyston {

/**
 * Builds an expression tree from a Python function, given its signature.
 * If it is not possible to do so (for instance, due to the use of branching conditional
 * on some placeholder), it will wrap the Python function in a compatible manner
 */
class ExpressionTreeBuilder {
public:
  /**
   * Build an expression tree, or wrap the Python function in a compatible manner
   * @tparam Signature
   *    Function signature (i.e. double(double,double))
   * @param pyfunc
   *    Python object pointing to a callable. Its signature must match the template.
   * @param build_params
   *    Required build parameters: either prototypes for AttributeSet, if any is passed along,
   *    or the number of elements for functions with variable number of parameters
   * @return
   *    A pair, where the first value is a boolean set to `true` if an expression tree could
   *    be built, false otherwise. The second value is the wrapping functor.
   */
  template <typename Signature, typename... BuildParams>
  ExpressionTree<Signature> build(const boost::python::object& pyfunc, BuildParams&&... build_params) const {
    return buildHelper<Signature>::build(pyfunc, std::forward<BuildParams>(build_params)...);
  }

  /**
   * Register a function
   * @tparam Signature
   *    Function signature
   * @param repr
   *    Function name
   * @note
   *    The return and parameter types are deduced from the Signature
   */
  template <typename Signature>
  void registerFunction(const std::string& repr, std::function<Signature> functor);

private:
  /**
   * Required to support function signatures
   */
  template <typename Signature>
  struct buildHelper;

  /**
   * Specialization for functions that receive a variable number of arguments of
   * the same type
   * @tparam R
   *    Return type
   * @tparam T
   *    Parameter type
   */
  template <typename R, typename T>
  struct buildHelper<R(const std::vector<T>&)> {
    static ExpressionTree<R(const std::vector<T>&)> build(const boost::python::object&, size_t n);
  };

  /**
   * Specialization that "unwraps" the function signature into return type and arguments
   */
  template <typename R, typename... Args>
  struct buildHelper<R(Args...)> {
    template <typename... Prototypes>
    static ExpressionTree<R(Args...)> build(const boost::python::object&, Prototypes&&...);
  };

  /**
   * Common to buildHelper specializations
   */
  template <typename R, typename... Args>
  static ExpressionTree<R(Args...)> compiledOrWrapped(const boost::python::object& pyfunc,
                                                      const boost::python::list&   placeholders);
};

}  // end of namespace Pyston

#define PYSTON_EXPRESSIONTREEBUILDER_IMPL
#include "Pyston/_impl/ExpressionTreeBuilder.icpp"
#undef PYSTON_EXPRESSIONTREEBUILDER_IMPL

#endif  // PYSTON_EXPRESSIONTREEBUILDER_H
