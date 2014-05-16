/**
 * @file CatalogFactory.cpp
 *
 * Created on: Apr 16, 2014
 *     Author: Pierre Dubath
 */
#include <vector>
#include "ChCatalog/CatalogFactory.h"
#include "ChCatalog/SourceAttributes/Photometry.h"
#include "ChTable/ColumnInfo.h"

using namespace std;
namespace ChCatalog {

CatalogFactory::CatalogFactory() {
  // @todo Auto-generated constructor stub

}

CatalogFactory::~CatalogFactory() {
  // @todo Auto-generated destructor stub
}

ChCatalog::Catalog CatalogFactory::createCatalog(
    const ChTable::Table& input_table, string source_id_name,
    std::vector<std::unique_ptr<AttributeFromTable>> attribute_handler_ptr_vector) {

  vector<Source> source_vector;
  unsigned long source_id_index = *(input_table.getColumnInfo()->find(
      source_id_name));

  vector<shared_ptr<Attribute>> attribute_ptr_vector;

  for (auto row : input_table) {

    uint64_t source_id = boost::get<long>(row[source_id_index]);

    for (auto& attribute_handler_ptr : attribute_handler_ptr_vector) {
      attribute_ptr_vector.push_back(
          attribute_handler_ptr->createAttribute(row));
    }

    source_vector.push_back(Source { source_id, attribute_ptr_vector });
  }

  return Catalog { source_vector };
}

}
// namespace ChDataModel
