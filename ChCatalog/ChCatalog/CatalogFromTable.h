/**
 * @file CatalogFactory.h
 *
 * Created on: Apr 15, 2014
 *     Author: Pierre Dubath
 */
#ifndef CATALOGFACTORY_H_
#define CATALOGFACTORY_H_
#include <string>
#include <utility>
#include <map>
#include <memory>


#include "ChCatalog/Catalog.h"
#include "ChCatalog/AttributeFromRow.h"
#include "ChTable/Table.h"


namespace ChCatalog {

class CatalogFromTable {
public:
  CatalogFromTable(std::shared_ptr<ChTable::ColumnInfo> column_info_ptr, const std::string source_id_column_name,
      std::vector<std::unique_ptr<AttributeFromRow>> attribute_from_row_ptr_vector);

  virtual ~CatalogFromTable();

  ChCatalog::Catalog createCatalog(const ChTable::Table& input_table);

private:
  size_t m_source_id_index;

  std::vector<std::unique_ptr<AttributeFromRow>> m_attribute_from_row_ptr_vector;

};

} // namespace ChCatalog

#endif // CATALOGFACTORY_H_ 
