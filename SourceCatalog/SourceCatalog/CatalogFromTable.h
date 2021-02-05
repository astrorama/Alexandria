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
 * @file SourceCatalog/CatalogFromTable.h
 *
 * Created on: Apr 15, 2014
 *     Author: Pierre Dubath
 */
#ifndef CATALOGFACTORY_H_
#define CATALOGFACTORY_H_
#include <map>
#include <memory>
#include <string>
#include <utility>

#include "ElementsKernel/Export.h"

#include "SourceCatalog/AttributeFromRow.h"
#include "SourceCatalog/Catalog.h"
#include "Table/Table.h"

namespace Euclid {
namespace SourceCatalog {

class ELEMENTS_API CatalogFromTable {
public:
  CatalogFromTable(std::shared_ptr<Euclid::Table::ColumnInfo> column_info_ptr, const std::string& source_id_column_name,
                   std::vector<std::shared_ptr<AttributeFromRow>> attribute_from_row_ptr_vector);

  virtual ~CatalogFromTable();

  Euclid::SourceCatalog::Catalog createCatalog(const Euclid::Table::Table& input_table);

private:
  size_t m_source_id_index;

  std::vector<std::shared_ptr<AttributeFromRow>> m_attribute_from_row_ptr_vector;
};

}  // namespace SourceCatalog
}  // end of namespace Euclid

#endif  // CATALOGFACTORY_H_
