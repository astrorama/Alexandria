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
 * @file src/lib/FitsReaderHelper.cpp
 * @date April 17, 2014
 * @author Nikolaos Apostolakos
 */

#include <CCfits/CCfits>
#include <boost/lexical_cast.hpp>
#include <boost/tokenizer.hpp>
#include "ElementsKernel/Exception.h"
#include "FitsReaderHelper.h"

namespace Euclid {
namespace Table {

std::vector<std::string> autoDetectColumnNames(const CCfits::Table& table_hdu) {
  std::vector<std::string> names {};
  for (int i=1; i<=table_hdu.numCols(); ++i) {
    std::string name = table_hdu.column(i).name();
    if (name.empty()) {
      name = "Col" + std::to_string(i);
    }
    names.push_back(std::move(name));
  }
  return names;
}

std::type_index asciiFormatToType(const std::string& format) {
  if (format[0] == 'A') {
    return typeid(std::string);
  } else if (format[0] == 'I') {
    return typeid(int64_t);
  } else if (format[0] == 'F') {
    return typeid(double);
  } else if (format[0] == 'E') {
    return typeid(double);
  } else if (format[0] == 'D') {
    return typeid(double);
  }
  throw Elements::Exception() << "FITS ASCII table format " << format << " is not "
                            << "yet supported";
}

std::type_index binaryFormatToType(const std::string& format, const std::vector<size_t>& shape) {
  if (format[0] == 'L') {
    return typeid(bool);
  } else if (format[0] == 'B') {
    return typeid(int32_t);
  } else if (format[0] == 'I') {
    return typeid(int32_t);
  } else if (format[0] == 'J') {
    return typeid(int32_t);
  } else if (format[0] == 'K') {
    return typeid(int64_t);
  } else if (format.back() == 'A') {
    return typeid(std::string);
  } else if (format[0] == 'E') {
    return typeid(float);
  } else if (format[0] == 'D') {
    return typeid(double);
  } else if (shape.empty()) {
    if (format.back() == 'B') {
      return typeid(std::vector<int32_t>);
    } else if (format.back() == 'I') {
      return typeid(std::vector<int32_t>);
    } else if (format.back() == 'J') {
      return typeid(std::vector<int32_t>);
    } else if (format.back() == 'K') {
      return typeid(std::vector<int64_t>);
    } else if (format.back() == 'E') {
      return typeid(std::vector<float>);
    } else if (format.back() == 'D') {
      return typeid(std::vector<double>);
    }
  } else {
    if (format.back() == 'B') {
      return typeid(NdArray::NdArray<int32_t>);
    } else if (format.back() == 'I') {
      return typeid(NdArray::NdArray<int32_t>);
    } else if (format.back() == 'J') {
      return typeid(NdArray::NdArray<int32_t>);
    } else if (format.back() == 'K') {
      return typeid(NdArray::NdArray<int64_t>);
    } else if (format.back() == 'E') {
      return typeid(NdArray::NdArray<float>);
    } else if (format.back() == 'D') {
      return typeid(NdArray::NdArray<double>);
    }
  }
  throw Elements::Exception() << "FITS binary table format " << format << " is not "
                            << "yet supported";
}

std::vector<size_t> parseTDIM(const std::string &tdim) {
  std::vector<size_t> result {};
  if (!tdim.empty() && tdim[0] == '(' && tdim.back() == ')') {
    boost::char_separator<char> sep{","};
    boost::tokenizer<boost::char_separator<char>> tok{tdim.substr(1, tdim.size() - 2), sep};
    for (auto& s : tok) {
      result.push_back(boost::lexical_cast<size_t>(s));
    }
    // Note: the shape is in fortran order, so we need to reverse
    std::reverse(result.begin(), result.end());
  }
  return result;
}

std::vector<std::type_index> autoDetectColumnTypes(const CCfits::Table& table_hdu) {
  std::vector<std::type_index> types {};
  for (int i=1; i<=table_hdu.numCols(); i++) {
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
  std::vector<std::string> units {};
  for (int i=1; i<=table_hdu.numCols(); ++i) {
    units.push_back(table_hdu.column(i).unit());
  }
  return units;
}

std::vector<std::string> autoDetectColumnDescriptions(const CCfits::Table& table_hdu) {
  std::vector<std::string> descriptions {};
  for (int i=1; i<=table_hdu.numCols(); ++i) {
    std::string desc;
    auto key = table_hdu.keyWord().find("TDESC" + std::to_string(i));
    if (key != table_hdu.keyWord().end()) {
      key->second->value(desc);
    }
    descriptions.push_back(desc);
  }
  return descriptions;
}

template<typename T>
std::vector<Row::cell_type> convertScalarColumn(CCfits::Column& column, long first, long last) {
  std::vector<T> data;
  column.read(data, first, last);
  std::vector<Row::cell_type> result;
  for (auto value : data) {
    result.push_back(value);
  }
  return result;
}

template<typename T>
std::vector<Row::cell_type> convertVectorColumn(CCfits::Column& column, long first, long last) {
  std::vector<std::valarray<T>> data;
  column.readArrays(data, first, last);
  std::vector<Row::cell_type> result;
  for (auto& valar : data) {
    result.push_back(std::vector<T>(std::begin(valar),std::end(valar)));
  }
  return result;
}

template<typename T>
std::vector<Row::cell_type> convertNdArrayColumn(CCfits::Column& column, long first, long last) {
  std::vector<std::valarray<T>> data;
  column.readArrays(data, first, last);
  std::vector<size_t> shape = parseTDIM(column.dimen());

  std::vector<Row::cell_type> result;
  for (auto& valar : data) {
    result.push_back(NdArray::NdArray<T>(shape, std::move(std::vector<T>(std::begin(valar), std::end(valar)))));
  }
  return result;
}

std::vector<Row::cell_type> translateColumn(CCfits::Column& column, std::type_index type) {
  return translateColumn(column, type, 1, column.rows());
}

std::vector<Row::cell_type> translateColumn(CCfits::Column& column, std::type_index type, long first, long last) {
  if (type == typeid(bool)) {
    return convertScalarColumn<bool>(column, first, last);
  } if (type == typeid(int32_t)) {
    return convertScalarColumn<int32_t>(column, first, last);
  } if (type == typeid(int64_t)) {
    return convertScalarColumn<int64_t>(column, first, last);
  } if (type == typeid(float)) {
    return convertScalarColumn<float>(column, first, last);
  } if (type == typeid(double)) {
    return convertScalarColumn<double>(column, first, last);
  } if (type == typeid(std::string)) {
    return convertScalarColumn<std::string>(column, first, last);
  } if (type == typeid(std::vector<int32_t>)) {
    return convertVectorColumn<int32_t>(column, first, last);
  } if (type == typeid(std::vector<int64_t>)) {
    return convertVectorColumn<int64_t>(column, first, last);
  } if (type == typeid(std::vector<float>)) {
    return convertVectorColumn<float>(column, first, last);
  } if (type == typeid(std::vector<double>)) {
    return convertVectorColumn<double>(column, first, last);
  } if (type == typeid(NdArray::NdArray<int32_t>)) {
    return convertNdArrayColumn<int32_t>(column, first, last);
  } if (type == typeid(NdArray::NdArray<int64_t>)) {
    return convertNdArrayColumn<int64_t>(column, first, last);
  } if (type == typeid(NdArray::NdArray<float>)) {
    return convertNdArrayColumn<float>(column, first, last);
  } if (type == typeid(NdArray::NdArray<double>)) {
    return convertNdArrayColumn<double>(column, first, last);
  }
  throw Elements::Exception() << "Unsupported column type " << type.name();
}

}
} // end of namespace Euclid
