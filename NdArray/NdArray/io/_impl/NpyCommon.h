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

#ifndef ALEXANDRIA_NDARRAY_IMPL_NPYCOMMON_H
#define ALEXANDRIA_NDARRAY_IMPL_NPYCOMMON_H

#include <boost/iostreams/device/mapped_file.hpp>
#include <boost/endian/arithmetic.hpp>
#include "AlexandriaKernel/StringUtils.h"

namespace Euclid {
namespace NdArray {

using boost::endian::little_uint16_t;
using boost::endian::little_uint32_t;

/**
 * Magic string for .npy files
 */
constexpr const char NPY_MAGIC[] = {'\x93', 'N', 'U', 'M', 'P', 'Y'};

/**
 * Map a primitive type to a string representation for numpy
 */
template<typename T>
struct NpyDtype {
};

template<>
struct NpyDtype<int8_t> {
  static constexpr const char *str = "b";
};

template<>
struct NpyDtype<int32_t> {
  static constexpr const char *str = "i4";
};

template<>
struct NpyDtype<int64_t> {
  static constexpr const char *str = "i8";
};

template<>
struct NpyDtype<uint8_t> {
  static constexpr const char *str = "B";
};

template<>
struct NpyDtype<uint32_t> {
  static constexpr const char *str = "u4";
};

template<>
struct NpyDtype<uint64_t> {
  static constexpr const char *str = "u8";
};

template<>
struct NpyDtype<float> {
  static constexpr const char *str = "f4";
};

template<>
struct NpyDtype<double> {
  static constexpr const char *str = "f8";
};

/**
 * Parse the dictionary serialized on the npy file
 * @param header
 *  String representation of the dictionary
 * @param fortran_order [out]
 *  Put here if the numpy array follows the Fortran convention
 * @param big_endian [out]
 *  Put here if the numpy array layout is big-endian
 * @param dtype
 *  Put here the read dtype
 * @param shape [out]
 *  Put here the read shape
 * @param n_elements [out]
 *  Total number of elements (multiplication of shape)
 */
void parseNpyDict(const std::string& header, bool& fortran_order, bool& big_endian,
                  std::string& dtype, std::vector<size_t>& shape, size_t& n_elements) {
  auto loc = header.find("fortran_order") + 16;
  fortran_order = (header.substr(loc, 4) == "True");

  loc = header.find("descr") + 9;
  big_endian = (header[loc] == '>');

  auto loc2 = header.find("'", loc);
  dtype = header.substr(loc + 1, loc2 - loc - 1);

  loc = header.find("shape") + 9;
  loc2 = header.find(")", loc);
  auto shape_str = header.substr(loc, loc2 - loc);
  if (shape_str.back() == ',')
    shape_str.resize(shape_str.size() - 1);
  shape = stringToVector<size_t>(shape_str);
  n_elements = std::accumulate(shape.begin(), shape.end(), 1, std::multiplies<size_t>());
}

/**
 * Read the npy header
 * @param input
 *  Input stream
 * @param dtype [out]
 *  Put here the read dtype
 * @param shape [out]
 *  Put here the read shape
 * @param n_elements [out]
 *  Total number of elements (multiplication of shape)
 * @return
 */
void readNpyHeader(std::istream& input, std::string& dtype, std::vector<size_t>& shape, size_t& n_elements) {
  // Magic
  char magic[6];
  input.read(magic, sizeof(magic));
  if (std::memcmp(magic, NPY_MAGIC, sizeof(NPY_MAGIC)) != 0) {
    throw Elements::Exception() << "Unexpected magic sequence";
  }

  // Version and header len
  little_uint32_t header_len;
  little_uint16_t version;
  input.read(reinterpret_cast<char *>(&version), sizeof(version));
  if (version > 30) {
    throw Elements::Exception() << "Only numpy arrays with version 3 or less are supported";
  }
  else if (version.data()[0] == 1) {
    // 16 bits integer in little endian
    little_uint16_t aux;
    input.read(reinterpret_cast<char *>(&aux), sizeof(aux));
    header_len = aux;
  }
  else {
    // 32 bits integer in little endian
    input.read(reinterpret_cast<char *>(&header_len), sizeof(header_len));
  }

  // Read header
  std::string header(header_len, '\0');
  input.read(&header[0], header_len);

  // Parse header
  bool fortran_order, big_endian;
  parseNpyDict(header, fortran_order, big_endian, dtype, shape, n_elements);

  if (fortran_order)
    throw Elements::Exception() << "Fortran order not supported";

  if (big_endian && (__BYTE_ORDER != __BIG_ENDIAN))
    throw Elements::Exception() << "Only native endianness supported for reading";
}

/**
 * A memory mapped container that can be used by NdArray.
 * Builds on top of boost::iostream::mapped_file
 * @tparam T
 *  Contained value type
 */
template<typename T>
class MappedContainer {
public:
  MappedContainer(size_t offset, size_t data_size, boost::iostreams::mapped_file&& input)
    : m_size(data_size), m_input(std::move(input)), m_data(reinterpret_cast<T *>(m_input.data() + offset)) {
  }

  size_t size() const {
    return m_size;
  }

  T* data () {
    return m_data;
  }

private:
  size_t m_size;
  boost::iostreams::mapped_file m_input;
  T *m_data;
};

} // end of namespace NdArray
} // end of namespace Euclid

#endif // ALEXANDRIA_NDARRAY_IMPL_NPYCOMMON_H
