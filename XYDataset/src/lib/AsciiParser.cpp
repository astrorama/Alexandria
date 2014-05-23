/**
 * @file AsciiParser.cpp
 *
 * @date May 13, 2014
 * @author Nicolas Morisset
 */

#include <boost/regex.hpp>
#include <fstream>
#include <iostream>

#include "ElementsKernel/ElementsException.h"
#include "ChTable/AsciiReader.h"
#include "XYDataset/AsciiParser.h"
#include "StringFunctions.h"

using boost::regex;
using boost::regex_match;

namespace XYDataset {

//
// Get dataset name from ASCII file
//
std::string AsciiParser::getName(const std::string& file) {

  std::ifstream sfile(file);
  // Check file exists
  if (!sfile) {
    throw ElementsException() << "File does not exist : " << file;
  }

  std::string line{};
  std::string dataset_name{};
  // Check dataset name is in the file
  // Convention: read until found first non empty line, removing empty lines.
  while (line.empty() && sfile.good()) {
    std::getline( sfile, line );
  }

  boost::regex expression(m_regex_name);
  boost::smatch s_match;
  if (boost::regex_match(line, s_match, expression)) {
     dataset_name = s_match[1].str();
  }
  else {
     // Dataset name is the filename without extension and path
     std::string str {};
     str          = removeAllBeforeLastSlash(file);
     dataset_name = removeExtension(str);
 }

  return (dataset_name);
}

//
// Get dataset from ASCII file
//
std::unique_ptr<XYDataset> AsciiParser::getDataset(const std::string& file) {

  std::unique_ptr<XYDataset> dataset_ptr {};
  std::ifstream sfile(file);
  // Check file exists
  if (sfile) {
    // Read file into a Table object
    ChTable::AsciiReader ascii_reader {{typeid(double), typeid(double)}};
    auto table = ascii_reader.read(sfile);
    // Put the Table data into vector pair
    std::vector<std::pair<double, double>> vector_pair;
    for (auto row : table) {
        vector_pair.push_back(std::make_pair( boost::get<double>(row[0]), boost::get<double>(row[1]) ));
    }
    dataset_ptr = std::unique_ptr<XYDataset> { new XYDataset(vector_pair) };
  }

 return(dataset_ptr);
}

} // XYDataset namespace
