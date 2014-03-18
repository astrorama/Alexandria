/**
 * @file IImport.h
 *
 *  Created on: Mar 4, 2013
 *      Author: Pavel Binko
 */

#ifndef IIMPORT_H_
#define IIMPORT_H_


#include <map>
#include <string>

#include "ChDataModel/Survey.h"
#include "ChDataModel/Catalog.h"
#include "ChDataModel/Source.h"


/**
 * @class IImport
 * @brief This pure abstract class is a base class of all different
 *        import classes, e.g. the Cosmos ASCII import class.
 */
class IImport {
public:

  /**
   * @brief Destructor
   */
  virtual ~IImport() {}

  /**
   * @brief Create source and its corresponding photometry
   *        from the input file.
   * @param cat : Catalog reference.
   * @return bool : true if the operation was successful.
   */
  virtual bool createSource( ChDataModel::Catalog & cat ) = 0;

  /**
   * @brief Create catalog, all contained sources and their corresponding photometry
   *        from the input file.
   * @param surv : Survey reference.
   * @return bool : true if the operation was successful.
   */
  virtual bool createCatalog( ChDataModel::Survey & surv ) = 0;

private:

  /**
   * @brief Read the next line of values from the input file.
   * @return bool : true if next row available.
   */
  virtual bool nextRow() = 0;

  //----------------------------------------------------------------------------
  // Conversion functions

  /**
   * @brief Get the std::string value row/column from the input file.
   * @param columnName : Column name reference (as a std::string).
   * @return The std::string value from the table.
   */
  virtual std::string & getRowColumnStringValue( const std::string & columnName ) = 0;

  /**
   * @brief Get the double value row/column from the input file.
   * @param columnName : Column name reference (as a std::string).
   * @return The double value from the table.
   */
  virtual double getRowColumnDoubleValue( const std::string & columnName ) = 0;

  /**
   * @brief Get the float value row/column from the input file.
   * @param columnName : Column name reference (as a std::string).
   * @return The float value from the table.
   */
  virtual float getRowColumnFloatValue( const std::string & columnName ) = 0;

  /**
   * @brief Get the long value row/column from the input file.
   * @param columnName : Column name reference (as a std::string).
   * @return The long value from the table.
   */
  virtual long getRowColumnLongValue( const std::string & columnName ) = 0;

  /**
   * @brief Get the integer value row/column from the input file.
   * @param columnName : Column name reference (as a std::string).
   * @return The integer value from the table.
   */
  virtual int getRowColumnIntValue( const std::string & columnName ) = 0;

}; // Eof class IImport


#endif /* IIMPORT_H_ */
