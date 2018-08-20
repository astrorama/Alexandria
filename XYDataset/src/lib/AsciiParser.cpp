/*
 * Copyright (C) 2012-2020 Euclid Science Ground Segment    
 *  
 * This library is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free 
 * Software Foundation; either version 3.0 of the License, or (at your option)  
 * any later version.  
 *  
 * This library is distributed in the hope that it will be useful, but WITHOUT 
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more  
 * details.  
 *  
 * You should have received a copy of the GNU Lesser General Public License 
 * along with this library; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA  
 */
 
 /**
 * @file src/lib/AsciiParser.cpp
 *
 * @date May 13, 2014
 * @author Nicolas Morisset
 */

#include <boost/regex.hpp>
#include <fstream>
#include <iostream>
#include <sstream>

#include "boost/lexical_cast.hpp"

#include "ElementsKernel/Exception.h"
#include "Table/AsciiReader.h"
#include "XYDataset/AsciiParser.h"
#include "StringFunctions.h"

using boost::regex;
using boost::regex_match;

namespace Euclid {
namespace XYDataset {

//
// Get dataset name from ASCII file
//
std::string AsciiParser::getName(const std::string& file) {

  std::ifstream sfile(file);
  // Check file exists
  if (!sfile) {
    throw Elements::Exception() << "File does not exist : " << file;
  }

  std::string line{};
  std::string dataset_name{};
  // Check dataset name is in the file
  // Convention: read until found first non empty line, removing empty lines.
  while (line.empty() && sfile.good()) {
    std::getline(sfile, line);
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

  return dataset_name;
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
    auto table = Table::AsciiReader{sfile}.fixColumnTypes({typeid(double), typeid(double)}).read();
    // Put the Table data into vector pair
    std::vector<std::pair<double, double>> vector_pair;
    for (auto row : table) {
        vector_pair.push_back(std::make_pair( boost::get<double>(row[0]), boost::get<double>(row[1]) ));
    }
    dataset_ptr = std::unique_ptr<XYDataset> { new XYDataset(vector_pair) };
  }

 return dataset_ptr;
}

bool AsciiParser::isDatasetFile(const std::string& file) {
  bool is_a_dataset_file = false;
  std::ifstream sfile(file);
  // Check file exists
  if (sfile) {
    std::string line{};
    // Convention: read until found first non empty line, removing empty lines.
    // Escape also the dataset name and comment lines
    boost::regex expression("\\s*#.*");
    boost::smatch s_match;
    while ((line.empty() || boost::regex_match(line, s_match, expression)) && sfile.good()) {
      std::getline(sfile, line);
    }
    if (sfile.good()) {
      // We should have 2 double values only on one line
      try {
        std::stringstream ss(line);
        std::string empty_string{};
        std::string d1, d2;
        ss >> d1 >> d2 >> empty_string;
        boost::lexical_cast<double>(d1);
        boost::lexical_cast<double>(d2);
        if (!empty_string.empty()){
          is_a_dataset_file = false;
        }
        else {
          is_a_dataset_file = true;
        }
      }
      catch(...){
        is_a_dataset_file = false;
      }
    }// Eof sfile.good()
  } // Eof sfile
 return is_a_dataset_file;
}

} // XYDataset namespace
} // end of namespace Euclid
