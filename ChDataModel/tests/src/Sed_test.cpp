/**
 * @file Sed_test.cpp
 *
 * Created on: May 27, 2013
 *     Author: Pavel Binko
 */

#include <boost/test/unit_test.hpp>
#include <iostream>
#include <vector>
#include "ChDataModel/Sed.h"

using namespace ChDataModel;
using namespace std;

//-----------------------------------------------------------------------------

struct SedFixture {

  const SedNames expectedSedName = SedNames::Ell1_A_0;
  std::vector<double> waveLengths;
  std::vector<double> sedValues;

  Sed * sedPtr = nullptr;

  SedFixture() {
//    cout << "setup" << endl;
    // filling x vector
    waveLengths.push_back(3560.0);
    waveLengths.push_back(3563.0);
    waveLengths.push_back(3665.0);
    waveLengths.push_back(4000.0);

    // filling y vector
    sedValues.push_back(0.465);
    sedValues.push_back(0.576);
    sedValues.push_back(0.7868);
    sedValues.push_back(0.231);
    sedPtr = new Sed(waveLengths, sedValues, expectedSedName);
  }

  ~SedFixture() {
//    cout << "teardown" << endl;
    delete sedPtr;
  }

  SedFixture(const SedFixture&) = delete;

};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Sed_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( constructors_test, SedFixture ) {

  BOOST_CHECK(sedPtr);

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( getter_test, SedFixture ) {

  double tolerence = 1e-6;

  for (size_t i = 0; i < waveLengths.size(); ++i) {
    BOOST_CHECK_CLOSE(waveLengths.at(i), sedPtr->getWaveLength(i), tolerence);
    BOOST_CHECK_CLOSE(sedValues.at(i), sedPtr->getIntensity(i), tolerence);
  }
  BOOST_CHECK_EQUAL(expectedSedName, sedPtr->getSedName());

}
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( getter_axis_test, SedFixture ) {

  double tolerence = 1e-6;

  std::vector<double> my_waveLengths  = sedPtr->getWaveLengths();
  std::vector<double> my_sedValues    = sedPtr->getIntensities();

  for (size_t i = 0; i < waveLengths.size(); ++i) {
    BOOST_CHECK_CLOSE(waveLengths.at(i), my_waveLengths.at(i), tolerence);
    BOOST_CHECK_CLOSE(sedValues.at(i), my_sedValues.at(i), tolerence);
  }

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()

