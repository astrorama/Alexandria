/**
 * @file FitsParser.cpp
 *
 * @date May 13, 2014
 * @author Nicolas Morisset
 */

#include <boost/regex.hpp>
#include <fstream>
#include <iostream>
#include <CCfits/CCfits>

#include "ElementsKernel/ElementsException.h"
#include "ChTable/FitsReader.h"
#include "XYDataset/FitsParser.h"
#include "StringFunctions.h"

using boost::regex;
using boost::regex_match;

namespace XYDataset {

//
// Get dataset name from a FITS file
//
std::string FitsParser::getName(const std::string& file) {

  std::cout<<"m_name_keyword "<< m_name_keyword<<std::endl;

  std::string dataset_name{};
  std::ifstream sfile(file);

  // Check file exists
  if (!sfile) {
    throw ElementsException() << "File does not exist : " << file;
  }
  std::cout<<"file"<< file<<std::endl;

  // Read first HDU
  std::unique_ptr<CCfits::FITS> fits { new CCfits::FITS(file, CCfits::RWmode::Read)};
  std::cout<<"111 file "<< file<<std::endl;
  CCfits::ExtHDU& table_hdu = fits->extension(0);
  std::cout<<"22 file "<< file<<std::endl;

  std::string key_value {};

  table_hdu.readKey(m_name_keyword, key_value);
std::cout<<"key_value"<< key_value<<std::endl;
  if (!key_value.empty()) {
    dataset_name = key_value;
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
// Get dataset from a FITS file
//
std::unique_ptr<XYDataset> FitsParser::getDataset(const std::string& file) {

  std::unique_ptr<XYDataset> dataset_ptr {};
  std::ifstream sfile(file);

  // Check file exists
  if (sfile) {
    std::unique_ptr<CCfits::FITS> fits { new CCfits::FITS(file, CCfits::RWmode::Read)};
    const CCfits::ExtHDU& table_hdu = fits->extension(1);

    // Read first HDU
    ChTable::FitsReader fits_reader {};
    auto table = fits_reader.read(table_hdu);

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



