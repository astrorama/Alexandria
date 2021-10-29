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

#ifndef PYSTON_TEXTREPRVISITOR_H
#define PYSTON_TEXTREPRVISITOR_H

#include "Pyston/Graph/Node.h"
#include <list>

namespace Pyston {

/**
 * Visit a computation tree, and generate a (more or less) human readable
 * representation of it
 */
class TextReprVisitor : public Visitor {
public:
  /**
   * Constructor
   * @param out_stream
   *    Serialize into this stream
   */
  TextReprVisitor(std::ostream& out_stream);

  /**
   * @copydoc Visitor::enter
   */
  void enter(const NodeBase* base) override;

  /**
   * @copydoc Visitor::exit
   */
  void exit(const NodeBase* node) override;

protected:
  std::ostream&                     m_stream;
  std::list<std::list<std::string>> m_stack;
};

}  // end of namespace Pyston

#endif  // PYSTON_TEXTREPRVISITOR_H
