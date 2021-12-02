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

#ifndef PYSTON_CONSTANT_H
#define PYSTON_CONSTANT_H

#include "Node.h"

namespace Pyston {

/**
 * Node that just wraps a constant
 * @tparam T
 *  The type of the constant
 */
template <typename T>
class Constant : public Node<T> {
public:
  /**
   * Constructor
   * @param value
   *    Wrapped value
   */
  explicit Constant(T value) : m_value{value} {}

  /**
   * @copydoc Node::repr
   */
  std::string repr() const final {
    return std::to_string(m_value);
  }

  /**
   * @copydoc Node::eval
   * @note
   *    Obviously this node does nothing with the arguments
   */
  T eval(const Context&, const Arguments&) const final {
    return m_value;
  }

  /**
   * @copydoc Node::visit
   */
  void visit(Visitor& visitor) const final {
    visitor.enter(this);
    visitor.exit(this);
  }

private:
  T m_value;
};

}  // end of namespace Pyston

#endif  // PYSTON_CONSTANT_H
