/*
 * AsciiCosmosImporter.cpp
 *
 * Created on: Jun 20, 2013
 *     Author: Pavel Binko
 */

#include <iostream>
#include <sstream>

//#include <boost/foreach.hpp>
#include <boost/tokenizer.hpp>
#include <boost/lexical_cast.hpp>

#include "ChDataHandling/AsciiCosmosImporter.h"
#include "ChDataHandling/CosmosAsciiMapping.h"

#include "ElementsKernel/ElementsException.h"

using namespace std;
using namespace boost;
using namespace boost::filesystem;
using namespace ChDataModel;

//-----------------------------------------------------------------------------
// Function importCatalog

void AsciiCosmosImporter::importCatalog(ChDataModel::Catalog & catalog,
    const std::string & path, int startRow, int numRows) {

  // Resolve the path into the vector of file names
  this->resolveFileNames(path);

  // Fill the catalog
  this->body_importCatalog(catalog, startRow, numRows);

} // Eof AsciiCosmosImporter::importCatalog

//-----------------------------------------------------------------------------
// Function importCatalog

void AsciiCosmosImporter::importCatalog(ChDataModel::Catalog & catalog,
    const std::vector<std::string> & vectorOfFiles, int startRow, int numRows) {

  // Copy the vector of files to the member data
  this->m_fileNames = vectorOfFiles;

  // Fill the catalog
  this->body_importCatalog(catalog, startRow, numRows);

} // Eof AsciiCosmosImporter::importCatalog

//-----------------------------------------------------------------------------
// Function body_importCatalog

void AsciiCosmosImporter::body_importCatalog(ChDataModel::Catalog & catalog,
    int startRow, int numRows) {

  // Read and analyze the headers
  this->readCosmosAsciiHeader();

  // Read data starting from startRow, number of rows numRows,
  //   create sources, fill them with photometry data
  //   and attach them to the catalog
  this->readCosmosAsciiData(catalog, startRow, numRows);

} // Eof AsciiCosmosImporter::body_importCatalog

//-----------------------------------------------------------------------------
// Function addSourceToCatalog

bool AsciiCosmosImporter::addSourceToCatalog(ChDataModel::Catalog & catalog,
    std::vector<std::string> & tokenizedRow) {

  // Create the source and attach it to its catalog.
  Source & src = catalog.addSource(
      Source(
          getInt64FromTokens(tokenizedRow,
              CosmosAsciiMapping::sourceMapping["sourceID"]),
          getDoubleFromTokens(tokenizedRow,
              CosmosAsciiMapping::sourceMapping["ra"]),
          getDoubleFromTokens(tokenizedRow,
              CosmosAsciiMapping::sourceMapping["dec"])));

  // Loop over all filter names in the enum class FilterNames
  //   and create a photometry objects.

  for (const auto& filtNam : FilterNames()) {

    // Try to find the column name in the header
    string colName = CosmosAsciiMapping::photometryMapping[filtNam].first;
    map<string, int>::iterator it = m_columnMap.find(colName);

    // Add photometry only if the column name exists
    if (it != m_columnMap.end()) {

      // Create the photometry and attach it to its source.
      src.addPhotometry(
          Photometry(filtNam, PhotometryTypes::AB_MAGNITUDE,
              getDoubleFromTokens(tokenizedRow, colName),
              getDoubleFromTokens(tokenizedRow,
                  CosmosAsciiMapping::photometryMapping[filtNam].second)));

    }

  } // Eof for( const auto& filtNam : FilterNames() )

  return true;

} // Eof addSourceToCatalog

//-----------------------------------------------------------------------------
// Function readCosmosAsciiData

void AsciiCosmosImporter::readCosmosAsciiData(ChDataModel::Catalog & catalog,
    int startRow, int numRows) {

  // Next row variables
  string nextRow = "";
  vector<string> tokenizedRow = { };
  bool isData = false;

  // Initialize the row counter
  int rowCounter = 0;
  // Initialize the stop row (last row which should be collected)
  int lastRow = startRow + numRows - 1;

  while (rowCounter < lastRow) {

    // Open the input file, if it is not opened yet
    if (!(m_inFileHandle.is_open())) {
      if (!(this->openNextFile())) {
        // No next file, return the number of data rows really processed
        break;
      }
    }

    // Read next row
    bool b = this->readNextRow(nextRow, tokenizedRow, isData);
    if (b == true) {
      // Next row available
      if (isData == true) {
        // Increment the counter of data rows
        ++rowCounter;
        // Data row - consider them only starting from startRow
        if (rowCounter >= startRow) {
          // Fill the source and attach it to the catalog
          this->addSourceToCatalog(catalog, tokenizedRow);
        }
      }
//      else {
//        // If not a data row, no action
//      }
    }
    else {
      // End of file - close it
      this->closeCurrentFile();
    }

  } // Eof while (rowCounter < startRow)

} // Eof AsciiCosmosImporter::readCosmosAsciiData

//-----------------------------------------------------------------------------
// Function readCosmosAsciiHeader

void AsciiCosmosImporter::readCosmosAsciiHeader() {

// Specific for Cosmos data
// For Cosmos data, loop over all files and compare the headers
  for (size_t fileCounter = 0; fileCounter < m_fileNames.size();
      ++fileCounter) {

    // Open the file
    this->openFile(m_fileNames.at(fileCounter));

    // Read the header into a local vector of header rows
    size_t rowCounter = 0;
    string readRow;
    vector<string> tokenizedRow;
    bool isData = false;
    bool b = false;

    while ((b = readNextRow(readRow, tokenizedRow, isData))) {

      // If it is a data row - stop reading the header in this file
      if (isData == true) {
        break;
      }

      // Header row
      // For the 1st file, just copy the tokenized header row into the member data
      if (fileCounter == 0) {
        m_header.push_back(tokenizedRow);
      }
      // For every next file, compare the current header with the previous headers
      else {
        // Compare the number of header rows
        if (m_header.size() == rowCounter) {
          // The headers differ in the number of rows
          stringstream errorBuffer;
          errorBuffer
              << "AsciiCosmosImporter::readCosmosAsciiHeader : The header of the file "
              << m_fileNames.at(fileCounter)
              << " has a different number of header rows than the previous files"
              << endl;
          throw ElementsException(errorBuffer.str());
        }

        // Compare the tokenized header rows
        for (size_t tok = 0; tok < tokenizedRow.size(); ++tok) {
          if (m_header.at(rowCounter).at(tok) != tokenizedRow.at(tok)) {
            stringstream errorBuffer;
            errorBuffer
                << "AsciiCosmosImporter::readCosmosAsciiHeader : The header of the file "
                << m_fileNames.at(fileCounter)
                << " has a different header than the previous files in the row : "
                << rowCounter + 1 << " and in the column : " << tok + 1 << endl;
            throw ElementsException(errorBuffer.str());
          }
        } // Eof for (size_t tok = 0; tok < tokenizedRow.size(); ++tok)

      } // Eof else of if (fileCounter == 0)

      // Increment the row counter
      ++rowCounter;

    } // Eof while ( (b = readNextRow(readRow, tokenizedRow, isData)) )

    // Check EOF and input error
    if (false == b) {

      // No action if end of file (no data in the file, only header rows)
      if (!m_inFileHandle.eof()) {
        // Other failure
        throw ElementsException(
            "AsciiCosmosImporter::readNextRow : Input error - cannot read the next data row.");
      }

    } // Eof if (false == b)

    // Close the currently opened file
    closeCurrentFile();

    // Compare the number of header rows
    if (m_header.size() != rowCounter) {
      // The headers differ in the number of rows
      stringstream errorBuffer;
      errorBuffer
          << "AsciiCosmosImporter::readCosmosAsciiHeader : The header of the file "
          << m_fileNames.at(fileCounter)
          << " has a different number of header rows than the previous files"
          << endl;
      throw ElementsException(errorBuffer.str());
    }

  } // Eof for (size_t fileCounter = 0; fileCounter < m_fileNames.size(); ++fileCounter)

  // Create a map of column names
  vector<string> v = m_header.at(0);
  for (size_t i = 0; i < v.size(); ++i) {
    m_columnMap[v[i]] = i;
  }

  // After reading all headers, reset the file index
  m_inFileIndex = 0;

} // Eof AsciiCosmosImporter::readCosmosAsciiHeader

