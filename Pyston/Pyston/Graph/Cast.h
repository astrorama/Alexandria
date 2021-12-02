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

#ifndef PYSTON_CAST_H
#define PYSTON_CAST_H

#include "Node.h"

#if BOOST_VERSION < 105600
#include <boost/units/detail/utility.hpp>
using boost::units::detail::demangle;
#else
using boost::core::demangle;
#endif

namespace Pyston {

/**
 * Node type that casts one type of value into another.
 * This is required so we can, for instance, add a boolean to a float.
 * @tparam To
 *  Cast type
 * @tparam From
 *  Casted type
 */
template <typename To, typename From>
class Cast : public Node<To> {
public:
  /**
   * Constructor
   * @param node
   *    Wrapped node, for which its eval result will be casted to To
   */
  explicit Cast(const std::shared_ptr<Node<From>>& node) : m_node{node} {}

  /**
   * @copydoc Node::repr
   */
  std::string repr() const final {
    return demangle(typeid(To).name());
  }

  /**
   * @copydoc Node::eval
   */
  To eval(const Context& context, const Arguments& args) const final {
    return static_cast<To>(m_node->eval(context, args));
  }

  /**
   * @copydoc Node::visit
   */
  void visit(Visitor& visitor) const final {
    visitor.enter(this);
    m_node->visit(visitor);
    visitor.exit(this);
  }

private:
  std::shared_ptr<Node<From>> m_node;
};

}  // end of namespace Pyston

#endif  // PYSTON_CAST_H
