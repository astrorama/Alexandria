/*
 * AsciiFilterImporter.cpp
 *
 * Created on: Jun 17, 2013
 *     Author: Pavel Binko
 */

#include <string>
#include <vector>
#include <iostream>

#include "ChDataHandling/AsciiFilterImporter.h"

#include "ElementsKernel/ElementsException.h"

using namespace std;
using namespace ChDataModel;

//-----------------------------------------------------------------------------
// Function importFilters

map<FilterNames, Filter> AsciiFilterImporter::importFilters(const string & path,
    const FilterTypes & filterType) {

  // Resolve the path into the vector of file names
  this->resolveFileNames(path);

  // Fill the catalog, and return it
  return this->body_importFilters(filterType);

} // Eof AsciiFilterImporter::importFilters

//-----------------------------------------------------------------------------
// Function importFilters

map<FilterNames, Filter> AsciiFilterImporter::importFilters(
    const vector<string> & vectorOfFiles, const FilterTypes & filterType) {

  // Copy the vector of files to the member data
  this->m_fileNames = vectorOfFiles;

  // Fill the catalog, and return it
  return this->body_importFilters(filterType);

} // Eof AsciiFilterImporter::importFilters

//-----------------------------------------------------------------------------
// Function body_importFilters

map<FilterNames, Filter> AsciiFilterImporter::body_importFilters(
    const FilterTypes & filterType) {

  // Map of filters
  map<FilterNames, Filter> filterMap;

  // Loop over all files
  for (auto & fileName : m_fileNames ) {

    // Fill the filter (one filter per file)
    Filter filter = this->createFilter(fileName, filterType);

    // Push back the filter into the map
    filterMap[filter.getFilterName()] = filter;

  }

  return filterMap;

} // Eof AsciiFilterImporter::body_importFilters

//-----------------------------------------------------------------------------
// Function createFilter

Filter AsciiFilterImporter::createFilter(const std::string & fileName,
    const FilterTypes & filterType) {

  // Open the file
  this->openFile(fileName);

  // Get the filter name
  FilterNames filterName = this->importFilterName(fileName);

  // Get the filter data
  VectorPair filterData = this->importFilterData();

  // Close the currently opened file
  this->closeCurrentFile();

  // Create the filter
  return Filter(filterData, filterType, filterName);

} // Eof AsciiFilterImporter::createFilter

//-----------------------------------------------------------------------------
// Function importFilterName

FilterNames AsciiFilterImporter::importFilterName(
    const std::string & fileName) {

  // Filter name
  string filterNameString = "Unknown";

  // Local variables
  string readRow;
  vector<string> tokenizedRow;
  bool isData = false;

  // The first row should contain the filter name
  bool b = readNextRow(readRow, tokenizedRow, isData);

  // Check EOF and input error
  if (false == b) {
    // No action if end of file (no data in the file, only header rows)
    if (m_inFileHandle.eof()) {
      // End of file - return the empty filter name
      return FilterNames::None;
    }
    else {
      // Other failure
      throw ElementsException(
          "AsciiFilterImporter::importFilterName : Input error - cannot read the next data row.");
    }
  }

  if (isData == false) {
    // The first token is the filter name
    filterNameString = tokenizedRow.at(0);
  }
  else {
    // Guess the filter name from the file name
    filterNameString = fileName.substr(fileName.find_last_of('/') + 1);
    filterNameString = filterNameString.substr(0,
        filterNameString.find_last_of('.'));
  }

  // Check if it is an known filter name (throws an exception, if not)
  try {
    FilterNames filterName = string2filterNames(filterNameString);
    return filterName;
  }
  catch (const ElementsException & e) {
    return FilterNames::None;
  }

} // Eof AsciiFilterImporter::importFilterName

//-----------------------------------------------------------------------------
// Function importFilterData

VectorPair AsciiFilterImporter::importFilterData() {

  // Rewind the file
  m_inFileHandle.seekg(0, ios_base::beg);

  // Simulate the filter header
  simulateFilterColumnDefinition();

  // Filter data
  vector<double> filterDataX = { };
  vector<double> filterDataY = { };

  // Local variables
  string readRow;
  vector<string> tokenizedRow;
  bool isData = false;
  bool b = false;

  while ((b = readNextRow(readRow, tokenizedRow, isData))) {

    // Consider only data rows (skip comment rows)
    if (isData == true) {
      filterDataX.push_back(getDoubleFromTokens(tokenizedRow, "WaveLength"));
      filterDataY.push_back(getDoubleFromTokens(tokenizedRow, "Efficiency"));
    }

  } // Eof while ( (b = readNextRow(readRow, tokenizedRow, isData)) )

  // Check EOF and input error
  if (false == b) {

    // No action if end of file (no data in the file, only header rows)
    if (!m_inFileHandle.eof()) {
      // Other failure
      throw ElementsException(
          "AsciiFilterImporter::importFilterData : Input error - cannot read the next data row.");
    }

  } // Eof if (false == b)

  return VectorPair(filterDataX, filterDataY);

} // Eof AsciiFilterImporter::importFilterData

//-----------------------------------------------------------------------------
// Function simulateFilterColumnDefinition

void AsciiFilterImporter::simulateFilterColumnDefinition() {

  // The first column is wave length
  m_columnMap["WaveLength"] = 0;
  // the second column is lotal filter efficiency
  m_columnMap["Efficiency"] = 1;

} // Eof AsciiFilterImporter::simulateFilterColumnDefinition

//-----------------------------------------------------------------------------
