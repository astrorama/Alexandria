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

#include "Pyston/ExceptionRaiser.h"
#include "Pyston/Graph/AttributeSet.h"
#include "Pyston/Graph/Functors.h"
#include "Pyston/Graph/Placeholder.h"
#include "Pyston/Helpers.h"
#include "Pyston/NodeConverter.h"
#include "Pyston/PythonExceptions.h"
#include <boost/python.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>

#if BOOST_VERSION < 105600
#include <boost/units/detail/utility.hpp>
using boost::units::detail::demangle;
#else
using boost::core::demangle;
#endif

namespace py = boost::python;

#if BOOST_VERSION < 106300
namespace boost {
namespace python {
namespace converter {

template <class T>
PyObject* shared_ptr_to_python(std::shared_ptr<T> const& x) {
  if (!x)
    return python::detail::none();
  else if (shared_ptr_deleter* d = std::get_deleter<shared_ptr_deleter>(x))
    return incref(get_pointer(d->owner));
  else
    return converter::registered<std::shared_ptr<T> const&>::converters.to_python(&x);
}

}  // namespace converter
}  // namespace python
}  // namespace boost
#endif

namespace Pyston {

// Sadly these have to be global
PyObject* pyRecoverableError   = nullptr;
PyObject* pyUnrecoverableError = nullptr;

template <typename T>
struct RegisterNode {

  using NodeType = py::class_<Node<T>, boost::noncopyable>;

  /**
   * Define operations where the other value has a different type (To)
   * i.e. if __add__ is called on a boolean, and the other value (To) is a float,
   * self has to be upcasted
   */
  template <typename To>
  static void defCastOperations(NodeType& node) {
    node.def("__add__", makeBinaryFunction<To(To, To)>("+", std::plus<To>()))
        .def("__sub__", makeBinaryFunction<To(To, To)>("-", std::minus<To>()))
        .def("__mul__", makeBinaryFunction<To(To, To)>("*", std::multiplies<To>()))
        .def("__truediv__", makeBinaryFunction<To(To, To)>("/", std::divides<To>()))
        .def("__radd__", makeBinaryFunction<To(To, To)>("+", std::plus<To>(), true))
        .def("__rsub__", makeBinaryFunction<To(To, To)>("-", std::minus<To>(), true))
        .def("__rmul__", makeBinaryFunction<To(To, To)>("x", std::multiplies<To>(), true))
        .def("__rtruediv__", makeBinaryFunction<To(To, To)>("/", std::divides<To>(), true));
  }

  /**
   * Methods for specific types
   */
  template <typename Y>
  static void specialized(NodeType& node, void*);

  /**
   * Methods for floating point types
   */
  template <typename Y>
  static void specialized(NodeType& node, typename std::enable_if<std::is_floating_point<Y>::value>::type* = nullptr) {
    node.def("__pow__", makeFunction<T(T, T)>("^", Pow<T>()))
        .def("__rpow__", makeBinaryFunction<T(T, T)>("^", Pow<T>(), true))
        .def("__round__", makeFunction<T(T)>("round", Round<T>()))
        .def("__abs__", makeFunction<T(T)>("abs", Abs<T>()));

    // Functions
    // When using numpy methods, numpy will delegate to these
    // Taken from here, although there are a bunch not implemented:
    // https://numpy.org/devdocs/reference/ufuncs.html
    node.def("exp", makeFunction<T(T)>("exp", Exp<T>()))
        .def("exp2", makeFunction<T(T)>("exp2", Exp2<T>()))
        .def("log", makeFunction<T(T)>("log", Log<T>()))
        .def("log2", makeFunction<T(T)>("log2", Log2<T>()))
        .def("log10", makeFunction<T(T)>("log10", Log10<T>()))
        .def("sqrt", makeFunction<T(T)>("sqrt", Sqrt<T>()))
        .def("sin", makeFunction<T(T)>("sin", Sin<T>()))
        .def("cos", makeFunction<T(T)>("cos", Cos<T>()))
        .def("tan", makeFunction<T(T)>("tan", Tan<T>()))
        .def("arcsin", makeFunction<T(T)>("arcsin", ArcSin<T>()))
        .def("arccos", makeFunction<T(T)>("arccos", ArcCos<T>()))
        .def("arctan", makeFunction<T(T)>("arctan", ArcTan<T>()))
        .def("arctan2", makeBinaryFunction<T(T, T)>("arctan2", ArcTan2<T>()))
        .def("sinh", makeFunction<T(T)>("sinh", Sinh<T>()))
        .def("cosh", makeFunction<T(T)>("cosh", Cosh<T>()))
        .def("tanh", makeFunction<T(T)>("tanh", Tanh<T>()))
        .def("arcsinh", makeFunction<T(T)>("arcsinh", ArcSinh<T>()))
        .def("arccosh", makeFunction<T(T)>("arccosh", ArcCosh<T>()))
        .def("arctanh", makeFunction<T(T)>("arctanh", ArcTanh<T>()))
        .def("fmod", makeFunction<T(T, T)>("fmod", Fmod<T>()));
  }

  /**
   * Methods for the boolean type
   */
  template <typename Y>
  static void specialized(NodeType& node, typename std::enable_if<std::is_same<Y, bool>::value>::type* = nullptr) {
    // Upcast to double and int
    defCastOperations<double>(node);
    defCastOperations<int64_t>(node);
  }

  /**
   * Methods for integral types, except bool
   */
  template <typename Y>
  static void
  specialized(NodeType& node,
              typename std::enable_if<std::is_integral<Y>::value && !std::is_same<Y, bool>::value>::type* = nullptr) {
    node.def("__abs__", makeFunction<T(T)>("abs", Abs<T>()));
    // Upcast to double
    defCastOperations<double>(node);
    node.def("__pow__", makeBinaryFunction<double(double, double)>("^", Pow<double>()))
        .def("__rpow__", makeBinaryFunction<double(double, double)>("^", Pow<double>(), true));
  }

  static void general(NodeType& node) {
    // https://docs.python.org/3/reference/datamodel.html#basic-customization
    node.def("__lt__", makeFunction<bool(T, T)>("<", std::less<T>()))
        .def("__le__", makeFunction<bool(T, T)>("<=", std::less_equal<T>()))
        .def("__eq__", makeFunction<bool(T, T)>("==", std::equal_to<T>()))
        .def("__ne__", makeFunction<bool(T, T)>("!=", std::not_equal_to<T>()))
        .def("__gt__", makeFunction<bool(T, T)>(">", std::greater<T>()))
        .def("__ge__", makeFunction<bool(T, T)>(">=", std::greater_equal<T>()));

    // https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
    node.def("__add__", makeFunction<T(T, T)>("+", std::plus<T>()))
        .def("__sub__", makeFunction<T(T, T)>("-", std::minus<T>()))
        .def("__mul__", makeFunction<T(T, T)>("*", std::multiplies<T>()))
        .def("__truediv__", makeFunction<T(T, T)>("/", std::divides<T>()))
        .def("__div__", makeFunction<T(T, T)>("/", std::divides<T>()))
        .def("__radd__", makeBinaryFunction<T(T, T)>("+", std::plus<T>(), true))
        .def("__rsub__", makeBinaryFunction<T(T, T)>("-", std::minus<T>(), true))
        .def("__rmul__", makeBinaryFunction<T(T, T)>("*", std::multiplies<T>(), true))
        .def("__rtruediv__", makeBinaryFunction<T(T, T)>("/", std::divides<T>(), true))
        .def("__rdiv__", makeBinaryFunction<T(T, T)>("/", std::divides<T>(), true))
        .def("__neg__", makeFunction<T(T)>("-", std::negate<T>()))
        .def("__pos__", makeFunction<T(T)>("+", (Identity<T>())));

    // Can not be used in conditionals!
#if PY_MAJOR_VERSION >= 3
#define AS_BOOL_METHOD "__bool__"
#else
#define AS_BOOL_METHOD "__nonzero__"
#endif
    node.def(AS_BOOL_METHOD,
             py::make_function(ExceptionRaiser<T>("Can not use variable placeholders in conditionals", true),
                               py::default_call_policies(),
                               boost::mpl::vector<void, const std::shared_ptr<Node<T>>>()));
  }

  static void Do() {
    auto     node_name = std::string("Node<") + demangle(typeid(T).name()) + ">";
    NodeType node(node_name.c_str(), "AST Node", py::no_init);

    // Operators and method applicable to all types
    general(node);

    // Operators and method applicable only to a given type
    // i.e. __floordiv__ is not applicable to float
    specialized<T>(node);

    // Register convertion between shared pointer and Node
    py::register_ptr_to_python<std::shared_ptr<Node<T>>>();
#if BOOST_VERSION < 106300
    py::implicitly_convertible<std::shared_ptr<Placeholder<T>>, std::shared_ptr<Node<T>>>();
#endif
    // Custom conversion so primitive values can be converted to a node
    py::converter::registry::push_back(&NodeConverter<T>::isConvertible, &NodeConverter<T>::construct,
                                       py::type_id<std::shared_ptr<Node<T>>>());

    // Triggers the building of a tree
    auto placeholder_name = std::string("Placeholder<") + demangle(typeid(T).name()) + ">";
    py::class_<Placeholder<T>, py::bases<Node<T>>>(placeholder_name.c_str(), "Variable placeholder", py::no_init);
    py::register_ptr_to_python<std::shared_ptr<Placeholder<T>>>();
  }
};

/**
 * Allow to use AttributeSet directly from Python
 */
struct VariantToPython : public boost::static_visitor<boost::python::object> {
  template <typename Content>
  py::object operator()(Content c) const {
    return py::object(c);
  }
};

py::object attributeSetGetter(const AttributeSet& attr_set, const std::string& name) {
  auto vi = attr_set.find(name);
  if (vi == attr_set.end()) {
    throw UnrecoverableError("AttributeSet has no attribute '" + name + "'");
  }
  return boost::apply_visitor(VariantToPython(), vi->second);
}

/**
 * Register the attribute set placeholder
 */
void RegisterAttributeSet() {
  py::class_<Placeholder<AttributeSet>, boost::noncopyable> node("AttributeSet", "AST Node", py::no_init);

  // Register convertion between shared pointer and Node
  py::register_ptr_to_python<std::shared_ptr<Placeholder<AttributeSet>>>();

  // Register __getattr__
  node.def("__getattr__", &Placeholder<AttributeSet>::get);

  // Register AttributeSet so it can be used directly from Python for
  // non-compiled expressions
  py::class_<AttributeSet> attr_set("AttributeSet", "Attribute set", py::no_init);
  attr_set.def("__getattr__", &attributeSetGetter);
}

/**
 * Create a new exception on the Python side
 * @details
 *  Used by Recoverable and Unrecoverable errors, which can not be directly exposed,
 *  since they do not (and can not due to boost::python API limitations) inherit from Python's Exception
 */
static PyObject* createExceptionClass(const std::string& name) {
  std::string scope   = py::extract<std::string>(py::scope().attr("__name__"));
  std::string qname   = scope + "." + name;
  PyObject*   excType = PyErr_NewException(const_cast<char*>(qname.c_str()), PyExc_RuntimeError, nullptr);
  if (!excType)
    py::throw_error_already_set();
  py::scope().attr(name.c_str()) = py::handle<>(py::borrowed(excType));
  return excType;
}

/**
 * Translate C++ recoverable exception to its Python counterpart
 */
void translateRecoverable(const RecoverableError& e) {
  PyErr_SetString(pyRecoverableError, e.what());
}

/**
 * Translate C++ unrecoverable exception to its Python counterpart
 */
void translateUnrecoverable(const UnrecoverableError& e) {
  PyErr_SetString(pyUnrecoverableError, e.what());
}

BOOST_PYTHON_MODULE(pyston) {
  RegisterNode<double>::Do();
  RegisterNode<int64_t>::Do();
  RegisterNode<bool>::Do();

  // AttributeSet is a bit special
  RegisterAttributeSet();

  // Vector types
  py::class_<std::vector<double>>("_DoubleVector").def(py::vector_indexing_suite<std::vector<double>>());
  py::class_<std::vector<int64_t>>("_IntVector").def(py::vector_indexing_suite<std::vector<int64_t>>());

  // Exceptions
  pyRecoverableError   = createExceptionClass("RecoverableError");
  pyUnrecoverableError = createExceptionClass("UnrecoverableError");

  // Exception translation
  py::register_exception_translator<RecoverableError>(&translateRecoverable);
  py::register_exception_translator<UnrecoverableError>(&translateUnrecoverable);
}

}  // end of namespace Pyston
