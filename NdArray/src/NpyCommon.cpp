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

#include "NdArray/io/_impl/NpyCommon.h"
#include "AlexandriaKernel/RegexHelper.h"

namespace Euclid {
namespace NdArray {

void parseSingleValue(const std::string& descr, bool& big_endian, std::string& dtype) {
  big_endian = (descr.front() == '>');
  dtype      = descr.substr(1);
}

inline void parseFieldValues(const std::string& descr, bool& big_endian, std::vector<std::string>& attrs,
                             std::string& dtype) {
  static const regex::regex field_expr("\\('([^']*)',\\s*'([^']*)'\\)");

  regex::match_results<std::string::const_iterator> match;
  auto                                              start = descr.begin();
  auto                                              end   = descr.end();

  while (regex::regex_search(start, end, match, field_expr)) {
    bool        endian_aux;
    std::string dtype_aux;

    parseSingleValue(match[2].str(), endian_aux, dtype_aux);
    if (dtype.empty()) {
      dtype      = dtype_aux;
      big_endian = endian_aux;
    } else if (dtype != dtype_aux || big_endian != endian_aux) {
      throw std::invalid_argument("NdArray only supports uniform types");
    }
    attrs.emplace_back(match[1].str());

    start = match[0].second;
  }
}

inline void parseNpyDict(const std::string& header, bool& fortran_order, bool& big_endian, std::string& dtype,
                         std::vector<size_t>& shape, std::vector<std::string>& attrs, size_t& n_elements) {
  auto loc      = header.find("fortran_order") + 16;
  fortran_order = (header.substr(loc, 4) == "True");

  loc = header.find("descr") + 8;

  if (header[loc] == '\'') {
    auto end = header.find('\'', loc + 1);
    parseSingleValue(header.substr(loc + 1, end - loc - 1), big_endian, dtype);
  } else if (header[loc] == '[') {
    auto end = header.find(']', loc + 1);
    parseFieldValues(header.substr(loc + 1, end - loc - 1), big_endian, attrs, dtype);
  } else {
    throw Elements::Exception() << "Failed to parse the array description: " << header;
  }

  loc            = header.find("shape") + 9;
  auto loc2      = header.find(')', loc);
  auto shape_str = header.substr(loc, loc2 - loc);
  if (shape_str.back() == ',')
    shape_str.resize(shape_str.size() - 1);
  shape      = stringToVector<size_t>(shape_str);
  n_elements = std::accumulate(shape.begin(), shape.end(), 1, std::multiplies<size_t>());
}

void readNpyHeader(std::istream& input, std::string& dtype, std::vector<size_t>& shape, std::vector<std::string>& attrs,
                   size_t& n_elements) {
  // Magic
  char magic[6];
  input.read(magic, sizeof(magic));
  if (std::memcmp(magic, NPY_MAGIC, sizeof(NPY_MAGIC)) != 0) {
    throw Elements::Exception() << "Unexpected magic sequence";
  }

  // Version and header len
  little_uint32_t header_len;
  little_uint16_t version;
  input.read(reinterpret_cast<char*>(&version), sizeof(version));
  if (version > 30) {
    throw Elements::Exception() << "Only numpy arrays with version 3 or less are supported";
  } else if (version.data()[0] == 1) {
    // 16 bits integer in little endian
    little_uint16_t aux;
    input.read(reinterpret_cast<char*>(&aux), sizeof(aux));
    header_len = aux;
  } else {
    // 32 bits integer in little endian
    input.read(reinterpret_cast<char*>(&header_len), sizeof(header_len));
  }

  // Read header
  std::string header(header_len, '\0');
  input.read(&header[0], header_len);

  // Parse header
  bool fortran_order, big_endian;
  parseNpyDict(header, fortran_order, big_endian, dtype, shape, attrs, n_elements);

  if (fortran_order)
    throw Elements::Exception() << "Fortran order not supported";

  if ((big_endian && (BYTE_ORDER != BIG_ENDIAN)) || (!big_endian && (BYTE_ORDER != LITTLE_ENDIAN)))
    throw Elements::Exception() << "Only native endianness supported for reading";
}

}  // namespace NdArray
}  // namespace Euclid
