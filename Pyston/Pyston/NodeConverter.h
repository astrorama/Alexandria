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

#ifndef PYSTON_NODECONVERTER_H
#define PYSTON_NODECONVERTER_H

#include "Pyston/Graph/Constant.h"
#include <boost/python.hpp>

namespace Pyston {

/**
 * Create a new Cast Node from a Node of some other type (i.e. bool => float)
 * @tparam From
 *    Original type
 * @param object
 *    Python object
 * @param storage
 *    Memory area, handled by boost::python, where to store the new object
 * @return
 *    true if it could be converted
 */
template <typename To, typename From>
static bool createCastNode(boost::python::object& object, void* storage) {
  using boost::python::extract;

  extract<std::shared_ptr<Node<From>>> extractor(object);
  if (!extractor.check())
    return false;

  new (storage) std::shared_ptr<Node<To>>(new Cast<To, From>(extractor));

  return true;
}

/**
 * Cast between node types
 * @tparam T
 *  Node type
 */
template <typename T>
struct NodeCast {
  /**
   * @return
   *    true if the object can be converted to T via an upcast
   */
  static bool isUpcast(PyObject*) {
    return false;
  }

  /**
   * Try to create cast nodes from different known Node types
   * @return
   *    true if it could be converted
   */
  static bool cast(PyObject*, void*) {
    return false;
  }
};

/**
 * Trait specialization for double
 * booleans and integers can be upcasted to double
 */
template <>
struct NodeCast<double> {

  /**
   * @copydoc NodeCast::isUpcast
   */
  static bool isUpcast(PyObject* obj_ptr) {
    using boost::python::borrowed;
    using boost::python::extract;
    using boost::python::handle;
    using boost::python::object;

    object                 object(handle<>(borrowed(obj_ptr)));
    extract<Node<bool>>    bool_extract(object);
    extract<Node<int64_t>> int_extract(object);

    if (bool_extract.check() || int_extract.check()) {
      return true;
    }

    return false;
  }

  /**
   * @copydoc NodeCast::cast
   */
  static bool cast(PyObject* obj_ptr, void* storage) {
    using boost::python::borrowed;
    using boost::python::handle;
    using boost::python::object;

    object object(handle<>(borrowed(obj_ptr)));

    return createCastNode<double, bool>(object, storage) || createCastNode<double, int64_t>(object, storage);
  }
};

/**
 * Trait specialization for integers
 * booleans can be upcasted to integers
 */
template <>
struct NodeCast<int64_t> {

  /**
   * @copydoc NodeCast::isUpcast
   */
  static bool isUpcast(PyObject* obj_ptr) {
    using boost::python::borrowed;
    using boost::python::extract;
    using boost::python::handle;
    using boost::python::object;

    object              object(handle<>(borrowed(obj_ptr)));
    extract<Node<bool>> bool_extract(object);

    return bool_extract.check();
  }

  /**
   * @copydoc NodeCast::cast
   */
  static bool cast(PyObject* obj_ptr, void* storage) {
    using boost::python::borrowed;
    using boost::python::handle;
    using boost::python::object;

    object object(handle<>(borrowed(obj_ptr)));

    return createCastNode<int64_t, bool>(object, storage);
  }
};

/**
 * Implements the conversion logic from python primitives into Node
 * @tparam T
 *  Node type *into* which types can be converted
 */
template <typename T>
struct NodeConverter {
  /**
   * Check if the python object can be converted to a known type
   * @param obj_ptr
   *    Python object
   * @return
   *    obj_ptr if it can be converted, NULL otherwise
   */
  static void* isConvertible(PyObject* obj_ptr) {
    using boost::python::borrowed;
    using boost::python::extract;
    using boost::python::handle;
    using boost::python::object;
    using boost::python::converter::registry::query;

    // Primitive numeric types are ok
#if PY_MAJOR_VERSION >= 3
    if (PyFloat_Check(obj_ptr) || PyLong_Check(obj_ptr) || PyBool_Check(obj_ptr)) {
      return obj_ptr;
    }
#else
    if (PyFloat_Check(obj_ptr) || PyLong_Check(obj_ptr) || PyBool_Check(obj_ptr) || PyInt_Check(obj_ptr)) {
      return obj_ptr;
    }
#endif

    // Upcasting one type of node to another is too
    if (NodeCast<T>::isUpcast(obj_ptr)) {
      return obj_ptr;
    }

    // Can't
    return nullptr;
  }

  /**
   * Create a new Constant Node from a python primitive type: python floats, longs or booleans
   * @param obj_ptr
   *    Python object
   * @param storage
   *    Memory area, handled by boost::python, where to store the new object
   * @return
   *    true if it could be converted
   */
  static bool fromPrimitive(PyObject* obj_ptr, void* storage) {
    // Rely on the casting done by C++
    T value = 0;
    if (PyFloat_Check(obj_ptr)) {
      value = PyFloat_AsDouble(obj_ptr);
    } else if (PyLong_Check(obj_ptr)) {
      value = PyLong_AsLong(obj_ptr);
    } else if (PyBool_Check(obj_ptr)) {
      value = (obj_ptr == Py_True);
#if PY_MAJOR_VERSION < 3
    } else if (PyInt_Check(obj_ptr)) {
      value = PyInt_AsLong(obj_ptr);
#endif
    } else {
      return false;
    }

    new (storage) std::shared_ptr<Node<T>>(new Constant<T>(value));
    return true;
  }

  /**
   * Construct a new Node type from the given python object
   * @param obj_ptr
   *    Python object
   * @param data
   *    boost python data required to construct the new object
   */
  static void construct(PyObject* obj_ptr, boost::python::converter::rvalue_from_python_stage1_data* data) {
    // Memory area where to store the new type
    void* storage =
        ((boost::python::converter::rvalue_from_python_storage<std::shared_ptr<Node<T>>>*)data)->storage.bytes;

    // Abort if can not convert, because isConvertible hasn't done its job
    if (!fromPrimitive(obj_ptr, storage) && !NodeCast<T>::cast(obj_ptr, storage))
      abort();

    data->convertible = storage;
  }
};

}  // end of namespace Pyston

#endif  // PYSTON_NODECONVERTER_H
