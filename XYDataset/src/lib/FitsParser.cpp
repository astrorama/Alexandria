/*
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
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
 * @file src/lib/FitsParser.cpp
 *
 * @date May 13, 2014
 * @author Nicolas Morisset
 */

#include "XYDataset/FitsParser.h"
#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Unused.h"
#include "StringFunctions.h"
#include "Table/FitsReader.h"
#include <CCfits/CCfits>
#include <fstream>
#include <iostream>

namespace Euclid {
namespace XYDataset {

//
// Get dataset name from a FITS file
//
std::string FitsParser::getName(const std::string& file) {

  std::string dataset_name = getParameter(file, m_name_keyword);
  if (dataset_name.empty()) {
    // Dataset name is the filename without extension and path
    std::string str{};
    str          = removeAllBeforeLastSlash(file);
    dataset_name = removeExtension(str);
  }
  return dataset_name;
}

std::string FitsParser::getParameter(const std::string& file, const std::string& key_word) {
  std::string   value{};
  std::ifstream sfile(file);

  // Check file exists
  if (!sfile) {
    throw Elements::Exception() << "File not found : " << file;
  }

  // Read first HDU
  auto            fits      = make_unique<CCfits::FITS>(file, CCfits::RWmode::Read);
  CCfits::ExtHDU& table_hdu = fits->extension(1);

  table_hdu.readAllKeys();
  auto keyword_map = table_hdu.keyWord();
  auto iter        = keyword_map.find(key_word);
  if (iter != keyword_map.end()) {
    iter->second->value(value);
  }

  return value;
}

//
// Get dataset from a FITS file
//
std::unique_ptr<XYDataset> FitsParser::getDataset(const std::string& file) {

  std::unique_ptr<XYDataset> dataset_ptr{};
  std::ifstream              sfile(file);

  CCfits::FITS::setVerboseMode(true);

  // Check file exists
  if (sfile) {
    auto fits = make_unique<CCfits::FITS>(file, CCfits::RWmode::Read);
    try {
      const CCfits::ExtHDU& table_hdu = fits->extension(1);
      // Read first HDU
      auto table = Table::FitsReader{table_hdu}.read();

      // Put the Table data into vector pair
      std::vector<std::pair<double, double>> vector_pair(table.size());
      std::transform(table.begin(), table.end(), vector_pair.begin(), [](const Table::Row& row) {
        return std::make_pair(boost::get<double>(row[0]), boost::get<double>(row[1]));
      });
      dataset_ptr = make_unique<XYDataset>(std::move(vector_pair));
    } catch (const CCfits::FitsException&) {
      throw Elements::Exception() << "FitsException catched! File: " << file;
    }  // Eof try-catch
  }    // Eof if

  return dataset_ptr;
}

//
// Check that the FITS file is a dataset file(with at least one HDU table)
//
bool FitsParser::isDatasetFile(const std::string& file) {
  bool is_a_dataset_file = true;
  try {
    auto                  fits      = make_unique<CCfits::FITS>(file, CCfits::RWmode::Read);
    const CCfits::ExtHDU& table_hdu = fits->extension(1);
    ELEMENTS_UNUSED auto& temp      = dynamic_cast<const CCfits::Table&>(table_hdu);
  } catch (const CCfits::FitsException&) {
    is_a_dataset_file = false;
  }
  return is_a_dataset_file;
}

}  // namespace XYDataset
}  // end of namespace Euclid
