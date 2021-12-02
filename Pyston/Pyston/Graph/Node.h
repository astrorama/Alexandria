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

#ifndef PYSTON_NODE_H
#define PYSTON_NODE_H

#include <boost/any.hpp>
#include <boost/variant.hpp>
#include <map>
#include <memory>
#include <string>
#include <typeindex>
#include <vector>

namespace Pyston {

// Forward declaration
class Visitor;

/**
 * To make the visitor independent of the primitive type wrapped by a Node, all instances
 * of the templated class inherit from this one, which declares the API required by the visitor
 */
class NodeBase {
public:
  /**
   * Constructor
   * @param type_info
   *    Type info of the inheriting Node T
   */
  explicit NodeBase(const std::type_index& type_index) : m_type_index{type_index} {}

  /**
   * Destructor
   */
  virtual ~NodeBase() = default;

  /**
   * @return
   *    A human readable representation of the node
   * @note
   *    It should *not* include the representation of the children, if any.
   *    That's what visitors are for.
   */
  virtual std::string repr() const = 0;

  /**
   * Entry point for the visitor
   */
  virtual void visit(Visitor&) const = 0;

  /**
   * @return
   *    The type information of the inheriting Node
   */
  const std::type_index& type() const {
    return m_type_index;
  }

private:
  const std::type_index m_type_index;
};

/**
 * Arbitrary key/value pairs, interpreted as an object attribute
 */
using Attribute    = boost::variant<bool, int64_t, double>;
using AttributeSet = std::map<std::string, Attribute>;

/**
 * Can hold any values a Placeholder may require
 */
using Value = boost::variant<bool, int64_t, double, AttributeSet>;

/**
 * A vector where the values correspond to the position placeholders have,
 * on the function call.
 */
using Arguments = std::vector<Value>;

/**
 * Arbitrary key/value pairing for giving a context to function calls
 */
using Context = std::map<std::string, boost::any>;

/**
 * A node on the computing tree, which has an associated primitive type
 */
template <typename T>
class Node : public NodeBase {
public:
  /**
   * Constructor
   */
  Node() : NodeBase(typeid(T)) {}

  /**
   * Destructor
   */
  virtual ~Node() = default;

  /**
   * Evaluate the computing tree
   * @details
   *    In principle one could avoid to pass any values here, and assign directly the
   *    final value to the placeholders that were used to create this tree. However, this
   *    would cause the placeholders not to be thread-safe, and a tree would have to be either
   *    cloned, either protected by a mutex.
   *    Passing the values as an argument allows making the full tree immutable once built,
   *    and fully thread safe.
   * @return
   *    Result of the evaluation
   */
  virtual T eval(const Context&, const Arguments&) const = 0;

  template <typename... Args>
  T eval(const Context& context, Args... args) const {
    Arguments arguments;
    return eval_helper(context, arguments, args...);
  }

  template <typename... Args>
  T eval(Args... args) const {
    return eval(Context{}, args...);
  }

protected:
  T eval_helper(const Context& context, Arguments& arguments) const {
    return eval(context, arguments);
  }

  template <typename A0, typename... AN>
  T eval_helper(const Context& context, Arguments& arguments, A0 v0, AN... an) const {
    arguments.push_back(v0);
    return eval_helper(context, arguments, an...);
  }
};

/**
 * Base class for visitors of a computing tree.
 * @details
 *  Leaf nodes will call enter and, immediately after, exit.
 *  For binary operators, the left side is visited first
 */
class Visitor {
public:
  /**
   * Called when a node is entered
   */
  virtual void enter(const NodeBase*) = 0;

  /**
   * Called when a node is left
   */
  virtual void exit(const NodeBase*) = 0;
};

}  // end of namespace Pyston

#endif  // PYSTON_NODE_H
