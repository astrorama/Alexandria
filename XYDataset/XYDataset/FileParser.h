/**
 * @file FileParser.h
 *
 * @date Apr 11, 2014
 * @author Nicolas Morisset
 */

#ifndef FILEPARSER_H_
#define FILEPARSER_H_

#include "XYDataset/XYDataset.h"

namespace XYDataset {

/**
 * The FileParser
 *
 */

class FileParser
{
 public:

  /**
   * @brief
   * @param
   * @return
   *
   */
   virtual std::string getName(const std::string& filename) = 0;
   virtual std::unique_ptr<XYDataset> getDataSet(const std::string& filename) = 0;

 private:

};

} /* namespace XYDataset */


#endif // FILEPARSER_H_ 
