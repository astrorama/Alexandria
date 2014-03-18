/**
 * FluxModeling_test.cpp
 *
 *  Created on: Dec 3, 2013
 *      Author : Nicolas Morisset
 */

#include <iostream>
#include <cmath>
#include <map>
#include <iomanip>
#include <vector>
#include <boost/test/unit_test.hpp>
#include <boost/filesystem/path.hpp>


#include "ChDataModel/Enumerations/FilterTypes.h"
#include "ProtoZ/FluxModeling.h"
#include "ProtoZ/parameter/FluxModelingParameters.h"

namespace param = ProtoZ::parameter;

namespace fs = boost::filesystem;

using namespace std;
namespace matrix = ProtoZ::matrix;

//-----------------------------------------------------------------------------

struct FluxModelingFix {

  char*       strPath;
  std::string alexandriaPath{};
  bool        test_result{};
  double      tolerence{};
  clock_t     begin_time{};
  string      interpolationMethodChosen{};


  FluxModeling*         fModeling_ptr = nullptr;
  InterpolationMethod   interpolationMethod{};
  string                method{};

  FluxModelingFix() {

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

    test_result = true;
    tolerence   = 0.0001;
    interpolationMethodChosen = "CUBIC";

    param::FluxModelingParameters* tmpPtr = new
    param::FluxModelingParameters {
          param::PhzParameterFactory::createFixedStepParameter("Z", 0., .1, 0.1),
          param::PhzParameterFactory::createFixedStepParameter("E(B-V)", 0., 1., 0.1),
          param::PhzParameterFactory::createSedParameterFromPath(alexandriaPath+"/PhotZAuxData/Sed/Cosmos"),
          param::PhzParameterFactory::createFilterParameterFromPath(alexandriaPath+"/PhotZAuxData/Filter/Cosmos", ChDataModel::FilterTypes::EUCLID),
          param::PhzParameterFactory::createExtLawParameterFromPath(alexandriaPath+"/PhotZAuxData/ExtLaw"),
          10.,
          interpolationMethodChosen};



    fModeling_ptr = new FluxModeling(tmpPtr);

  }
  ~FluxModelingFix() {
    // teardown
    delete fModeling_ptr;
 }

};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (FluxModeling_test)

//-----------------------------------------------------------------------------
//                       getInterpolationMethod_test
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( getInterpolationMethod_test, FluxModelingFix ) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the getInterpolationMethod function");
  BOOST_TEST_MESSAGE(" ");

  std::string result = fModeling_ptr->getInterpolationMethod();

  BOOST_CHECK_EQUAL(result, interpolationMethodChosen);

}


//-----------------------------------------------------------------------------
//                       applyRedshift_test
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( applyRedshift_test, FluxModelingFix ) {

  begin_time = clock();

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the applyRedshift function");
  BOOST_TEST_MESSAGE(" ");

  vector<double> wavelength     = {0., 0.1, 0.25, 0.3, 0.45, 0.5};
  vector<double> expectedResult = {0., 0.12, 0.3, 0.36, 0.54, 0.6};

  double z = 0.2;

  vector<double> result = fModeling_ptr->applyRedshift(z, wavelength);

  test_result = true;

  // Check result
  for (uint32_t i=0; i< result.size(); ++i) {
    if (result[i] != expectedResult[i]) {
      test_result = false;
      break;
    }

  }

 BOOST_CHECK_EQUAL(test_result, true);


  // time elapsed in seconds
  BOOST_TEST_MESSAGE(" ");
  cout<< "Elapsed time: "<<float( clock () - begin_time ) /  CLOCKS_PER_SEC<<" seconds"<<endl;
  BOOST_TEST_MESSAGE(" ");
}

//-----------------------------------------------------------------------------
//                         applyExtinctionLaw_test
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( applyExtinctionLaw_test, FluxModelingFix ) {

  begin_time = clock();

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the applyExtinctionLaw function");
  BOOST_TEST_MESSAGE(" ");

  vector<double> wavelength     = {0., 1., 2., 3., 4., 5.};
  vector<double> intensity      = {0., 1, 2, 3, 4, 5};
  vector<double> kExtension     = {0 ,2. , 3., 4., 5., 6.};
  double         ebmv           = 1;

  vector<double> result = fModeling_ptr->applyExtinctionLaw( wavelength,
                                                             intensity,
                                                             wavelength,
                                                             kExtension,
                                                             ebmv);

  vector<double> expected_result = {0, 0.1584893, 0.1261914, 0.07535659, 0.04, 0.01990535};

  BOOST_CHECK_CLOSE(result[0], expected_result[0], tolerence);
  BOOST_CHECK_CLOSE(result[1], expected_result[1], tolerence);
  BOOST_CHECK_CLOSE(result[2], expected_result[2], tolerence);
  BOOST_CHECK_CLOSE(result[3], expected_result[3], tolerence);
  BOOST_CHECK_CLOSE(result[4], expected_result[4], tolerence);
  BOOST_CHECK_CLOSE(result[5], expected_result[5], tolerence);


  // time elapsed in seconds
  BOOST_TEST_MESSAGE(" ");
  cout<< "Elapsed time: "<<float( clock () - begin_time ) /  CLOCKS_PER_SEC<<" seconds"<<endl;
  BOOST_TEST_MESSAGE(" ");
}

//-----------------------------------------------------------------------------
//                      simpsonCubicIntegration_test
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( simpsonCubicIntegration_test, FluxModelingFix ) {

  begin_time = clock();

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the simpsonCubicIntegration function");
  BOOST_TEST_MESSAGE(" ");

  vector<double>  values = {0., 10., 20., 30., 40., 50., 60.};
  double          step   = 10.;

  double result = fModeling_ptr->simpsonCubicIntegration(step, values);

  double expected_result = 1800;

  BOOST_CHECK_EQUAL(result, expected_result);

  // time elapsed in seconds
  BOOST_TEST_MESSAGE(" ");
  cout<< "Elapsed time: "<<float( clock () - begin_time ) /  CLOCKS_PER_SEC<<" seconds"<<endl;
  BOOST_TEST_MESSAGE(" ");
}

//-----------------------------------------------------------------------------
//                         resample_test
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( resample_test, FluxModelingFix ) {

  begin_time = clock();

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the resample function");
  BOOST_TEST_MESSAGE(" ");

  vector<double> wavelengths    = {5., 10., 20., 30., 40., 50., 60.};
  vector<double> efficiencies   = {0.1 , 1 , 1.5, 2, 1.2, 0.8, 0.5};

  unique_ptr<VectorPair> ptr = fModeling_ptr->resample(wavelengths, efficiencies);

  vector<double> resampled_wavelengths  = ptr->getAxisX();
  vector<double> resampled_efficiencies = ptr->getAxisY();

  vector<double> expected_result = {0.1, 1.3530429, 1.82533, 1.6831436, 0.929597, 0.660968, 0.};

  BOOST_CHECK_EQUAL(15, resampled_wavelengths[1]);
  BOOST_CHECK_EQUAL(65, resampled_wavelengths[6]);

  BOOST_CHECK_CLOSE(resampled_efficiencies[0], expected_result[0], tolerence);
  BOOST_CHECK_CLOSE(resampled_efficiencies[2], expected_result[2], tolerence);
  BOOST_CHECK_CLOSE(resampled_efficiencies[4], expected_result[4], tolerence);
  BOOST_CHECK_CLOSE(resampled_efficiencies[6], expected_result[6], tolerence);

  // time elapsed in seconds
  BOOST_TEST_MESSAGE(" ");
  cout<< "Elapsed time: "<<float( clock () - begin_time ) /  CLOCKS_PER_SEC<<" seconds"<<endl;
  BOOST_TEST_MESSAGE(" ");
}

//-----------------------------------------------------------------------------
//                         integrateSed_test
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( integrateSed_test, FluxModelingFix ) {

  begin_time = clock();

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the integrateSed function");
  BOOST_TEST_MESSAGE(" ");

  vector<double> wavelengths    = {10., 20., 30., 40., 50., 60., 70};
  vector<double> efficiencies   = {10, 20, 30, 30, 15, 10, 5};
  vector<double> intensities    = {5, 30, 35, 20, 10, 5, 0};

  VectorPair  filterResampledVPair(wavelengths, efficiencies);
  VectorPair  sedResampledVpair(wavelengths, intensities) ;
  double      filterIntegral       = 1050.;

   double result = fModeling_ptr->integrateSed( filterResampledVPair,
                                                wavelengths,
                                                intensities,
                                                filterIntegral);

  double expected_result = 24.285714016071378;

  BOOST_CHECK_CLOSE(result, expected_result, tolerence);

  // time elapsed in seconds
  BOOST_TEST_MESSAGE(" ");
  cout<< "Elapsed time: "<<float( clock () - begin_time ) /  CLOCKS_PER_SEC<<" seconds"<<endl;
  BOOST_TEST_MESSAGE(" ");
}


BOOST_AUTO_TEST_SUITE_END ()





