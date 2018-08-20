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
 * @file src/lib/AsciiWriterHelper.h
 * @date April 16, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef TABLE_ASCIIWRITERHELPER_H
#define TABLE_ASCIIWRITERHELPER_H

#include <vector>
#include <typeindex>

#include "ElementsKernel/Export.h"


#include "Table/Table.h"

namespace Euclid {
namespace Table {

/**
 * @brief
 * Converts a type to its string representation
 *
 * @param type The type to convert
 * @return The string representation
 * @throws Elements::Exception
 *    if the given type is not supported
 */
ELEMENTS_API std::string typeToKeyword(std::type_index type);

/**
 * @brief
 * Calculates the sizes in characters each column of the table needs
 * @details
 * The size is calculated as the size of the longest column entry (including type
 * and name) plus one to ensure separation of the values.
 *
 * @param table The table
 * @return  the sizes of the columns
 */
ELEMENTS_API std::vector<size_t> calculateColumnLengths(const Table& table);

}
} // end of namespace Euclid

#endif /* TABLE_ASCIIWRITERHELPER_H */
