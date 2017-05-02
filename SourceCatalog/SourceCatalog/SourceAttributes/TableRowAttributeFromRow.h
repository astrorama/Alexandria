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

/* 
 * @file TableRowAttributeFromRow.h
 * @author nikoapos
 */

#ifndef _SOURCECATALOG_SOURCEATTRIBUTES_TABLEROWATTRIBUTEFROMROW_H
#define _SOURCECATALOG_SOURCEATTRIBUTES_TABLEROWATTRIBUTEFROMROW_H

#include "SourceCatalog/AttributeFromRow.h"

namespace Euclid {
namespace SourceCatalog {

/**
 * @class TableRowAttributeFromRow
 * 
 * @brief Implementation of the AttributeFromRow interfaces for the
 * TableRowAttribute
 */
class TableRowAttributeFromRow : public AttributeFromRow {
  
public:
  
  /// Destructor
  virtual ~TableRowAttributeFromRow() = default;
  
  /// Create a TableRowAttribute from the given row
  std::unique_ptr<Attribute> createAttribute(const Euclid::Table::Row& row) override;
  
};

} // namespace SourceCatalog
} // end of namespace Euclid

#endif /* _SOURCECATALOG_SOURCEATTRIBUTES_TABLEROWATTRIBUTEFROMROW_H */

