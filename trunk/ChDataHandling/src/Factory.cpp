/**
 * @file Factory.cpp
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

#include "ChDataHandling/Factory.h"
#include "ChDataHandling/AsciiCosmosImporter.h"
#include "ChDataHandling/AsciiFilterImporter.h"
#include "ChDataHandling/AsciiSedImporter.h"
#include "ChDataHandling/FitsImageImporter.h"

#include "ChDataModel/Survey.h"
#include "ChDataModel/Catalog.h"

#include "ElementsKernel/ElementsException.h"

using namespace std;
using namespace ChDataModel;
using namespace Fits;

//-----------------------------------------------------------------------------
// Function createSurvey

Survey * Factory::createSurvey(const ChDataModel::SurveyNames & surveyName) {

  // Create an empty survey with the survey name
  Survey * survey = new Survey(surveyName);

  // Return the filled survey object
  return survey;

} // Eof Factory::createSurvey

//-----------------------------------------------------------------------------
// Function createSurvey

Survey * Factory::createSurvey(const string & surveyName) {

  // Create an empty survey with the survey name
  Survey * survey = new Survey(surveyName);

  // Return the filled survey object
  return survey;

} // Eof Factory::createSurvey

//-----------------------------------------------------------------------------
// Function createCatalogInSurvey

Catalog * Factory::createCatalogInSurvey(Survey * survey,
    const std::string & path, int64_t startRow /* = 1 */,
    int64_t numRows /* = INT64_MAX */) {

  // Create an empty catalog in the survey
  Catalog & catalog = survey->createCatalog();

  // Create an importer to read ASCII data from the file
  if (SurveyNames::COSMOS == survey->getSurveyName()) {
    AsciiCosmosImporter * input = new AsciiCosmosImporter();
    input->importCatalog(catalog, path, startRow, numRows);
    delete input;
  }
  else if (SurveyNames::VVDS == survey->getSurveyName()) {
    throw ElementsException(
        "ChDataHandling::Factory : Apologies, the VVDS Importer is currently not available");
  }
  else {
    throw ElementsException(
        "ChDataHandling::Factory : Unknown survey name : "
            + surveyNames2string(survey->getSurveyName()));
  }

  // Return the filled survey object
  return &catalog;

} // Eof Factory::createCatalogInSurvey

//-----------------------------------------------------------------------------
// Function createCatalogInSurvey

Catalog * Factory::createCatalogInSurvey(Survey * survey,
    const std::vector<std::string> & vectorOfFiles, int64_t startRow /* = 1 */,
    int64_t numRows /* = INT64_MAX */) {

  // Create an empty catalog in the survey
  Catalog & catalog = survey->createCatalog();

  // Create an importer to read ASCII data from the file
  if (SurveyNames::COSMOS == survey->getSurveyName()) {
    AsciiCosmosImporter * input = new AsciiCosmosImporter();
    input->importCatalog(catalog, vectorOfFiles, startRow, numRows);
    delete input;
  }
  else if (SurveyNames::VVDS == survey->getSurveyName()) {
    throw ElementsException(
        "ChDataHandling::Factory : Apologies, the VVDS Importer is currently not available");
  }
  else {
    throw ElementsException(
        "ChDataHandling::Factory : Unknown survey name : "
            + surveyNames2string(survey->getSurveyName()));
  }

  // Return the filled survey object
  return &catalog;

} // Eof Factory::createCatalogInSurvey

//-----------------------------------------------------------------------------
// Function createFiltersInSurvey

void Factory::createFiltersInSurvey(ChDataModel::Survey * survey,
    const std::string & path, const ChDataModel::FilterTypes & filterType) {

  // Create an importer to read ASCII data from the file
  if (SurveyNames::COSMOS == survey->getSurveyName()) {

    // Create the ASCII filter importer
    AsciiFilterImporter * input = new AsciiFilterImporter();

    // Create a map of filters
    map<FilterNames, Filter> filterMap = input->importFilters(path, filterType);

    // Delete the ASCII filter importer
    delete input;

    // Attach the filters to the survey
    survey->setFilterMap(filterMap);

  }
  else if (SurveyNames::VVDS == survey->getSurveyName()) {
    throw ElementsException(
        "ChDataHandling::Factory : Apologies, the VVDS Importer is currently not available");
  }
  else {
    throw ElementsException(
        "ChDataHandling::Factory : Unknown survey name : "
            + surveyNames2string(survey->getSurveyName()));
  }

} // Eof Factory::createFiltersInSurvey

//-----------------------------------------------------------------------------
// Function createFiltersInSurvey

void Factory::createFiltersInSurvey(ChDataModel::Survey * survey,
    const std::vector<std::string> & vectorOfFiles,
    const ChDataModel::FilterTypes & filterType) {

  // Create an importer to read ASCII data from the file
  if (SurveyNames::COSMOS == survey->getSurveyName()) {

    // Create the ASCII filter importer
    AsciiFilterImporter * input = new AsciiFilterImporter();

    // Create a map of filters
    map<FilterNames, Filter> filterMap = input->importFilters(vectorOfFiles,
        filterType);

    // Delete the ASCII filter importer
    delete input;

    // Attach the filters to the survey
    survey->setFilterMap(filterMap);

  }
  else if (SurveyNames::VVDS == survey->getSurveyName()) {
    throw ElementsException(
        "ChDataHandling::Factory : Apologies, the VVDS Importer is currently not available");
  }
  else {
    throw ElementsException(
        "ChDataHandling::Factory : Unknown survey name : "
            + surveyNames2string(survey->getSurveyName()));
  }

} // Eof Factory::createFiltersInSurvey

//-----------------------------------------------------------------------------
// Function createSedsInSurvey

void Factory::createSedsInSurvey(ChDataModel::Survey * survey,
    const std::string & path) {

// Create an importer to read ASCII data from the file
  if (SurveyNames::COSMOS == survey->getSurveyName()) {

    // Create the ASCII SED importer
    AsciiSedImporter * input = new AsciiSedImporter();

    // Create a map of SEDs
    map<SedNames, Sed> sedMap = input->importSeds(path);

    // Delete the ASCII SED importer
    delete input;

    // Attach the SEDs to the survey
    survey->setSedMap(sedMap);

  }
  else if (SurveyNames::VVDS == survey->getSurveyName()) {
    throw ElementsException(
        "ChDataHandling::Factory : Apologies, the VVDS Importer is currently not available");
  }
  else {
    throw ElementsException(
        "ChDataHandling::Factory : Unknown survey name : "
            + surveyNames2string(survey->getSurveyName()));
  }

} // Eof Factory::createSedsInSurvey

//-----------------------------------------------------------------------------
// Function createSedsInSurvey

void Factory::createSedsInSurvey(ChDataModel::Survey * survey,
    const std::vector<std::string> & vectorOfFiles) {

// Create an importer to read ASCII data from the file
  if (SurveyNames::COSMOS == survey->getSurveyName()) {

    // Create the ASCII SED importer
    AsciiSedImporter * input = new AsciiSedImporter();

    // Create a map of SEDs
    map<SedNames, Sed> sedMap = input->importSeds(vectorOfFiles);

    // Delete the ASCII SED importer
    delete input;

    // Attach the SEDs to the survey
    survey->setSedMap(sedMap);

  }
  else if (SurveyNames::VVDS == survey->getSurveyName()) {
    throw ElementsException(
        "ChDataHandling::Factory : Apologies, the VVDS Importer is currently not available");
  }
  else {
    throw ElementsException(
        "ChDataHandling::Factory : Unknown survey name : "
            + surveyNames2string(survey->getSurveyName()));
  }

} // Eof Factory::createSedsInSurvey

//-----------------------------------------------------------------------------
// Function createFitsImage

Image * Factory::createFitsImage(const string & fileName,
    const string & hduName) {

  // Create the FITS image importer
  FitsImageImporter * input = new FitsImageImporter(fileName);

  // Create an image
  Image * image = input->importImage(hduName);

  // Delete the FITS image importer
  delete input;

  return image;

} // Eof Factory::createFitsImage

//-----------------------------------------------------------------------------
