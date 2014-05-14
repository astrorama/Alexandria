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
 * @class FileParser
 * Interface class
 * @ brief
 * Interface class which permits to get a dataset name(identifier) and
 * the data itself stored into a XYDataset object.
 */

class FileParser
{
 public:

  /**
   * @brief
   * Get the dataset name or identifier from a file
   * @param file
   * filename including absolute path
   * @return
   * a dataset name
   */
   virtual std::string getName(const std::string& file) = 0;
   /**
    * @brief
    * Get the dataset from a file
    * @param file
    * filename including absolute path
    * @return
    * a unique pointer of a XYDataset object
    */
   virtual std::unique_ptr<XYDataset> getDataset(const std::string& file) = 0;

 private:

};

} /* namespace XYDataset */


#endif // FILEPARSER_H_ 
