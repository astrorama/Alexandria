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

#ifndef PYSTON_PYTHONCALL_H
#define PYSTON_PYTHONCALL_H

#include "Node.h"
#include "Pyston/Exceptions.h"
#include "Pyston/GIL.h"
#include "Pyston/SharedContext.h"
#include <boost/python/object.hpp>
#include <boost/python/tuple.hpp>

namespace Pyston {

/**
 * A PythonCall node hides a call to a wrapped Python function when
 * the tree can not be evaluated
 */
template <typename T>
class PythonCall : public Node<T> {
public:
  PythonCall(boost::python::object callable) : m_callable(callable) {}

  std::string repr() const override {
    return "PythonCall";
  }

  void visit(Visitor& visitor) const override {
    visitor.enter(this);
    visitor.exit(this);
  }

  T eval(const Context& context, const Arguments& arguments) const override {
    GILLocker locker;
    sharedContext = context;
    try {
      boost::python::list py_args;
      for (auto& a : arguments) {
        py_args.append(boost::apply_visitor(to_python_visitor(), a));
      }
      auto obj = m_callable(*boost::python::tuple(py_args));
      return boost::python::extract<T>(obj);
    } catch (const boost::python::error_already_set&) {
      throw Exception();
    }
  }

private:
  /**
   * Unroll the variant type into a python type
   */
  struct to_python_visitor : public boost::static_visitor<boost::python::object> {
    template <typename From>
    boost::python::object operator()(From v) const {
      return boost::python::object(v);
    }
  };

  boost::python::object m_callable;
};

}  // end of namespace Pyston

#endif  // PYSTON_PYTHONCALL_H
