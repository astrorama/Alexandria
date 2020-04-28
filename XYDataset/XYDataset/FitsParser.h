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
 * @file XYDataset/FitsParser.h
 *
 * @date Apr 14, 2014
 * @author admin
 */

#ifndef FITSPARSER_H_
#define FITSPARSER_H_

#include "ElementsKernel/Export.h"

#include "XYDataset/XYDataset.h"
#include "XYDataset/FileParser.h"

namespace Euclid {
namespace XYDataset {

/**
 * @class FitsParser
 *
 * @brief
 * Tool for reading FITS tables from streams
 * @details
 * The FitsParser reads FITS file which contains a primary HDU and one binary
 * extension. The extension must contain two columns of double types. The first
 * column contains the X data and the second the Y data. The name of the dataset
 * is extracted from one of the keywords stored in the first extension. The name
 * of this keyword can be specified in the constructor. If the keyword does
 * not exist, the dataset name is extracted from the FITS filename itself
 * removing the path and extension (.fits).
 */
class ELEMENTS_API FitsParser : public FileParser
{
 public:

  /**
   * @brief Constructor
   * Tool for reading FITS tables from streams
   * @param keyword
   * The keyword name where the dataset name is stored in the FITS file. The default is the
   * empty string.
   */
  FitsParser(const std::string& keyword = "") : FileParser(), m_name_keyword(keyword) {}

  /**
   * @brief
   * Get the dataset name of a FITS file
   * @details
   * This function gets the dataset name. It tries first to get the dataset name
   * from the keyword stored in the binary extension. The keyword name to look for is
   * specified at the constructor level. If no keyword specified or found, the dataset name
   *  is extracted from the filename removing the path and the extension.
   * @param file
   * Filename of the file to be read including absolute path
   * @return
   * The name of the datatset
   * @throw
   * ElementException : File not found
   */
  std::string getName(const std::string& file) override;

   /**
   * @brief
   * Get the parameter identified by a given key_word value from a file
   * @details
   * This function gets the the parameter if present in the fits HDU keyword.
   * Return an empty string if the key word is not present.
   * @param file
   * Filename of the file to be read including absolute path
   * @param key_word
   * key word identifying the parameter
   * @return
   * The name of the datatset
   * @throw
   * ElementException : File not found
   */
  std::string getParameter(const std::string& file, const std::string& key_word) override;

  /**
   * @brief
   * Get a XYDataset object reading data from an FITS file
   * @details
   * It reads data in the first extension of a FITS file and put the data into a
   * XYDataset object. It makes the assumption that the file only contains two
   * columns of double values.
   * @param file
   * Filename of the FITS file to be read (including the absolute path).
   * @return
   * A unique pointer to a XYDatatset object or null pointer.
   * @throw Elements::Exception
   * A FITS exception occured
   */
  std::unique_ptr<XYDataset> getDataset(const std::string& file) override;

  /**
   * @brief
   * Check that the FITS file is a dataset file(with at least one HDU table)
   * @details
   * This checking should avoid reading any files which do not contain
   * any dataset.
   * @param file
   * Filename of the FITS file to be read including the absolute path.
   * @return
   * true if it is a FITS file with dataset(at least with one HDU table)
   */
  bool isDatasetFile(const std::string& file) override;

 private:

  // keyword name of the dataset
  std::string m_name_keyword;

};

} /* namespace XYDataset */
} // end of namespace Euclid



#endif // FITSPARSER_H_
