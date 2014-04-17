/**
 * @file AttributeHandler.h
 *
 * @date Apr 17, 2014
 * @author dubath
 */

#ifndef ATTRIBUTEHANDLER_H_
#define ATTRIBUTEHANDLER_H_

#include "ChCatalog/Attribute.h"
#include "ChTable/Row.h"

namespace ChCatalog {

class AttributeHandler {
public:
  AttributeHandler();
  virtual ~AttributeHandler();

  virtual std::unique_ptr<Attribute> createAttribute(const ChTable::Row& row) = 0;

};

} // namespace ChCatalog 

#endif // ATTRIBUTEHANDLER_H_ 
