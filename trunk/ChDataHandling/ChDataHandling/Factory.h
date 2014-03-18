/**
 * @file Factory.h
 *
 * Created on: May 17, 2013
 *
 * @author dubath
 *
 * @section LICENSE
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 2 of
 * the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * General Public License for more details at
 * http://www.gnu.org/copyleft/gpl.html
 *
 * @section DESCRIPTION
 *
 * This class represents ...
 */

#ifndef FACTORY_H_
#define FACTORY_H_

#include <string>
#include "ChDataModel/Survey.h"
#include "ChDataModel/Enumerations/SurveyNames.h"
#include "ChDataModel/Enumerations/FilterTypes.h"
#include "ChDataModel/Fits/Image.h"

class Factory {

public:

  /**
   * @brief createSurvey
   *   Creates a survey
   * @param surveyName
   *   Survey name (as enum class SurveyNames)
   * @return
   *   Pointer to the created survey
   */
  static ChDataModel::Survey * createSurvey(
      const ChDataModel::SurveyNames & surveyName);

  /**
   * @brief createSurvey
   *   Creates a survey
   * @param surveyName
   *   Survey name (as string)
   * @return
   *   Pointer to the created survey
   */
  static ChDataModel::Survey * createSurvey(const std::string & surveyName);

  /**
   * @brief createCatalogInSurvey
   *   In a given survey, it creates a catalog and imports data into it
   * @details
   *   It means all its sources and their corresponding photometry
   * @param survey
   *   Pointer to the survey, where the created catalog should be attached to
   * @param path
   *   Either a path to a single file or to a directory. In the latter case,
   *   all files from that directory will be considered for import.
   * @param startRow
   *   The first data row to be imported (startRow-1 rows will be skipped)
   * @param numRows
   *   Number of data rows which will be imported
   * @return
   *   Pointer to the created catalog in the survey
   */
  static ChDataModel::Catalog * createCatalogInSurvey(
      ChDataModel::Survey * survey, const std::string & path, int64_t startRow =
          1, int64_t numRows = INT64_MAX);

  /**
   * @brief createCatalogInSurvey
   *   In a given survey, it creates a catalog and imports data into it
   * @details
   *   It means all its sources and their corresponding photometry
   * @param survey
   *   Pointer to the survey, where the created catalog should be attached to
   * @param vectorOfFiles
   *   Vector of file names, which will be considered for import
   * @param startRow
   *   The first data row to be imported (startRow-1 rows will be skipped)
   * @param numRows
   *   Number of data rows which will be imported
   * @return
   *   Pointer to the created catalog in the survey
   */
  static ChDataModel::Catalog * createCatalogInSurvey(
      ChDataModel::Survey * survey,
      const std::vector<std::string> & vectorOfFiles, int64_t startRow = 1,
      int64_t numRows = INT64_MAX);

  /**
   * @brief createFiltersInSurvey
   *   In a given survey, it creates map of filters
   * @param survey
   *   Pointer to the survey, where the created catalog should be attached to
   * @param path
   *   Either a path to a single file or to a directory. In the latter case,
   *   all files from that directory will be considered for import.
   * @param filterType
   *   Filter type (one of EUCLID, OPTICS, FILTER, CCD)
   */
  static void createFiltersInSurvey(ChDataModel::Survey * survey,
      const std::string & path, const ChDataModel::FilterTypes & filterType);

  /**
   * @brief createFiltersInSurvey
   *   In a given survey, it creates map of filters
   * @param survey
   *   Pointer to the survey, where the created catalog should be attached to
   * @param vectorOfFiles
   *   Vector of file names, which will be considered for import
   * @param filterType
   *   Filter type (one of EUCLID, OPTICS, FILTER, CCD)
   */
  static void createFiltersInSurvey(ChDataModel::Survey * survey,
      const std::vector<std::string> & vectorOfFiles,
      const ChDataModel::FilterTypes & filterType);

  /**
   * @brief createSedsInSurvey
   *   In a given survey, it creates map of filters
   * @param survey
   *   Pointer to the survey, where the created catalog should be attached to
   * @param path
   *   Either a path to a single file or to a directory. In the latter case,
   *   all files from that directory will be considered for import.
   */
  static void createSedsInSurvey(ChDataModel::Survey * survey,
      const std::string & path);

  /**
   * @brief createSedsInSurvey
   *   In a given survey, it creates map of filters
   * @param survey
   *   Pointer to the survey, where the created catalog should be attached to
   * @param vectorOfFiles
   *   Vector of file names, which will be considered for import
   */
  static void createSedsInSurvey(ChDataModel::Survey * survey,
      const std::vector<std::string> & vectorOfFiles);

  /**
   * @brief createFitsImage
   *   In a given survey, it creates map of filters
   * @param fitsFileName
   *   Name of the file containing an image
   * @param hduName
   *   Name of the HDU containing an image
   * @return
   *   Pointer to the created image
   */
  static ChDataModel::Fits::Image * createFitsImage(
      const std::string & fitsFileName, const std::string & hduName);

};

#endif /* FACTORY_H_ */
