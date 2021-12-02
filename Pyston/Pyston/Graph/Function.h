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

#ifndef PYSTON_FUNCTION_H
#define PYSTON_FUNCTION_H

#include "Node.h"
#include <functional>
#include <memory>
#include <string>
#include <vector>

namespace Pyston {

/**
 * Template class for unary operators
 * @tparam R
 *  Operator return type
 * @tparam T
 *  Operator parameter type
 */
template <typename R, typename... Args>
class Function : public Node<R> {
public:
  using functor_t  = std::function<R(const Context&, Args...)>;
  using children_t = std::tuple<std::shared_ptr<Node<Args>>...>;

  /**
   * Constructor
   * @param node
   *    Value to which the operator will be applied
   * @param functor
   *    Implements the operator
   * @param repr
   *    Human readable representation of the functor (i.e. +, -, abs, exp, ...)
   */
  Function(const std::string& repr_, std::function<R(const Context&, Args...)> functor,
           const std::shared_ptr<Node<Args>>... args)
      : m_repr(repr_), m_functor(functor), m_children(args...) {}

  /**
   * @copydoc Node::repr
   */
  std::string repr() const final {
    return m_repr;
  }

  /**
   * @copydoc Node::eval
   */
  R eval(const Context& context, const Arguments& args) const final;

  /**
   * @copydoc Node::visit
   */
  void visit(Visitor& visitor) const final;

private:
  std::string m_repr;
  functor_t   m_functor;
  children_t  m_children;
};

template <typename Signature>
class FunctionFactory;

/**
 * Specialization for functions that receive a context
 *
 * @tparam R
 *  Type corresponding to the created new Node
 * @tparam T
 *  Type corresponding to the received Node
 */
template <typename R, typename... Args>
class FunctionFactory<R(Args...)> {
public:
  /**
   * Constructor
   * @param functor
   *    The functor that will be passed down to the created UnaryOperator nodes
   * @param repr
   *    Human readable representation of the operator
   */
  FunctionFactory(const std::string& repr, std::function<R(const Context&, Args...)> functor)
      : m_repr(repr), m_functor(functor) {}

  /**
   * Callable that creates the Node
   * @details
   *    This is what gets called from Python when an operator is used. For instance `-a` will
   *    trigger a call `factory(a)`. Unlike the BinaryOperatorFactory, this will *not* be called
   *    is a is not of type Node, since there would be no reason to!
   */
  std::shared_ptr<Node<R>> operator()(const std::shared_ptr<Node<Args>>&... nodes) const {
    return std::make_shared<Function<R, Args...>>(m_repr, m_functor, nodes...);
  }

protected:
  std::string                               m_repr;
  std::function<R(const Context&, Args...)> m_functor;
};

}  // end of namespace Pyston

#define PYSTON_GRAPH_FUNCTION_IMPL
#include "_impl/Function.icpp"
#undef PYSTON_GRAPH_FUNCTION_IMPL

#endif  // PYSTON_FUNCTION_H
