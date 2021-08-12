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

#include "Table/ColumnDescription.h"
#include "AlexandriaKernel/RegexHelper.h"
#include "ElementsKernel/Exception.h"

namespace Euclid {
namespace Table {

ColumnDescription::ColumnDescription(std::string input_name, std::type_index input_type, std::string input_unit,
                                     std::string input_description)
    : name(input_name), type(input_type), unit(input_unit), description(input_description) {
  static const regex::regex vertical_whitespace{".*[\\n\\v\\f\\r].*"};

  if (input_name.empty()) {
    throw Elements::Exception() << "Empty string name is not allowed";
  }
  if (regex_match(input_name, vertical_whitespace)) {
    throw Elements::Exception() << "Column name '" << input_name << "' contains "
                                << "vertical whitespace characters";
  }
}

}  // namespace Table
}  // namespace Euclid
