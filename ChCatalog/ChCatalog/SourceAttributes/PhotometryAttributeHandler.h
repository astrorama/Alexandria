/**
 * @file PhotometryAttributeHandler.h
 *
 * @date Apr 17, 2014
 * @author Pierre Dubath
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

/**
 * @class PhotometryAttributeHandler
 * @brief Implementation of the AttributeHandler for a photometry attribute
 *
 */
class PhotometryAttributeHandler : public AttributeHandler {
public:
  /**
   * @brief Create a PhotometryAttributeHandler object
   *
   * @details Create a PhotometryAttributeHandler object, setting up the rule for building
   * PhotometryAttribute from a Table row. The filter_name_mapping provides the correspondence
   * between the FilterName and the names used for the Table columns. These names (of the flux
   * and the error columns) are searched in the columnInfo of the Table and a new mapping between the
   * FilterName and the indices of the flux and of the error columns is built. The user must
   * provide this mapping between the FilterName (which are then used throughout the processing)
   * and the column names which comes from the input photometric (ASCII or FITS) catalog.
   *
   * @param columnInfo
   *    describes the columns of the Table providing in particular the require column names
   *
   * @param filter_name_mapping
   *    supplies the mapping between the FilterName and the Table column names, both for the
   *    flux and for the error columns
   *
   * @exception
   *  An exception is thrown if the names provided in the mapping are not present in the columnInfo.
   */
  PhotometryAttributeHandler(std::shared_ptr<ChTable::ColumnInfo> column_info_ptr,
      const std::map<FilterName, std::pair<std::string, std::string>> filter_name_mapping);

  virtual ~PhotometryAttributeHandler();

  /**
   * @brief Create a photometricAttribute from a Table row
   * @details Create a photometricAttribute from a Table row using the mapping included in this object
   * @param A ChTable row
   * @return A unique pointer to a (Photometry) Attribute
   */
  std::unique_ptr<Attribute> createAttribute(const ChTable::Row& row) override;

  /**
   * @brief Getting the private m_filter_index_mapping for testing purpose only
   * @return The filter_index_mapping
   */
  const std::map<ChCatalog::FilterName, std::pair<size_t, size_t> >& getFilterIndexMapping() const {
    return m_filter_index_mapping;
  }

private:
  /**
   * Map string the correspondence between the FilterName and the names used for the Table columns
   */
  std::map<ChCatalog::FilterName, std::pair<size_t, size_t> > m_filter_index_mapping;

  std::shared_ptr<std::vector<FilterName>> m_filter_name_vector_ptr;

};

} // namespace ChCatalog 

#endif // PHOTOMETRYATTRIBUTEHANDLER_H_ 
