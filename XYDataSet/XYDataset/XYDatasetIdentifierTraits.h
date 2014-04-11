/**
 * @file XYDatasetIdentifierTraits.h
 *
 * @date Apr 10, 2014
 * @author Nicolas Morisset
 */

#ifndef XYDATASETIDENTIFIERTRAITS_H_
#define XYDATASETIDENTIFIERTRAITS_H_

#include <memory>
#include <vector>
#include <string>
#include "XYDataset/XYDataset.h"

namespace XYdataset {

/**
 * The XYDatasetIdentifierTraits Trait class converts a given identifier
 * to its qualified name.
 *
 */
template <class T>

class XYDatasetIdentifierTraits
{
 public:

  /**
   * @brief
   * Converts a given identifier to its qualified name.
   * @param identifier
   * identifier of class T which has a getID method
   * @return
   * String of the qualified name
   *
   */
  static std::string getQualifiedName(const T& identifier) {
                     return identifier.getID();
                    }

 private:

}


/**
 * The XYDatasetIdentifierTraits Trait class converts a given string identifier
 * to its qualified name.
 *
 */

template <>

class XYDatasetIdentifierTraits
{
 public:
  /**
   * @brief
   * Converts a given string identifier to its qualified name.
   * @param identifier
   * Identifier of string type which has a getID method
   * @return
   * String of the qualified name
   *
   */
  static std::string getQualifiedName(const string& identifier) {
                     return identifier.getID();
                    }

 private:

}

} /* namespace XYDataset */




#endif // XYDATASETIDENTIFIERTRAITS_H_ 
