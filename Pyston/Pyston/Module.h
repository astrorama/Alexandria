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

#ifndef PYSTON_MODULE_H
#define PYSTON_MODULE_H

#include <Python.h>

extern "C" {
/**
 * Method used by Python to import this library. It can be used directly when
 * embedding via:
 *    PyImport_AppendInittab("pyston", &PyInit_pyston)
 * This *must* be done before calling Py_Initialize
 */
#if PY_MAJOR_VERSION >= 3
PyObject* PyInit_pyston(void);

#define PYSTON_MODULE_INIT &PyInit_pyston
#else
void initpyston(void);

#define PYSTON_MODULE_INIT &initpyston
#endif
}

#endif  // PYSTON_MODULE_H
