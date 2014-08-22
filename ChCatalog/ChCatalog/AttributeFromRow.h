/**
 * @file ChCatalog/AttributeFromRow.h
 *
 * @date Apr 17, 2014
 * @author Pierre Dubath
 */
#ifndef ATTRIBUTEHANDLER_H_
#define ATTRIBUTEHANDLER_H_

#include "ChCatalog/Attribute.h"
#include "ChTable/Row.h"

namespace Euclid {
namespace ChCatalog {

/**
 * @class AttributeFromRow
 * @brief Interface for building a source Attribute from a table Row
 *
 * @details This interface is defined to build source Attributes from table rows. The rules
 * for formatting the specific Attribute from the general Table columns must be provided
 * in the implementation constructors. They are then defined during object creation only
 * once for the complete Table. The createAttribute method can then be called for each
 * source, i.e., for each row of the Table.
 *
 */
class AttributeFromRow {

public:
  virtual ~AttributeFromRow() {
  }

  /**
   * @brief The createAttribute method for creating an Attribute from a Table row
   * @details
   * @param row A reference to a Row of a Table
   * @return A unique pointer to the newly created Attribute
   */
  virtual std::unique_ptr<Attribute> createAttribute(
      const Euclid::ChTable::Row& row) = 0;

};

} // namespace ChCatalog 
} // end of namespace Euclid

#endif // ATTRIBUTEHANDLER_H_ 
