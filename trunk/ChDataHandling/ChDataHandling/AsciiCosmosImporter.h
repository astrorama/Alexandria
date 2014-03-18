/**
 * @file AsciiCosmosImporter.h
 *
 * Created on: Jun 20, 2013
 *     Author: Pavel Binko
 */

#ifndef ASCIICOSMOSIMPORTER_H_
#define ASCIICOSMOSIMPORTER_H_


#include <string>
#include <vector>
#include <map>

#include "ChDataHandling/AsciiImporter.h"

#include "ChDataModel/VectorPair.h"
#include "ChDataModel/Filter.h"
#include "ChDataModel/Enumerations/FilterNames.h"
#include "ChDataModel/Enumerations/FilterTypes.h"

/**
 * @class AsciiCosmosImporter
 * @brief
 *   Imports COSMOS data in the ASCII format
 */
class AsciiCosmosImporter: public AsciiImporter {

public:

  /**
   * @brief Destructor
   */
  virtual ~AsciiCosmosImporter() {
  }

  /**
   * @brief importCatalog
   *   Imports data into a catalog together with its sources and
   *   their corresponding photometry
   * @details
   *   It is Cosmos data specific
   * @param catalog
   *   Reference to the Catalog object to be filled with the data
   * @param path
   *   Either a path to a single file or to a directory. In the latter case,
   *   all files from that directory will be considered for import.
   * @param startRow
   *   The first data row to be imported (startRow-1 rows will be skipped)
   * @param numRows
   *   Number of data rows which will be imported
   */
  void importCatalog(ChDataModel::Catalog & catalog, const std::string & path,
      int startRow, int numRows);

  /**
   * @brief importCatalog
   *   Imports data into a catalog together with its sources and
   *   their corresponding photometry
   * @details
   *   It is Cosmos data specific.
   * @param catalog
   *   Reference to the Catalog object to be filled with the data
   * @param vectorOfFiles
   *   Vector of file names, which will be considered for import
   * @param startRow
   *   The first data row to be imported (startRow-1 rows will be skipped)
   * @param numRows
   *   Number of data rows which will be imported
   */
  void importCatalog(ChDataModel::Catalog & catalog,
      const std::vector<std::string> & vectorOfFiles, int startRow,
      int numRows);

  /**
   * @brief addSourceToCatalog
   *   Reads the next row from the Cosmos ASCII input file and creates
   *   the source object and its corresponding photometry objects available.
   * @details
   *   One row contains one source and the several corresponding photometries
   *   in different bands.
   * @param catalog
   *   Reference to the Catalog object to be filled with the data
   * @param tokenizedRow
   *   Tokenized row
   * @return
   *   True if source was created.
   */
  bool addSourceToCatalog(ChDataModel::Catalog & catalog,
      std::vector<std::string> & tokenizedRow);

  /**
   * @brief readCosmosAsciiHeader
   *   Opens all files in the input vector of file names, reads the headers,
   *   compares them, and accepts them, if all of them are identical
   *   (input data header consistency check).
   * @details
   *   It is Cosmos data specific.
   *   It requires the vector of file names filled properly (by resolveFileNames)
   *   and creates the headers if consistent.
   * @throws
   *   ElementsException, if the headers are not consistent.
   */
  void readCosmosAsciiHeader();

  /**
   * @brief readCosmosAsciiData
   *   Reads Cosmos ASCII data starting from startRow, number of rows numRows
   *   into a container. Consecutive opening and closing files is automated.
   * @details
   *   The data rows from 0 to startRow-1 will be skipped
   * @param catalog
   *   Reference to the Catalog object to be filled with the data
   * @param startRow
   *   The number of the row, which should be read as the first valid data row
   * @param numRows
   *   The number of data rows to be processed
   */
  void readCosmosAsciiData(ChDataModel::Catalog & catalog, int startRow, int numRows);

private:

  /**
   * @brief body_importCatalog
   *   Function, which performs the functionality for both importCatalog
   *   functions (after path resolution).
   * @param catalog
   *   Reference to the Catalog object to be filled with the data
   * @param startRow
   *   The first data row to be imported (startRow-1 rows will be skipped)
   * @param numRows
   *   Number of data rows which will be imported
   */
  void body_importCatalog(ChDataModel::Catalog & catalog, int startRow,
      int numRows);

};

#endif /* ASCIICOSMOSIMPORTER_H_ */
