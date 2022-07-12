/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
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
 * @file SourceCatalog/AttributeFromRow.h
 *
 * @date Apr 17, 2014
 * @author Pierre Dubath
 */
#ifndef ATTRIBUTEHANDLER_H_
#define ATTRIBUTEHANDLER_H_

#include "SourceCatalog/Attribute.h"
#include "Table/Row.h"

namespace Euclid {
namespace SourceCatalog {

/**
 * @class AttributeFromRow
 * @brief Interface for building a source Attribute from a table Row
 *
 * @details This interface is defined to build source Attributes from table rows. The rules
 * for formatting the specific Attribute from the general Table columns must be provided
 * in the implementation constructors. They are then defined during object creation only
 * once for the complete Table. The createAttribute method can then be called for each
 * source, i.e., for each row of the Table.
 *
 */
class AttributeFromRow {

public:
  virtual ~AttributeFromRow() = default;

  /**
   * @brief The createAttribute method for creating an Attribute from a Table row
   * @details
   * @param row A reference to a Row of a Table
   * @return A unique pointer to the newly created Attribute
   */
  virtual std::unique_ptr<Attribute> createAttribute(const Euclid::Table::Row& row) = 0;
};

}  // namespace SourceCatalog
}  // end of namespace Euclid

#endif  // ATTRIBUTEHANDLER_H_
