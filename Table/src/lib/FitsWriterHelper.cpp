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
 * @file src/lib/FitsWriterHelper.cpp
 * @date April 23, 2014
 * @author Nikolaos Apostolakos
 */

#include <algorithm>
#include <sstream>
#include <iomanip>
#include <valarray>
#include <boost/lexical_cast.hpp>
#include <CCfits/CCfits>
#include "FitsWriterHelper.h"
#include "Table/Table.h"
#include "ElementsKernel/Exception.h"

namespace Euclid {
namespace Table {

using NdArray::NdArray;

template<typename T>
std::string scientificFormat(T value) {
  std::ostringstream stream;
  stream << std::scientific << value;
  return stream.str();
}

size_t maxWidth(const Table& table, size_t column_index) {
  size_t width = 0;
  for (const auto& row : table) {
    width = std::max(width, boost::lexical_cast<std::string>(row[column_index]).size());
  }
  return width;
}

size_t maxWidthScientific(const Table& table, size_t column_index) {
  size_t width = 0;
  for (const auto& row : table) {
    width = std::max(width, scientificFormat(row[column_index]).size());
  }
  return width;
}

std::vector<std::string> getAsciiFormatList(const Table& table) {
  auto column_info = table.getColumnInfo();
  std::vector<std::string> format_list {};
  for (size_t column_index=0; column_index<column_info->size(); ++column_index) {
    auto type = column_info->getDescription(column_index).type;
    if (type == typeid(bool)) {
      format_list.push_back("I1");
    } else if (type == typeid(int32_t) || type == typeid(int64_t)) {
      size_t width = maxWidth(table, column_index);
      format_list.push_back("I" + boost::lexical_cast<std::string>(width));
    } else if (type == typeid(float) || type == typeid(double)) {
      size_t width = maxWidthScientific(table, column_index);
      format_list.push_back("E" + boost::lexical_cast<std::string>(width));
    } else if (type == typeid(std::string)) {
      size_t width = maxWidth(table, column_index);
      format_list.push_back("A" + boost::lexical_cast<std::string>(width));
    } else {
      throw Elements::Exception() << "Unsupported column format for FITS ASCII table export: " << type.name();
    }
  }
  return format_list;
}

template <typename T>
size_t vectorSize(const Table& table, size_t column_index) {
  size_t size = boost::get<std::vector<T>>(table[0][column_index]).size();
  for (const auto& row : table) {
    if (boost::get<std::vector<T>>(row[column_index]).size() != size) {
      throw Elements::Exception() << "Binary FITS table variable length vector columns are not supported";
    }
  }
  return size;
}

template <typename T>
size_t ndArraySize(const Table& table, size_t column_index) {
  const auto &ndarray = boost::get<NdArray<T>>(table[0][column_index]);
  size_t size = ndarray.size();
  auto shape = ndarray.shape();
  for (const auto& row : table) {
    if (boost::get<NdArray<T>>(row[column_index]).shape() != shape) {
      throw Elements::Exception() << "Binary FITS table variable shape array columns are not supported";
    }
  }
  return size;
}

std::vector<std::string> getBinaryFormatList(const Table& table) {
  auto column_info = table.getColumnInfo();
  std::vector<std::string> format_list {};
  for (size_t column_index=0; column_index<column_info->size(); ++column_index) {
    auto type = column_info->getDescription(column_index).type;
    if (type == typeid(bool)) {
      format_list.push_back("L");
    } else if (type == typeid(int32_t)) {
      format_list.push_back("J");
    } else if (type == typeid(int64_t)) {
      format_list.push_back("K");
    } else if (type == typeid(float)) {
      format_list.push_back("E");
    } else if (type == typeid(double)) {
      format_list.push_back("D");
    } else if (type == typeid(std::string)) {
      size_t width = maxWidth(table, column_index);
      format_list.push_back(boost::lexical_cast<std::string>(width) + "A");
    } else if (type == typeid(std::vector<bool>)) {
      size_t size = vectorSize<bool>(table, column_index);
      format_list.push_back(boost::lexical_cast<std::string>(size) + "L");
    } else if (type == typeid(std::vector<int32_t>)) {
      size_t size = vectorSize<int32_t>(table, column_index);
      format_list.push_back(boost::lexical_cast<std::string>(size) + "J");
    } else if (type == typeid(std::vector<int64_t>)) {
      size_t size = vectorSize<int64_t>(table, column_index);
      format_list.push_back(boost::lexical_cast<std::string>(size) + "K");
    } else if (type == typeid(std::vector<float>)) {
      size_t size = vectorSize<float>(table, column_index);
      format_list.push_back(boost::lexical_cast<std::string>(size) + "E");
    } else if (type == typeid(std::vector<double>)) {
      size_t size = vectorSize<double>(table, column_index);
      format_list.push_back(boost::lexical_cast<std::string>(size) + "D");
    } else if (type == typeid(NdArray<bool>)) {
      size_t size = ndArraySize<bool>(table, column_index);
      format_list.push_back(boost::lexical_cast<std::string>(size) + "L");
    } else if (type == typeid(NdArray<int32_t>)) {
      size_t size = ndArraySize<int32_t>(table, column_index);
      format_list.push_back(boost::lexical_cast<std::string>(size) + "J");
    } else if (type == typeid(NdArray<int64_t>)) {
      size_t size = ndArraySize<int64_t>(table, column_index);
      format_list.push_back(boost::lexical_cast<std::string>(size) + "K");
    } else if (type == typeid(NdArray<float>)) {
      size_t size = ndArraySize<float>(table, column_index);
      format_list.push_back(boost::lexical_cast<std::string>(size) + "E");
    } else if (type == typeid(NdArray<double>)) {
      size_t size = ndArraySize<double>(table, column_index);
      format_list.push_back(boost::lexical_cast<std::string>(size) + "D");
    } else {
      throw Elements::Exception() << "Unsupported column format for FITS binary table export: " << type.name();
    }
  }
  return format_list;
}

template<typename T>
std::vector<T> createColumnData(const Euclid::Table::Table& table, size_t column_index) {
  std::vector<T> data {};
  for (const auto& row : table) {
    data.push_back(boost::get<T>(row[column_index]));
  }
  return data;
}

template <typename T>
std::vector<std::valarray<T>> createVectorColumnData(const Euclid::Table::Table& table, size_t column_index) {
  std::vector<std::valarray<T>> result {};
  for (auto& row : table) {
    const auto& vec = boost::get<std::vector<T>>(row[column_index]);
    result.emplace_back(vec.data(), vec.size());
  }
  return result;
}

template <typename T>
std::vector<T> createSingleValueVectorColumnData(const Euclid::Table::Table& table, size_t column_index) {
  std::vector<T> result {};
  for (auto& row : table) {
    const auto& vec = boost::get<std::vector<T>>(row[column_index]);
    result.push_back(vec.front());
  }
  return result;
}

template <typename T>
std::vector<std::valarray<T>> createNdArrayColumnData(const Euclid::Table::Table& table, size_t column_index) {
  std::vector<std::valarray<T>> result{};
  for (auto& row : table) {
    const auto& ndarray = boost::get<NdArray<T>>(row[column_index]);
    result.emplace_back(ndarray.data().data(), ndarray.size());
  }
  return result;
}

template <typename T>
void populateVectorColumn(const Table& table, size_t column_index, CCfits::ExtHDU& table_hdu, long first_row) {
  const auto& vec = boost::get<std::vector<T>>(table[0][column_index]);
  if (vec.size() > 1) {
    table_hdu.column(column_index+1).writeArrays(createVectorColumnData<T>(table, column_index), first_row);
  } else {
    table_hdu.column(column_index+1).write(createSingleValueVectorColumnData<T>(table, column_index), first_row);
  }
}

template <typename T>
void populateNdArrayColumn(const Table& table, size_t column_index, CCfits::ExtHDU& table_hdu, long first_row) {
  table_hdu.column(column_index+1).writeArrays(createNdArrayColumnData<T>(table, column_index), first_row);
}

std::string getTDIM(const Table& table, size_t column_index) {
  auto& first_row = table[0];
  auto& cell = first_row[column_index];
  auto type = table.getColumnInfo()->getDescription(column_index).type;
  std::vector<size_t> shape;

  if (type == typeid(NdArray<bool>)) {
    shape = boost::get<NdArray<bool>>(cell).shape();
  } else if (type == typeid(NdArray<int32_t>)) {
    shape = boost::get<NdArray<int32_t>>(cell).shape();
  } else if (type == typeid(NdArray<int64_t>)) {
    shape = boost::get<NdArray<int64_t>>(cell).shape();
  } else if (type == typeid(NdArray<float>)) {
    shape = boost::get<NdArray<float>>(cell).shape();
  } else if (type == typeid(NdArray<double>)) {
    shape = boost::get<NdArray<double>>(cell).shape();
  } else {
    return "";
  }


  std::stringstream stream;
  stream << '(';

  int j;
  for (j = shape.size() - 1; j > 0; --j) {
    stream << shape[j] << ",";
  }

  stream << shape[j] << ')';
  return stream.str();
}

void populateColumn(const Table& table, size_t column_index, CCfits::ExtHDU& table_hdu, long first_row) {
  auto type = table.getColumnInfo()->getDescription(column_index).type;
  // CCfits indices start from 1
  if (type == typeid(bool)) {
    table_hdu.column(column_index+1).write(createColumnData<bool>(table, column_index), first_row);
  } else if (type == typeid(int32_t)) {
    table_hdu.column(column_index+1).write(createColumnData<int32_t>(table, column_index), first_row);
  } else if (type == typeid(int64_t)) {
    table_hdu.column(column_index+1).write(createColumnData<int64_t>(table, column_index), first_row);
  } else if (type == typeid(float)) {
    table_hdu.column(column_index+1).write(createColumnData<float>(table, column_index), first_row);
  } else if (type == typeid(double)) {
    table_hdu.column(column_index+1).write(createColumnData<double>(table, column_index), first_row);
  } else if (type == typeid(std::string)) {
    table_hdu.column(column_index+1).write(createColumnData<std::string>(table, column_index), first_row);
  } else if (type == typeid(std::vector<int32_t>)) {
    populateVectorColumn<int32_t>(table, column_index, table_hdu, first_row);
  } else if (type == typeid(std::vector<int64_t>)) {
    populateVectorColumn<int64_t>(table, column_index, table_hdu, first_row);
  } else if (type == typeid(std::vector<float>)) {
    populateVectorColumn<float>(table, column_index, table_hdu, first_row);
  } else if (type == typeid(std::vector<double>)) {
    populateVectorColumn<double>(table, column_index, table_hdu, first_row);
  } else if (type == typeid(NdArray<int32_t>)) {
    populateNdArrayColumn<int32_t>(table, column_index, table_hdu, first_row);
  } else if (type == typeid(NdArray<int64_t>)) {
    populateNdArrayColumn<int64_t>(table, column_index, table_hdu, first_row);
  } else if (type == typeid(NdArray<float>)) {
    populateNdArrayColumn<float>(table, column_index, table_hdu, first_row);
  } else if (type == typeid(NdArray<double>)) {
    populateNdArrayColumn<double>(table, column_index, table_hdu, first_row);
  } else {
    throw Elements::Exception() << "Cannot populate FITS column with data of type " << type.name();
  }
}

}
} // end of namespace Euclid
