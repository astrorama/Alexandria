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
 * @file src/lib/ColumnDescription.cpp
 * @date 09/06/16
 * @author nikoapos
 */

// The std regex library is not fully implemented in GCC 4.8. The following lines
// make use of the BOOST library and can be modified if GCC 4.9 will be used in
// the future.
#if defined(__GNUC__) && __GNUC__ == 4 && __GNUC_MINOR__ <= 8
#include <boost/regex.hpp>
using boost::regex;
using boost::regex_match;
#else
#include <regex>
using std::regex;
using std::regex_match;
#endif
#include "ElementsKernel/Exception.h"

#include "Table/ColumnDescription.h"

namespace Euclid {
namespace Table {

ColumnDescription::ColumnDescription(std::string input_name, std::type_index input_type, std::string input_unit,
                                     std::string input_description)
    : name(input_name), type(input_type), unit(input_unit), description(input_description) {
  static const regex vertical_space_regex{".*[\\n\\v\\f\\r].*"};

  if (input_name.empty()) {
    throw Elements::Exception() << "Empty string name is not allowed";
  }
  if (regex_match(input_name, vertical_space_regex)) {
    throw Elements::Exception() << "Column name '" << input_name << "' contains "
                                << "vertical whitespace characters";
  }
}

}  // namespace Table
}  // namespace Euclid
