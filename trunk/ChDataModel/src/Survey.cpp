/**
 * @file Survey.cpp
 *
 * @author Pierre Dubath
 *
 * Created on: Feb. 6, 2013
 */

#include <sstream>
#include <iostream>
#include <map>

#include "ChDataModel/Survey.h"

using namespace std;

namespace ChDataModel {

//-----------------------------------------------------------------------------

Catalog & Survey::createCatalog() {

  // Create a new catalog
  Catalog catalog = Catalog();
  // set survey back pointer
  catalog.setSurveyPtr(this);

  // Build a valid key for the catalog map
  map<int, Catalog>::iterator itr;
  int newKey = 0;
  if (!m_catalog_map.empty()) {
    // Map iterator to one past last element of the current map
    itr = m_catalog_map.end();
    // last element;
    --itr;
    // The map key for the new catalog will be the last key + 1
    newKey = itr->first + 1;
  }

  // Copy the catalog into the map
  m_catalog_map[newKey] = catalog;

  // Map iterator to one past last element of the current map
  itr = m_catalog_map.end();
  // last element;
  --itr;  // Map iterator

  // Return the last catalog from the map.
  return itr->second;

} // Eof Survey::createCatalog

Catalog & Survey::getFirstCatalog() {
  return this->getCatalogMap()[0];
}

//-----------------------------------------------------------------------------

void Survey::printCatalogsInSurvey() {

  cout << "###############################################\n";
  cout << "#                                             #\n";
  cout << "#     Print catalogs in survey                #\n";
  cout << "#                                             #\n";
  cout << "###############################################\n\n";

  // Information from the survey

  cout << "In Survey : Survey name         = " << m_survey_name << endl;
  cout << "In Survey : Number of catalogs  = " << catalogSize() << endl;

  // Loop over catalogs

  int catNr = 0;
  for (Survey::CatalogIterator it1 = catalogBegin(); it1 != catalogEnd(); ++it1) {

    cout << "\n***** Catalog no. " << ++catNr << " **************************\n";
    cout << "In Catalog : Survey name         = "
        << it1->getSurveyPtr()->getSurveyName() << endl;

    it1->printCatalog();

  } // Eof for(catalogs)

  cout << "##### End of the print catalogs in survey #####\n\n\n";

} // Eof Source::printCatalogsInSurvey

//-----------------------------------------------------------------------------

void Survey::printFiltersInSurvey() {

  cout << "###############################################\n";
  cout << "#                                             #\n";
  cout << "#     Print filters in survey                 #\n";
  cout << "#                                             #\n";
  cout << "###############################################\n\n";

  // Loop over filters

  int filterNr = 0;
  for (Survey::FilterIterator it1 = filterBegin(); it1 != filterEnd(); ++it1) {

    cout << "\n***** Filter no. " << ++filterNr << " ***************************\n";
    it1->printFilter();

  } // Eof for(filters)

  cout << "##### End of the print filters in survey ######\n\n\n";

} // Eof Source::printFiltersInSurvey

//-----------------------------------------------------------------------------

void Survey::printSedsInSurvey() {

  cout << "###############################################\n";
  cout << "#                                             #\n";
  cout << "#     Print SEDs in survey                    #\n";
  cout << "#                                             #\n";
  cout << "###############################################\n\n";

  // Loop over SEDs

  int sedNr = 0;
  for (Survey::SedIterator it1 = sedBegin(); it1 != sedEnd(); ++it1) {

    cout << "\n***** SED no. " << ++sedNr << " ******************************\n";
    it1->printSed();

  } // Eof for(SEDs)

  cout << "##### End of the print SEDs in survey #########\n\n\n";

} // Eof Source::printSedsInSurvey

//-----------------------------------------------------------------------------

void Survey::printSurvey() {

  cout << "###############################################\n";
  cout << "#                                             #\n";
  cout << "#     Print the full contents of the survey   #\n";
  cout << "#                                             #\n";
  cout << "###############################################\n\n";

  printCatalogsInSurvey();
  printFiltersInSurvey();
  printSedsInSurvey();

} // Eof Source::printSurvey

//-----------------------------------------------------------------------------

} /* namespace ChDataModel */
