/**
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
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

#ifndef PYSTON_EXCEPTIONS_H
#define PYSTON_EXCEPTIONS_H

#include <ElementsKernel/Exception.h>
#include <ElementsKernel/Logging.h>
#include <boost/python/object.hpp>

namespace Pyston {

/**
 * Exception class
 * Used to wrap Python exceptions so the caller code can handle them
 * transparently
 */
class Exception : public Elements::Exception {
public:
  /// Traceback location
  struct Location {
    std::string filename, funcname;
    long        lineno;
  };

  /**
   * Constructor
   * The error message is retrieved from the exception thrown inside Python
   * @note
   *    If there is no error set on the Python side, a generic error will be used instead
   * @note
   *    The constructor will take care of calling PyErr_clear
   * @warning
   *    The caller is assumed to own the global interlock!
   */
  Exception();

  /// @return Error traceback
  const std::list<Location>& getTraceback() const;

  /// Log error message and traceback
  const Exception& log(log4cpp::Priority::Value level, Elements::Logging& logger) const;

  /// Call PyErr_Restore and restore the error. This can be used when Pyston::Exception goes back to Python.
  void restore() const;

private:
  std::list<Location>   m_traceback;
  boost::python::object m_error_type;
  boost::python::object m_error_value;
  boost::python::object m_error_traceback;
};

}  // end of namespace Pyston

#endif  // PYSTON_EXCEPTIONS_H
