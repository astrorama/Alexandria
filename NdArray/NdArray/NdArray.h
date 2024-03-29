/**
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
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
 * @file NdArray/NdArray.h
 * @date November 21, 2018
 * @author Alejandro Alvarez Ayllon
 */

#ifndef ALEXANDRIA_NDARRAY_H
#define ALEXANDRIA_NDARRAY_H

#include "AlexandriaKernel/memory_tools.h"
#include <cassert>
#include <iostream>
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
template <typename T>
class NdArray {
private:
  struct ContainerInterface;

  template <template <class...> class Container = std::vector>
  struct ContainerWrapper;

public:
  using self_type = NdArray<T>;

  /**
   * Iterator type
   * @tparam Const
   *    If true, this defines a const iterator
   */
  template <bool Const>
  class Iterator
      : public std::iterator<std::random_access_iterator_tag, typename std::conditional<Const, const T, T>::type> {
  private:
    ContainerInterface* m_container_ptr;
    size_t              m_offset;
    size_t              m_row_size;
    size_t              m_stride;
    size_t              m_i;

    Iterator(ContainerInterface* container_ptr, size_t offset, const std::vector<size_t>& shape,
             const std::vector<size_t>& strides, size_t start);

    Iterator(ContainerInterface* container_ptr, size_t offset, size_t row_size, size_t stride, size_t start);

    friend class NdArray;

  public:
    using value_t = typename std::conditional<Const, const T, T>::type;
    using typename std::iterator<std::random_access_iterator_tag, value_t>::reference;
    using typename std::iterator<std::random_access_iterator_tag, value_t>::pointer;
    using typename std::iterator<std::random_access_iterator_tag, value_t>::difference_type;

    /**
     * Construct a const iterator from a non-const iterator
     */
    Iterator(const Iterator<false>& other);  // cppcheck-suppress  noExplicitConstructor

    /**
     * Pre-increment
     */
    Iterator& operator++();

    /**
     * Post-increment
     */
    const Iterator operator++(int);

    /**
     * Two iterators are equal if they point to the same position on the same data
     */
    bool operator==(const Iterator& other) const;

    /**
     * Two iterators are not equal if they point to different data, or to different positions on the same
     */
    bool operator!=(const Iterator& other) const;

    /**
     * De-reference operator
     * @return
     *  A modifiable reference to the value
     */
    value_t& operator*();

    /**
     * De-reference operator
     * @return
     *  A non modifiable copy of the value
     */
    value_t operator*() const;

    /**
     * Increment the iterator n times in place
     * @note
     *  No out of bounds check is perform! Going beyond the end of the container is undefined behavior
     */
    Iterator& operator+=(size_t n);

    /**
     * @return A new iterator incremented n times
     * @note
     *  No out of bounds check is perform! Going beyond the end of the container is undefined behavior
     */
    Iterator operator+(size_t n) const;

    /**
     * Decrement the iterator n times in place
     * @note
     *  There is an assert in place to make sure n is not greater than the current position.
     *  However, the assert can be gone when compiling for release
     */
    Iterator& operator-=(size_t n);

    /**
     * @return A new iterator incremented n times
     * @note
     *  There is an assert in place to make sure n is not greater than the current position.
     *  However, the assert can be gone when compiling for release
     */
    Iterator operator-(size_t n) const;

    /**
     * @return The number of positions between this and other
     * @note
     *  If this and other point to different underlying data, this is undefined behavior
     */
    difference_type operator-(const Iterator& other);

    /**
     * Equivalent to *(iterator + i)
     */
    value_t& operator[](size_t i);

    /**
     * Equivalent to *(iterator + i)
     */
    value_t operator[](size_t i) const;

    /**
     * @return true if this is less than other
     * @note
     *  If this and other point to different underlying data, this is undefined behavior
     */
    bool operator<(const Iterator& other);

    /**
     * @return true if this is greater than other
     * @note
     *  If this and other point to different underlying data, this is undefined behavior
     */
    bool operator>(const Iterator& other);
  };

  using const_iterator = Iterator<true>;
  using iterator       = Iterator<false>;

  /**
   * Destructor.
   */
  ~NdArray() = default;

  /**
   * Constructs a default-initialized matrix with the given shape.
   * @param shape_
   *    The shape of the matrix. The number of elements in shape corresponds to the number
   *    of dimensions, the values to each dimension size.
   */
  explicit NdArray(std::vector<size_t> shape_);

  /**
   * Constructs a matrix and initialize it with the given data.
   * @param shape_
   *    The shape of the matrix. The number of elements in shape corresponds to the number
   *    of dimensions, the values to each dimension size.
   * @param data
   *    The initial data. It *must* match exactly the matrix size (shape[0]*shape[1]...*shape[n]).
   * @throws std::invalid_argument
   *    If the data size does not corresponds to the matrix size.
   */
  template <template <class...> class Container = std::vector>
  NdArray(std::vector<size_t> shape_, const Container<T>& data);

  /**
   * Constructs a matrix and initialize it with the given data.
   * @tparam Container
   *    Owns the memory used by the NdArray. It must expose the methods size(), resize() and data().
   * @param shape_
   *    The shape of the matrix. The number of elements in shape corresponds to the number
   *    of dimensions, the values to each dimension size.
   * @param data
   *    The initial data. It *must* match exactly the matrix size (shape[0]*shape[1]...*shape[n]).
   *    The NdArray will move the data into its internal storage! This avoids a copy, but remember to
   *    not use data after this call.
   * @throws std::invalid_argument
   *    If the data size does not corresponds to the matrix size.
   */
  template <template <class...> class Container = std::vector>
  NdArray(std::vector<size_t> shape_, Container<T>&& data);

  /**
   * Construct a matrix with a custom container and strides.
   * @tparam Container
   *    Owns the memory used by the NdArray. It must expose the methods size(), resize() and data().
   * @param shape_
   *    The shape of the matrix. The number of elements in shape corresponds to the number
   *    of dimensions, the values to each dimension size.
   * @param strides_
   *    The number of bytes we need to jump between adjacent positions on a given dimension
   * @param data
   *    The initial data.
   *    The NdArray will move the data into its internal storage! This avoids a copy, but remember to
   *    not use data after this call.
   * @throws std::runtime_error
   *    If the data is not in C order.
   * @throws std::invalid_argument
   *    If the shape and strides dimension do not match.
   */
  template <template <class...> class Container = std::vector>
  NdArray(std::vector<size_t> shape_, std::vector<size_t> strides_, Container<T>&& data);

  /**
   * Constructs a matrix and initialize it with from the given iterators
   * @param shape_
   *    The shape of the matrix. The number of elements in shape corresponds to the number
   *    of dimensions, the values to each dimension size.
   * @param begin
   *    The beginning of the data
   * @param end
   *    The end of the data
   * @throws std::invalid_argument
   *    If the data size does not corresponds to the matrix size.
   */
  template <typename Iterator>
  NdArray(std::vector<size_t> shape_, Iterator begin, Iterator end);

  /**
   * Constructs a matrix, giving a name to each of the items on the last dimension
   * @param attr_names
   *    Names for the dimensions of the last axis
   * @param shape_
   *    Shape for the matrix
   * @note
   *    Unlike numpy, attr_names is treated strictly as an alias, so
   *    NdArray<float>({20}, {"X", "Y"}) has a shape of (20, 2)
   */
  template <typename... Args>
  NdArray(const std::vector<size_t>& shape_, const std::vector<std::string>& attr_names, Args&&... args);

  /**
   * Constructs a default-initialized matrix with the given shape (as an initializer list).
   * @param shape_
   *    The shape of the matrix. The number of elements in shape corresponds to the number
   *    of dimensions, the values to each dimension size.
   */
  explicit NdArray(const std::initializer_list<size_t>& shape_) : NdArray(std::vector<size_t>{shape_}) {}

  /**
   * Copy constructor
   * @note
   *    The underlying data is not copied, but shared
   */
  NdArray(const self_type&);

  /**
   * Move constructor
   */
  NdArray(self_type&&) noexcept = default;

  /**
   * Assignment
   * @note
   *    The underlying data is not copied, but shared
   */
  NdArray& operator=(const NdArray&);

  /**
   * Create a copy of the NdArray
   */
  NdArray copy() const {
    return self_type{this};
  }

  /**
   * Gets the shape of the matrix.
   * @return
   *    A vector with as many elements as number of dimensions, containing the size of each one.
   */
  const std::vector<size_t>& shape() const {
    return m_details_ptr->m_shape;
  }

  /**
   * @param i
   * @return The size of the axis i
   */
  size_t shape(std::size_t i) const {
    return m_details_ptr->m_shape[i];
  }

  const std::vector<std::size_t>& strides() const {
    return m_details_ptr->m_stride_size;
  }

  std::size_t strides(std::size_t i) const {
    return m_details_ptr->m_stride_size[i];
  }

  /**
   * Reshape the NdArray.
   * @note This modifies the object
   * @param new_shape
   *    A vector with as many elements as number of dimensions, containing the size of each one.
   * @throws std::range_error
   *    If the new shape does not match the number of elements already contained within the NdArray.
   * @return
   *    *this
   * @throws std::invalid_argument
   *    If the array has attribute names
   */
  self_type& reshape(const std::vector<size_t>& new_shape);

  /**
   * Reshape the NdArray.
   * @note This modifies the object
   * @param new_shape
   *    A vector with as many elements as number of dimensions, containing the size of each one.
   * @throws std::range_error
   *    If the new shape does not match the number of elements already contained within the NdArray.
   * @return
   *    *this
   */
  template <typename... D>
  self_type& reshape(size_t i, D... rest);

  /**
   * @return A reference to the front element
   */
  const T& front() const;

  /**
   * Gets a reference to the value stored at the given coordinates.
   * @param coords
   *    Elements coordinates.
   * @throws std::out_of_range
   *    If the number of coordinates is invalid, or any of them is out of bounds.
   */
  T& at(const std::vector<size_t>& coords);

  /**
   * Gets a constant reference to the value stored at the given coordinates
   * @param coords
   *    Elements coordinates.
   * @throws std::out_of_range
   *    If the number of coordinates is invalid, or any of them is out of bounds.
   */
  const T& at(const std::vector<size_t>& coords) const;

  /**
   * Gets a reference to the value stored at the given coordinates.
   * @param coords
   *    Elements coordinates, except last one
   * @param attr
   *    Attribute name used to determine the last coordinate
   * @throws std::out_of_range
   *    If the number of coordinates is invalid, or any of them is out of bounds.
   */
  T& at(const std::vector<size_t>& coords, const std::string& attr);

  /**
   * Gets a constant reference to the value stored at the given coordinates.
   * @param coords
   *    Elements coordinates, except last one
   * @param attr
   *    Attribute name used to determine the last coordinate
   * @throws std::out_of_range
   *    If the number of coordinates is invalid, or any of them is out of bounds.
   */
  const T& at(const std::vector<size_t>& coords, const std::string& attr) const;

  /**
   * Gets a reference to the value stored at the given coordinates.
   * @param coords
   *    Elements coordinates.
   * @warning
   *    This method does *not* test for bounds, but it uses asserts to catch bad accesses on debug builds.
   * @note
   *    This is a convenience function that allows access without requiring a vector when the
   *    number of dimensions is known in advance (i.e. `at(x, y, z)` instead of `at(std::vector<size_t>{x, y, z})`).
   */
  template <typename... D>
  T& at(size_t i, D... rest);

  /**
   * Gets a constant reference to the value stored at the given coordinates.
   * @param coords
   *    Elements coordinates.
   * @warning
   *    This method does *not* test for bounds, but it uses asserts to catch bad accesses on debug builds.
   * @note
   *    This is a convenience function that allows access without requiring a vector when the
   *    number of dimensions is known in advance (i.e. `at(x, y, z)` instead of `at(std::vector<size_t>{x, y, z})`).
   */
  template <typename... D>
  const T& at(size_t i, D... rest) const;

  /**
   * @return An iterator pointing to the first element (which corresponds to the one with
   * the coordinates set to 0).
   */
  iterator begin();

  /**
   * @return An iterator pointing just after the last element (which correspond to the one with
   * the coordinates set to (shape[0]-1, shape[1]-1, ... shape[n]-1).
   */
  iterator end();

  /**
   * @return A constant iterator pointing to the first element (which corresponds to the one with
   * the coordinates set to 0).
   */
  const_iterator begin() const;

  /**
   * @return A constant iterator pointing just after the last element (which correspond to the one with
   * the coordinates set to (shape[0]-1, shape[1]-1, ... shape[n]-1).
   */
  const_iterator end() const;

  /**
   * Size of the underlying container
   */
  size_t size() const;

  /**
   * Two NdArrays are equal if their shapes and their content are equal
   */
  bool operator==(const self_type& b) const;

  /**
   * Two NdArrays are not equal if their shapes or their content are not equal
   */
  bool operator!=(const self_type& b) const;

  /**
   * Concatenate to this array another one *along the first axis*
   * @return *this
   */
  self_type& concatenate(const self_type& other);

  /**
   * Return a slice of the array cutting along the first axis
   */
  self_type slice(size_t i);

  /**
   * Return a slice of the array cutting along the first axis
   */
  const self_type slice(size_t i) const;

  /**
   * Return a slice of the array cutting along the last axis
   */
  self_type rslice(size_t i);

  /**
   * Return a slice of the array cutting along the last axis
   */
  const self_type rslice(size_t i) const;

  void next_slice(void);

  /**
   * @return
   *    Attribute names
   */
  const std::vector<std::string>& attributes() const;

private:
  struct ContainerInterface {
    /// Owned by the specific implementation ContainerWrapper,
    /// but exposed here to avoid indirections
    char* m_data_ptr;

    virtual ~ContainerInterface() = default;

    /// Get the element at the given absolute offset (in bytes)
    T get(size_t offset) const {
      return *reinterpret_cast<T*>(m_data_ptr + offset);
    }

    /// Get a reference to the element at the given absolute offset (in bytes)
    T& get(size_t offset) {
      return *reinterpret_cast<T*>(m_data_ptr + offset);
    }

    /// @copydoc std::vector::size
    virtual size_t size() const = 0;

    /// Get the size in bytes
    virtual size_t nbytes() const = 0;

    /// Resize container
    virtual void resize(const std::vector<size_t>& shape) = 0;

    /// Expected to generate a deep copy of the underlying data
    virtual std::unique_ptr<ContainerInterface> copy() const = 0;
  };

  template <template <class...> class Container>
  struct ContainerWrapper : public ContainerInterface {
    using ContainerInterface::m_data_ptr;

    Container<T> m_container;

    ~ContainerWrapper() = default;

    ContainerWrapper(const ContainerWrapper&) = delete;

    ContainerWrapper(ContainerWrapper&&) = default;

    template <typename... Args>
    explicit ContainerWrapper(Args&&... args) : m_container(std::forward<Args>(args)...) {
      m_data_ptr = reinterpret_cast<char*>(m_container.data());
    }

    size_t size() const final {
      return m_container.size();
    }

    template <typename T2>
    auto nbytesImpl(int) const -> decltype(std::declval<Container<T2>>().nbytes()) {
      return m_container.nbytes();
    }

    template <typename T2>
    size_t nbytesImpl(...) const {
      return m_container.size() * sizeof(T2);
    }

    size_t nbytes() const final {
      return nbytesImpl<T>(0);
    }

    template <typename T2>
    auto resizeImpl(const std::vector<size_t>& shape)
        -> decltype((void)std::declval<Container<T2>>().resize(std::vector<size_t>{}), void()) {
      m_container.resize(shape);
    }

    template <typename T2>
    auto resizeImpl(const std::vector<size_t>& shape)
        -> decltype((void)std::declval<Container<T2>>().resize(size_t{}), void()) {
      auto new_size = std::accumulate(shape.begin(), shape.end(), 1u, std::multiplies<size_t>());
      m_container.resize(new_size);
    }

    /**
     * @copybrief std::vector::resize
     * @note
     *  This method delegates to resizeImpl, which uses SFINAE to switch at compilation time between
     *  an implementation adapted to STL containers [resize(size_t)], and another for containers that need
     *  the shape information (i.e. Npy)
     */
    void resize(const std::vector<size_t>& shape) final {
      resizeImpl<T>(shape);
      m_data_ptr = reinterpret_cast<char*>(m_container.data());
    }

    std::unique_ptr<ContainerInterface> copy() const final {
      return Euclid::make_unique<ContainerWrapper>(m_container);
    }
  };

  // NdArray is used inside Table as one of the possible column types
  // Since the cell_type is a variant, it must be as big as the biggest type (NdArray)
  // plus a marker for the valid type, plus any alignment requirement.
  // This indirection makes NdArray only 8 bytes in size!
  struct Details {
    size_t                              m_offset;
    size_t                              m_size;
    size_t                              m_total_stride;
    std::vector<size_t>                 m_shape;
    std::vector<size_t>                 m_stride_size;
    std::vector<std::string>            m_attr_names;
    std::shared_ptr<ContainerInterface> m_container;
  };
  std::unique_ptr<Details> m_details_ptr;

  /**
   * Private constructor used for deep copies
   */
  explicit NdArray(const self_type* other);

  /**
   * Private constructor used for slices
   */
  NdArray(std::shared_ptr<ContainerInterface> container, size_t offset, std::vector<size_t> shape,
          std::vector<size_t> stride, std::vector<std::string> attr_names);

  /**
   * Gets the total offset for the given coordinates.
   * @throws std::out_of_range
   *    If the number of coordinates is invalid, or any of them is out of bounds.
   */
  size_t get_offset(const std::vector<size_t>& coords) const;

  /**
   * Get the offset for the given attribute name
   * @throws std::out_of_range
   *    If the attribute is unknown.
   */
  size_t get_attr_offset(const std::string& attr) const;

  /**
   * Compute the stride size for each dimension
   */
  void update_strides();

  /**
   * Helper to expand at with a variable number of arguments
   */
  template <typename... D>
  T& at_helper(size_t offset_acc, size_t axis, size_t i, D... rest);

  /**
   * Helper to expand at with a variable number of arguments (base case)
   */
  T& at_helper(size_t offset_acc, size_t axis);

  /**
   * Helper to expand at with a variable number of arguments, being the last an attribute name
   */
  T& at_helper(size_t offset_acc, size_t axis, const std::string& attr);

  /**
   * Helper to expand constant at with a variable number of arguments
   */
  template <typename... D>
  const T& at_helper(size_t offset_acc, size_t axis, size_t i, D... rest) const;

  /**
   * Helper to expand constant at with a variable number of arguments (base case)
   */
  const T& at_helper(size_t offset_acc, size_t axis) const;

  /**
   * Helper to expand constant at with a variable number of arguments, being the last an attribute name
   */
  const T& at_helper(size_t offset_acc, size_t axis, const std::string& attr) const;

  template <typename... D>
  self_type& reshape_helper(std::vector<size_t>& acc, size_t i, D... rest);

  self_type& reshape_helper(std::vector<size_t>& acc);
};

/**
 * Serialize a NdArray
 */
template <typename T>
std::ostream& operator<<(std::ostream& out, const NdArray<T>& ndarray);

}  // namespace NdArray
}  // namespace Euclid

#define NDARRAY_IMPL
#include "NdArray/_impl/NdArray.icpp"
#undef NDARRAY_IMPL

#endif  // ALEXANDRIA_NDARRAY_H
