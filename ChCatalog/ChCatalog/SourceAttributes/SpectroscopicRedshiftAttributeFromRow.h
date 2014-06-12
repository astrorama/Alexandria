/**
 * @file SpectroscopicRedshiftAttributeHandler.h
 *
 * @date Apr 17, 2014
 * @author Pierre Dubath
 */

#ifndef SPECTROSCOPICATTRIBUTEFROMROW_H_
#define SPECTROSCOPICATTRIBUTEFROMROW_H_
#include <map>
#include <utility>
#include <string>
#include <memory>

#include "ChCatalog/AttributeFromRow.h"
#include "ChCatalog/Catalog.h"
#include "ChTable/Table.h"

using namespace ChCatalog;
using namespace std;

namespace ChCatalog {

/**
 * @class SpectroscopicRedshiftAttributeFromRow
 *
 * @brief Implementation of the AttributeFromRow for a SpectroscopicRedshift attribute.
 * This class implements the createAttribute method that must be used to
 * create SpectroscopicRedshift objects.
 *
 */
class SpectroscopicRedshiftAttributeFromRow: public AttributeFromRow {
public:
  /**
   * @brief Create a SpectroscopicRedshiftAttributeFromRow object
   *
   * @details Create a SpectroscopicRedshiftAttributeFromRow object, setting up the rule for building
   * SpectroscopicRedshiftAttribute from table rows. The names provides the names used for
   * the Table columns.
   *
   * @param column_info
   *    describes the columns of the Table, providing in particular the required column names
   *
   * @param specz_value_column_name
   *    give the name of the spectroscopic redshift value table column
   *
   * @param specz_value_column_name
   *    give the name of the spectroscopic redshift error table column
   *
   * @exception
   *  An exception is thrown if the names provided in the mapping are not present in the columnInfo.
   */
  SpectroscopicRedshiftAttributeFromRow(
      std::shared_ptr<ChTable::ColumnInfo> column_info_ptr,
      const std::string specz_value_column_name,
      const std::string specz_error_column_name) {

    unique_ptr<size_t> specz_value_column_index_ptr = column_info_ptr->find(
        specz_value_column_name);
    if (specz_value_column_index_ptr == nullptr
        || type_index(typeid(double))
            != column_info_ptr->getType(*(specz_value_column_index_ptr))) {
      throw ElementsException()
          << "Column info does not have the expected spectroscopic redshift value column of type: double";
    }
    unique_ptr<size_t> specz_error_column_index_ptr = column_info_ptr->find(
        specz_error_column_name);
    if (specz_error_column_index_ptr == nullptr
        || type_index(typeid(double))
            != column_info_ptr->getType(*(specz_error_column_index_ptr))) {
      throw ElementsException()
          << "Column info does not have the expected spectroscopic redshift error column of type: double";
    }
    m_value_column_index = *(specz_value_column_index_ptr);
    m_error_column_index = *(specz_error_column_index_ptr);
  }

  virtual ~SpectroscopicRedshiftAttributeFromRow() {

  }

  /**
   * @brief Create a photometricAttribute from a Table row
   * @details Create a photometricAttribute from a Table row using the mapping included in this object
   * @param A ChTable row
   * @return A unique pointer to a (SpectroscopicRedshift) Attribute
   */
  std::unique_ptr<Attribute> createAttribute(const ChTable::Row& row) override {
    return std::unique_ptr<Attribute> { new SpectroscopicRedshift {
      boost::get<double>(row[m_value_column_index]),
      boost::get<double>(row[m_error_column_index]) } };
  }

private:
  /**
   * Indices of the spectroscopic redshift value and error columns in the table
   */
  size_t m_value_column_index;
  size_t m_error_column_index;

};

} // namespace ChCatalog 

#endif // SPECTROSCOPICATTRIBUTEFROMROW_H_
