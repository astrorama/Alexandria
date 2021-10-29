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

#ifndef PYSTON_PLACEHOLDER_H
#define PYSTON_PLACEHOLDER_H

#include "Node.h"

namespace Pyston {

/**
 * Placeholder node, pretty much like a variable.
 * @tparam T
 *  Type of the placeholder
 */
template <typename T>
class Placeholder : public Node<T> {
public:
  /**
   * Constructor
   * @param pos
   *    Position of the Placeholder. It will be used to retrieve later the value assigned to it.
   */
  explicit Placeholder(const unsigned pos) : m_pos{pos} {}

  /**
   * @copydoc Node::repr
   */
  std::string repr() const final {
    return "_" + std::to_string(m_pos);
  }

  /**
   * @copydoc Node::eval
   * @throw std::out_of_range
   *    There is no value assigned to this placeholder
   * @throw boost::bad_get
   *    The type of the value assigned to the placeholder does not correspond to the
   *    expected type T
   */
  T eval(const Context&, const Arguments& args) const final {
    return boost::get<T>(args.at(m_pos));
  }

  /**
   * @copydoc Node::visit
   */
  void visit(Visitor& visitor) const final {
    visitor.enter(this);
    visitor.exit(this);
  }

private:
  unsigned m_pos;
};

}  // end of namespace Pyston

#endif  // PYSTON_PLACEHOLDER_H
