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

/**
 * @file src/lib/AsciiWriterHelper.cpp
 * @date April 16, 2014
 * @author Nikolaos Apostolakos
 */

#include "AsciiWriterHelper.h"
#include "ElementsKernel/Exception.h"
#include <algorithm>
#include <boost/lexical_cast.hpp>
#include <boost/regex.hpp>

#if BOOST_VERSION < 107300
#include <boost/io/detail/quoted_manip.hpp>
#else
#include <boost/io/quoted.hpp>
#endif

namespace Euclid {
namespace Table {

using boost::regex;
using boost::regex_match;
using NdArray::NdArray;

std::string typeToKeyword(std::type_index type) {
  if (type == typeid(bool)) {
    return "bool";
  }
  if (type == typeid(int32_t)) {
    return "int";
  }
  if (type == typeid(int64_t)) {
    return "long";
  }
  if (type == typeid(float)) {
    return "float";
  }
  if (type == typeid(double)) {
    return "double";
  }
  if (type == typeid(std::string)) {
    return "string";
  }
  if (type == typeid(std::vector<bool>)) {
    return "[bool]";
  }
  if (type == typeid(std::vector<int32_t>)) {
    return "[int]";
  }
  if (type == typeid(std::vector<int64_t>)) {
    return "[long]";
  }
  if (type == typeid(std::vector<float>)) {
    return "[float]";
  }
  if (type == typeid(std::vector<double>)) {
    return "[double]";
  }
  if (type == typeid(NdArray<int32_t>)) {
    return "[int+]";
  }
  if (type == typeid(NdArray<int64_t>)) {
    return "[long+]";
  }
  if (type == typeid(NdArray<float>)) {
    return "[float+]";
  }
  if (type == typeid(NdArray<double>)) {
    return "[double+]";
  }
  throw Elements::Exception() << "Conversion to string for type " << type.name() << " is not supported";
}

std::vector<size_t> calculateColumnLengths(const Table& table) {
  std::vector<size_t> sizes{};
  // We initialize the values to the required size for the column name
  auto column_info = table.getColumnInfo();
  for (size_t i = 0; i < column_info->size(); ++i) {
    sizes.push_back(quoted(column_info->getDescription(i).name).size());
  }
  for (auto row : table) {
    for (size_t i = 0; i < sizes.size(); ++i) {
      sizes[i] = std::max(sizes[i], boost::apply_visitor(ToStringVisitor{}, row[i]).size());
    }
  }
  for (auto& s : sizes) {
    s += 1;
  }
  return sizes;
}

std::string quoted(const std::string& str) {
  regex whitespace_quotes{".*[\\s\"].*"};
  if (!regex_match(str, whitespace_quotes))
    return str;
  std::stringstream q;
  q << boost::io::quoted(str);
  return q.str();
}

}  // namespace Table
}  // end of namespace Euclid
