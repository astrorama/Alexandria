/*
 * Copyright (C) 2012-2020 Euclid Science Ground Segment
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

#ifndef NDARRAY_TEST_H
#define NDARRAY_TEST_H

#include "ElementsKernel/Temporary.h"
#include <boost/filesystem/path.hpp>
#include <boost/process.hpp>
#include <boost/test/unit_test.hpp>
#include <sstream>

/**
 * Run embedded Python code
 */
static std::stringstream runPython(const char* code, const boost::filesystem::path& npy) {
  namespace bp = boost::process;
  Elements::TempFile code_file("npy_%%%%.py");
  std::ofstream      out(code_file.path().native());
  out << code;
  out.close();

  auto python_exec = bp::search_path("python3");
  if (python_exec.empty())
    python_exec = bp::search_path("python");
  BOOST_CHECK(!python_exec.empty());

  bp::ipstream py_output;
  int          r = bp::system(python_exec, code_file.path().native(), npy.native(), bp::std_out > py_output);
  BOOST_CHECK_EQUAL(r, 0);

  std::stringstream stream;
  stream << py_output.rdbuf();
  return stream;
}

#endif  // NDARRAY_TEST_H
