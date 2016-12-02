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
 * @file src/lib/AsciiReader.cpp
 * @date 12/02/16
 * @author nikoapos
 */

#include "ElementsKernel/Exception.h"
#include "Table/AsciiReader.h"

namespace Euclid {
namespace Table {

AsciiReader& AsciiReader::setCommentIndicator(const std::string& indicator) {
  if (m_reading_started) {
    throw Elements::Exception() << "Changing comment indicator after reading "
            << "has started is not allowed";
  }
  if (indicator.empty()) {
    throw Elements::Exception() << "Empty string as comment indicator";
  }
  m_comment = indicator;
  return *this;
}

//const ColumnInfo& AsciiReader::getInfo() {
//  
//}
//
//Table AsciiReader::read(long rows) {
//
//}
//
//void AsciiReader::skip(long rows) {
//
//}
//
//bool AsciiReader::hasMoreRows() {
//
//}

} // Table namespace
} // Euclid namespace



