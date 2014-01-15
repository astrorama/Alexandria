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
          param::PhzParameterFactory::createFixedStepParameter("Z", 0., 1., 0.1),
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
//                         ProduceFluxMatrix_test
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( ProduceFluxMatrix_test, FluxModelingFix ) {

  begin_time = clock();

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Produce a flux Matrix and store it to binary file");
  BOOST_TEST_MESSAGE(" ");

  ProtoZ::matrix::FluxMatrix fm = fModeling_ptr->computeFluxMatrix();

  BOOST_TEST_MESSAGE("Writing the matrix to disk...");

  // Write the matrix to binary file
  fm.writeInFile(alexandriaPath+"/ProtoZ/tests/data/FluxMatrix.dat");
  //fm.exportAsAscii("/Users/admin/tmp/FluxMatrix_acsii.dat");

  BOOST_TEST_MESSAGE("Reading the matrix...");

  // time elapsed in seconds
  BOOST_TEST_MESSAGE(" ");
  cout<< "Elapsed time: "<<float( clock () - begin_time ) /  CLOCKS_PER_SEC<<" seconds"<<endl;
  BOOST_TEST_MESSAGE(" ");

}

BOOST_AUTO_TEST_SUITE_END ()





