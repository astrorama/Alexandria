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
#include "PythonFixture.h"
#include <boost/test/unit_test.hpp>

using namespace Pyston;
namespace py = boost::python;

BOOST_AUTO_TEST_SUITE(Constant_test)

BOOST_FIXTURE_TEST_CASE(FloatConstant_test, PythonFixture) {
  auto                          function = py::eval("lambda: 5.", main_namespace);
  auto                          ret      = function();
  std::shared_ptr<Node<double>> node     = py::extract<std::shared_ptr<Node<double>>>(ret);
  BOOST_CHECK_EQUAL(node->repr().substr(0, 2), "5.");
  BOOST_CHECK_EQUAL(node->eval({}), 5.);
}

BOOST_FIXTURE_TEST_CASE(IntConstant_test, PythonFixture) {
  auto                           function = py::eval("lambda: 42", main_namespace);
  auto                           ret      = function();
  std::shared_ptr<Node<int64_t>> node     = py::extract<std::shared_ptr<Node<int64_t>>>(ret);
  BOOST_CHECK_EQUAL(node->repr(), "42");
  BOOST_CHECK_EQUAL(node->eval({}), 42);
}

BOOST_FIXTURE_TEST_CASE(BoolConstant_test, PythonFixture) {
  auto                        function = py::eval("lambda: True", main_namespace);
  auto                        ret      = function();
  std::shared_ptr<Node<bool>> node     = py::extract<std::shared_ptr<Node<bool>>>(ret);
  BOOST_CHECK_EQUAL(node->repr(), "1");
  BOOST_CHECK(node->eval({}));
}

BOOST_FIXTURE_TEST_CASE(IntToFloatConstant_test, PythonFixture) {
  auto                          function = py::eval("lambda: 128", main_namespace);
  auto                          ret      = function();
  std::shared_ptr<Node<double>> node     = py::extract<std::shared_ptr<Node<double>>>(ret);
  BOOST_CHECK_EQUAL(node->eval({}), 128.);
}

BOOST_FIXTURE_TEST_CASE(WrongCast_test, PythonFixture) {
  auto                                       function = py::eval("lambda: 'this is a string'", main_namespace);
  auto                                       ret      = function();
  py::extract<std::shared_ptr<Node<double>>> extractor(ret);
  BOOST_CHECK(!extractor.check());
}

BOOST_FIXTURE_TEST_CASE(ConstantOps_test, PythonFixture) {
  auto                          function = py::eval("lambda: 1 + 2 + 3", main_namespace);
  auto                          ret      = function();
  std::shared_ptr<Node<double>> node     = py::extract<std::shared_ptr<Node<double>>>(ret);
  BOOST_CHECK_EQUAL(node->eval({}), 6);
}

BOOST_FIXTURE_TEST_CASE(ConstantNumpy_test, PythonFixture) {
  auto                          function = py::eval("lambda: np.exp2(1) + np.log10(2**3)", main_namespace);
  auto                          ret      = function();
  std::shared_ptr<Node<double>> node     = py::extract<std::shared_ptr<Node<double>>>(ret);
  BOOST_CHECK_CLOSE(node->eval({}), 2.9031, 1e-3);
}

BOOST_FIXTURE_TEST_CASE(Visit_test, PythonFixture) {
  auto                          function = py::eval("lambda: 1 + 2 + 3", main_namespace);
  auto                          ret      = function();
  std::shared_ptr<Node<double>> node     = py::extract<std::shared_ptr<Node<double>>>(ret);
  auto                          txt      = textRepr(node);
  BOOST_CHECK_EQUAL(txt, "6.000000");
}

BOOST_AUTO_TEST_SUITE_END()
