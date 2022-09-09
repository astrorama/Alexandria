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

#ifndef ALEXANDRIA_BORROWED_H
#define ALEXANDRIA_BORROWED_H

#include <new>

namespace Euclid {
namespace NdArray {

template <typename T>
struct BorrowedRange {
  T* const          m_begin;
  std::size_t const m_size;

  T* data() const {
    return m_begin;
  }

  std::size_t size() const {
    return m_size;
  }

  void resize(std::size_t) const {
    throw std::bad_alloc();
  }
};

}  // namespace NdArray
}  // namespace Euclid

#endif  // ALEXANDRIA_BORROWED_H
