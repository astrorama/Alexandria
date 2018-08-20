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
 * @file src/lib/FitsWriterHelper.h
 * @date April 23, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef TABLE_FITSWRITERHELPER_H
#define TABLE_FITSWRITERHELPER_H

#include <string>
#include <vector>
#include <typeindex>
#include <CCfits/CCfits>

#include "ElementsKernel/Export.h"

#include "Table/Table.h"

namespace Euclid {
namespace Table {

/**
 * @brief
 * Returns a vector with strings representing the FITS ASCII table formats for
 * the given table
 * @details
 * For more details on the conversions between the table formats and the FITS
 * ASCII formats see the documentation of the FitsWriter::write() method.
 *
 * @param table The table
 * @return The list of FITS ASCII table formats
 */
ELEMENTS_API std::vector<std::string> getAsciiFormatList(const Table& table);

/**
 * @brief
 * Returns a vector with strings representing the FITS binary table formats for
 * the given table
 * @details
 * For more details on the conversions between the table formats and the FITS
 * binary formats see the documentation of the FitsWriter::write() method.
 *
 * @param table The table
 * @return The list of FITS binary table formats
 */
ELEMENTS_API std::vector<std::string> getBinaryFormatList(const Table& table);

void populateColumn(const Table& table, size_t column_index, CCfits::ExtHDU& table_hdu, long first_row=1);

}
} // end of namespace Euclid

#endif /* TABLE_FITSWRITERHELPER_H */
