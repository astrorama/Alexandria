/**
 * @file SourceCatalog/CatalogFromTable.h
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

#include "ElementsKernel/Export.h"

#include "SourceCatalog/Catalog.h"
#include "SourceCatalog/AttributeFromRow.h"
#include "Table/Table.h"


namespace Euclid {
namespace SourceCatalog {

class ELEMENTS_API CatalogFromTable {
public:
  CatalogFromTable(std::shared_ptr<Euclid::Table::ColumnInfo> column_info_ptr,
                   const std::string& source_id_column_name,
                   std::vector<std::shared_ptr<AttributeFromRow>> attribute_from_row_ptr_vector);

  virtual ~CatalogFromTable();

  Euclid::SourceCatalog::Catalog createCatalog(const Euclid::Table::Table& input_table);

private:
  size_t m_source_id_index;

  std::vector<std::shared_ptr<AttributeFromRow>> m_attribute_from_row_ptr_vector;

};

} // namespace SourceCatalog
} // end of namespace Euclid

#endif // CATALOGFACTORY_H_
