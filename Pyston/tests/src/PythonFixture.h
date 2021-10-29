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

#ifndef PYSTON_PYTHONFIXTURE_H
#define PYSTON_PYTHONFIXTURE_H

#include "Pyston/Exceptions.h"
#include "Pyston/Module.h"
#include "Pyston/Util/GraphvizGenerator.h"
#include "Pyston/Util/TextReprVisitor.h"
#include <boost/python/exec.hpp>
#include <boost/python/extract.hpp>
#include <boost/python/import.hpp>
#include <boost/python/object.hpp>
#include <boost/test/unit_test.hpp>
#include <boost/test/unit_test_monitor.hpp>
#include <iomanip>

namespace Pyston {

struct PythonFixture {

  struct Singleton {
    Singleton() {
      if (PyImport_AppendInittab("pyston", PYSTON_MODULE_INIT) == -1)
        abort();
      Py_Initialize();
#if PY_MAJOR_VERSION == 3 && PY_MINOR_VERSION <= 6
      PyEval_InitThreads();
#endif
      PyEval_SaveThread();
    }
  };

  boost::python::object main_namespace;
  PyGILState_STATE      gil_state;

  static void boost_py_exc(const boost::python::error_already_set&) {
    Exception e;
    BOOST_FAIL(e.what());
  }

  PythonFixture() {
    static Singleton singleton;
    gil_state                = PyGILState_Ensure();
    auto main_module         = boost::python::import("__main__");
    main_namespace           = main_module.attr("__dict__");
    main_namespace["pyston"] = boost::python::import("pyston");
    main_namespace["np"]     = boost::python::import("numpy");
    main_namespace["np"]     = boost::python::import("numpy");
    // Register python exceptions
    boost::unit_test::unit_test_monitor.register_exception_translator<boost::python::error_already_set>(&boost_py_exc);
  }

  ~PythonFixture() {
    PyGILState_Release(gil_state);
  }

  template <typename T>
  std::string textRepr(const std::shared_ptr<Node<T>>& root) const {
    std::stringstream text_stream;
    TextReprVisitor   text_visitor{text_stream};
    root->visit(text_visitor);
    return text_stream.str();
  }
};

}  // end of namespace Pyston

#endif  // PYSTON_PYTHONFIXTURE_H
