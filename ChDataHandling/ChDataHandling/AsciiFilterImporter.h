/**
 * @file AsciiFilterImporter.h
 *
 * Created on: Jun 17, 2013
 *     Author: Pavel Binko
 */

#ifndef ASCIIFILTERIMPORTER_H_
#define ASCIIFILTERIMPORTER_H_

#include <string>
#include <vector>
#include <map>

#include "ChDataHandling/AsciiImporter.h"

#include "ChDataModel/VectorPair.h"
#include "ChDataModel/Filter.h"
#include "ChDataModel/Enumerations/FilterNames.h"
#include "ChDataModel/Enumerations/FilterTypes.h"

/**
 * @class AsciiFilterImporter
 * @brief
 *   Imports filters in the ASCII format
 */
class AsciiFilterImporter: public AsciiImporter {

public:

  /**
   * @brief Destructor
   */
  virtual ~AsciiFilterImporter() {
  }

  /**
   * @brief importFilters
   *   Imports data into a filter or set of filters
   * @param path
   *   Either a path to a single file or to a directory. In the latter case,
   *   all files from that directory will be considered for import.
   * @param filterType
   *   Filter type (one of EUCLID, OPTICS, FILTER, CCD)
   * @return
   *   Map of filters
   */
  std::map<ChDataModel::FilterNames, ChDataModel::Filter> importFilters(
      const std::string & path, const ChDataModel::FilterTypes & filterType);

  /**
   * @brief importFilters
   *   Imports data into a filter or set of filters
   * @param vectorOfFiles
   *   Vector of file names, which will be considered for import
   * @param filterType
   *   Filter type (one of EUCLID, OPTICS, FILTER, CCD)
   * @return
   *   Map of filters
   */
  std::map<ChDataModel::FilterNames, ChDataModel::Filter> importFilters(
      const std::vector<std::string> & vectorOfFiles,
      const ChDataModel::FilterTypes & filterType);

  /**
   * @brief createFilter
   *   Creates the filter
   * @param fileName
   *   File name (with the values)
   * @param filterType
   *   Filter type (one of EUCLID, OPTICS, FILTER, CCD)
   * @return
   *   The filter
   */
  ChDataModel::Filter createFilter(const std::string & fileName,
      const ChDataModel::FilterTypes & filterType);

  /**
   * @brief importFilterName
   *   Gets the filter name :
   *   - either from the 1st comment row
   *   - or from the file name
   * @param fileName
   *   File name (containing the SED values)
   * @return
   *   The filter name
   */
  ChDataModel::FilterNames importFilterName(const std::string & fileName);

  /**
   * @brief importFilterData
   *   Fills the filter with the data (all rows from a file)
   * @return
   *   The filter data as a vector pair
   */
  ChDataModel::VectorPair importFilterData();

  /**
   * @brief simulateFilterColumnDefinition
   *   Simulates the filter column definition (because the filter files
   *   do not contain definitions of the columns)
   * @details
   *   Filter efficiency (Y axis) as a function of wave length (X axis)
   */
  void simulateFilterColumnDefinition();

private:

  /**
   * @brief body_importFilters
   *   Function, which performs the functionality for both importFilters
   *   functions (after the path resolution)
   * @param filterType
   *   Filter type
   * @return
   *   Map of filters
   */
  std::map<ChDataModel::FilterNames, ChDataModel::Filter> body_importFilters(
      const ChDataModel::FilterTypes & filterType);

};

#endif /* ASCIIFILTERIMPORTER_H_ */
