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
 * @file src/lib/FitsReaderHelper.h
 * @date April 17, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef FITSREADERHELPER_H
#define FITSREADERHELPER_H

#include <CCfits/CCfits>
#include <string>
#include <typeindex>
#include <vector>

#include "ElementsKernel/Export.h"

#include "Table/Row.h"

namespace Euclid {
namespace Table {

/**
 * @brief
 * Reads the column names of the given table HDU
 * @details
 * For more information about the column naming see the constructor of FitsReader.
 *
 * @param table_hdu The HDU to read the columns from
 * @return the column names
 */
ELEMENTS_API std::vector<std::string> autoDetectColumnNames(const CCfits::Table& table_hdu);

/**
 * @brief
 * Reads the column types of the given table HDU
 * @details
 * For more information about the supported types and the type conversion see the
 * FitsReader::read() method.
 *
 * @param table_hdu The HDU to read the types from
 * @return the column types
 * @throws Elements::Exception
 *    if a column type is not supported
 */
ELEMENTS_API std::vector<std::type_index> autoDetectColumnTypes(const CCfits::Table& table_hdu);

/// Reads the column units based on the TUNITn keyword
ELEMENTS_API std::vector<std::string> autoDetectColumnUnits(const CCfits::Table& table_hdu);

/// Reads the column descriptions based on the TDESCn keyword
ELEMENTS_API std::vector<std::string> autoDetectColumnDescriptions(const CCfits::Table& table_hdu);

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
ELEMENTS_API std::vector<Row::cell_type> translateColumn(CCfits::Column& column, std::type_index type);

ELEMENTS_API std::vector<Row::cell_type> translateColumn(CCfits::Column& column, std::type_index type, long first, long last);

}  // namespace Table
}  // end of namespace Euclid

#endif /* FITSREADERHELPER_H */
