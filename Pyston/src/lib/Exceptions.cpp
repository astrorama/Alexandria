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

  py::handle<> handle_type(ptype);
  py::handle<> handle_value(pvalue);
  py::handle<> handle_traceback(py::allow_null(ptraceback));

  // Get only the error message
  py::object err_msg_obj(py::handle<>(PyObject_Str(pvalue)));
  m_error_msg = py::extract<std::string>(err_msg_obj);
  if (m_error_msg.empty()) {
    py::object err_repr_obj(py::handle<>(PyObject_Repr(pvalue)));
    m_error_msg = py::extract<std::string>(err_repr_obj);
  }

  // Generate traceback
  if (ptraceback) {
    py::object traceback(handle_traceback);
    while (traceback) {
      Location loc;
      loc.lineno   = py::extract<long>(traceback.attr("tb_lineno"));
      loc.filename = py::extract<std::string>(traceback.attr("tb_frame").attr("f_code").attr("co_filename"));
      loc.funcname = py::extract<std::string>(traceback.attr("tb_frame").attr("f_code").attr("co_name"));

      m_traceback.emplace_back(loc);

      traceback = traceback.attr("tb_next");
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

}  // end of namespace Pyston
