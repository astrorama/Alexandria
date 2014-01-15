/*
 * MagnitudeCalculation_test.cpp
 *
 *  Created on: Jun 17, 2013
 *      Author: admin
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
  AsciiFilterImporter*  inputFilter, inputAllFilters;
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
//                       Linear_Interpolation_Test
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( Linear_Interpolation_Test, MagnitudeCalculationFix ) {

  BOOST_TEST_MESSAGE("--> Testing linearInterpolation function");

  Point  firstPoint(2, 1);
  Point  secondPoint(4, 3);

  double abscissa        = 3;
  double expected_result = 2;

  double result = magnitudeCalculation->linearInterpolation(firstPoint, secondPoint, abscissa);

  BOOST_TEST_CHECKPOINT("result : "<< result);

  BOOST_CHECK_CLOSE(expected_result, result, tolerence);

}


//-----------------------------------------------------------------------------
//                    Convolution_Integration_Test
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( Convolution_Integration_Test, MagnitudeCalculationFix ) {

  BOOST_TEST_MESSAGE("--> Testing convolution function");

  double smax            = 4.;
  double smin            = 5.;
  double fmax            = 2.;
  double fmin            = 3.;
  double deltaLambda     = 1.;
  double lambda_mean     = 1.5;

  double expected_flux_result   = 11.25;
  double expected_filter_result = 3.33103e+18;

  pair<double, double> result{};
  result = magnitudeCalculation->convolutionIntegration(fmin,
                                                        fmax,
                                                        smin,
                                                        smax,
                                                        lambda_mean,
                                                        deltaLambda);

  //BOOST_TEST_CHECKPOINT("flux result : " << result.first);
  //BOOST_TEST_CHECKPOINT("flux result : " << result.first);

  BOOST_CHECK_CLOSE(expected_flux_result, result.first, tolerence);

  tolerence = 0.00001e+18;
  BOOST_CHECK_CLOSE(expected_filter_result, result.second, tolerence);

}

//-----------------------------------------------------------------------------
//                    getSedSubsetPoints_test
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( getSedSubsetPoints_test, MagnitudeCalculationFix ) {

  BOOST_TEST_MESSAGE("--> Testing getSedSubsetPoints function");

  Point pointWavelength      = Point(3, 2);
  Point pointWavelength_next = Point(5, 3);

  vector<Point> sedPointsOutput{};
  vector<Point> filterPointsOutput{};

  vector<double> waveLengths { 1, 2, 4, 6, 7 };
  vector<double> sedValues { 1, 3, 4, 4, 3 };

  ChDataModel::Sed sedVector{};

  sedVector = Sed(waveLengths, sedValues, SedNames::None);

  vector<Point> expectedSed{};
  Point sed_p1(3,4), sed_p2(4,4), sed_p3(5,4);
  expectedSed = { sed_p1, sed_p2, sed_p3 };

  vector<Point> expectedFilter{};
  Point filter_p1(3,2), filter_p2(4,2.5), filter_p3(5,3);
  expectedFilter = { filter_p1, filter_p2, filter_p3 };

  bool expected_result = true;

  magnitudeCalculation->getSedSubsetPoints(sedVector, pointWavelength, pointWavelength_next, sedPointsOutput, filterPointsOutput);

  //
  // Check the expectedSed vector is identical to sedPoints
  //
  auto it_sed_expected = expectedSed.begin();
  auto it_sed           = sedPointsOutput.begin();

  bool result = false;

  //
  // check the SED vector
  //
  while ( it_sed != sedPointsOutput.end() )
  {

    if ( *it_sed != *it_sed_expected)
    {
       cout << "SED result is not the expected value, see below!"<< endl;
       it_sed->print();
       it_sed_expected->print();
       cout << "----------------------------------------------------"<< endl;
       result = false;
       break;
    }

    result = true;
    ++it_sed;
    ++it_sed_expected;

  } // eof while

  //
  // check the filter vector
  //

  auto it_filter_expected = expectedFilter.begin();
  auto it_filter          = filterPointsOutput.begin();

  while ( it_filter != filterPointsOutput.end() )
  {

    if ( *it_filter != *it_filter_expected)
    {
       cout << "FILTER result is not the expected value, see below!"<< endl;
       it_filter->print();
       it_filter_expected->print();
       cout << "----------------------------------------------------"<< endl;
       result = false;
       break;
    }

    result = true;
    ++it_filter;
    ++it_filter_expected;

  } // eof while


  BOOST_CHECK_EQUAL(expected_result, result);

}

//-----------------------------------------------------------------------------
//                       subsetIntegration_test
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( subsetIntegration_test, MagnitudeCalculationFix ) {


  BOOST_TEST_MESSAGE("--> Testing subsetIntegration function");

  vector<Point> sedPointsVector;
  vector<Point> filterPointsvector;

  Point psed0(0,1), psed1(1,4), psed2(2,5), psed3(3,4), psed4(4,2);
  Point pfilter0(0,0), pfilter1(1,1), pfilter2(2,2), pfilter3(3,2), pfilter4(4,0);

  sedPointsVector    = { psed0, psed1, psed2, psed3, psed4 };
  filterPointsvector = { pfilter0, pfilter1, pfilter2, pfilter3, pfilter4 };

  double expected_flux_result   = 20;
  double expected_filter_result = 9.19853e+18;

  pair<double,double> result;
  result = magnitudeCalculation->subsetIntegration(sedPointsVector, filterPointsvector);

  BOOST_CHECK_CLOSE(expected_flux_result, result.first, tolerence);

  tolerence = 0.00001e+18;
  BOOST_CHECK_CLOSE(expected_filter_result, result.second, tolerence);

}

//-----------------------------------------------------------------------------
//                       brokenLineIntegration_test
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( brokenLineIntegration_test, MagnitudeCalculationFix ) {

  BOOST_TEST_MESSAGE("--> Testing brokenLineIntegration function");

  tolerence = 0.0001; // New value otherwise BOOST_CHECK_CLOSE crashed

  vector<double> waveLengthsSed { 0., 1.5, 4., 5.5, 8.,   9. };
  vector<double> sedValues      { 0., 2., 3., 3., 2., 0.5 };

  vector<double> waveLengthsFilter { 1., 3., 5., 7. };
  vector<double> efficiencyValues  { 1., 3., 4., 1. };

  ChDataModel::Sed sedVector{};
  ChDataModel::Filter filterVector{};

  sedVector = Sed(waveLengthsSed, sedValues, SedNames::None);
  filterVector = Filter(waveLengthsFilter, efficiencyValues, filterType, FilterNames::None);

  double expected_flux_result   = 43.1979;
  double expected_filter_result = 4.9901e+18;

  pair<double,double> result;

  result = magnitudeCalculation->brokenLineIntegration(sedVector, filterVector);

  BOOST_CHECK_CLOSE(expected_flux_result, result.first, tolerence);

  tolerence = 0.00001e+18;
  BOOST_CHECK_CLOSE(expected_filter_result, result.second, tolerence);

}

//
//-----------------------------------------------------------------------------
//                       MagnitudeWithImporter_test
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( MagnitudeUsingAsciiImporter_test, MagnitudeCalculationFix ) {

  BOOST_TEST_MESSAGE("--> Testing Magnitude class using AsciiImporter loading) "
                     " only the <u_cfhtl.res> FILTER and only the <Ell1_A_0.sed> SED");

  // --- Read FILTER ---

  // Set the filter path
  fs::path filterPath(alexandriaPath);
  filterPath /= "PhotZAuxData";
  filterPath /= "Filter";
  filterPath /= "Cosmos";

  // Set filter filename
  fs::path filterFileName(filterPath);
  filterFileName /= "u_cfht.res";

  FilterTypes filterType = FilterTypes::EUCLID;

  // Import filters into the map
  map<FilterNames, Filter> filterMap = inputFilter->importFilters(filterFileName.string(), filterType);

  Filter filter = filterMap[FilterNames::u_CFHT];

  BOOST_TEST_MESSAGE("----> FILTER loaded");

  // --- Read SED ---

  // Get the SED path
  fs::path sedPath(alexandriaPath);
  sedPath /= "PhotZAuxData";
  sedPath /= "Sed";
  sedPath /= "Cosmos";

  // Set SED path+filename
  fs::path sedFileName(sedPath);
  sedFileName /= "Ell1_A_0.sed";

  // Import SEDs into the map
  map<SedNames, Sed> sedMap = inputSed->importSeds(sedFileName.string());

    Sed sed = sedMap[SedNames::Ell1_A_0];

  BOOST_TEST_MESSAGE("----> SED loaded");

  double expected_flux_result   = 1.35194;
  double expected_filter_result = 6.69709e+13;

  pair<double,double> result;

  result = magnitudeCalculation->brokenLineIntegration(sed, filter);

  tolerence = 0.0001;
  BOOST_CHECK_CLOSE(expected_flux_result, result.first, tolerence);

  tolerence = 0.00001e+13;
  BOOST_CHECK_CLOSE(expected_filter_result, result.second, tolerence);

}

//-----------------------------------------------------------------------------
//                       Magnitude_test
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( Magnitude_test, MagnitudeCalculationFix ) {

  BOOST_TEST_MESSAGE("--> Testing Magnitude function ");

  double flux_integration   = 1.35194;
  double filter_integration = 6.69709e+13;

  double result = magnitudeCalculation->computeMagnitude(flux_integration, filter_integration);

  double expected_result = -14.3627; // Magnitude AB at z=0

  tolerence = 0.001;
  BOOST_CHECK_CLOSE(expected_result, result, tolerence);

}


//____________________________________________________________________________//
BOOST_AUTO_TEST_SUITE_END ()



