/**
 * @file ImportCosmosAscii.h
 *
 *  Created on: Feb 14, 2013
 *      Author: Pavel Binko
 */

#ifndef IMPORTCOSMOSASCII_H_
#define IMPORTCOSMOSASCII_H_

#include <fstream>
#include <string>
#include <vector>
#include <map>

#include "ChDataHandling/IImport.h"

#include "ChDataModel/Survey.h"
#include "ChDataModel/Catalog.h"
#include "ChDataModel/Source.h"

#include "ChDataModel/Filter.h"
#include "ChDataModel/Sed.h"
#include "ChDataModel/VectorPair.h"


/**
 * @class ImportCosmosAscii.
 * @brief Imports data in the Cosmos ASCII format.
 */
class ImportCosmosAscii : public IImport {

public:

  /**
   * @brief Constructor : Throws an exception, because no input Cosmos ASCII
   *        file name was given.
   */
  ImportCosmosAscii();

  /**
   * @brief Constructor : Opens the input Cosmos Ascii file and reads the first four lines
   *        (in the form of a comment) and interprets them as :
   *        - 1st line - Column names (read and analyzed here).
   *        - 2nd line - Types.
   *        - 3rd line - Units.
   *        - 4th line - Values, which mean not defined value.
   * @details The 2nd, 3rd and 4th line are read and analyzed using
   *          the function readLineDefinition.
   * @param fileName : File name of the input Cosmos ASCII file.
   */
  ImportCosmosAscii( std::string fileName );

  /**
   * @brief Constructor : Opens the input Cosmos Ascii file and reads the first four lines
   *        (in the form of a comment) and interprets them as :
   *        - 1st line - Column names (read and analyzed here).
   *        - 2nd line - Types.
   *        - 3rd line - Units.
   *        - 4th line - Values, which mean not defined value.
   * @details The 2nd, 3rd and 4th line are read and analyzed using
   *          the function readLineDefinition.
   * @param fileName : File name of the input Cosmos ASCII file.
   * @param surv     : Survey reference, the survey will be filled with
   *                   all catalogs and the corresponding data.
   */
  ImportCosmosAscii( std::string fileName, ChDataModel::Survey & surv );

  /**
   * @brief Constructor : Opens the input filter file and skips all comment lines
   *        at the beginning
   * @details Usually, there is 1 comment line containing the name of the filter.
   *          The consecutive lines contain pairs :
   *          - Filter
   *          - Wave length
   * @param fileNames   : File names of the input filter file.
   * @param filter : Filter reference, the filter will be filled with
   *                     the corresponding data.
   */
  //ImportCosmosAscii( std::string fileName, ChDataModel::Filter & filter );

  ImportCosmosAscii( std::vector<std::string> fileNames, ChDataModel::Survey & surv );


  /**
   * @brief Destructor : Closes the input file.
   */
  virtual ~ImportCosmosAscii();

  /**
   * @brief Reads the next row from the Cosmos ASCII input file and creates
   *        the source object and its corresponding photometry objects available.
   * @details One row contains one source and the several corresponding
   *        photometries in different bands.
   * @param cat : Catalog reference.
   * @return True if source was created.
   */
  virtual bool createSource( ChDataModel::Catalog & cat );

  /**
   * @brief Reads all rows from the Cosmos ASCII input file (from one catalog)
   *        and creates the catalog object, all contained source objects and
   *        their corresponding photometry objects available.
   * @details One catalog contains several rows, it means several sources.
   * @param surv : Survey reference.
   * @return True if catalog was created.
   */
  virtual bool createCatalog( ChDataModel::Survey & surv );

private:

  /**
   * @brief Reads all rows from an ASCII input file (from an filter or a Sed)
   *        and fills the object with X axis and Y axis.
   * @param vectPair : VectorPair reference.
   * @return True if VectorPair was filled.
   */
//  virtual bool fillVectorPair( ChDataModel::VectorPair & vectPair );


private:

  /**
   * @brief Function readCosmosDefinitions : used for reading all data definitions
   *        contained in the input data file.
   * @param fileName
   *   Input file name
   */
  void readCosmosDefinitions( std::string fileName );

  /**
   * @brief Function readLineDefinition : Is Used for reading
   *        2nd, 3rd and 4th line of the file description.
   * @details The 1st line is read and analyzed in the constructor.
   * @return A map containing all tokens of the file description.
   */
  std::map< std::string, std::string > readLineDefinition();

  /**
   * @brief Function nextRow : Reads and analyzes the next row from the input file
   *        The result is in the map "m_row".
   * @return True if the next line exists, false if end of file.
   */
  bool nextRow();

  /**
   * @brief Get the std::string value row/column from the input file.
   * @param columnName : Column name reference (as a std::string).
   * @return The std::string value from the table.
   */
  virtual std::string & getRowColumnStringValue( const std::string & columnName );

  /**
   * @brief Get the double value row/column from the input file.
   * @param columnName : Column name reference (as a std::string).
   * @return The double value from the table.
   */
  virtual double getRowColumnDoubleValue( const std::string & columnName );

  /**
   * @brief Get the float value row/column from the input file.
   * @param columnName : Column name reference (as a std::string).
   * @return The float value from the table.
   */
  virtual float getRowColumnFloatValue( const std::string & columnName );

  /**
   * @brief Get the long value row/column from the input file.
   * @param columnName : Column name reference (as a std::string).
   * @return The long value from the table.
   */
  virtual long getRowColumnLongValue( const std::string & columnName );

  /**
   * @brief Get the integer value row/column from the input file.
   * @param columnName : Column name reference (as a std::string).
   * @return The integer value from the table.
   */
  virtual int getRowColumnIntValue( const std::string & columnName );

private:

  /// Name of the Cosmos ASCI file name.
  std::string m_fileName;
  /// File handle of the input Cosmos ASCI file.
  std::ifstream m_inFileHandle;

  /// Data definitions - vector of column names.
  std::vector<std::string> m_names;

  /// Data definitions - map of the data types from the 2nd comment line (e.g. int, double).
  std::map<std::string, std::string> m_types;
  /// Data definitions - map of the units (e.g. number, mag, degrees, pixels).
  std::map<std::string, std::string> m_units;
  /// Data definitions - map of the "no values" (e.g. null, 0, -99).
  std::map<std::string, std::string> m_novals;

  /// Number of columns in the Cosmos ASCII file.
  long m_nofColumns;

  /// Map of all values (in the format string) of the current row.
  std::map<std::string, std::string> m_row;

  /// The current row number.
  long m_rowNumber;

}; /* class ImportCosmosAscii */


#endif /* IMPORTCOSMOSASCII_H_ */
