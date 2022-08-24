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

#include "Pyston/GIL.h"

namespace Pyston {

static size_t s_lock_count = 0;

GILLocker::GILLocker() {
  if (Py_IsInitialized()) {
    m_state = PyGILState_Ensure();
    ++s_lock_count;
  }
}

GILLocker::~GILLocker() {
  if (Py_IsInitialized()) {
    PyGILState_Release(m_state);
  }
}

size_t GILLocker::getLockCount() {
  return s_lock_count;
}

GILReleaser::GILReleaser(PyGILState_STATE& state) : m_state(state) {
  PyGILState_Release(m_state);
}

GILReleaser::GILReleaser(GILLocker& locker) : m_state(locker.m_state) {
  PyGILState_Release(m_state);
}

GILReleaser::~GILReleaser() {
  m_state = PyGILState_Ensure();
  ++s_lock_count;
}

}  // end of namespace Pyston
