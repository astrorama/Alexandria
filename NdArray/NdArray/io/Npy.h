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

#ifndef ALEXANDRIA_NDARRAY_NPY_H
#define ALEXANDRIA_NDARRAY_NPY_H

#include "NdArray/NdArray.h"
#include <boost/filesystem/path.hpp>
#include <fstream>

namespace Euclid {
namespace NdArray {

/**
 * Write an NdArray to a file following numpy format
 * @see
 *  https://numpy.org/devdocs/reference/generated/numpy.lib.format.html
 * @tparam T
 *  NdArray cell type
 * @tparam Container
 *  NdArray container type
 * @param out
 *  Output stream
 * @param array
 *  NdArray to write
 */
template <typename T>
void writeNpy(std::ostream& out, const NdArray<T>& array);

/**
 * Read an NdArray from a file following numpy format
 * @tparam T
 *  NdArray cell type
 * @tparam Container
 *  NdArray container type
 * @param input
 *  Input stream
 * @return
 *  A new NdArray
 * @note
 *  The underlying numpy format is expected to match the template type T
 */
template <typename T>
NdArray<T> readNpy(std::istream& input);

/**
 * @see
 *  https://numpy.org/devdocs/reference/generated/numpy.lib.format.html
 * @tparam T
 *  NdArray cell type
 * @tparam Container
 *  NdArray container type
 * @param path
 *  Output path
 * @param array
 *  NdArray to write
 */
template <typename T>
void writeNpy(const boost::filesystem::path& path, const NdArray<T>& array) {
  std::ofstream output(path.native(), std::ios_base::out | std::ios_base::binary);
  writeNpy(output, array);
}

/**
 * Read an NdArray from a file following numpy format
 * @tparam T
 *  NdArray cell type
 * @tparam Container
 *  NdArray container type
 * @param path
 *  Input path
 * @return
 *  A new NdArray
 * @note
 *  The underlying numpy format is expected to match the template type T
 */
template <typename T>
NdArray<T> readNpy(const boost::filesystem::path& path) {
  std::ifstream input(path.native(), std::ios_base::in | std::ios_base::binary);
  return readNpy<T>(input);
}

}  // end of namespace NdArray
}  // end of namespace Euclid

#define NPY_IMPL
#include "NdArray/io/_impl/NpyReader.icpp"
#include "NdArray/io/_impl/NpyWriter.icpp"
#undef NPY_IMPL

#endif  // ALEXANDRIA_NDARRAY_NPY_H
