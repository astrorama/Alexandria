/**
 * @file SourceCatalog/SourceAttributes/SpectroscopicRedshiftAttributeFromRow.h
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

#include "ElementsKernel/Logging.h"
#include "SourceCatalog/AttributeFromRow.h"
#include "SourceCatalog/Catalog.h"
#include "Table/Table.h"
#include "Table/CastVisitor.h"

using namespace Euclid::SourceCatalog;
using namespace std;

namespace Euclid {
namespace SourceCatalog {

static Elements::Logging logger = Elements::Logging::getLogger("SpectroscopicRedshiftAttributeFromRow");

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
   * @param column_info_ptr
   *    describes the columns of the Table, providing in particular the required column names
   *
   * @param specz_value_column_name
   *    give the name of the spectroscopic redshift value table column
   *
   * @param specz_error_column_name
   *    give the name of the spectroscopic redshift error table column,
   *    if this name is missing or the column not found, the error is defaulted to 0
   *
   * @exception
   *  An exception is thrown if the names provided in the mapping are not present in the columnInfo.
   */
  SpectroscopicRedshiftAttributeFromRow(std::shared_ptr<Euclid::Table::ColumnInfo> column_info_ptr,
                                        const std::string&                         specz_value_column_name,
                                        const std::string&                         specz_error_column_name) {

    unique_ptr<size_t> specz_value_column_index_ptr = column_info_ptr->find(specz_value_column_name);
    if (specz_value_column_index_ptr == nullptr) {
      throw Elements::Exception() << "Column info does not have the spectroscopic redshift value column!";
    }

    unique_ptr<size_t> specz_error_column_index_ptr = column_info_ptr->find(specz_error_column_name);
    if (specz_error_column_index_ptr == nullptr) {
      throw Elements::Exception() << "Column info does not have the spectroscopic redshift error column!";
    }

    m_has_error_column=true;
    m_error_column_index = *(specz_error_column_index_ptr);
    m_value_column_index = *(specz_value_column_index_ptr);

 }

  /**
   * @brief Create a SpectroscopicRedshiftAttributeFromRow object
   *
   * @details Create a SpectroscopicRedshiftAttributeFromRow object, setting up the rule for building
   * SpectroscopicRedshiftAttribute from table rows. The names provides the names used for
   * the Table columns. This constructor is used when there is no Z error column
   * in the catalog
   *
   * @param column_info_ptr
   *    describes the columns of the Table, providing in particular the required column names
   *
   * @param specz_value_column_name
   *    give the name of the spectroscopic redshift value table column
   *
   * @exception
   *  An exception is thrown if the names provided in the mapping are not present in the columnInfo.
   */
 SpectroscopicRedshiftAttributeFromRow(std::shared_ptr<Euclid::Table::ColumnInfo> column_info_ptr,
                                       const std::string&                         specz_value_column_name) {

    unique_ptr<size_t> specz_value_column_index_ptr = column_info_ptr->find(specz_value_column_name);
    if (specz_value_column_index_ptr == nullptr) {
      throw Elements::Exception() << "Column info does not have the spectroscopic redshift value column!";
    }

    m_has_error_column=false;
    m_error_column_index = 0;
    m_value_column_index = *(specz_value_column_index_ptr);

    // Log a warning as row is set to zero
    logger.warn() << "specz error values are set to zero by default! ";
 }

  virtual ~SpectroscopicRedshiftAttributeFromRow() {

  }

  /**
   * @brief Create a photometricAttribute from a Table row
   * @details Create a photometricAttribute from a Table row using the mapping included in this object
   * @param row A Table row
   * @return A unique pointer to a (SpectroscopicRedshift) Attribute
   */
  std::unique_ptr<Attribute> createAttribute(const Euclid::Table::Row& row) override {
    double z = boost::apply_visitor(Table::CastVisitor<double>{}, row[m_value_column_index]);
    double e = 0.;
    if (m_has_error_column) {
      e = boost::apply_visitor(Table::CastVisitor<double>{}, row[m_error_column_index]);
    }
    return std::unique_ptr<Attribute> {new SpectroscopicRedshift {z, e}};
  }

private:
  /**
   * Indices of the spectroscopic redshift value and error columns in the table
   */
  size_t m_value_column_index;
  bool   m_has_error_column;
  size_t m_error_column_index;

};


} // namespace SourceCatalog
} // end of namespace Euclid

#endif // SPECTROSCOPICATTRIBUTEFROMROW_H_
