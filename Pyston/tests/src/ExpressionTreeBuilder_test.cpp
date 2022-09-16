/*
 * Copyright (C) 2022 Euclid Science Ground Segment
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

#include "Pyston/ExpressionTreeBuilder.h"
#include "Pyston/Graph/Functors.h"
#include "PythonFixture.h"
#include <boost/test/unit_test.hpp>

using namespace Pyston;
namespace py = boost::python;

BOOST_AUTO_TEST_SUITE(FunctionWrapper_test)

/**
 * Wrap a simple lambda expression. It should be able to
 * translate directly, so no more calls to Python are required
 */
BOOST_FIXTURE_TEST_CASE(Wrapper_test, PythonFixture) {
  ExpressionTreeBuilder builder;
  auto                  py_func = py::eval("lambda x, y: x**2 + y");

  std::function<double(double, double)> transparent;
  {
    auto tree = builder.build<double(double, double)>(py_func);
    BOOST_CHECK(tree.isCompiled());
    BOOST_TEST_MESSAGE(textRepr(tree.getTree()));
    transparent = tree;
  }
  // Original is out of scope, std::function should still be alive
  BOOST_CHECK_EQUAL(transparent(3, 2), 11);
}

/**
 * Wrap a lambda expression that can *not* be translated, since one of the
 * variables is used on a flow control statement (if).
 * It should still be callable, even if through the interpreter. The flag
 * must be set accordingly in any case.
 */
BOOST_FIXTURE_TEST_CASE(WrapperFallback_test, PythonFixture) {
  ExpressionTreeBuilder builder;
  auto                  py_func = py::eval("lambda x, y, z: x ** 2 + y if z > 0.5 else z", main_namespace);

  std::function<double(double, double, double)> transparent;
  // Call directly
  {
    auto tree = builder.build<double(double, double, double)>(py_func);
    BOOST_CHECK(!tree.isCompiled());
    BOOST_TEST_MESSAGE(textRepr(tree.getTree()));
    transparent = tree;
  }
  // Original is out of scope, std::function should still be alive
  BOOST_CHECK_EQUAL(transparent(1, 2, 0.6), 3);
  BOOST_CHECK_EQUAL(transparent(1, 2, 0.4), 0.4);
}

/**
 * Wrap a lambda expression that can *not* be translated, and that,
 * on top of it, will raise an exception in some cases. The wrapper must
 * be able to catch and translate into a C++ exception.
 */
BOOST_FIXTURE_TEST_CASE(WrapperException_test, PythonFixture) {
  ExpressionTreeBuilder builder;
  py::exec(R"PYCODE(
def raises_exception(x, y, z):
  if z > 0.5:
    return x **2 + y
  else:
    raise ValueError('Invalid Z value')
)PYCODE",
           main_namespace);

  std::function<double(double, double, double)> transparent;
  {
    auto py_func = main_namespace["raises_exception"];
    auto tree    = builder.build<double(double, double, double)>(py_func);
    BOOST_CHECK(!tree.isCompiled());
    BOOST_TEST_MESSAGE(textRepr(tree.getTree()));
    transparent = tree;
  }

  // Call that succeeds
  BOOST_CHECK_EQUAL(transparent(1, 2, 0.6), 3);

  // Call that raises exception
  try {
    transparent(1, 2, 0.4);
    BOOST_FAIL("Call should have raised an exception");
  } catch (const Exception& ex) {
    BOOST_CHECK_EQUAL(std::string(ex.what()), "ValueError: Invalid Z value");
    BOOST_CHECK_GT(ex.getTraceback().size(), 0);
    bool func_in_trace = false;
    for (auto& trace : ex.getTraceback()) {
      BOOST_TEST_MESSAGE(trace.filename << ": " << trace.funcname << " line " << trace.lineno);
      func_in_trace |= trace.funcname == "raises_exception";
    }
    BOOST_CHECK(func_in_trace);
  }
}

/**
 * Custom functions
 */
template <typename T>
struct World2Pixel {
  T operator()(const Context& context, T x) const {
    double scale = 3.;
    if (context.count("scale"))
      scale = boost::any_cast<double>(context.at("scale"));
    return std::sin(x) * scale;
  }
};

double mishmash(double x, double y) {
  return std::asinh(x) - std::log(y / 2);
}

/**
 * Register a custom unary function, evaluated within an Expression Tree
 */
BOOST_FIXTURE_TEST_CASE(AddUnaryFunction_test, PythonFixture) {
  ExpressionTreeBuilder builder;
  builder.registerFunction<double(const Context&, double)>("world2pixel", World2Pixel<double>());

  py::exec(R"PYCODE(
def uses_function(x, y):
  return pyston.world2pixel(x + y)
)PYCODE",
           main_namespace);

  std::function<double(const Context&, double, double)> transparent;
  {
    auto py_func = main_namespace["uses_function"];
    auto tree    = builder.build<double(double, double)>(py_func);
    BOOST_CHECK(tree.isCompiled());
    BOOST_TEST_MESSAGE(textRepr(tree.getTree()));
    transparent = tree;
  }

  double r = transparent({{"scale", 20.}}, 10, 20);
  BOOST_CHECK_CLOSE(r, std::sin(30.) * 20, 1e-8);

  r = transparent({{"scale", 5.4}}, 10, 20);
  BOOST_CHECK_CLOSE(r, std::sin(30.) * 5.4, 1e-8);
}

/**
 * Register an unary function, evaluated directly via Python since there is
 * a conditional
 */
BOOST_FIXTURE_TEST_CASE(AddUnaryFunctionNonCompilable_test, PythonFixture) {
  ExpressionTreeBuilder builder;
  builder.registerFunction<double(const Context&, double)>("world2pixel", World2Pixel<double>());

  py::exec(R"PYCODE(
def uses_function(x, y):
  if y > x:
    return pyston.world2pixel(x + y)
  else:
    return y
)PYCODE",
           main_namespace);

  std::function<double(const Context&, double, double)> transparent;
  {
    auto py_func = main_namespace["uses_function"];
    auto tree    = builder.build<double(double, double)>(py_func);
    BOOST_CHECK(!tree.isCompiled());
    BOOST_TEST_MESSAGE(textRepr(tree.getTree()));
    transparent = tree;
  }

  double r = transparent({{"scale", 20.}}, 10, 20);
  BOOST_CHECK_CLOSE(r, std::sin(30.) * 20., 1e-8);

  r = transparent({{"scale", 5.4}}, 20, 10);
  BOOST_CHECK_CLOSE(r, 10., 1e-8);
}

/**
 * Register a binary function, evaluated within an Expression Tree
 */
BOOST_FIXTURE_TEST_CASE(AddBinaryFunction_test, PythonFixture) {
  ExpressionTreeBuilder builder;
  builder.registerFunction<double(double, double)>("mishmash", &mishmash);

  py::exec(R"PYCODE(
def uses_function(x, y):
  return pyston.mishmash(x * 2, y)
)PYCODE",
           main_namespace);

  std::function<double(double, double)> transparent;
  {
    auto py_func = main_namespace["uses_function"];
    auto tree    = builder.build<double(double, double)>(py_func);
    BOOST_CHECK(tree.isCompiled());
    BOOST_TEST_MESSAGE(textRepr(tree.getTree()));
    transparent = tree;
  }

  double r = transparent(10, 20);
  BOOST_CHECK_CLOSE(r, mishmash(10 * 2, 20), 1e-8);
}

/**
 * Register a binary function, evaluated directly via Python since there is
 * a conditional
 */
BOOST_FIXTURE_TEST_CASE(AddBinaryFunctionNonCompilable_test, PythonFixture) {
  ExpressionTreeBuilder builder;
  builder.registerFunction<double(double, double)>("mishmash", &mishmash);

  py::exec(R"PYCODE(
def uses_function(x, y):
  if y > 0:
    return pyston.mishmash(x * 2, y)
  else:
    return -1
)PYCODE",
           main_namespace);

  std::function<double(double, double)> transparent;
  {
    auto py_func = main_namespace["uses_function"];
    auto tree    = builder.build<double(double, double)>(py_func);
    BOOST_CHECK(!tree.isCompiled());
    BOOST_TEST_MESSAGE(textRepr(tree.getTree()));
    transparent = tree;
  }

  double r = transparent(10, 20);
  BOOST_CHECK_CLOSE(r, mishmash(10 * 2, 20), 1e-8);

  r = transparent(22, -1);
  BOOST_CHECK_EQUAL(r, -1.);
}

/**
 * Compile a function that receives an object
 */
BOOST_FIXTURE_TEST_CASE(WithObject_test, PythonFixture) {
  ExpressionTreeBuilder builder;

  auto         py_func = py::eval("lambda o, y: np.log(o.flux) * y", main_namespace);
  AttributeSet prototype{{"flux", 0.}};

  std::function<double(AttributeSet, double)> transparent;
  {
    auto tree = builder.build<double(AttributeSet, double)>(py_func, prototype);
    BOOST_CHECK(tree.isCompiled());
    BOOST_TEST_MESSAGE(textRepr(tree.getTree()));
    transparent = tree;
  }

  prototype["flux"] = 42.;
  double r          = transparent(prototype, 5);
  BOOST_CHECK_CLOSE(r, 18.68835, 1e-4);
}

/**
 * Non compilable function that receives an object
 */
BOOST_FIXTURE_TEST_CASE(WithObjectNonCompilable_test, PythonFixture) {
  ExpressionTreeBuilder builder;

  py::exec(R"PYCODE(
def non_compilable(o, y):
  if o.flux > 0:
    return np.log(o.flux)
  else:
    return y
)PYCODE",
           main_namespace);

  AttributeSet                                prototype{{"flux", 0.}};
  std::function<double(AttributeSet, double)> transparent;
  {
    auto py_func = main_namespace["non_compilable"];
    auto tree    = builder.build<double(AttributeSet, double)>(py_func, prototype);
    BOOST_CHECK(!tree.isCompiled());
    BOOST_TEST_MESSAGE(textRepr(tree.getTree()));
    transparent = tree;
  }

  prototype["flux"] = 88.;
  double r          = transparent(prototype, 5);
  BOOST_CHECK_CLOSE(r, 4.477337, 1e-4);

  prototype["flux"] = -4.;
  r                 = transparent(prototype, 5);
  BOOST_CHECK_CLOSE(r, 5, 1e-8);
}

/**
 * Attribute set by reference should be acceptable too
 */
BOOST_FIXTURE_TEST_CASE(WithObjectRef_test, PythonFixture) {
  ExpressionTreeBuilder builder;

  auto         py_func = py::eval("lambda o, y: np.log(o.flux) * y", main_namespace);
  AttributeSet prototype{{"flux", 0.}};

  std::function<double(const AttributeSet&, double)> transparent;
  {
    auto tree = builder.build<double(const AttributeSet&, double)>(py_func, prototype);
    BOOST_CHECK(tree.isCompiled());
    BOOST_TEST_MESSAGE(textRepr(tree.getTree()));
    transparent = tree;
  }

  prototype["flux"] = 42.;
  double r          = transparent(prototype, 5);
  BOOST_CHECK_CLOSE(r, 18.68835, 1e-4);
}

/**
 * Function with variable, unknown at compile time, number of parameters
 */
BOOST_FIXTURE_TEST_CASE(WithVectorOfDouble_test, PythonFixture) {
  ExpressionTreeBuilder builder;
  auto                  py_func = py::eval("lambda x, y, z: x + y + z", main_namespace);

  std::function<double(const std::vector<double>&)> transparent;
  {
    auto tree = builder.build<double(const std::vector<double>&)>(py_func, 3);
    BOOST_CHECK(tree.isCompiled());
    BOOST_TEST_MESSAGE(textRepr(tree.getTree()));
    transparent = tree;
  }

  double r = transparent({1, 2, 3});
  BOOST_CHECK_EQUAL(6, r);
}

/**
 * Accessing an unknown attribute must be a fast-fail
 */
BOOST_FIXTURE_TEST_CASE(UnknownAttribute_test, PythonFixture) {
  ExpressionTreeBuilder builder;
  auto                  py_func = py::eval("lambda x: x.radius + 10", main_namespace);

  AttributeSet prototype{{"flux", 0.}};
  BOOST_CHECK_THROW(builder.build<double(const AttributeSet&)>(py_func, prototype), Exception);
}

/**
 * Using an unknown member of, say, numpy, must be fast-fail
 */
BOOST_FIXTURE_TEST_CASE(UnknownNumpyMethod_test, PythonFixture) {
  ExpressionTreeBuilder builder;
  auto                  py_func = py::eval("lambda x: np.grapefruit(x)", main_namespace);

  BOOST_CHECK_THROW(builder.build<double(double)>(py_func), Exception);
}

/**
 * Attribute set with no prototype, should not even compile
 * Uncomment to actually test this
 */
/*
BOOST_FIXTURE_TEST_CASE(WithObjectForgotPrototype_test, PythonFixture) {
 ExpressionTreeBuilder builder;

 auto py_func = py::eval("lambda o, y: np.log(o.flux) * y", main_namespace);
 AttributeSet prototype{{"flux", 0.}};

 builder.build < double(
 const AttributeSet&, double)>(py_func);
}
*/

BOOST_AUTO_TEST_SUITE_END()
