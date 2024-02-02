/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
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

#ifndef ALEXANDRIA_NDARRAY_OPERATIONS_H
#define ALEXANDRIA_NDARRAY_OPERATIONS_H

#include "NdArray/NdArray.h"

namespace Euclid {
namespace NdArray {

/**
 * Given an "flat" index (i.e a memory offset), return the appropriate coordinates for an ndarray of the given shape
 * @param index
 *  Flat index
 * @param shape
 *  Array shape
 * @return
 *  The coordinates
 * @throw std::out_of_range
 *  If the index goes beyond the size of an ndarray with the given shape
 */
std::vector<std::size_t> unravel_index(std::size_t index, const std::vector<std::size_t>& shape);

/**
 * Sum all elements in an ndarray
 * @param array
 *  The ndarray
 */
template <typename T>
T sum(const NdArray<T>& array);

/**
 * Sum elements in an ndarray along the given axis
 * @param array
 *  The ndarray
 * @param axis
 *  The axis. 0 is the first. Negative values index from the end.
 * @return
 *  Another NdArray with one axis less
 */
template <typename T>
NdArray<T> sum(const NdArray<T>& array, int axis);

/**
 * Integrate elements in an ndarray along the given axis
 * @param array
 *  The ndarray
 * @param kbegin
 *  Iterator to the beginning of the knot values
 * @param kend
 *  Iterator to the end of the knot values
 * @param axis
 *  The axis. 0 is the first. Negative values index from the end.
 * @return
 */
template <typename T, typename Iterator>
NdArray<T> trapz(const NdArray<T>& array, const Iterator kbegin, const Iterator kend, int axis);

/**
 * Return the coordinates for the maximum element
 * @tparam T
 *  NdArray type
 * @param array
 *  The ndarray
 * @return
 *  Coordinates for the element with the highest value
 */
template <typename T>
std::vector<std::size_t> argmax(const NdArray<T>& array);

/**
 * Return the coordinates for the minimum element
 * @tparam T
 *  NdArray type
 * @param array
 *  The ndarray
 * @return
 *  Coordinates for the element with the lowest value
 */
template <typename T>
std::vector<std::size_t> argmin(const NdArray<T>& array);

/**
 * Sort in place a 2D NdArray based on the attribute names
 * @tparam T
 *  NdArray type
 * @param array
 *  The ndarray
 * @param attrs
 *  List of attributes to use for the sorting
 */
template <typename T>
void sort(NdArray<T>& array, const std::vector<std::string>& attrs);

/**
 * Check 2 ndarray have the same dimensions
 * @param array_1
 *  The first ndarray
 * @param array_2
 *  The second ndarray
 * @return
 *  evaluation result
 */
template <typename T1, typename T2>
bool sameShape(const NdArray<T1>& array_1, const NdArray<T2>& array_2);

/**
 * Multiply element-wise 2 ndarray with the same dimensions. Both NdArray must be in {int,float,double} wider first.
 * @param array_1
 *  The first ndarray
 * @param array_2
 *  The second ndarray
 * @throws std::invalid_argument
 *    If the 2 array have not the same dimensions.
 * @return
 *  Another NdArray
 */
template <typename T1, typename T2>
NdArray<T1> multiplyElements(const NdArray<T1>& array_1, const NdArray<T2>& array_2);

/**
 * Add element-wise 2 ndarray with the same dimensions. Both NdArray must be in {int,float,double} wider first.
 * @param array_1
 *  The first ndarray
 * @param array_2
 *  The second ndarray
 * @throws std::invalid_argument
 *    If the 2 array have not the same dimensions.
 * @return
 *  Another NdArray
 */
template <typename T1, typename T2>
NdArray<T1> addElements(const NdArray<T1>& array_1, const NdArray<T2>& array_2);


}  // namespace NdArray
}  // namespace Euclid

#define NDARRAY_OPS_IMPL
#include "NdArray/_impl/Operations.icpp"
#undef NDARRAY_OPS_IMPL

#endif  // ALEXANDRIA_NDARRAY_OPERATIONS_H
