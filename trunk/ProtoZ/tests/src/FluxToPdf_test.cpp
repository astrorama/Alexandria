/**
 * @file FluxToPdf_test.cpp
 *
 * Created on: Dec 13, 2013
 *     Author: Pierre Dubath
 */
#include "ProtoZ/FluxToPdf.h"

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
#include "ProtoZ/matrix/FluxMatrix.h"

namespace parameter = ProtoZ::parameter;
namespace matrix = ProtoZ::matrix;
namespace fs = boost::filesystem;

using namespace std;

//-----------------------------------------------------------------------------

struct FluxToPdfFix {

  char*       strPath;
  std::string alexandriaPath{};
  bool        test_result{};
  double      tolerence{};
  clock_t     begin_time{};
  string      interpolationMethodChosen{};

  matrix::FluxMatrix* flux_matrix {};

  FluxToPdfFix() {

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

    const param::FluxModelingParameters tmpPtr  {
          param::PhzParameterFactory::createFixedStepParameter("Z", 0., 2., 0.1),
          param::PhzParameterFactory::createFixedStepParameter("E(B-V)", 0., 1., 0.1),
          param::PhzParameterFactory::createSedParameterFromPath(alexandriaPath+"/PhotZAuxData/Sed/Cosmos"),
          param::PhzParameterFactory::createFilterParameterFromPath(alexandriaPath+"/PhotZAuxData/Filter/Cosmos", ChDataModel::FilterTypes::EUCLID),
          param::PhzParameterFactory::createExtLawParameterFromPath(alexandriaPath+"/PhotZAuxData/ExtLaw"), 10., interpolationMethodChosen
    };

    //matrix::FluxMatrix matrixFromParams {fmp};
    flux_matrix = new matrix::FluxMatrix(tmpPtr);

  }
  ~FluxToPdfFix() {
    // teardown
    delete flux_matrix;
 }

};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (FluxToPdf_test)

//-----------------------------------------------------------------------------
//                       getInterpolationMethod_test
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( getInterpolationMethod_test, FluxToPdfFix ) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the getInterpolationMethod function");
  BOOST_TEST_MESSAGE(" ");

  cout << "Everything is fine" << endl;

  //BOOST_CHECK_EQUAL(result, interpolationMethodChosen);

}

BOOST_AUTO_TEST_SUITE_END ()
