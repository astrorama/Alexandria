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

#ifndef PYSTON_GIL_H
#define PYSTON_GIL_H

#include <Python.h>

namespace Pyston {

/**
 * RAII for the Global Interlock: Acquires at construction and releases at destruction
 */
class GILLocker {
public:
  GILLocker();

  ~GILLocker();

  static size_t getLockCount();

protected:
  PyGILState_STATE m_state;
  friend class GILReleaser;
};

/**
 * RAII for the Global Interlock: Releases at construction and locks at destruction
 */
class GILReleaser {
public:
  explicit GILReleaser(PyGILState_STATE& state);

  explicit GILReleaser(GILLocker&);

  ~GILReleaser();

protected:
  PyGILState_STATE& m_state;
};

class SaveThread {
public:
  SaveThread();

  ~SaveThread();

protected:
  PyThreadState* m_state;
};

}  // end of namespace Pyston

#endif  // PYSTON_GIL_H
