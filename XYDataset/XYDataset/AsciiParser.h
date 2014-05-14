/**
 * @file AsciiParser.h
 *
 * @date Apr 14, 2014
 * @author admin
 */

#ifndef ASCIIPARSER_H_
#define ASCIIPARSER_H_

#include "XYDataset/XYDataset.h"
#include "XYDataset/FileParser.h"


namespace XYDataset {

/**
 * The AsciiParser
 *
 */

class AsciiParser : public FileParser
{
 public:

  AsciiParser(const std::string& regex_str="^\\s*#\\s*(\\w+)\\s*$") : FileParser(), m_regex_name(regex_str) {}

  /**
   * @brief
   * Get the dataset name of a ASCII file
   * @details
   * This function gets the name of a dataset.The datatset name could be
   * the filename or is included in the file. If the dataset is not inclued in
   * file, the filename itself is the dataset name removing the path and the
   * extension. If the dataset name is inside the file the function looks for
   * a line starting with a "#" character and extract the word after the hash
   * @param file
   *  Filename of the file to be read including absolute path
   * @return
   * The name of the datatset
   */
  std::string getName(const std::string& file) override;

  /**
   * @brief
   * Get the dataset from a ASCII file
   * @Details
   *
   * @param file
   *  Filename of the file to be read including absolute path
   * @return
   * The datatset
   */
  std::unique_ptr<XYDataset> getDataset(const std::string& file) override;

 private:

  std::string m_regex_name;

};

} /* namespace XYDataset */



#endif // ASCIIPARSER_H_ 
