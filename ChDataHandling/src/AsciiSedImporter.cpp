/*
 * AsciiSedImporter.cpp
 *
 * Created on: Jun 17, 2013
 *     Author: Pavel Binko
 */

#include <string>
#include <vector>
#include <iostream>

#include <boost/filesystem.hpp>

#include "ChDataHandling/AsciiSedImporter.h"

#include "ElementsKernel/ElementsException.h"

using namespace std;
using namespace ChDataModel;

//-----------------------------------------------------------------------------
// Function importSeds

map<SedNames, Sed> AsciiSedImporter::importSeds(const string & path) {

  // Resolve the path into the vector of file names
  this->resolveFileNames(path);

  // Fill the catalog, and return it
  return this->body_importSeds();

} // Eof AsciiSedImporter::importSeds

//-----------------------------------------------------------------------------
// Function importSeds

map<SedNames, Sed> AsciiSedImporter::importSeds(
    const vector<string> & vectorOfFiles) {

  // Copy the vector of files to the member data
  this->m_fileNames = vectorOfFiles;

  // Fill the catalog, and return it
  return this->body_importSeds();

} // Eof AsciiSedImporter::importSeds

//-----------------------------------------------------------------------------
// Function body_importSeds

map<SedNames, Sed> AsciiSedImporter::body_importSeds() {

  // Map of SEDs
  map<SedNames, Sed> sedMap;

  // Loop over all files
  for (auto & fileName : m_fileNames ) {

    // Fill the SED (one SED per file)
    Sed sed = this->createSed(fileName);

    // Push back the SED into the map
    sedMap[sed.getSedName()] = sed;

  }

  return sedMap;

} // Eof AsciiSedImporter::body_importSeds

//-----------------------------------------------------------------------------
// Function createSed

Sed AsciiSedImporter::createSed(const std::string & fileName) {

  // Open the file
  this->openFile(fileName);

  // Get the SED name
  SedNames sedName = this->importSedName(fileName);

  // Get the SED data
  VectorPair sedData = this->importSedData();

  // Close the currently opened file
  this->closeCurrentFile();

  // Create the SED
  return Sed(sedData, sedName);

} // Eof AsciiSedImporter::createSed

//-----------------------------------------------------------------------------
// Function importSedName

SedNames AsciiSedImporter::importSedName(const std::string & fileName) {

  // SED name
  string sedNameString = "Unknown";

  // Local variables
  string readRow;
  vector<string> tokenizedRow;
  bool isData = false;

  // The first row should contain the SED name
  bool b = readNextRow(readRow, tokenizedRow, isData);

  // Check EOF and input error
  if (false == b) {
    // No action if end of file (no data in the file, only header rows)
    if (m_inFileHandle.eof()) {
      // End of file - return the empty SED name
      return SedNames::None;
    }
    else {
      // Other failure
      throw ElementsException(
          "AsciiSedImporter::importSedName : Input error - cannot read the next data row.");
    }
  }

  if (isData == false) {
    // The first token is the SED name
    sedNameString = tokenizedRow.at(0);
  }
  else {
    // Guess the SED name from the file name
    sedNameString = fileName.substr(fileName.find_last_of('/') + 1);
    sedNameString = sedNameString.substr(0, sedNameString.find_last_of('.'));
  }

  // Check if it is an known SED name (throws an exception, if not)
  try {
    SedNames sedName = string2sedNames(sedNameString);
    return sedName;
  }
  catch (const ElementsException & e) {
    return SedNames::None;
  }

} // Eof AsciiSedImporter::importSedName

//-----------------------------------------------------------------------------
// Function importSedData

VectorPair AsciiSedImporter::importSedData() {

  // Rewind the file
  m_inFileHandle.seekg(0, ios_base::beg);

  // Simulate the SED header
  simulateSedColumnDefinition();

  // SED data
  vector<double> sedDataX = { };
  vector<double> sedDataY = { };

  // Local variables
  string readRow;
  vector<string> tokenizedRow;
  bool isData = false;
  bool b = false;

  while ((b = readNextRow(readRow, tokenizedRow, isData))) {

    // Consider only data rows (skip comment rows)
    if (isData == true) {
      sedDataX.push_back(getDoubleFromTokens(tokenizedRow, "WaveLength"));
      sedDataY.push_back(getDoubleFromTokens(tokenizedRow, "Intensity"));
    }

  } // Eof while ( (b = readNextRow(readRow, tokenizedRow, isData)) )

  // Check EOF and input error
  if (false == b) {

    // No action if end of file (no data in the file, only header rows)
    if (!m_inFileHandle.eof()) {
      // Other failure
      throw ElementsException(
          "AsciiSedImporter::importSedData : Input error - cannot read the next data row.");
    }

  } // Eof if (false == b)

  return VectorPair(sedDataX, sedDataY);

} // Eof AsciiSedImporter::importSedData

//-----------------------------------------------------------------------------
// Function simulateSedColumnDefinition

void AsciiSedImporter::simulateSedColumnDefinition() {

  // The first column is wave length
  m_columnMap["WaveLength"] = 0;
  // the second column is lotal SED intensity
  m_columnMap["Intensity"] = 1;

} // Eof AsciiSedImporter::simulateSedColumnDefinition

//-----------------------------------------------------------------------------
