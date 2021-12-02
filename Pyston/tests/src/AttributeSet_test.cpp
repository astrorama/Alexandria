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
#include "Pyston/Graph/AttributeSet.h"
#include "PythonFixture.h"
#include <boost/test/unit_test.hpp>

using namespace Pyston;
namespace py = boost::python;

BOOST_AUTO_TEST_SUITE(AttributeSet_test)

/**
 * Base case, all good
 */
BOOST_FIXTURE_TEST_CASE(GoodAttribute_test, PythonFixture) {
  auto         add = py::eval("lambda o, y: 5 * o.flux + y");
  AttributeSet prototype{{"flux", 0.}};
  auto         X = std::make_shared<Placeholder<AttributeSet>>(0, prototype);
  auto         Y = std::make_shared<Placeholder<double>>(1);

  auto                                       py_comp = add(X, Y);
  py::extract<std::shared_ptr<Node<double>>> comp(py_comp);

  BOOST_TEST_MESSAGE(textRepr(comp()));

  prototype["flux"] = 22.;
  BOOST_CHECK_EQUAL(comp()->eval(prototype, 55.), 165.);
  BOOST_CHECK_EQUAL(comp()->eval(prototype, -55.), 55.);
}

/**
 * Ask for an unknown attribute
 */
BOOST_FIXTURE_TEST_CASE(NoAttribute_test, PythonFixture) {
  auto         add = py::eval("lambda o, y: o.radius + y");
  AttributeSet prototype{{"flux", 0.}};
  auto         X = std::make_shared<Placeholder<AttributeSet>>(0, prototype);
  auto         Y = std::make_shared<Placeholder<double>>(1);

  BOOST_CHECK_THROW(add(X, Y), py::error_already_set);
  Exception e;
  BOOST_TEST_MESSAGE(e.what());
}

/**
 * Pass the wrong set of attributes when calling the compiled version
 */
BOOST_FIXTURE_TEST_CASE(NoAttributeCall_test, PythonFixture) {
  auto         add = py::eval("lambda o, y: o.flux + y");
  AttributeSet prototype{{"flux", 0.}};
  auto         X = std::make_shared<Placeholder<AttributeSet>>(0, prototype);
  auto         Y = std::make_shared<Placeholder<double>>(1);

  auto                                       py_comp = add(X, Y);
  py::extract<std::shared_ptr<Node<double>>> comp(py_comp);

  BOOST_TEST_MESSAGE(textRepr(comp()));
  prototype.erase("flux");
  prototype["radius"] = 55l;
  BOOST_CHECK_THROW(comp()->eval(prototype, 123.), std::out_of_range);
}

/**
 * A double used as an object
 */
BOOST_FIXTURE_TEST_CASE(InvalidArgument_test, PythonFixture) {
  auto add = py::eval("lambda o, y: o.flux + y");
  auto X   = std::make_shared<Placeholder<double>>(0);
  auto Y   = std::make_shared<Placeholder<double>>(1);

  BOOST_CHECK_THROW(add(X, Y), py::error_already_set);
  Exception e;
  BOOST_TEST_MESSAGE(e.what());
}

/**
 * Pass a wrong value on the AttributeSet
 */
BOOST_FIXTURE_TEST_CASE(InvalidArgumentCall_test, PythonFixture) {
  auto         add = py::eval("lambda o, y: o.flux + y");
  AttributeSet prototype{{"flux", 0.}};
  auto         X = std::make_shared<Placeholder<AttributeSet>>(0, prototype);
  auto         Y = std::make_shared<Placeholder<double>>(1);

  auto                                       py_comp = add(X, Y);
  py::extract<std::shared_ptr<Node<double>>> comp(py_comp);

  BOOST_TEST_MESSAGE(textRepr(comp()));

  prototype["flux"] = true;
  BOOST_CHECK_THROW(comp()->eval(prototype, 55.), boost::bad_get);
}

/**
 * Use an expression that can not be compiled
 */
BOOST_FIXTURE_TEST_CASE(NotCompiled_test, PythonFixture) {
  py::exec(R"PYCODE(
def with_conditional(o, y):
  if o.flux > 0:
    return np.sqrt(o.flux) + y
  else:
    return o.flux - y**2
)PYCODE",
           main_namespace);

  auto         py_func = main_namespace["with_conditional"];
  AttributeSet prototype{{"flux", -2.}};
  auto         ret = py_func(prototype, 4.);
  double       rv  = py::extract<double>(ret);

  BOOST_CHECK_CLOSE(rv, -18., 1e-8);

  prototype["flux"] = 16l;
  ret               = py_func(prototype, 8.);
  rv                = py::extract<double>(ret);
  BOOST_CHECK_CLOSE(rv, 12., 1e-8);
}

BOOST_AUTO_TEST_SUITE_END()
