/** 
 * @file ReaderHelper.h
 * @date April 21, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHTABLE_READERHELPER_H
#define	CHTABLE_READERHELPER_H

#include <memory>
#include <string>
#include <vector>
#include <typeindex>
#include "ChTable/ColumnInfo.h"

namespace ChTable {



/// Creates a ColumnInfo object from the given names and types
std::shared_ptr<ColumnInfo> createColumnInfo(const std::vector<std::string>& names,
                                             const std::vector<std::type_index>& types);

}

#endif	/* CHTABLE_READERHELPER_H */

