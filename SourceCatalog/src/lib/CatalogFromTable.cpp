/*
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
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
 * @file src/lib/CatalogFromTable.cpp
 *
 * Created on: Apr 16, 2014
 *     Author: Pierre Dubath
 */
#include "SourceCatalog/CatalogFromTable.h"
#include "ElementsKernel/Exception.h"
#include "SourceCatalog/PhotometryParsingException.h"
#include "SourceCatalog/SourceAttributes/Photometry.h"
#include "Table/CastVisitor.h"
#include "Table/ColumnInfo.h"
#include <vector>

namespace Euclid {
namespace SourceCatalog {

CatalogFromTable::CatalogFromTable(std::shared_ptr<Euclid::Table::ColumnInfo>     column_info_ptr,
                                   const std::string&                             source_id_column_name,
                                   std::vector<std::shared_ptr<AttributeFromRow>> attribute_from_row_ptr_vector) {

  std::unique_ptr<size_t> source_id_index_ptr = column_info_ptr->find(source_id_column_name);
  if (source_id_index_ptr == nullptr) {
    throw Elements::Exception() << "Column info does not have the column " << source_id_column_name;
  }
  m_source_id_index = *source_id_index_ptr;

  m_attribute_from_row_ptr_vector = std::move(attribute_from_row_ptr_vector);
}

CatalogFromTable::~CatalogFromTable() = default;

Euclid::SourceCatalog::Catalog CatalogFromTable::createCatalog(const Euclid::Table::Table& input_table) {

  std::vector<Source> source_vector;

  // Figure out the type of the first row, and then assume all following
  // must be of the same
  CastSourceIdVisitor castVisitor;

  for (const auto& row : input_table) {

    auto source_id = boost::apply_visitor(castVisitor, row[m_source_id_index]);

    std::vector<std::shared_ptr<Attribute>> attribute_ptr_vector(m_attribute_from_row_ptr_vector.size());
    try {
      std::transform(m_attribute_from_row_ptr_vector.begin(), m_attribute_from_row_ptr_vector.end(),
                     attribute_ptr_vector.begin(),
                     [&row](const std::shared_ptr<AttributeFromRow>& attr) { return attr->createAttribute(row); });
    } catch (const PhotometryParsingException& parsing_exception) {
      throw Elements::Exception() << "Parsing error while parsing the source with Id = " << source_id << " : "
                                  << parsing_exception.what();
    } catch (const std::exception& e) {
      throw Elements::Exception() << "Error while parsing the source with Id = " << source_id << " : " << e.what();
    } catch (...) {
      throw Elements::Exception() << "Error while parsing the source with Id = " << source_id;
    }

    source_vector.emplace_back(source_id, std::move(attribute_ptr_vector));
  }

  return Catalog{source_vector};
}

}  // namespace SourceCatalog
}  // end of namespace Euclid
