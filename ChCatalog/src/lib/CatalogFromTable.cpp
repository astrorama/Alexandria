/**
 * @file CatalogFactory.cpp
 *
 * Created on: Apr 16, 2014
 *     Author: Pierre Dubath
 */
#include <vector>
#include "ChCatalog/CatalogFromTable.h"
#include "ChCatalog/SourceAttributes/Photometry.h"
#include "ChTable/ColumnInfo.h"

using namespace std;
namespace ChCatalog {

CatalogFromTable::CatalogFromTable(size_t source_id_index,
    std::vector<std::unique_ptr<AttributeFromRow>> attribute_from_table_ptr_vector) :
    m_source_id_index(source_id_index) {
        m_attribute_from_table_ptr_vector = std::move(attribute_from_table_ptr_vector);
}

CatalogFromTable::~CatalogFromTable() {
  // @todo Auto-generated destructor stub
}

ChCatalog::Catalog CatalogFromTable::createCatalog(
    const ChTable::Table& input_table) {

  vector<Source> source_vector;
  vector<shared_ptr<Attribute>> attribute_ptr_vector;

  for (auto row : input_table) {

    int64_t source_id = boost::get<int64_t>(row[m_source_id_index]);

    for (auto& attribute_from_table_ptr : m_attribute_from_table_ptr_vector) {
      attribute_ptr_vector.push_back(
          attribute_from_table_ptr->createAttribute(row));
    }

    source_vector.push_back(Source { source_id, attribute_ptr_vector });
  }

  return Catalog { source_vector };
}

}
// namespace ChDataModel
