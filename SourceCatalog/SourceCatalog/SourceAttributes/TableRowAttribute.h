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
 * @file TableRowAttribute.h
 * @author nikoapos
 */

#ifndef _SOURCECATALOG_SOURCEATTRIBUTES_TABLEROWATTRIBUTE_H
#define _SOURCECATALOG_SOURCEATTRIBUTES_TABLEROWATTRIBUTE_H

#include "Table/Row.h"
#include "SourceCatalog/Attribute.h"

namespace Euclid {
namespace SourceCatalog {

/**
 * @class TableRowAttribute
 * 
 * @brief Source attribute which can be used to retrieve the table row used
 * to create the source
 */
class TableRowAttribute  : public Attribute {
  
public:
  
  /// Constructs a new TableRowAttribute with the given row
  TableRowAttribute(Table::Row row);

  /// Destructor
  virtual ~TableRowAttribute() = default;
  
  /// Returns the table row
  const Table::Row& getRow() const;
  
private:
  
  Table::Row m_row;
  
};

} // namespace SourceCatalog
} // end of namespace Euclid

#endif /* _SOURCECATALOG_SOURCEATTRIBUTES_TABLEROWATTRIBUTE_H */

