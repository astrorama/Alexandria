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

#include "Pyston/Exceptions.h"
#include "Pyston/GIL.h"
#include <Python.h>
#include <boost/python/extract.hpp>
#include <boost/python/handle.hpp>
#include <boost/python/object.hpp>

namespace py = boost::python;

namespace Pyston {

Exception::Exception() {
  GILLocker locker;

  PyObject *ptype, *pvalue, *ptraceback;
  PyErr_Fetch(&ptype, &pvalue, &ptraceback);
  PyErr_NormalizeException(&ptype, &pvalue, &ptraceback);

  m_error_type      = py::object(py::handle<>(ptype));
  m_error_value     = py::object(py::handle<>(pvalue));
  m_error_traceback = py::object(py::handle<>(py::allow_null(ptraceback)));

  // Get the error message and exception type
  py::object err_msg_obj(py::handle<>(PyObject_Str(pvalue)));
  m_error_msg = py::extract<std::string>(err_msg_obj);
  if (m_error_msg.empty()) {
    py::object err_repr_obj(py::handle<>(PyObject_Repr(pvalue)));
    m_error_msg = py::extract<std::string>(err_repr_obj);
  }
  py::object err_msg_type(py::handle<>(PyObject_GetAttrString(ptype, "__name__")));
  m_error_msg = std::string(py::extract<std::string>(err_msg_type)) + ": " + m_error_msg;

  // Generate traceback
  if (ptraceback) {
    for (auto traceback = m_error_traceback; traceback; traceback = traceback.attr("tb_next")) {
      Location loc;
      loc.lineno   = py::extract<long>(traceback.attr("tb_lineno"));
      loc.filename = py::extract<std::string>(traceback.attr("tb_frame").attr("f_code").attr("co_filename"));
      loc.funcname = py::extract<std::string>(traceback.attr("tb_frame").attr("f_code").attr("co_name"));
      m_traceback.emplace_back(loc);
    }
  }

  // Done
  PyErr_Clear();
}

auto Exception::getTraceback() const -> const std::list<Location>& {
  return m_traceback;
}

const Exception& Exception::log(log4cpp::Priority::Value level, Elements::Logging& logger) const {
  for (auto& trace : m_traceback) {
    std::stringstream msg;
    msg << "File \"" << trace.filename << "\", line " << trace.lineno << ", in " << trace.funcname;
    logger.log(level, msg.str());
  }
  return *this;
}

void Exception::restore() const {
  PyErr_Restore(py::xincref(m_error_type.ptr()), py::xincref(m_error_value.ptr()), py::xincref(m_error_traceback.ptr()));
}

}  // end of namespace Pyston
