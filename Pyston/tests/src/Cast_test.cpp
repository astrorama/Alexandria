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
#include <Pyston/Exceptions.h>
#include <boost/test/unit_test.hpp>

using namespace Pyston;
namespace py = boost::python;

BOOST_AUTO_TEST_SUITE(UnaryOperator_test)

/**
 * Cast a boolean to left of the operator into a float
 */
BOOST_FIXTURE_TEST_CASE(OpBoolFloat_test, PythonFixture) {
  auto function = py::eval("lambda x, y: (x > 0.) * y", main_namespace);
  auto X        = std::make_shared<Placeholder<double>>(0);
  auto Y        = std::make_shared<Placeholder<double>>(1);

  auto                                       py_comp = function(X, Y);
  py::extract<std::shared_ptr<Node<double>>> comp(py_comp);

  BOOST_CHECK_EQUAL(comp()->eval(4., 2.), 2.);
  BOOST_CHECK_EQUAL(comp()->eval(-4., 2.), 0.);
}

/**
 * Cast a boolean to the right of the operator into a float
 */
BOOST_FIXTURE_TEST_CASE(OpFloatBool_test, PythonFixture) {
  auto function = py::eval("lambda x, y: y * (x > 0.)", main_namespace);
  auto X        = std::make_shared<Placeholder<double>>(0);
  auto Y        = std::make_shared<Placeholder<double>>(1);

  auto                                       py_comp = function(X, Y);
  py::extract<std::shared_ptr<Node<double>>> comp(py_comp);

  BOOST_CHECK_EQUAL(comp()->eval(4., 2.), 2.);
  BOOST_CHECK_EQUAL(comp()->eval(-4., 2.), 0.);
}

/**
 * Cast a boolean to an integer (5 * bool), and the integer into a float (+y)
 */
BOOST_FIXTURE_TEST_CASE(OpInt_test, PythonFixture) {
  auto function = py::eval("lambda x, y: (5 * (x > 0.)) / y", main_namespace);
  auto X        = std::make_shared<Placeholder<double>>(0);
  auto Y        = std::make_shared<Placeholder<double>>(1);

  auto                                       py_comp = function(X, Y);
  py::extract<std::shared_ptr<Node<double>>> comp(py_comp);

  BOOST_TEST_MESSAGE(textRepr(comp()));

  BOOST_CHECK_CLOSE(comp()->eval(4., 2.), 2.5, 1e-8);
  BOOST_CHECK_EQUAL(comp()->eval(-4., 2.), 0.);
}

/**
 * Cast a boolean to an integer (bool * 5), and the integer into a float (y +)
 * Operators are reverse to test the cast is done properly regardless
 */
BOOST_FIXTURE_TEST_CASE(OpIntReversed_test, PythonFixture) {
  auto function = py::eval("lambda x, y: y / ((x > 0.) * 5)", main_namespace);
  auto X        = std::make_shared<Placeholder<double>>(0);
  auto Y        = std::make_shared<Placeholder<double>>(1);

  auto                                       py_comp = function(X, Y);
  py::extract<std::shared_ptr<Node<double>>> comp(py_comp);

  BOOST_CHECK_CLOSE(comp()->eval(4., 2.), 0.4, 1e-8);
  BOOST_CHECK(std::isinf(comp()->eval(-4., 2.)));
}

/**
 * Using a placeholder on a flow control statement is not allowed
 */
BOOST_FIXTURE_TEST_CASE(AsBool_test, PythonFixture) {
  auto function = py::eval("lambda x: 0 if x else 1");
  auto X        = std::make_shared<Placeholder<double>>(0);
  BOOST_CHECK_THROW(function(X), py::error_already_set);
}

/**
 * Visit a graph with casts
 */
BOOST_FIXTURE_TEST_CASE(Visit_test, PythonFixture) {
  auto function = py::eval("lambda x, y: y + (x > 0.) * 5", main_namespace);
  auto X        = std::make_shared<Placeholder<double>>(0);
  auto Y        = std::make_shared<Placeholder<double>>(1);

  auto                                       py_comp = function(X, Y);
  py::extract<std::shared_ptr<Node<double>>> comp(py_comp);

  auto txt = textRepr(comp());
  if (sizeof(long) == 8) {
    BOOST_CHECK_EQUAL(txt, "(_1 + double((long((_0 > 0.000000)) * 5)))");
  } else {
    BOOST_CHECK_EQUAL(txt, "(_1 + double((long long((_0 > 0.000000)) * 5)))");
  }
}

BOOST_AUTO_TEST_SUITE_END()
