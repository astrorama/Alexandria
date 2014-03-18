/**
 * @file AsciiImporter.h
 *
 *  Created on: May 29, 2013
 *      Author: Pavel Binko
 */

#ifndef ASCIIIMPORTER_H_
#define ASCIIIMPORTER_H_

#include <fstream>
#include <string>
#include <vector>
#include <map>

#include <boost/filesystem.hpp>

#include "ChDataHandling/IImport.h"

#include "ChDataModel/Catalog.h"
#include "ChDataModel/Source.h"

#include "ChDataModel/Filter.h"
#include "ChDataModel/Sed.h"
#include "ChDataModel/VectorPair.h"

/**
 * @class ImportCosmosAscii.
 * @brief Imports data in the Cosmos ASCII format.
 */
class AsciiImporter {

public:

  /**
   * @brief Constructor
   */
   AsciiImporter() = default ;

  /**
   * @brief Destructor
   *   Closes the currently opened input file
   */
  virtual ~AsciiImporter();

  /**
   * @brief resolveFileNames
   *   Takes a path (directory or file name) and returns a vector of fileNames
   * @param path
   *   Path to the data. It can be either a file name or a directory name.
   * @throws
   *   ElementsException if path does not exist
   */
  void resolveFileNames(const std::string & path);

  /**
   * @brief readNextRow
   * @details
   *   It skips empty lines and lines containing inly white spaces
   * @param nextRow
   *   String containing the full row read
   * @param tokenizedRow
   *   Individual tokens, extracted from the nextRow
   * @param isData
   *   True if the nextRow is a data row
   *   False if the nextRow is a header row
   * @return bool
   *   True if the next row was read properly
   *   False if end of file
   */
  bool readNextRow(std::string & nextRow,
      std::vector<std::string> & tokenizedRow, bool & isData);

  /**
   * @brief analyzerRow
   * @param headerRow
   *   String containing one header row
   * @param delim
   *   String containing a single character to recognize the header
   * @return
   *   The tokenized header row
   */
  std::vector<std::string> tokenizeRow(std::string & headerRow,
      const std::string & delim);

  /**
   * @brief openFile
   *   Opens the specified file
   * @details
   *   Throws an exception, if the open failed
   * @param fileName
   *   The name of the file to be opened
   */
  void openFile(const std::string & fileName);

  /**
   * @brief openNextFile
   *   Opens the next file from the vector of file names
   * @details
   *   Increments the file index and calls openFile to open that file
   * @return
   *   The value true means, that the next file exists and has been opened.
   *   The value false means, that there is no next file.
   */
  bool openNextFile();

  /**
   * @brief closeCurrentFile
   *   Closes the current file from the vector of file names
   */
  void closeCurrentFile();

  /**
   * @brief getInt64FromTokens
   * @param columnName
   */
  int64_t getInt64FromTokens(std::vector<std::string> & tokenizedRow,
      const std::string & columnName);

  /**
   * @brief getInt32FromTokens
   * @param columnName
   */
  int32_t getInt32FromTokens(std::vector<std::string> & tokenizedRow,
      const std::string & columnName);

  /**
   * @brief getDoubleFromTokens
   * @param columnName
   */
  double getDoubleFromTokens(std::vector<std::string> & tokenizedRow,
      const std::string & columnName);

  /**
   * @brief removeFileExtension
   * @param fileName
   * @return
   *   The file name without the extension
   */
  std::string removeFileExtension(std::string const & fileName);

public:

  const std::map<std::string, int>& getColumnMap() const {
    return m_columnMap;
  }

  void setColumnMap(const std::map<std::string, int>& columnMap) {
    m_columnMap = columnMap;
  }

  const std::vector<std::string>& getFileNames() const {
    return m_fileNames;
  }

  void setFileNames(const std::vector<std::string>& fileNames) {
    m_fileNames = fileNames;
  }

  const std::vector<std::vector<std::string> >& getHeader() const {
    return m_header;
  }

  void setHeader(const std::vector<std::vector<std::string> >& header) {
    m_header = header;
  }

  const std::ifstream & getInFileHandle() const {
    return m_inFileHandle;
  }

protected:

  /**
   * Vector of file names is constructed from the input path
   */
  std::vector<std::string> m_fileNames { };

  /**
   * Map of column names
   */
  std::map<std::string, int> m_columnMap { };

  /**
   * File handle of the file currently opened
   */
  std::ifstream m_inFileHandle { };

  /**
   * Accumulated header rows.
   * The "outer" vector corresponds to the rows
   * The "inner"vector corresponds to the columns
   */
  std::vector<std::vector<std::string>> m_header { };

  /**
   * File index (in the vector m_fileNames).
   * If the file is opened - it points to the currently opened file.
   * If the file is closed - it points to the file to be opened as next.
   */
  size_t m_inFileIndex { 0 };

};

#endif /* ASCIIIMPORTER_H_ */
