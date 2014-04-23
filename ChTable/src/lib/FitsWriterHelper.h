/** 
 * @file FitsWriterHelper.h
 * @date April 23, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHTABLE_FITSWRITERHELPER_H
#define	CHTABLE_FITSWRITERHELPER_H

#include <string>
#include <vector>
#include <typeindex>
#include <CCfits/CCfits>
#include "ChTable/Table.h"

namespace ChTable {

std::vector<std::string> getAsciiFormatList(const Table& table);

std::vector<std::string> getBinaryFormatList(const Table& table);

void populateColumn(const Table& table, size_t column_index, CCfits::Table* table_hdu);

}

#endif	/* CHTABLE_FITSWRITERHELPER_H */

