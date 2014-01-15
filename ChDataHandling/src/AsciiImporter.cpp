/*
 * AsciiImporter.cpp
 *
 * Created on: May 30, 2013
 *     Author: Pavel Binko
 */

#include <iostream>
#include <sstream>

//#include <boost/foreach.hpp>
#include <boost/tokenizer.hpp>
#include <boost/lexical_cast.hpp>

#include "ChDataHandling/AsciiImporter.h"
#include "ChDataHandling/CosmosAsciiMapping.h"

#include "ElementsKernel/ElementsException.h"

using namespace std;
using namespace boost;
using namespace boost::filesystem;
using namespace ChDataModel;

//-----------------------------------------------------------------------------
// Destructor

AsciiImporter::~AsciiImporter() {
  // Close the currently opened input file
  closeCurrentFile();
}

//-----------------------------------------------------------------------------
// Function resolveFileNames

void AsciiImporter::resolveFileNames(const std::string & fileOrDir) {

  if (!(exists(fileOrDir))) {
    // fileOrDir does not exist, throw an exception
    stringstream errorBuffer;
    errorBuffer << "AsciiImporter::resolveFileNames : The path " << fileOrDir
        << " does not exist" << endl;
    throw ElementsException(errorBuffer.str());
  }

// fileOrDir exists
  if (is_regular_file(fileOrDir)) {
    // It is a regular file, push it into the vector of file names as single element
    m_fileNames.push_back(fileOrDir);
  } else if (is_directory(fileOrDir)) {
    // It is a directory, push its contents into the vector of file names
    // Store the paths, so we can sort them later
    vector<path> v;
    copy(directory_iterator(fileOrDir), directory_iterator(), back_inserter(v));
    // Sort, since directory iteration is not ordered on some file systems
    sort(v.begin(), v.end());
    // Fill the vector of file names
    for (auto it(v.begin()), it_end(v.end()); it != it_end; ++it) {
      // Consider only regular files in the vector of file names
      // The input data should be clean, no sub-directories, no links. etc.
      string item_str(it->string());
      if (is_regular_file(item_str)) {
        m_fileNames.push_back(item_str);
      }
//      else if (is_directory(it->string())) {
//        // It is a directory, no action
//      }
//      else {
//        // Neither regular file, nor directory, no action
//      }
    }
  } else {
    // Neither regular file, nor directory, throw an exception
    stringstream errorBuffer;
    errorBuffer << "AsciiImporter::resolveFileNames : The path " << fileOrDir
        << " is neither regular file, nor directory" << endl;
    throw ElementsException(errorBuffer.str());
  }

} // Eof void AsciiImporter::resolveFileNames

//-----------------------------------------------------------------------------
// Function readNextRow

bool AsciiImporter::readNextRow(std::string & nextRow,
    std::vector<std::string> & tokenizedRow, bool & isData) {

  // Flag, if the next row is OK
  bool b = false;

  // Read the first non white space row
  while (std::getline(m_inFileHandle, nextRow)) {

    // Tokenize the row (on one of the characters : '#', '|', space and tab)
    tokenizedRow = this->tokenizeRow(nextRow, "#| \t");

    // Stop reading, if there are tokens
    if (tokenizedRow.size() != 0) {
      // As b = std::getline(...) is not possible, set b = true here by hand
      b = true;
      break;
    }

  } // Eof while ((b = getline(m_inFileHandle, nextRow)))

  // Check EOF and input error
  if (false == b) {

    // Reset the next row variable
    nextRow = "";

    if (m_inFileHandle.eof()) {
      // Return false only if end of file
      return false;
    } else {
      // Other failure
      throw ElementsException(
          "AsciiImporter::readNextRow : Input error - cannot read the next data row.");
    }

  } // Eof if (false == b)

  // Check if it is data row (isData=true) or header row (isData=false)
  isData = true;
  try {
    boost::lexical_cast<double>(tokenizedRow.at(0));
  } catch (boost::bad_lexical_cast& e) {
    // The first token is not a number
    isData = false;
  }

  return true;

} // Eof AsciiImporter::readNextRow

//-----------------------------------------------------------------------------
// Function tokenizeRow

std::vector<std::string> AsciiImporter::tokenizeRow(std::string & headerRow,
    const std::string & delim) {

  // Local vector of tokens
  vector<string> vecTokens;

  // Tokenizer, separate on the delimiter and on spaces and on tabs
  char_separator<char> sep((delim).c_str());
  tokenizer<char_separator<char> > tokens(headerRow, sep);

  // Insert the definitions into the vector of tokens
  //  for (tokenizer<char_separator<char> >::const_iterator it = ...
  for (auto it = tokens.begin(); it != tokens.end(); ++it) {
    vecTokens.push_back(*it);
  }

  return vecTokens;

} // Eof AsciiImporter::tokenizeRow

//-----------------------------------------------------------------------------
// Function openFile

void AsciiImporter::openFile(const std::string & fileName) {

  // Open the file
  m_inFileHandle.open(fileName.c_str(), std::ios::in);
  if (!m_inFileHandle) {
    // Cannot open the file
    stringstream errorBuffer;
    errorBuffer << "AsciiImporter::openFile : The file " << fileName
        << " cannot be opened" << endl;
    throw ElementsException(errorBuffer.str());
  }

} // Eof AsciiImporter::openFile

//-----------------------------------------------------------------------------
// Function openNextFile

bool AsciiImporter::openNextFile() {

  // Check if current file is still open
  if (m_inFileHandle.is_open()) {
    m_inFileHandle.close();
    stringstream errorBuffer;
    errorBuffer << "AsciiImporter::openNextFile : The file "
        << m_fileNames.at(m_inFileIndex)
        << "is open while trying to open the next file" << endl;
    throw ElementsException(errorBuffer.str());
  }

  // Check the file index
  // No file is opened - m_inFileIndex points to the file to be opened as next
  if (m_inFileIndex == m_fileNames.size()) {
    // There is no next file
    return false;
  }

  // Open the file
  this->openFile(m_fileNames.at(m_inFileIndex));
  // After that, m_inFileIndex points to the file currently opened

  return true;

} // Eof AsciiImporter::openNextFile

//-----------------------------------------------------------------------------
// Function closeCurrentFile

void AsciiImporter::closeCurrentFile() {

  // Close the currently opened file
  if (m_inFileHandle.is_open()) {

    m_inFileHandle.close();

    // Increment the file index - points to the file to be opened as next
    ++m_inFileIndex;

  }

} // Eof AsciiImporter::closeCurrentFile

//-----------------------------------------------------------------------------

int64_t AsciiImporter::getInt64FromTokens(
    std::vector<std::string> & tokenizedRow, const std::string & columnName) {

  return lexical_cast<int64_t>(tokenizedRow.at(m_columnMap[columnName]));

} // Eof AsciiImporter::getLongFromTokens

//-----------------------------------------------------------------------------

int32_t AsciiImporter::getInt32FromTokens(
    std::vector<std::string> & tokenizedRow, const std::string & columnName) {

  return lexical_cast<int32_t>(tokenizedRow.at(m_columnMap[columnName]));

} // Eof AsciiImporter::getLongFromTokens

//-----------------------------------------------------------------------------

double AsciiImporter::getDoubleFromTokens(
    std::vector<std::string> & tokenizedRow, const std::string & columnName) {
  return lexical_cast<double>(tokenizedRow.at(m_columnMap[columnName]));

//  Conversion string to double using stringstream (slower)
//  stringstream ss;
//  double number;
//  ss << m_row[columnName];
//  ss >> number;
//  return number;

} // Eof AsciiImporter::getDoubleFromTokens

//-----------------------------------------------------------------------------

string AsciiImporter::removeFileExtension(string const & fileName) {

//  string::const_reverse_iterator pivot = find(fileName.rbegin(),
//      fileName.rend(), '.');
//  return
//      pivot == fileName.rend() ?
//          fileName : string(fileName.begin(), pivot.base() - 1);

//  std::string getFileName(const std::string& fileName)
//      {
//  size_t iLastSeparator = 0;
//  return fileName.substr((iLastSeparator = fileName.find_last_of("/")) != std::string::npos ? iLastSeparator + 1 : 0, fileName.size() - fileName.find_last_of("."));

  size_t iLastSeparator = fileName.find_last_of('/');
  return fileName.substr(
      iLastSeparator != std::string::npos ? iLastSeparator + 1 : 0,
      fileName.size() - fileName.find_last_of('.'));
//      }

} // Eof AsciiImporter::removeExtension

//-----------------------------------------------------------------------------
