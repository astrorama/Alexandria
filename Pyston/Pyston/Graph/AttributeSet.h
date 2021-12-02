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

#ifndef PYSTON_ATTRIBUTESET_H
#define PYSTON_ATTRIBUTESET_H

#include "Pyston/Graph/Placeholder.h"
#include "Pyston/PythonExceptions.h"
#include <boost/python/object.hpp>
#include <set>
#include <string>

namespace Pyston {

/**
 * A node that retrieves the value from a dictionary
 */
template <typename T>
class AttrGetter : public Node<T> {
public:
  /**
   * Constructor
   * @param pos
   *    Position of the Placeholder. It will be used to retrieve later the value assigned to it.
   * @param name
   *    The name of the attribute
   */
  AttrGetter(const unsigned pos, const std::string& name) : m_pos{pos}, m_name{name} {}

  /**
   * @copydoc Node<T>::repr
   */
  std::string repr() const override {
    return "_" + std::to_string(m_pos) + "." + m_name;
  }

  /**
   * @copydoc Node::visit
   */
  void visit(Visitor& visitor) const override {
    visitor.enter(this);
    visitor.exit(this);
  }

  /**
   * @copydoc Node::eval
   * @throw
   *    std::out_of_range if the key is missing
   */
  T eval(const Context&, const Arguments& arguments) const override {
    auto& attr_set   = boost::get<AttributeSet>(arguments[m_pos]);
    auto  value_iter = attr_set.find(m_name);
    if (value_iter == attr_set.end()) {
      throw std::out_of_range("AttributeSet object has no attribute '" + m_name + "'");
    }
    return boost::get<T>(value_iter->second);
  }

private:
  unsigned    m_pos;
  std::string m_name;
};

/**
 * Specialization of Placeholder for object-like variables.
 * Note that, unlike other placeholders, this is used only during the evaluation.
 * The final tree uses AttrGetter instances
 */
template <>
class Placeholder<AttributeSet> {
public:
  /**
   * Constructor
   * @param name
   *    Name of the Placeholder. It will be used to retrieve later the value assigned to it.
   * @param attrs
   *    Acceptable attribute names, with an instance of the acceptable type
   */
  Placeholder(const unsigned pos, const AttributeSet& attrs) : m_pos{pos}, m_attrs{attrs} {}

  /**
   * Unfortunately we have to return directly a python object wrapping the appropiate
   * AttrGetter
   * @param name
   *    Parameter name
   * @throws UnrecoverableError
   *    If the name is not a known parameter. Fallback to Python interpretation will not help.
   * @details
   *    It uses a boost visitor to generate the right AttrGetter depending on the
   *    value stored on the prototype object passed to the constructor
   */
  boost::python::object get(const std::string& name) const {
    if (m_attrs.count(name) == 0)
      throw UnrecoverableError("AttributeSet object has no attribute '" + name + "'");
    return boost::apply_visitor(AttrGetterFactory(m_pos, name), m_attrs.at(name));
  }

private:
  unsigned     m_pos;
  AttributeSet m_attrs;

  struct AttrGetterFactory : public boost::static_visitor<boost::python::object> {
    unsigned    m_pos;
    std::string m_name;

    AttrGetterFactory(unsigned pos, const std::string& name) : m_pos{pos}, m_name{name} {}

    template <typename Content>
    boost::python::object operator()(Content) const {
      std::shared_ptr<Node<Content>> node = std::make_shared<AttrGetter<Content>>(m_pos, m_name);
      return boost::python::object(node);
    }
  };
};
}  // namespace Pyston

#endif  // PYSTON_ATTRIBUTESET_H
