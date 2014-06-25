/** 
 * @file src/lib/AsciiWriterHelper.h
 * @date April 16, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHTABLE_ASCIIWRITERHELPER_H
#define	CHTABLE_ASCIIWRITERHELPER_H

#include <vector>
#include <typeindex>
#include "ChTable/Table.h"

namespace ChTable {

/**
 * @brief
 * Converts a type to its string representation
 * 
 * @param type The type to convert
 * @return The string representation
 * @throws ElementsException
 *    if the given type is not supported
 */
std::string typeToKeyword(std::type_index type);

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
std::vector<size_t> calculateColumnLengths(const Table& table);

}

#endif	/* CHTABLE_ASCIIWRITERHELPER_H */

