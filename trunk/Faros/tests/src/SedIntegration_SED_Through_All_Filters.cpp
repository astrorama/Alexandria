/*
 * SedIntegration_SED_Through_All_Filters.cpp
 *
 *  Created on: Oct 11, 2013
 *      Author: admin
 */


#include <iostream>
#include <cmath>
#include <map>
#include <iomanip>
#include <vector>
#include <boost/test/unit_test.hpp>
#include <boost/filesystem/path.hpp>

#include "ChDataModel/Enumerations/FilterTypes.h"
#include "ChDataHandling/AsciiFilterImporter.h"
#include "ChDataHandling/AsciiSedImporter.h"

#include "Faros/SedIntegration.h"


namespace fs = boost::filesystem;

using namespace ChDataModel;
using namespace std;

//-----------------------------------------------------------------------------

struct SedIntegrationFix {

  char* strPath;
  std::string alexandriaPath{};

  SedIntegration*       sed_integration_ptr = nullptr;
  AsciiFilterImporter*  inputFilter         = nullptr;
  AsciiSedImporter*     inputSed            = nullptr;
  InterpolationMethod   interpolationMethod{};
  string                method{};

  FilterTypes           filterType{};


  double       tolerence{};
  double       redshift_step{};
  unsigned int redshift_max{};

  SedIntegrationFix() {

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

    // setup
    interpolationMethod = InterpolationMethod::CUBIC;
    //interpolationMethod = InterpolationMethod::LINEAR;

    // Purpose: Can not use an enum for string concatenation
    if (interpolationMethod == InterpolationMethod::LINEAR)
    {
      method = "LINEAR";
    }
    else
    {
      method = "CUBIC";
    }

    redshift_step = 0.01;
    redshift_max  = 1;
    sed_integration_ptr = new SedIntegration(interpolationMethod, redshift_max, redshift_step);
    inputFilter         = new AsciiFilterImporter();
    inputSed            = new AsciiSedImporter();

    tolerence    = 1e-5;
    filterType   = FilterTypes::EUCLID;

  }
  ~SedIntegrationFix() {
    // teardown
    delete sed_integration_ptr;
    delete inputFilter;
    delete inputSed;
 }

};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (SedIntegration_test)


BOOST_FIXTURE_TEST_CASE( All_SEDs_FILTERs_integration_test, SedIntegrationFix ) {
  /*
   * Here we testing the full integration of the SED throught one filter
   * and computing the magnitude
   */
  const clock_t begin_time = clock();

  BOOST_TEST_MESSAGE("--> Testing the SedIntegration class, all SEDs through all cosmos filters");

  // --- Read FILTER ---

  // Set the filter path
  fs::path filterPath(alexandriaPath);
  filterPath /= "PhotZAuxData";
  filterPath /= "Filter";
  filterPath /= "Cosmos";
  //zzz filterPath /= "Cosmos/"; // Used for only  few filters, filter list below

  // Use list instead zzz
//  vector<string>filter_list = {
//      filterPath.string()+"IA427.res",
//      filterPath.string()+"IA464.res",
//      filterPath.string()+"IA484.res",
//      filterPath.string()+"IA505.res",
//      filterPath.string()+"IA527.res",
//      filterPath.string()+"IA574.res",
//      filterPath.string()+"IA624.res",
//      filterPath.string()+"IA679.res",
//      filterPath.string()+"IA709.res",
//      filterPath.string()+"IA738.res",
//      filterPath.string()+"IA767.res",
//      filterPath.string()+"IA827.res",
//      filterPath.string()+"J_wfcam.res",
//      filterPath.string()+"NB711.pb",
//      filterPath.string()+"NB816.pb",
//      filterPath.string()+"V_subaru.res",
//      filterPath.string()+"f814.pb",
//      filterPath.string()+"flamingos_Ks.res",
//      filterPath.string()+"g_SDSS.res",
//      filterPath.string()+"g_subaru.res",
//      filterPath.string()+"i_SDSS.res",
//      filterPath.string()+"i_cfht.res",
//      filterPath.string()+"i_subaru.res",
//      filterPath.string()+"r_SDSS.res",
//      filterPath.string()+"r_subaru.res",
//      filterPath.string()+"u_SDSS.res",
//      filterPath.string()+"u_cfht.res"
//      filterPath.string()+"wircam_Ks.res",
//      filterPath.string()+"z_SDSS.res",
//      filterPath.string()+"z_subaru.res"
//      };

  // Import filters into the map
  map<FilterNames, Filter> filterMap = inputFilter->importFilters(filterPath.string(), filterType);
  //zzz map<FilterNames, Filter> filterMap = inputFilter->importFilters(filter_list, filterType); // Used only froma filter list

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

  // Filename for outputs, storage of all magnitudes in ascii format as follows
  // Sedname Filtername Magnitude z_step
  string outputFilename = "/tmp/magnitude_all_seds_all_filters_" + method + ".txt";
  stringstream ss;
  ofstream mag_file(outputFilename,ios::out);

  // Write Header
  mag_file<<"#  SED     FILTER          Magnitude     z_step"<<"\n";

  for (auto it_sed : sedMap )
  {

    Sed sed = it_sed.second;
    cout <<""<<endl;

    // Loop on ALL filters
    for (auto it_filter : filterMap )
    {
      Filter filter = it_filter.second;

      // Integration of one SED through one filter
      vector<double> allFlux = sed_integration_ptr->computeFlux(filter, sed);

      vector<double> magVector = sed_integration_ptr->computeMagnitude(allFlux);

      double redshift = 0.0;

      for (unsigned int mag = 0; mag < magVector.size(); ++mag)
      {
        cout << "Sedname:    " << setw(10) << setiosflags(ios::left) << sed.getSedName()
             <<" Filtername: " << setw(20) << setiosflags(ios::left) << filter.getFilterName()
             <<" Magnitude:  " << setw(20) << setiosflags(ios::left) << setprecision(15) << magVector[mag]
             <<" z_step:     " << setw(20) << setiosflags(ios::left) << setprecision(2) << fixed<< redshift<<endl;

        if ( !mag_file )
        {
            std::cerr<<"Cannot open the output file."<<std::endl;
            break;
        }  // Loop on ALL SEDs
        else
        {
          // Store in file
          mag_file<< setw(10) << setiosflags(ios::left) << sed.getSedName()
                  << setw(20) <<setiosflags(ios::left) <<it_filter.first
                  << setw(20) <<setprecision(15) << magVector[mag]
                  << setw(20) <<setiosflags(ios::left) <<setprecision(2) << fixed<< redshift<<"\n" ;
        }// eof if

        redshift += redshift_step;

      }// eof for magfile

    } //eof for filter

  } // eof for SED

  mag_file.close();

  // time elapsed in seconds
  BOOST_TEST_MESSAGE(" ");
  cout<< "Elapsed time: "<<float( clock () - begin_time ) /  CLOCKS_PER_SEC<<" seconds"<<endl;
  BOOST_TEST_MESSAGE(" ");

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("----> Result is stored into: " << outputFilename);
  BOOST_TEST_MESSAGE(" ");


//  BOOST_CHECK_CLOSE(expected_result, result, tolerence);
}


BOOST_AUTO_TEST_SUITE_END ()


