/*
 * Magnitude_SED_Through_All_Filters.cpp
 *
 *  Created on: Sep 3, 2013
 *  Author : Nicolas Morisset
 */

#include <vector>
#include <boost/test/unit_test.hpp>
#include <boost/filesystem/path.hpp>
#include "ChDataModel/Source.h"
#include "ChDataModel/Enumerations/FilterTypes.h"
#include "ChDataHandling/AsciiFilterImporter.h"
#include "ChDataHandling/AsciiSedImporter.h"
#include <iostream>
#include <cmath>
#include <map>
#include "Faros/MagnitudeCalculation.h"

namespace fs = boost::filesystem;

using namespace ChDataModel;
using namespace std;

//____________________________________________________________________________//


struct MagnitudeCalculationFix {

  MagnitudeCalculation* magnitudeCalculation;
  AsciiFilterImporter*  inputFilter;
  AsciiSedImporter*     inputSed;

  char* strPath;
  std::string alexandriaPath{};

  double      tolerence;
  FilterTypes filterType;

  MagnitudeCalculationFix() {

    // Get Alexandria path
    strPath = getenv("ALEXANDRIA_PROJECT_ROOT");
    alexandriaPath = "";
    if (strPath != NULL)
    {
       alexandriaPath = std::string(strPath);
    }
    else
    {
      cout << "ERROR : <ALEXANDRIA_PROJECT_ROOT> environment variable is empty!!!";
    }

    magnitudeCalculation = new MagnitudeCalculation();
    inputFilter          = new AsciiFilterImporter();
    inputSed             = new AsciiSedImporter();

    filterType   = FilterTypes::EUCLID;

    tolerence    = pow(10., -10.);


  } // eof MagnitudeCalculationFix

  ~MagnitudeCalculationFix() {
    // teardown
    delete magnitudeCalculation;
    delete inputFilter;
    delete inputSed;
  }

  MagnitudeCalculationFix(const MagnitudeCalculationFix &) = delete ;

};

//=============================================================================
// Starting test
//=============================================================================

BOOST_AUTO_TEST_SUITE(MagnitudeCalculation_test)




//-----------------------------------------------------------------------------
//                       Magnitude_SED_Through_All_Filters_test
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( Magnitude_SED_Through_All_Filters_test, MagnitudeCalculationFix ) {

  BOOST_TEST_MESSAGE("--> Testing the Magitude computation of one SED through all cosmos filters, "
                     " SED used: Ell1_A_0.sed");

  // --- Read FILTER ---

  // Set the filter path
  fs::path filterPath(alexandriaPath);
  filterPath /= "PhotZAuxData";
  filterPath /= "Filter";
  filterPath /= "Cosmos";

  // Import filters into the map
  map<FilterNames, Filter> filterMap = inputFilter->importFilters(filterPath.string(), filterType);

  BOOST_TEST_MESSAGE("----> FILTER loaded");

  // --- Read SED ---

  // Get the SED path
  fs::path sedPath(alexandriaPath);
  sedPath /= "PhotZAuxData";
  sedPath /= "Sed";
  sedPath /= "Cosmos";

  // Import SEDs into the map
  map<SedNames, Sed> sedMap = inputSed->importSeds(sedPath.string());


  BOOST_TEST_MESSAGE("----> SED loaded");

  Filter filter{};
  pair<double,double> result_integration{};
  double magnitude{};

  // Magnitude are stored into a file
  stringstream ss;

  ofstream mag_file("/tmp/magnitude_all_seds_all_filters.txt",ios::out);
  mag_file<<"#    SED     FILTER     Magnitude"<<"\n";

  for (auto it_sed : sedMap )
  {

    Sed sed = it_sed.second;
    cout <<""<<endl;

    // Loop on ALL filters
    for (auto it_filter : filterMap )
    {
      filter = it_filter.second;
      result_integration.first  = 0.0;
      result_integration.second = 0.0;
      result_integration = magnitudeCalculation->brokenLineIntegration(sed, filter);
      magnitude = magnitudeCalculation->computeMagnitude(result_integration.first, result_integration.second);

      if ( !mag_file )
      {
          std::cerr<<"Cannot open the output file."<<std::endl;
          break;
      }  // Loop on ALL SEDs
      else
      {
        // Print on screen
        cout<< setw(10) << setiosflags(ios::left) << sed.getSedName()
                << setw(20) <<setiosflags(ios::left) <<it_filter.first
                << magnitude <<endl ;
        // Store in file
        mag_file<< setw(10) << setiosflags(ios::left) << sed.getSedName()
                << setw(20) <<setiosflags(ios::left) <<it_filter.first
                << magnitude <<"\n" ;
      }// eof if
    } //eof for filter

  } // eof for SED

  mag_file.close();

//  BOOST_CHECK_CLOSE(expected_filter_result, result.second, tolerence);

}



//____________________________________________________________________________//
BOOST_AUTO_TEST_SUITE_END ()
