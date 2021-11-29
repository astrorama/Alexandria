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

#ifndef ALEXANDRIA_NDARRAY_IMPL_NPYCOMMON_H
#define ALEXANDRIA_NDARRAY_IMPL_NPYCOMMON_H

#include "AlexandriaKernel/StringUtils.h"
#include <boost/endian/arithmetic.hpp>
#include <boost/filesystem/operations.hpp>
#include <boost/iostreams/device/mapped_file.hpp>
#include <numeric>

namespace Euclid {
namespace NdArray {

using boost::endian::little_uint16_t;
using boost::endian::little_uint32_t;

/**
 * Magic string for .npy files
 */
constexpr const char NPY_MAGIC[] = {'\x93', 'N', 'U', 'M', 'P', 'Y'};

/**
 * Endianness marker for the numpy array
 */
#if BYTE_ORDER == LITTLE_ENDIAN
constexpr const char* ENDIAN_MARKER = "<";
#elif BYTE_ORDER == BIG_ENDIAN
constexpr const char* ENDIAN_MARKER = ">";
#else
#error "PDP_ENDIAN not supported"
#endif

/**
 * Map a primitive type to a string representation for numpy
 */
template <typename T>
struct NpyDtype {};

template <>
struct NpyDtype<int8_t> {
  static constexpr const char* str = "b";
};

template <>
struct NpyDtype<int16_t> {
  static constexpr const char* str = "i2";
};

template <>
struct NpyDtype<int32_t> {
  static constexpr const char* str = "i4";
};

template <>
struct NpyDtype<int64_t> {
  static constexpr const char* str = "i8";
};

template <>
struct NpyDtype<uint8_t> {
  static constexpr const char* str = "B";
};

template <>
struct NpyDtype<uint16_t> {
  static constexpr const char* str = "u2";
};

template <>
struct NpyDtype<uint32_t> {
  static constexpr const char* str = "u4";
};

template <>
struct NpyDtype<uint64_t> {
  static constexpr const char* str = "u8";
};

template <>
struct NpyDtype<float> {
  static constexpr const char* str = "f4";
};

template <>
struct NpyDtype<double> {
  static constexpr const char* str = "f8";
};

/**
 * Parse a single dtype description (i.e. '<f8')
 */
void parseSingleValue(const std::string& descr, bool& big_endian, std::string& dtype);

/**
 * Parse the description field from npy arrays with named fields, which are stored as the
 * string representation of a list of tuples (name, dtype). i.e:
 * [('a', '<i4'), ('b', '<i4')]
 * @throws std::invalid_argument
 *  NdArrays only support uniform types, so this method will fail if there are mixed types on the
 *  npy file
 */
void parseFieldValues(const std::string& descr, bool& big_endian, std::vector<std::string>& attrs, std::string& dtype);

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
 * @param attrs[out]
 *  Put here the attribute names
 * @param n_elements [out]
 *  Total number of elements (multiplication of shape)
 */
void parseNpyDict(const std::string& header, bool& fortran_order, bool& big_endian, std::string& dtype,
                  std::vector<size_t>& shape, std::vector<std::string>& attrs, size_t& n_elements);

/**
 * Read the npy header
 * @param input
 *  Input stream
 * @param dtype [out]
 *  Put here the read dtype
 * @param shape [out]
 *  Put here the read shape
 * @param attrs [out]
 *  Put here the attribute names
 * @param n_elements [out]
 *  Total number of elements (multiplication of shape)
 * @return
 */
void readNpyHeader(std::istream& input, std::string& dtype, std::vector<size_t>& shape, std::vector<std::string>& attrs,
                   size_t& n_elements);

/**
 * We write arrays following 2.0 version (32 bits header size)
 */
constexpr const uint8_t NPY_VERSION[] = {'\x02', '\x00'};

/**
 * Generate a string that represents an NdArray shape vector as a Python tuple
 * @param shape
 *  A string with the Python representation of a tuple
 */
inline std::string npyShape(std::vector<size_t> shape) {
  std::stringstream shape_stream;
  shape_stream << "(";
  for (auto s : shape) {
    shape_stream << s << ',';
  }
  shape_stream << ")";
  return shape_stream.str();
}

inline std::string typeDescription(const std::string& type, const std::vector<std::string>& attrs) {
  std::stringstream dtype;
  if (attrs.empty()) {
    dtype << '\'' << ENDIAN_MARKER << type << '\'';
  } else {
    dtype << '[';
    for (auto& attr : attrs) {
      dtype << "('" << attr << "', '" << ENDIAN_MARKER << type << "'), ";
    }
    dtype << ']';
  }
  return dtype.str();
}

/**
 * Write header
 */
template <typename T>
void writeNpyHeader(std::ostream& out, std::vector<size_t> shape, const std::vector<std::string>& attrs) {
  if (!attrs.empty()) {
    if (attrs.size() != shape.back()) {
      throw std::out_of_range("Last axis does not match number of attribute names");
    }
    shape.pop_back();
  }
  // Serialize header as a Python dict
  std::stringstream header;
  header << "{"
         << "'descr': " << typeDescription(NpyDtype<T>::str, attrs)
         << ", 'fortran_order': False, 'shape': " << npyShape(shape) << "}";
  auto            header_str = header.str();
  little_uint32_t header_len = header_str.size();

  // Pad header with spaces so the header block is 64 bytes aligned
  size_t total_length = sizeof(NPY_MAGIC) + sizeof(NPY_VERSION) + sizeof(header_len) + header_len + 1;  // Keep 1 for \n
  size_t padding      = 64 - total_length % 64;
  if (padding) {
    header << std::string(padding, '\x20');
  }
  header << '\n';
  header_str = header.str();
  header_len = header_str.size();

  // Magic and version
  out.write(NPY_MAGIC, sizeof(NPY_MAGIC));
  out.write(reinterpret_cast<const char*>(&NPY_VERSION), sizeof(NPY_VERSION));

  // HEADER_LEN
  out.write(reinterpret_cast<char*>(&header_len), sizeof(header_len));

  // HEADER
  out.write(header_str.data(), header_str.size());
}

/**
 * A memory mapped container that can be used by NdArray.
 * Builds on top of boost::iostream::mapped_file
 * @tparam T
 *  Contained value type
 */
template <typename T>
class MappedContainer {
public:
  MappedContainer(const boost::filesystem::path& path, size_t data_offset, size_t n_elements,
                  const std::vector<std::string>& attr_names, boost::iostreams::mapped_file&& input, size_t max_size)
      : m_path(path)
      , m_data_offset(data_offset)
      , m_n_elements(n_elements)
      , m_max_size(max_size)
      , m_attr_names(attr_names)
      , m_mapped(std::move(input))
      , m_data(reinterpret_cast<T*>(const_cast<char*>(m_mapped.const_data()) + data_offset)) {}

  size_t size() const {
    return m_n_elements;
  }

  T* data() {
    return m_data;
  }

  void resize(const std::vector<size_t>& shape) {
    // Generate header
    std::stringstream header;
    writeNpyHeader<T>(header, shape, m_attr_names);
    auto header_str  = header.str();
    auto header_size = header_str.size();
    // Make sure we are in place
    if (header_size != m_data_offset) {
      throw Elements::Exception() << "Can not resize memory mapped NPY file. "
                                     "The new header length must match the allocated space.";
    }

    m_n_elements    = std::accumulate(shape.begin(), shape.end(), 1u, std::multiplies<size_t>());
    size_t new_size = header_size + sizeof(T) * m_n_elements;
    if (new_size > m_max_size) {
      throw Elements::Exception() << "resize request bigger than maximum allocated size: " << new_size << " > "
                                  << m_max_size;
    }
    boost::filesystem::resize_file(m_path, new_size);
    std::copy(header_str.begin(), header_str.end(), m_mapped.data());
  }

private:
  boost::filesystem::path       m_path;
  size_t                        m_data_offset, m_n_elements, m_max_size;
  std::vector<std::string>      m_attr_names;
  boost::iostreams::mapped_file m_mapped;
  T*                            m_data;
};

}  // end of namespace NdArray
}  // end of namespace Euclid

#endif  // ALEXANDRIA_NDARRAY_IMPL_NPYCOMMON_H
