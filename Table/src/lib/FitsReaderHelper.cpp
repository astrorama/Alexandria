/*
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
 * @file src/lib/FitsReaderHelper.cpp
 * @date April 17, 2014
 * @author Nikolaos Apostolakos
 */

#include "FitsReaderHelper.h"
#include "ElementsKernel/Exception.h"
#include <CCfits/CCfits>
#include <boost/lexical_cast.hpp>
#include <boost/tokenizer.hpp>

namespace Euclid {
namespace Table {

using NdArray::NdArray;

std::vector<std::string> autoDetectColumnNames(const CCfits::Table& table_hdu) {
  std::vector<std::string> names{};
  for (int i = 1; i <= table_hdu.numCols(); ++i) {
    std::string name = table_hdu.column(i).name();
    if (name.empty()) {
      name = "Col" + std::to_string(i);
    }
    names.push_back(std::move(name));
  }
  return names;
}

std::pair<std::type_index, std::size_t> asciiFormatToType(const std::string& format) {
  if (format[0] == 'A') {
    std::size_t size = std::stoi(format.substr(1));
    return {typeid(std::string), size};
  } else if (format[0] == 'I') {
    return {typeid(int64_t), 0};
  } else if (format[0] == 'F') {
    return {typeid(double), 0};
  } else if (format[0] == 'E') {
    return {typeid(double), 0};
  } else if (format[0] == 'D') {
    return {typeid(double), 0};
  }
  throw Elements::Exception() << "FITS ASCII table format " << format << " is not "
                              << "yet supported";
}

extern const std::vector<std::pair<char, std::type_index>>  //
    NdTypeMap{
        {'J', typeid(NdArray<int32_t>)}, {'B', typeid(NdArray<int32_t>)}, {'I', typeid(NdArray<int32_t>)},
        {'K', typeid(NdArray<int64_t>)}, {'E', typeid(NdArray<float>)},   {'D', typeid(NdArray<double>)},
    },
    ScalarTypeMap{{'L', typeid(bool)},    {'J', typeid(int32_t)}, {'B', typeid(int32_t)}, {'I', typeid(int32_t)},
                  {'K', typeid(int64_t)}, {'E', typeid(float)},   {'D', typeid(double)},  {'A', typeid(std::string)}},
    VectorTypeMap{{'B', typeid(std::vector<int32_t>)}, {'I', typeid(std::vector<int32_t>)},
                  {'J', typeid(std::vector<int32_t>)}, {'K', typeid(std::vector<int64_t>)},
                  {'E', typeid(std::vector<float>)},   {'D', typeid(std::vector<double>)},
                  {'A', typeid(std::string)}};

std::pair<std::type_index, std::size_t> binaryFormatToType(const std::string&         format,
                                                           const std::vector<size_t>& shape) {
  // Get the size out of the format string
  char ft   = format.front();
  int  size = 1;
  if (std::isdigit(format.front())) {
    size = std::stoi(format.substr(0, format.size() - 1));
    ft   = format.back();
  }

  // If shape is set *and* it has more than one dimension, it is an NdArray
  if (shape.size() > 1) {
    auto i = std::find_if(NdTypeMap.begin(), NdTypeMap.end(),
                          [ft](const std::pair<char, std::type_index>& p) { return p.first == ft; });
    if (i != NdTypeMap.end()) {
      return {i->second, size};
    }
  }
  // If the dimensionality is 1, it is a scalar
  else if (size == 1) {
    auto i = std::find_if(ScalarTypeMap.begin(), ScalarTypeMap.end(),
                          [ft](const std::pair<char, std::type_index>& p) { return p.first == ft; });
    if (i != ScalarTypeMap.end()) {
      return {i->second, size};
    }
  }
  // Last, vectors
  else {
    auto i = std::find_if(VectorTypeMap.begin(), VectorTypeMap.end(),
                          [ft](const std::pair<char, std::type_index>& p) { return p.first == ft; });
    if (i != VectorTypeMap.end()) {
      return {i->second, size};
    }
  }
  throw Elements::Exception() << "FITS binary table format " << format << " is not "
                              << "yet supported";
}

std::vector<size_t> parseTDIM(const std::string& tdim) {
  std::vector<size_t> result{};
  if (!tdim.empty() && tdim.front() == '(' && tdim.back() == ')') {
    auto                                          subtdim = tdim.substr(1, tdim.size() - 2);
    boost::char_separator<char>                   sep{","};
    boost::tokenizer<boost::char_separator<char>> tok{subtdim, sep};
    std::transform(tok.begin(), tok.end(), std::back_inserter(result),
                   [](const std::string& s) { return boost::lexical_cast<size_t>(s); });
    // Note: the shape is in fortran order, so we need to reverse
    std::reverse(result.begin(), result.end());
  }
  return result;
}

std::vector<std::pair<std::type_index, std::size_t>> autoDetectColumnTypes(const CCfits::Table& table_hdu) {
  std::vector<std::pair<std::type_index, std::size_t>> types{};
  for (int i = 1; i <= table_hdu.numCols(); i++) {
    auto& column = table_hdu.column(i);

    if (typeid(table_hdu) == typeid(CCfits::BinTable)) {
      column.setDimen();
      types.push_back(binaryFormatToType(column.format(), parseTDIM(column.dimen())));
    } else {
      types.push_back(asciiFormatToType(column.format()));
    }
  }
  return types;
}

std::vector<std::string> autoDetectColumnUnits(const CCfits::Table& table_hdu) {
  std::vector<std::string> units{};
  for (int i = 1; i <= table_hdu.numCols(); ++i) {
    units.push_back(table_hdu.column(i).unit());
  }
  return units;
}

std::vector<std::string> autoDetectColumnDescriptions(const CCfits::Table& table_hdu) {
  std::vector<std::string> descriptions{};
  for (int i = 1; i <= table_hdu.numCols(); ++i) {
    std::string desc;
    auto        key = table_hdu.keyWord().find("TDESC" + std::to_string(i));
    if (key != table_hdu.keyWord().end()) {
      key->second->value(desc);
    }
    descriptions.push_back(desc);
  }
  return descriptions;
}

template <typename T>
std::vector<Row::cell_type> convertScalarColumn(CCfits::Column& column, long first, long last) {
  std::vector<T> data;
  column.read(data, first, last);
  std::vector<Row::cell_type> result;
  std::copy(data.begin(), data.end(), std::back_inserter(result));
  return result;
}

template <typename T>
std::vector<Row::cell_type> convertVectorColumn(CCfits::Column& column, long first, long last) {
  std::vector<std::valarray<T>> data;
  column.readArrays(data, first, last);
  std::vector<Row::cell_type> result;
  result.reserve(data.size());
  std::transform(data.begin(), data.end(), std::back_inserter(result),
                 [](const std::valarray<T>& valar) { return std::vector<T>(std::begin(valar), std::end(valar)); });
  return result;
}

template <typename T>
std::vector<Row::cell_type> convertNdArrayColumn(CCfits::Column& column, long first, long last) {
  std::vector<std::valarray<T>> data;
  column.readArrays(data, first, last);
  std::vector<size_t>         shape = parseTDIM(column.dimen());
  std::vector<Row::cell_type> result;
  result.reserve(data.size());
  std::transform(data.begin(), data.end(), std::back_inserter(result), [&shape](const std::valarray<T>& valar) {
    return NdArray<T>(shape, std::move(std::vector<T>(std::begin(valar), std::end(valar))));
  });
  return result;
}

std::vector<Row::cell_type> translateColumn(CCfits::Column& column, std::type_index type) {
  return translateColumn(column, type, 1, column.rows());
}

std::vector<Row::cell_type> translateColumn(CCfits::Column& column, std::type_index type, long first, long last) {
  if (type == typeid(bool)) {
    return convertScalarColumn<bool>(column, first, last);
  } else if (type == typeid(int32_t)) {
    return convertScalarColumn<int32_t>(column, first, last);
  } else if (type == typeid(int64_t)) {
    return convertScalarColumn<int64_t>(column, first, last);
  } else if (type == typeid(float)) {
    return convertScalarColumn<float>(column, first, last);
  } else if (type == typeid(double)) {
    return convertScalarColumn<double>(column, first, last);
  } else if (type == typeid(std::string)) {
    return convertScalarColumn<std::string>(column, first, last);
  } else if (type == typeid(std::vector<int32_t>)) {
    return convertVectorColumn<int32_t>(column, first, last);
  } else if (type == typeid(std::vector<int64_t>)) {
    return convertVectorColumn<int64_t>(column, first, last);
  } else if (type == typeid(std::vector<float>)) {
    return convertVectorColumn<float>(column, first, last);
  } else if (type == typeid(std::vector<double>)) {
    return convertVectorColumn<double>(column, first, last);
  } else if (type == typeid(NdArray<int32_t>)) {
    return convertNdArrayColumn<int32_t>(column, first, last);
  } else if (type == typeid(NdArray<int64_t>)) {
    return convertNdArrayColumn<int64_t>(column, first, last);
  } else if (type == typeid(NdArray<float>)) {
    return convertNdArrayColumn<float>(column, first, last);
  } else if (type == typeid(NdArray<double>)) {
    return convertNdArrayColumn<double>(column, first, last);
  }
  throw Elements::Exception() << "Unsupported column type " << type.name();
}

}  // namespace Table
}  // end of namespace Euclid
