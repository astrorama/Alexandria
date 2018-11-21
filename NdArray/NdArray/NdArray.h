/*
 * Copyright (C) 2012-2020 Euclid Science Ground Segment
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

/**
* @file Matrix/Matrix.h
* @date November 21, 2018
* @author Alejandro Alvarez Ayllon
*/

#ifndef ALEXANDRIA_MATRIX_H
#define ALEXANDRIA_MATRIX_H

#include <numeric>
#include <stdexcept>
#include <vector>


namespace Euclid {
namespace NdArray {

/**
 * Stores a multidimensional array in a contiguous piece of memory in row-major order
 * @tparam T
 *  Data type
 * @tparam Container
 *  Which container to use, by default std::vector
 */
template<typename T, template<class...> class Container = std::vector>
class NdArray {
public:
  typedef typename Container<T>::iterator iterator;
  typedef typename Container<T>::const_iterator const_iterator;

  /**
   * Destructor.
   */
  virtual ~NdArray() = default;

  /**
   * Constructs a default-initialized matrix with the given shape.
   * @param shape
   *    The shape of the matrix. The number of elements in shape corresponds to the number
   *    of dimensions, the values to each dimension size.
   */
  NdArray(const std::vector<size_t> &shape) : m_shape{shape}, m_container(
    std::accumulate(m_shape.begin(), m_shape.end(), 1, std::multiplies<size_t>())) {
    m_stride_size.resize(m_shape.size());

    size_t acc = 1;
    for (int i = m_stride_size.size() - 1; i >= 0; --i) {
      m_stride_size[i] = acc;
      acc *= m_shape[i];
    }
  }

  /**
   * Constructs a matrix and initialize it with the given data.
   * @param shape
   *    The shape of the matrix. The number of elements in shape corresponds to the number
   *    of dimensions, the values to each dimension size.
   * @param data
   *    The initial data. It *must* match exactly the matrix size (shape[0]*shape[1]...*shape[n]).
   * @throws std::invalid_argument
   *    If the data size does not corresponds to the matrix size.
   */
  NdArray(const std::vector<size_t> &shape, const Container<T> &data) : m_shape{shape}, m_container{data} {
    size_t expected_size = std::accumulate(m_shape.begin(), m_shape.end(), 1, std::multiplies<size_t>());
    if (expected_size != m_container.size()) {
      throw std::invalid_argument("Data size does not match the shape");
    }

    m_stride_size.resize(m_shape.size());

    size_t acc = 1;
    for (int i = m_stride_size.size() - 1; i >= 0; --i) {
      m_stride_size[i] = acc;
      acc *= m_shape[i];
    }
  }

  /**
   * Constructs a default-initialized matrix with the given shape (as an initializer list).
   * @param shape
   *    The shape of the matrix. The number of elements in shape corresponds to the number
   *    of dimensions, the values to each dimension size.
   */
  NdArray(const std::initializer_list<size_t> &shape) : NdArray(std::vector<size_t>{shape}) {}

  /**
   * Gets the shape of the matrix.
   * @return
   *    A vector with as many elements as number of dimensions, containing the size of each one.
   */
  const std::vector<size_t> getShape() const {
    return m_shape;
  }

  /**
   * Gets a reference to the value stored at the given coordinates.
   * @param coords
   *    Elements coordinates.
   * @throws std::out_of_range
   *    If the number of coordinates is invalid, or any of them is out of bounds.
   */
  T &at(const std::vector<size_t> &coords) {
    auto offset = getOffset(coords);
    return m_container[offset];
  };

  /**
   * Gets a constant reference to the value stored at the given coordinates
   * @param coords
   *    Elements coordinates.
   * @throws std::out_of_range
   *    If the number of coordinates is invalid, or any of them is out of bounds.
   */
  const T &at(const std::vector<size_t> &coords) const {
    auto offset = getOffset(coords);
    return m_container[offset];
  };

  /**
   * Gets a reference to the value stored at the given coordinates.
   * @param coords
   *    Elements coordinates.
   * @throws std::out_of_range
   *    If the number of coordinates is invalid, or any of them is out of bounds.
   * @note
   *    This is a convenience function that allows access without requiring a vector when the
   *    number of dimensions is known in advance (i.e. `at(x, y, z)` instead of `at(std::vector<size_t>{x, y, z})`).
   */
  template <typename ...D>
  T &at(unsigned i, D... rest) {
    std::vector<size_t> acc{i};
    return at_helper(acc, rest...);
  }

  /**
   * Gets a constant reference to the value stored at the given coordinates.
   * @param coords
   *    Elements coordinates.
   * @throws std::out_of_range
   *    If the number of coordinates is invalid, or any of them is out of bounds.
   * @note
   *    This is a convenience function that allows access without requiring a vector when the
   *    number of dimensions is known in advance (i.e. `at(x, y, z)` instead of `at(std::vector<size_t>{x, y, z})`).
   */
  template <typename ...D>
  const T &at(size_t i, D... rest) const {
    std::vector<size_t> acc{i};
    return at_helper(acc, rest...);
  }

  /**
   * @return An iterator pointing to the first element (which corresponds to the one with
   * the coordinates set to 0).
   */
  iterator begin() {
    return m_container.begin();
  }

  /**
   * @return An iterator pointing just after the last element (which correspond to the one with
   * the coordinates set to (shape[0]-1, shape[1]-1, ... shape[n]-1).
   */
  iterator end() {
    return m_container.end();
  }

  /**
   * @return A constant iterator pointing to the first element (which corresponds to the one with
   * the coordinates set to 0).
   */
  const_iterator begin() const {
    return m_container.begin();
  }

  /**
   * @return A constant iterator pointing just after the last element (which correspond to the one with
   * the coordinates set to (shape[0]-1, shape[1]-1, ... shape[n]-1).
   */
  const_iterator end() const {
    return m_container.end();
  }

private:
  std::vector<size_t> m_shape, m_stride_size;
  Container<T> m_container;

  /**
   * Gets the total offset for the given coordinates.
   * @throws std::out_of_range
   *    If the number of coordinates is invalid, or any of them is out of bounds.
   */
  size_t getOffset(const std::vector<size_t> &coords) const {
    if (coords.size() != m_shape.size()) {
      throw std::out_of_range(
        "Invalid number of coordinates, got " + std::to_string(coords.size()) + ", expected " + std::to_string(m_shape.size())
      );
    }

    size_t offset = 0;
    for (int i = 0; i < coords.size(); ++i) {
      if (coords[i] >= m_shape[i]) {
        throw std::out_of_range(
          std::to_string(coords[i]) + " >= " + std::to_string(m_shape[i]) + " for axis " + std::to_string(i)
        );
      }
      offset += coords[i] * m_stride_size[i];
    }

    assert(offset < m_container.size());
    return offset;
  };

  /**
   * Helper to expand at with a variable number of arguments
   */
  template <typename ...D>
  T &at_helper(std::vector<size_t> &acc, size_t i, D... rest) {
    acc.push_back(i);
    return at_helper(acc, rest...);
  }

  /**
   * Helper to expand at with a variable number of arguments (base case)
   */
  T &at_helper(std::vector<size_t> &acc) {
    return at(acc);
  }

  /**
   * Helper to expand constant at with a variable number of arguments
   */
  template <typename ...D>
  const T &at_helper(std::vector<size_t> &acc, size_t i, D... rest) const {
    acc.push_back(i);
    return at_helper(acc, rest...);
  }

  /**
   * Helper to expand constant at with a variable number of arguments (base case)
   */
  const T &at_helper(std::vector<size_t> &acc) const {
    return at(acc);
  }
};

} // end NdArray
} // end Euclid

#endif // ALEXANDRIA_MATRIX_H
