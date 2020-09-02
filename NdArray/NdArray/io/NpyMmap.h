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

#ifndef ALEXANDRIA_NDARRAY_IO_NPYMMAP_H
#define ALEXANDRIA_NDARRAY_IO_NPYMMAP_H

#include <boost/filesystem/path.hpp>
#include <boost/iostreams/device/mapped_file.hpp>
#include "NdArray/NdArray.h"

namespace Euclid {
namespace NdArray {

/**
 * Open using mmap an existing numpy file
 * @tparam T
 *  NdArray cell type
 * @param path
 *  Input path
 * @param mode
 *  Open mode. By default read/write, so changes are persisted to disk.
 *  boost::iostreams::mapped_file_base::priv enabled a Copy-On-Write, so the memory can be modified
 *  but the changes will not persist
 * @param max_size
 *  Maximum size of the file. If you are going to call NdArray<T>::concatenate, mind this parameter!
 * @return
 *  A new NdArray
 * @note
 *  The underlying numpy format is expected to match the template type T
 * @note
 *  If you open in read-only mode, assign to a const NdArray to avoid accidental writes
 */
template<typename T>
NdArray<T> mmapNpy(const boost::filesystem::path& path,
                   boost::iostreams::mapped_file_base::mapmode mode = boost::iostreams::mapped_file_base::readwrite,
                   size_t max_size = 0);

/**
 * Create using mmap an NdArray backed by a numpy file
 * @tparam T
 *  NdArray cell type
 * @param path
 *  Output path
 * @param shape
 *  NdArray shape
 * @param attr_names
 *  Attribute names
 * @param max_size
 *  Maximum size of the file. If you are going to call NdArray<T>::concatenate, mind this parameter!
 * @return
 *  A new NdArray
 */
template<typename T>
NdArray<T> createMmapNpy(const boost::filesystem::path& path, const std::vector<size_t>& shape,
                         const std::vector<std::string>& attr_names, size_t max_size = 0);

/**
 * Create using mmap an NdArray backed by a numpy file
 * @tparam T
 *  NdArray cell type
 * @param path
 *  Output path
 * @param shape
 *  NdArray shape
 * @param max_size
 *  Maximum size of the file. If you are going to call NdArray<T>::concatenate, mind this parameter!
 * @return
 *  A new NdArray
 */
template<typename T>
NdArray<T> createMmapNpy(const boost::filesystem::path& path, const std::vector<size_t>& shape,
                         size_t max_size = 0) {
  return createMmapNpy<T>(path, shape, {}, max_size);
}

} // end of namespace NdArray
} // end of namespace Euclid

#define NPYMMAP_IMPL
#include "NdArray/io/_impl/NpyMmap.icpp"
#undef NPYMMAP_IMPL

#endif // ALEXANDRIA_NDARRAY_IO_NPYMMAP_H
