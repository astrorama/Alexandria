/**
 * @file PhotometryAttributeHandler.h
 *
 * @date Apr 17, 2014
 * @author dubath
 */

#ifndef PHOTOMETRYATTRIBUTEHANDLER_H_
#define PHOTOMETRYATTRIBUTEHANDLER_H_
#include <map>
#include <utility>
#include <string>
#include <memory>


#include "ChCatalog/AttributeHandler.h"
#include "ChCatalog/Catalog.h"
#include "ChCatalog/FilterName.h"
#include "ChTable/Table.h"

namespace ChCatalog {

class PhotometryAttributeHandler: public AttributeHandler {
public:
  PhotometryAttributeHandler(const ChTable::ColumnInfo column_info,
      const std::map<FilterName, std::pair<std::string, std::string>> filter_name_mapping);

  virtual ~PhotometryAttributeHandler();

  std::unique_ptr<Attribute> createAttribute(const ChTable::Row& row);

private:
  std::map<FilterName, std::pair<size_t, size_t>> m_filter_index_mapping;

};

} // namespace ChCatalog 

#endif // PHOTOMETRYATTRIBUTEHANDLER_H_ 
