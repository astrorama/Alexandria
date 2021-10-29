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

#include "Pyston/Graph/Node.h"
#include "Pyston/Graph/Placeholder.h"
#include "PythonFixture.h"
#include <boost/test/unit_test.hpp>

using namespace Pyston;
namespace py = boost::python;

BOOST_AUTO_TEST_SUITE(UnaryOperator_test)

BOOST_FIXTURE_TEST_CASE(UnaryDouble_test, PythonFixture) {
  auto negative = py::eval("lambda x: -x", main_namespace);
  auto identity = py::eval("lambda x: +x", main_namespace);
  auto X        = std::make_shared<Placeholder<double>>(0);

  auto py_negative_comp = negative(X);
  auto py_identiy_comp  = identity(X);

  py::extract<std::shared_ptr<Node<double>>> negative_comp(py_negative_comp);
  py::extract<std::shared_ptr<Node<double>>> identity_comp(py_identiy_comp);

  BOOST_CHECK_EQUAL(negative_comp()->eval(22.), -22.);
  BOOST_CHECK_EQUAL(negative_comp()->eval(48.5), -48.5);

  BOOST_CHECK_EQUAL(identity_comp()->eval(22.), 22.);
  BOOST_CHECK_EQUAL(identity_comp()->eval(48.5), 48.5);
}

BOOST_FIXTURE_TEST_CASE(UnaryInt_test, PythonFixture) {
  auto negative = py::eval("lambda x: -x", main_namespace);
  auto identity = py::eval("lambda x: +x", main_namespace);
  auto X        = std::make_shared<Placeholder<int64_t>>(0);

  auto py_negative_comp = negative(X);
  auto py_identiy_comp  = identity(X);

  py::extract<std::shared_ptr<Node<int64_t>>> negative_comp(py_negative_comp);
  py::extract<std::shared_ptr<Node<int64_t>>> identity_comp(py_identiy_comp);

  BOOST_CHECK_EQUAL(negative_comp()->eval(22l), -22);
  BOOST_CHECK_EQUAL(negative_comp()->eval(48l), -48);

  BOOST_CHECK_EQUAL(identity_comp()->eval(22l), 22);
  BOOST_CHECK_EQUAL(identity_comp()->eval(48l), 48);
}

BOOST_FIXTURE_TEST_CASE(Functions_test, PythonFixture) {
  auto log = py::eval("lambda x: np.log(x)", main_namespace);
  auto abs = py::eval("lambda x: np.abs(x)", main_namespace);
  auto cos = py::eval("lambda x: np.cos(x)", main_namespace);
  auto X   = std::make_shared<Placeholder<double>>(0);

  auto py_log_comp = log(X);
  auto py_abs_comp = abs(X);
  auto py_cos_comp = cos(X);

  py::extract<std::shared_ptr<Node<double>>> log_comp(py_log_comp);
  py::extract<std::shared_ptr<Node<double>>> abs_comp(py_abs_comp);
  py::extract<std::shared_ptr<Node<double>>> cos_comp(py_cos_comp);

  // Warning: If compiling with --ffast-math, the compiler assumes there will be
  // no NaN and Inf, so std::isnan will fail to identify a NaN.
  // We wrap the check and do the test depending on the behavior
  auto nan = std::numeric_limits<double>::quiet_NaN();
  if (nan != nan) {
    BOOST_CHECK(std::isnan(log_comp()->eval(-10.)));
  } else {
    BOOST_TEST_MESSAGE("nan == nan, compiled with -ffinite-math-only?");
  }

  BOOST_CHECK_CLOSE(log_comp()->eval(100.), 4.6052, 1e-3);
  BOOST_CHECK_CLOSE(abs_comp()->eval(100.), 100., 1e-3);
  BOOST_CHECK_CLOSE(abs_comp()->eval(-543.), 543., 1e-3);
  BOOST_CHECK_CLOSE(cos_comp()->eval(0.), 1., 1e-3);
  BOOST_CHECK_CLOSE(cos_comp()->eval(M_PI), -1., 1e-3);
}

BOOST_FIXTURE_TEST_CASE(Visit_test, PythonFixture) {
  auto func = py::eval("lambda x: +np.log(-x)", main_namespace);
  auto X    = std::make_shared<Placeholder<double>>(0);

  auto py_comp = func(X);

  py::extract<std::shared_ptr<Node<double>>> comp(py_comp);

  auto txt = textRepr(comp());
  BOOST_CHECK_EQUAL(txt, "+log(-_0)");
}

BOOST_AUTO_TEST_SUITE_END()
