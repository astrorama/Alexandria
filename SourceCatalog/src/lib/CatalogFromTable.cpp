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


  for (auto row : input_table) {

    int64_t source_id = boost::apply_visitor(Table::CastVisitor<int64_t>{}, row[m_source_id_index]);

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
