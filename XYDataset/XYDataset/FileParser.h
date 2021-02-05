/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
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
 * @file XYDataset/FileParser.h
 *
 * @date Apr 11, 2014
 * @author Nicolas Morisset
 */

#ifndef FILEPARSER_H_
#define FILEPARSER_H_

#include "XYDataset/XYDataset.h"

namespace Euclid {
namespace XYDataset {

/**
 * @class FileParser
 * Interface class
 * @ brief
 * Interface class which permits to get a dataset name (identifier) and
 * the data itself stored into a XYDataset object.
 */

class FileParser {
public:
  /**
   * @brief
   * Get the dataset name or identifier from a file
   * @param file
   * Filename including absolute path
   * @return
   * A dataset name
   */
  virtual std::string getName(const std::string& file) = 0;

  /**
   * @brief
   * Get the parameter identified by a given key_word value from a file
   * @param file
   * Filename including absolute path
   * @param key_word
   * key word identifying the parameter
   * @return
   * A dataset name
   */
  virtual std::string getParameter(const std::string& file, const std::string& key_word) = 0;

  /**
   * @brief
   * Get the dataset from a file
   * @param file
   * Filename including absolute path
   * @return
   * A unique pointer of a XYDataset object or a null pointer
   */
  virtual std::unique_ptr<XYDataset> getDataset(const std::string& file) = 0;

  /**
   * @brief
   * Check that we are in presence of a dataset file
   * @param file
   * Filename including the absolute path
   * @return
   * true: it is file containing datasets
   */
  virtual bool isDatasetFile(const std::string& file) = 0;

  /// Default destructor
  virtual ~FileParser() = default;
};

} /* namespace XYDataset */
}  // end of namespace Euclid

#endif  // FILEPARSER_H_
