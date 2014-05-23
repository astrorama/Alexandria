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
 * @details zzzzzzzzzzzzzzzzzzzzzzzzzz
 *
 * The FitsParser reads FITS files which contain space or tab separated
 * tables of two columns. The first column contains the X data and the second
 * the Y data. The name of the dataset is extracted from the first non-empty
 * line of the file, as the first match of a regular expression. If the regular
 * expression does not match, the name of the file (excluding the extension)
 * is used as the name of the dataset. Comments are supported by using the Õ#Õ
 * character.
 * @throw
 * ElementException : File not found
 */
class FitsParser : public FileParser
{
 public:

  FitsParser(const std::string& keyword="") : FileParser(), m_name_keyword(keyword) {}

  /**
   * @brief
   * Get the dataset name of a ASCII file
   * @details
   * This function gets the name of a dataset.The datatset name could be
   * the filename or is included in the file. If the dataset is not included
   * into the file, the filename itself is the dataset name removing the path
   * and the extension. If the dataset name is inside the file the function
   * looks for a line starting with a "#" character and extract the word after
   *  the hash
   * @param file
   *  Filename of the file to be read including absolute path
   * @return
   * The name of the datatset
   * @throw
   * ElementException : File not found
   */
  std::string getName(const std::string& file) override;

  /**
   * @brief
   * Get a XYDataset object reading data from an ASCII file
   * @Details
   * Read an ASCII file and put the data into a XYDataset object. It makes the
   * assumption that the file only contains two columns of double values
   * @param file
   *  Filename of the file to be read including the absolute path
   * @return
   * A unique pointer to a XYDatatset object or null pointer.
   */
  std::unique_ptr<XYDataset> getDataset(const std::string& file) override;

 private:

  // Name keyword of the dataset
  std::string m_name_keyword;

};

} /* namespace XYDataset */



#endif // FITSPARSER_H_ 
