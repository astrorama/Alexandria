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

using boost::regex;
using boost::regex_match;

namespace XYDataset {

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
  do {
    std::getline( sfile, line );
  } while (line.empty());

  boost::regex expression(m_regex_name);
  boost::smatch s_match;
  if (boost::regex_match(line, s_match, expression)) {
     dataset_name = s_match[1].str();
  }
  else {
     // Dataset name is the filename without extension and path
     size_t pos = file.find_last_of("/");
     // Remove all characters before /
     std::string str = file.substr(pos+1);
     // Remove any file extension
     pos = str.find_last_of(".");
     dataset_name = str.substr(0, pos);
  }

  return (dataset_name);
}


std::unique_ptr<XYDataset> AsciiParser::getDataset(const std::string& file) {

  std::ifstream sfile(file);
  // Check file exists
  if (!sfile) {
    throw ElementsException() << "File does not exist : " << file;
  }
  // Read file into a Table object
  ChTable::AsciiReader ascii_reader {{typeid(double), typeid(double)}};
  auto table = ascii_reader.read(sfile);
  // Put the Table data into vector pair
  std::vector<std::pair<double, double>> vector_pair;
  for (auto row : table) {
      vector_pair.push_back(std::make_pair( boost::get<double>(row[0]), boost::get<double>(row[1]) ));
  }
  std::unique_ptr<XYDataset> dataset_ptr( new XYDataset(vector_pair) );

 return(dataset_ptr);
}

} // XYDataset namespace
