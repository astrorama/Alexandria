/**
 * @file AsciiSedImporter.h
 *
 * Created on: Jun 26, 2013
 *     Author: Pavel Binko
 */

#ifndef ASCIISEDIMPORTER_H_
#define ASCIISEDIMPORTER_H_

#include <string>
#include <vector>
#include <map>

#include "ChDataHandling/AsciiImporter.h"

#include "ChDataModel/VectorPair.h"
#include "ChDataModel/Sed.h"
#include "ChDataModel/Enumerations/SedNames.h"

/**
 * @class AsciiSedImporter
 * @brief
 *   Imports SEDs in the ASCII format
 */
class AsciiSedImporter: public AsciiImporter {

public:

  /**
   * @brief Destructor
   */
  virtual ~AsciiSedImporter() {
  }

  /**
   * @brief importSeds
   *   Imports data into an SED or set of SEDs
   * @param path
   *   Either a path to a single file or to a directory. In the latter case,
   *   all files from that directory will be considered for import.
   * @return
   *   Map of SEDs
   */
  std::map<ChDataModel::SedNames, ChDataModel::Sed> importSeds(
      const std::string & path);

  /**
   * @brief importSeds
   *   Imports data into an SED or set of SEDs
   * @param vectorOfFiles
   *   Vector of file names, which will be considered for import
   * @return
   *   Map of SEDs
   */
  std::map<ChDataModel::SedNames, ChDataModel::Sed> importSeds(
      const std::vector<std::string> & vectorOfFiles);

  /**
   * @brief createSed
   *   Creates the SED
   * @param fileName
   *   File name (containing the SED values)
   * @return
   *   The SED
   */
  ChDataModel::Sed createSed(const std::string & fileName);

  /**
   * @brief importSedName
   *   Gets the SED name :
   *   - either from the 1st comment row
   *   - or from the file name
   * @param fileName
   *   File name (containing the SED values)
   * @return
   *   The SED name
   */
  ChDataModel::SedNames importSedName(const std::string & fileName);

  /**
   * @brief importSedData
   *   Fills the SED with the data (all rows from a file)
   * @return
   *   The SED data as a vector pair
   */
  ChDataModel::VectorPair importSedData();

  /**
   * @brief simulateSedColumnDefinition
   *   Simulates the SED column definition (because the SED files
   *   do not contain definitions of the columns)
   * @details
   *   SED intensity (Y axis) as a function of wave length (X axis)
   */
  void simulateSedColumnDefinition();

private:

  /**
   * @brief body_importSeds
   *   Function, which performs the functionality for both importSeds
   *   functions (after the path resolution)
   * @return
   *   Map of SEDs
   */
  std::map<ChDataModel::SedNames, ChDataModel::Sed> body_importSeds();

};

#endif /* ASCIISEDIMPORTER_H_ */
