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
 * @file src/lib/AsciiWriterHelper.cpp
 * @date April 16, 2014
 * @author Nikolaos Apostolakos
 */

#include "AsciiWriterHelper.h"
#include "AlexandriaKernel/RegexHelper.h"
#include "ElementsKernel/Exception.h"
#include <algorithm>
#include <boost/lexical_cast.hpp>

#if BOOST_VERSION < 107300
#include <boost/io/detail/quoted_manip.hpp>
#else
#include <boost/io/quoted.hpp>
#endif

namespace Euclid {
namespace Table {

using NdArray::NdArray;
extern const std::vector<std::pair<std::string, std::type_index>> KeywordTypeMap;

std::string typeToKeyword(std::type_index type) {
  auto i = std::find_if(KeywordTypeMap.begin(), KeywordTypeMap.end(),
                        [type](const std::pair<std::string, std::type_index>& p) { return p.second == type; });
  if (i != KeywordTypeMap.end()) {
    return i->first;
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
  for (const auto& row : table) {
    for (size_t i = 0; i < sizes.size(); ++i) {
      sizes[i] = std::max(sizes[i], boost::apply_visitor(ToStringVisitor{}, row[i]).size());
    }
  }
  std::for_each(sizes.begin(), sizes.end(), [](size_t& s) { ++s; });
  return sizes;
}

std::string quoted(const std::string& str) {
  regex::regex whitespace_quotes{".*[\\s\"].*"};
  if (!regex_match(str, whitespace_quotes))
    return str;
  std::stringstream q;
  q << boost::io::quoted(str);
  return q.str();
}

}  // namespace Table
}  // end of namespace Euclid
