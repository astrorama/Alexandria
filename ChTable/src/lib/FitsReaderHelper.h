/** 
 * @file src/lib/FitsReaderHelper.h
 * @date April 17, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef FITSREADERHELPER_H
#define	FITSREADERHELPER_H

#include <vector>
#include <string>
#include <typeindex>
#include <CCfits/CCfits>
#include "ChTable/Row.h"

namespace ChTable {

/**
 * @brief
 * Reads the column names of the given table HDU
 * @details
 * For more information about the column naming see the constructor of FitsReader.
 * 
 * @param table_hdu The HDU to read the columns from
 * @return the column names
 */
std::vector<std::string> autoDetectColumnNames(const CCfits::Table& table_hdu);

/**
 * @brief
 * Reads the column types of the given table HDU
 * @details
 * For more information about the supported types and the type conversion see the
 * FitsReader::read() method.
 * 
 * @param table_hdu The HDU to read the types from
 * @return the column types
 * @throws ElementsException
 *    if a column type is not supported
 */
std::vector<std::type_index> autoDetectColumnTypes(const CCfits::Table& table_hdu);

/**
 * @brief
 * Returns a vector representing the given FITS table column data, converted to
 * the requested type.
 * @details
 * Note that the column CCfits::Column does not provide const versions of the
 * read methods, so the column argument cannot be const.
 * 
 * @param column The column to convert
 * @param type The type of the column
 * @return The data in Row::cell_type format
 */
std::vector<Row::cell_type> translateColumn(CCfits::Column& column, std::type_index type);

}

#endif	/* FITSREADERHELPER_H */

