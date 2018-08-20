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
 * @file src/lib/AsciiReaderHelper.h
 * @date April 15, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef TABLE_ASCIIREADERHELPER_H
#define TABLE_ASCIIREADERHELPER_H

#include <istream>
#include <string>
#include <typeindex>
#include <map>


#include "ElementsKernel/Export.h"
#include "Table/Row.h"

namespace Euclid {
namespace Table {

/**
 * @class StreamRewinder
 *
 * @brief
 * This class gets a stream as argument during construction and when it is deleted
 * it sets the position of the stream back to where it was during the constructor
 * call.
 */
class StreamRewinder {
public:
  StreamRewinder(std::istream& stream) : m_stream(stream), m_state(stream.exceptions()), m_position(stream.tellg()) { }
  ~StreamRewinder() {
    m_stream.clear();
    m_stream.seekg(m_position);
    m_stream.setstate(m_state);
  }
private:
  std::istream& m_stream;
  std::ios::iostate m_state;
  int m_position;
};

/**
 * @brief
 * Returns the number of whitespace separated tokens of the first non commented
 * line
 * @details
 * When the method returns the given stream is positioned at the same position
 * like before the method was called.
 *
 * @param in The string to read from
 * @param comment The comment pattern
 * @return The number of columns
 * @throws Elements::Exception
 *    if there is no uncommented, non-empty line
 */
ELEMENTS_API size_t countColumns(std::istream& in, const std::string& comment);

/**
 * @brief
 * Reads the column descriptions of the given stream
 * @details
 * For more information about the auto-detection rules see the constructor of
 * AsciiReader. When the method returns, the given stream is positioned at the
 * same position like before the method was called.
 *
 * @param in The stream to read the column names from
 * @param comment The comment pattern
 * @return The column descriptions from the stream comments
 * @throws Elements::Exception
 *    if there are duplicate column names
 * @throws Elements::Exception
 *    if any of the types is not one of the valid keywords
 */
ELEMENTS_API std::map<std::string, ColumnDescription> autoDetectColumnDescriptions(
                                      std::istream& in, const std::string& comment);

/**
 * @brief
 * Reads the column names of the given stream
 * @details
 * For more information about the auto-detection rules see the constructor of
 * AsciiReader. When the method returns, the given stream is positioned at the
 * same position like before the method was called.
 *
 * @param in The stream to read the column names from
 * @param comment The comment pattern
 * @param columns_number The number of columns
 * @return The auto-detected names of the columns
 * @throws Elements::Exception
 *    if there are duplicate column names
 */
ELEMENTS_API std::vector<std::string> autoDetectColumnNames(std::istream& in,
                                               const std::string& comment,
                                               size_t columns_number);

/**
 * @brief
 * Converts the given value to a Row::cell_type of the given type
 * @details
 * For more information of the supported types see the documentation of the
 * Euclid::Table::AsciiReader constructor.
 *
 * @param value The value to convert
 * @param type The type of the cell
 * @return The Row::cell_type representing the value
 * @throws Elements::Exception
 *    if the conversion fails
 */
ELEMENTS_API Row::cell_type convertToCellType(const std::string& value, std::type_index type);

ELEMENTS_API bool hasNextRow(std::istream& in, const std::string& comment);

ELEMENTS_API std::size_t countRemainingRows(std::istream& in, const std::string& comment);

}
} // end of namespace Euclid

#endif /* TABLE_ASCIIREADERHELPER_H */
