/**
 * @file src/lib/ReaderHelper.h
 * @date April 21, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef TABLE_READERHELPER_H
#define TABLE_READERHELPER_H

#include <memory>
#include <string>
#include <vector>
#include <typeindex>
#include "Table/ColumnInfo.h"

namespace Euclid {
namespace Table {

/// Creates a ColumnInfo object from the given names and types
std::shared_ptr<ColumnInfo> createColumnInfo(const std::vector<std::string>& names,
                                             const std::vector<std::type_index>& types);

}
} // end of namespace Euclid

#endif /* TABLE_READERHELPER_H */

