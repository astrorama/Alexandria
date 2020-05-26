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
 * @file src/lib/ColumnDescription.cpp
 * @date 09/06/16
 * @author nikoapos
 */

// The std regex library is not fully implemented in GCC 4.8. The following lines
// make use of the BOOST library and can be modified if GCC 4.9 will be used in
// the future.
// #include <regex>
#include <boost/regex.hpp>
using boost::regex;
using boost::regex_match;
#include "ElementsKernel/Exception.h"

#include "Table/ColumnDescription.h"

namespace Euclid {
namespace Table {

ColumnDescription::ColumnDescription(std::string name, std::type_index type,
                                     std::string unit, std::string description)
        : name(name), type(type), unit(unit), description(description) {
    if (name.empty()) {
      throw Elements::Exception() << "Empty string name is not allowed";
    }
    if (regex_match(name, regex{".*\\v.*"})) {
      throw Elements::Exception() << "Column name '" << name << "' contains "
                                << "vertical whitespace characters";
    }
}

} // Table namespace
} // Euclid namespace



