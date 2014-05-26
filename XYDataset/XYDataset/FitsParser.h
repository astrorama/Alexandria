/**
 * @file FitsParser.h
 *
 * @date Apr 14, 2014
 * @author admin
 */

#ifndef FITSPARSER_H_
#define FITSPARSER_H_

#include "XYDataset/XYDataset.h"
#include "XYDataset/FileParser.h"

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
 * of this keyword can be specified by in the constructor. If the keyword does
 * not exist, the dataset name is extracted from the FITS filename itself
 * removing the path and extension (.fits).
 */
class FitsParser : public FileParser
{
 public:

  /**
   * @brief Constructor
   * Tool for reading FITS tables from streams
   * @param keyword
   * The keyword name where is stored the dataset name. The default is the
   * empty string.
   */
  FitsParser(const std::string& keyword="") : FileParser(), m_name_keyword(keyword) {}

  /**
   * @brief
   * Get the dataset name of a FITS file
   * @details
   * This function gets the name of a dataset from aa filename. The function
   * tries first to get the dataset name from the keyword stored into the binary
   * extension. The keyword name to look for is specified at the constructor
   * level. If no keyword specified or found, the dataset name is extracted from
   * the file name removing the path and the extension. I
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
   * Get a XYDataset object reading data from an FITS file
   * @Details
   * Read data in the first extension from a FITS file and put the data into a
   * XYDataset object. It makes the assumption that the file only contains two
   * columns of double values
   * @param file
   *  Filename of the file to be read including the absolute path
   * @return
   * A unique pointer to a XYDatatset object or null pointer.
   * @throw ElementsException()
   * FitsException occured
   */
  std::unique_ptr<XYDataset> getDataset(const std::string& file) override;

 private:

  // Name keyword of the dataset
  std::string m_name_keyword;

};

} /* namespace XYDataset */



#endif // FITSPARSER_H_ 
