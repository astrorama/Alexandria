/**
 * @file CosmosAsciiMapping.h
 *
 *  Created on: Mar 5, 2013
 *      Author: Pavel Binko
 */

#ifndef COSMOSASCIIMAPPING_H_
#define COSMOSASCIIMAPPING_H_


#include <map>
#include <utility>
#include <string>

#include "ChDataModel/Enumerations/FilterNames.h"


/**
 * @class CosmosAsciiMapping.
 * @brief Class defines the mapping between the column names in the Cosmos
 *        ASCII data file and the data members in the corresponding classes
 *        in the Euclid data model.
 */
class CosmosAsciiMapping {
public:
  CosmosAsciiMapping();
  virtual ~CosmosAsciiMapping();

  /**
   * @brief Photometry mapping.
   * @details Map of :
   *          - first  : Filter name.
   *          - second : Pair of column names :
   *                     first  : Value.
   *                     second : Value error.
   */
  static std::map<ChDataModel::FilterNames, std::pair<std::string, std::string>> photometryMapping;

  /**
   * @brief Source mapping.
   * @details Map of :
   *          - first  : Name of the variable in the class Source.
   *          - second : Column name.
   */
  static std::map<std::string, std::string> sourceMapping;

};

#endif /* COSMOSASCIIMAPPING_H_ */
