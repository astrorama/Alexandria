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
                                             const std::vector<std::type_index>& types,
                                             const std::vector<std::string>& units,
                                             const std::vector<std::string>& descriptions);

}
} // end of namespace Euclid

#endif /* TABLE_READERHELPER_H */
