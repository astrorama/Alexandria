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
 * @file src/lib/CatalogFromTable.cpp
 *
 * Created on: Apr 16, 2014
 *     Author: Pierre Dubath
 */
#include <vector>
#include "SourceCatalog/CatalogFromTable.h"
#include "SourceCatalog/SourceAttributes/Photometry.h"
#include "Table/ColumnInfo.h"
#include "Table/CastVisitor.h"

using namespace std;
namespace Euclid {
namespace SourceCatalog {

class CastSourceIdVisitor: public boost::static_visitor<Source::id_type> {
    template <typename From>
    static constexpr bool is_integer() {
      return std::is_integral<From>::value && !std::is_same<From, bool>::value;
    }

public:
    const Table::CastVisitor<int64_t> int64_cast{};
    bool cast_strings;

    CastSourceIdVisitor(): cast_strings(false) {}

    Source::id_type operator() (const std::string &from) const {
      if (cast_strings) {
        return int64_cast(from);
      }
      return from;
    }

    template <typename From>
    Source::id_type operator() (const From &from, typename std::enable_if<is_integer<From>()>::type* = 0) const {
      return Source::id_type(static_cast<int64_t>(from));
    }

    template <typename From>
    Source::id_type operator() (const From &, typename std::enable_if<!is_integer<From>()>::type* = 0) const {
      throw Elements::Exception() << "Only std::string and int64_t are supported types for a source ID, got "
        << typeid(From).name() << " instead";
    }
};

CatalogFromTable::CatalogFromTable(
    std::shared_ptr<Euclid::Table::ColumnInfo> column_info_ptr,
    const string& source_id_column_name,
    std::vector<std::shared_ptr<AttributeFromRow>> attribute_from_row_ptr_vector) {

  unique_ptr<size_t> source_id_index_ptr = column_info_ptr->find(source_id_column_name);
  if (source_id_index_ptr == nullptr) {
    throw Elements::Exception() << "Column info does not have the column " << source_id_column_name;
  }
  m_source_id_index = *(source_id_index_ptr);

  m_attribute_from_row_ptr_vector = std::move(
      attribute_from_row_ptr_vector);
}

CatalogFromTable::~CatalogFromTable() {
  // @todo Auto-generated destructor stub
}

Euclid::SourceCatalog::Catalog CatalogFromTable::createCatalog(
    const Euclid::Table::Table& input_table) {

  vector<Source> source_vector;

  // Figure out the type of the first row, and then assume all following
  // must be of the same
  CastSourceIdVisitor castVisitor;
  if (input_table.size() > 0) {
    auto first = input_table[0];
    try {
      boost::apply_visitor(castVisitor.int64_cast, first[m_source_id_index]);
      castVisitor.cast_strings = true;
    }
    catch (...) {}
  }

  for (auto row : input_table) {

    auto source_id = boost::apply_visitor(castVisitor, row[m_source_id_index]);

    vector<shared_ptr<Attribute>> attribute_ptr_vector;

    for (auto& attribute_from_table_ptr : m_attribute_from_row_ptr_vector) {
      attribute_ptr_vector.push_back(
          attribute_from_table_ptr->createAttribute(row));
    }

    source_vector.push_back(Source { source_id, move(attribute_ptr_vector) });
  }

  return Catalog { source_vector };
}

} // namespace SourceCatalog
} // end of namespace Euclid
