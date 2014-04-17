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
#include "ChCatalog/AttributeHandler.h"
#include "ChTable/Table.h"


namespace ChCatalog {

class CatalogFactory {
public:
  CatalogFactory();
  virtual ~CatalogFactory();

  ChCatalog::Catalog createCatalog(const ChTable::Table& input_table, std::string source_id_name,
        std::vector<std::unique_ptr<AttributeHandler>> attribute_handler_vector_ptr);

};

} // namespace ChCatalog

#endif // CATALOGFACTORY_H_ 
