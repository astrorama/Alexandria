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

#ifndef GRIDCONTAINER_GRIDCELLMANAGERVECTOROFVECTORS_H
#define GRIDCONTAINER_GRIDCELLMANAGERVECTOROFVECTORS_H

#include "AlexandriaKernel/memory_tools.h"
#include "GridContainer/GridCellManagerTraits.h"
#include <cstddef>
#include <vector>

namespace Euclid {
namespace GridContainer {

template <typename T>
struct VectorValueProxy;

/**
 * It allocates a conceptual vector of vectors container as a single
 * vector traversed in strides.
 */
template <typename T>
struct GridCellManagerVectorOfVectors {

  /**
   * Iterator that strides over the underlying vector, so +1 actually steps n positions
   */
  struct StrideIterator {
    StrideIterator(typename std::vector<T>::iterator start, int stride) : m_i(start), m_stride(stride) {}

    bool operator!=(const StrideIterator& other) const {
      return m_i != other.m_i;
    }

    bool operator>(const StrideIterator& other) const {
      return m_i > other.m_i;
    }

    StrideIterator& operator++() {
      m_i += m_stride;
      return *this;
    }

    StrideIterator& operator+=(int diff) {
      m_i += diff;
      return *this;
    }

    ptrdiff_t operator-(const StrideIterator& other) const {
      return (m_i - other.m_i) / m_stride;
    }

    VectorValueProxy<T> operator*() {
      return {m_i, m_i + m_stride};
    }

    VectorValueProxy<T> operator->() {
      return {m_i, m_i + m_stride};
    }

  private:
    typename std::vector<T>::iterator m_i;
    int                               m_stride;
  };

  /**
   * Constructor
   * @param size
   *    Number of cells
   * @param nested_values
   *    Number of values per cell
   */
  GridCellManagerVectorOfVectors(size_t size, int nested_values)
      : m_values(size * nested_values), m_cell_size(nested_values) {}

  /**
   * Destructor
   */
  ~GridCellManagerVectorOfVectors() = default;

  /**
   * Non-copyable to avoid expensive copies by mistake
   */
  GridCellManagerVectorOfVectors(const GridCellManagerVectorOfVectors&) = delete;

  /**
   * Movable
   */
  GridCellManagerVectorOfVectors(GridCellManagerVectorOfVectors&&) = default;

  /**
   * Access cell
   * @param i
   *    Cell index
   * @return
   *    A reference to the first value on the cell i
   */
  VectorValueProxy<T> operator[](int i) {
    auto iter = m_values.begin() + i * m_cell_size;
    return {iter, iter + m_cell_size};
  }

  size_t getCellSize() const {
    return m_cell_size;
  }

  size_t getTotalSize() const {
    return m_values.size();
  }

private:
  std::vector<T> m_values;
  int            m_cell_size;

  friend struct GridCellManagerTraits<GridCellManagerVectorOfVectors>;
};

template <typename T>
struct VectorValueProxy {
  using iterator       = typename std::vector<T>::iterator;
  using const_iterator = typename std::vector<T>::const_iterator;

  iterator begin() {
    return m_begin;
  }

  iterator end() {
    return m_end;
  }

  const_iterator begin() const {
    return m_begin;
  }

  const_iterator end() const {
    return m_end;
  }

  std::size_t size() const {
    return m_end - m_begin;
  }

  VectorValueProxy* operator->() const {
    return const_cast<VectorValueProxy*>(this);
  }

  VectorValueProxy& operator=(const VectorValueProxy& other) {
    std::copy(other.begin(), other.end(), begin());
    return *this;
  }

  bool operator==(const VectorValueProxy& other) const {
    return size() == other.size() && std::equal(m_begin, m_end, other.m_begin);
  }

  bool operator!=(const VectorValueProxy& other) const {
    return size() != other.size() || !std::equal(m_begin, m_end, other.m_begin);
  }

  operator std::vector<T>() const {
    return {begin(), end()};
  }

  T& operator[](const size_t i) {
    return *(m_begin + i);
  }

  const T& operator[](const size_t i) const {
    return *(m_begin + i);
  }

private:
  VectorValueProxy(typename std::vector<T>::iterator begin_, typename std::vector<T>::iterator end_)
      : m_begin(begin_), m_end(end_){};

  typename std::vector<T>::iterator m_begin, m_end;

  friend struct GridCellManagerVectorOfVectors<T>;
};

/**
 * GridCellManagerTraits specialization
 */
template <typename T>
struct GridCellManagerTraits<GridCellManagerVectorOfVectors<T>> {
  typedef std::vector<double>                                        data_type;
  typedef VectorValueProxy<T>                                        reference_type;
  typedef VectorValueProxy<T>                                        pointer_type;
  typedef typename GridCellManagerVectorOfVectors<T>::StrideIterator iterator;

  static std::unique_ptr<GridCellManagerVectorOfVectors<T>> factory(size_t size, size_t nested_values) {
    return Euclid::make_unique<GridCellManagerVectorOfVectors<T>>(size, nested_values);
  }

  static iterator begin(GridCellManagerVectorOfVectors<T>& c) {
    return {c.m_values.begin(), c.m_cell_size};
  }

  static iterator end(GridCellManagerVectorOfVectors<T>& c) {
    return {c.m_values.end(), c.m_cell_size};
  }
};
}  // namespace GridContainer
}  // namespace Euclid

#endif  // GRIDCONTAINER_GRIDCELLMANAGERVECTOROFVECTORS_H
