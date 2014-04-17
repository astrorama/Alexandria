/**
 * @file XYDatasetProvider.h
 *
 * @date Apr 10, 2014
 * @author Nicolas Morisset
 */

#ifndef XYDATASETPROVIDER_H_
#define XYDATASETPROVIDER_H_

#include <memory>
#include <vector>
#include <string>
#include "XYDataset/XYDataset.h"

namespace XYDataset {

/**
 * The XYDatasetProvider template class provides the dataset following
 * an identifier object
 */

template <typename T>

class XYDatasetProvider
{
 public:
  /**
   * @brief
   * Virtual function to list all files contents in the "group" path
   * @details
   * let's take the folleoing example. if you have a group sets to "A/B/C" and
   * under the "C" repository there is the following structure :
   * C/file1
   * C/file2
   * C/D/file3
   * etc...
   * then the vector of strings returned will contain the following elements:
   * vector[0] = "A/B/C/file1"
   * vector[1] = "A/B/C/file2"
   * vector[3] = "A/B/C/D/file3"
   * etc...
   * Note: The empty string for the group means the root group
   * @param group
   * Name of the dataset group
   * @return
   * A vector of strings of all files included their path
   */
   virtual std::vector<std::string> listContents(const std::string& group) = 0;

  /**
   * @brief
   * Virtual function for getting from an identifier the dataset of
   * XYDataset type
   * @param identifier
   * Identifier object of the dataset
   * @return
   * A unique pointer of XYDataset type to the dataset
   */
   virtual std::unique_ptr<XYDataset> getDataset(const T &identifier) = 0;

 private:

};

} /* namespace XYDataset */

#endif // XYDATASETPROVIDER_H_ 
