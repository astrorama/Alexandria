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

void populateColumn(const Table& table, size_t column_index, CCfits::Table* table_hdu);

}
} // end of namespace Euclid

#endif /* TABLE_FITSWRITERHELPER_H */
