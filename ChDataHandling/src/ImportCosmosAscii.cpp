/*
 * ImportCosmosAscii.cpp
 *
 *  Created on: Feb 14, 2013
 *      Author: Pavel Binko
 */

#include <iostream>
#include <fstream>
#include <sstream>

#include <vector>
#include <boost/foreach.hpp>
#include <boost/tokenizer.hpp>
#include <boost/lexical_cast.hpp>

#include "ChDataHandling/ImportCosmosAscii.h"
#include "ChDataHandling/CosmosAsciiMapping.h"

#include "ElementsKernel/ElementsException.h"

#include "ChDataModel/Enumerations/PhotometryTypes.h"

using namespace std;
using namespace boost;
using namespace ChDataModel;


//-----------------------------------------------------------------------------
// Constructor.

ImportCosmosAscii::ImportCosmosAscii() :
    m_names(), m_types(), m_units(), m_novals(),
    m_nofColumns(0), m_row(), m_rowNumber(0) {
  throw ElementsException(
      "ImportCosmosAscii::ImportCosmosAscii() : File name must be given.");
}


//-----------------------------------------------------------------------------
// Constructor.

ImportCosmosAscii::ImportCosmosAscii( std::string fileName ) :
    m_fileName(fileName), m_inFileHandle(fileName, ios_base::in),
    m_names(), m_types(), m_units(), m_novals(),
    m_nofColumns(0), m_row(), m_rowNumber(0) {

  // Open the input file and read all lines with the data definitions
  readCosmosDefinitions( fileName );

} // Eof ImportCosmosAscii::ImportCosmosAscii


//-----------------------------------------------------------------------------
// Constructor.

ImportCosmosAscii::ImportCosmosAscii( std::string fileName, ChDataModel::Survey & surv ) :
    m_fileName(fileName), m_inFileHandle(fileName, ios_base::in),
    m_names(), m_types(), m_units(), m_novals(),
    m_nofColumns(0), m_row(), m_rowNumber(0) {

  // Open the input file and read all lines with the data definitions
  readCosmosDefinitions( fileName );

  // Create catalog attached to the survey
  bool b = createCatalog(surv);
  if (false == b) {
    throw ElementsException("ImportCosmosAscii::ImportCosmosAscii : Create catalog failed.");
  }

} // Eof ImportCosmosAscii::ImportCosmosAscii


//-----------------------------------------------------------------------------
// Constructor.

ImportCosmosAscii::ImportCosmosAscii( std::vector<std::string> fileNames, ChDataModel::Survey & surv ) :
    m_fileName(fileNames[1]), m_inFileHandle(fileNames[1], ios_base::in), m_names(), m_types(),
    m_units(), m_novals(), m_nofColumns(0), m_row(), m_rowNumber(0) {

  ///@todo test the length of the vector

  // Open the input file and read all lines with the data definitions
  readCosmosDefinitions( fileNames[1] );

  // Create catalog attached to the survey
  bool b = createCatalog(surv);
  if (false == b) {
    throw ElementsException("ImportCosmosAscii::ImportCosmosAscii : Create catalog failed.");
  }

} // Eof ImportCosmosAscii::ImportCosmosAscii


//-----------------------------------------------------------------------------
// Destructor.

ImportCosmosAscii::~ImportCosmosAscii() {

  // Close the file.
  if (m_inFileHandle.good()) {
    m_inFileHandle.close();
  }

} // Eof ImportCosmosAscii::~ImportCosmosAscii


//-----------------------------------------------------------------------------
// Function readLineDefinition.

void ImportCosmosAscii::readCosmosDefinitions( std::string fileName ) {

  // Open the file.
  if (!(m_inFileHandle.good())) {
    throw ElementsException(
        "ImportCosmosAscii::ImportCosmosAscii : File open failed : "
            + fileName);
  }

  // Read the definitions : 1st line - column names.
  string line;

  if ( getline(m_inFileHandle, line) ) {

    // Tokenizer.
    char_separator<char> sep("| ");
    tokenizer<char_separator<char> > tokens(line, sep);

    for (tokenizer<char_separator<char> >::const_iterator ii = tokens.begin();
        ii != tokens.end(); ++ii) {
      m_names.push_back(*ii);
    }
    m_nofColumns = m_names.size();


  } else {

    if (m_inFileHandle.eof()) {
      // End of file.
      throw ElementsException(
          "ImportCosmosAscii::readLineDefinition : End of file " + m_fileName
              + " while trying to read a definition line.");
    } else {
      // Other failure.
      throw ElementsException(
          "ImportCosmosAscii::readLineDefinition : Cannot read the definition line.");
    }

  } // Eof if ( getline(...) )

  // Read the definitions : 2nd line - types.
  m_types = readLineDefinition();

  // Read the definitions : 3rd line - units.
  m_units = readLineDefinition();

  // Read the definitions : 4th line - values, which mean not defined value.
  m_novals = readLineDefinition();

} // Eof ImportCosmosAscii::readCosmosDefinitions


//-----------------------------------------------------------------------------
// Function readLineDefinition.

map<string, string> ImportCosmosAscii::readLineDefinition() {

  string line;
  map<string, string> myMap;

  if ( getline(m_inFileHandle, line) ) {

    // The definition line must start with "|".
    if (line.compare(0, 1, "|") != 0) {
      throw ElementsException(
          "ImportCosmosAscii::readLineDefinition : Definition line must start with \"|\" : "
              + line);
    }

    // Tokenizer.
    char_separator<char> sep("| ");
    tokenizer<char_separator<char> > tokens(line, sep);

    // Insert the definitions into the map.
    int i = 0;
    for (tokenizer<char_separator<char> >::const_iterator it = tokens.begin();
        it != tokens.end(); ++it) {
      myMap[m_names[i++]] = *it;
    }

  } else {

    if (m_inFileHandle.eof()) {
      // End of file.
      throw ElementsException(
          "ImportCosmosAscii::readLineDefinition : End of file " + m_fileName
              + " while trying to read a definition line.");
    } else {
      // Other failure.
      throw ElementsException(
          "ImportCosmosAscii::readLineDefinition : Cannot read the definition line.");
    }

  } // Eof if ( getline(...) )

  return myMap;

} // Eof ImportCosmosAscii::readLineDefinition

//-----------------------------------------------------------------------------
// Function nextRow.

bool ImportCosmosAscii::nextRow() {

  // One row with the data.
  string row;

  if ( getline(m_inFileHandle, row) ) {

    // The data row must not start with "|".
    if (row.compare(0, 1, "|") == 0) {
      throw ElementsException(
          "ImportCosmosAscii::readLineDefinition : Data row must not start with \"|\" : "
              + row);
    }

    // Tokenizer.
    char_separator<char> sep(" ");
    tokenizer<char_separator<char> > tokens(row, sep);

    // Insert the values into the map.
    m_row = {};
    int i = 0;
    for (tokenizer<char_separator<char> >::const_iterator it = tokens.begin();
        it != tokens.end(); ++it) {
      m_row[m_names[i++]] = *it;
    }

    // Row read and analyzed.
    m_rowNumber += 1;
    return true;

  }
  else {

    if (m_inFileHandle.eof()) {
      // End of file.
      return false;
    } else {
      // Other failure.
      throw ElementsException(
          "ImportCosmosAscii::nextRow : Input error - cannot read the next data row.");
    }

  } // Eof if ( getline(...) )

  return true;

} // Eof ImportCosmosAscii::nextRow

//-----------------------------------------------------------------------------

string& ImportCosmosAscii::getRowColumnStringValue(
    const string & columnName) {
  return m_row[columnName];
} // Eof ImportCosmosAscii::getRowColumnStringValue

//-----------------------------------------------------------------------------

double ImportCosmosAscii::getRowColumnDoubleValue(
    const string & columnName) {
  return lexical_cast<double>(m_row[columnName]);

//  Conversion string to double using stringstream (slower)
//  stringstream ss;
//  double number;
//  ss << m_row[columnName];
//  ss >> number;
//  return number;

} // Eof ImportCosmosAscii::getRowColumnDoubleValue

//-----------------------------------------------------------------------------

float ImportCosmosAscii::getRowColumnFloatValue(
    const string & columnName) {
  return lexical_cast<float>(m_row[columnName]);
} // Eof ImportCosmosAscii::getRowColumnFloatValue

//-----------------------------------------------------------------------------
long ImportCosmosAscii::getRowColumnLongValue(const string & columnName) {
  return lexical_cast<long>(m_row[columnName]);
} // Eof ImportCosmosAscii::getRowColumnLongValue

//-----------------------------------------------------------------------------

int ImportCosmosAscii::getRowColumnIntValue(const string & columnName) {
  return lexical_cast<int>(m_row[columnName]);
} // Eof ImportCosmosAscii::getRowColumnIntValue

//=============================================================================
// Function createSource.

bool ImportCosmosAscii::createSource(Catalog & cat) {

  // Read the next row.
  if (false == nextRow()) {
    return false;
  }

  // Create the source and attach it to its catalog.
  Source & src = cat.addSource(
      Source(
          getRowColumnLongValue(CosmosAsciiMapping::sourceMapping["sourceID"]),
          getRowColumnDoubleValue(CosmosAsciiMapping::sourceMapping["ra"]),
          getRowColumnDoubleValue(CosmosAsciiMapping::sourceMapping["dec"])));

  // Loop over all filter names in the enum class FilterNames
  //   and create a photometry objects.

  for (const auto& filtNam : FilterNames()) {

    // Create the photometry and attach it to its source.
    src.addPhotometry(
        Photometry(filtNam, PhotometryTypes::AB_MAGNITUDE,
            getRowColumnDoubleValue(
                CosmosAsciiMapping::photometryMapping[filtNam].first),
            getRowColumnDoubleValue(
                CosmosAsciiMapping::photometryMapping[filtNam].second)));

  } // Eof for( const auto& filtNam : FilterNames() )

  return true;

} // Eof createSource

//=============================================================================
// Function createCatalog

bool ImportCosmosAscii::createCatalog(Survey & surv) {

  // Create new empty catalog, attached to the survey.
  Catalog & catInSurv = surv.createCatalog();

  // Create all sources and attach them into the catalog.
  while (true == createSource(catInSurv)) {
  }

  return true;

} // Eof createCatalog

//=============================================================================

