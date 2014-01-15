/**
 * @file Filter_test.cpp
 *
 * Created on: May 27, 2013
 *     Author: Pavel Binko
 */

#include <boost/test/unit_test.hpp>
#include <iostream>
#include <vector>
#include "ChDataModel/Filter.h"
#include "ChDataModel/Enumerations/FilterNames.h"

using namespace ChDataModel;
using namespace std;

//-----------------------------------------------------------------------------

struct FilterFixture {

  const FilterTypes expectedFilterType = FilterTypes::EUCLID;
  const FilterNames expectedName = FilterNames::g_Subaru;
  std::vector<double> waveLengths;
  std::vector<double> filterValues;

  Filter * filterPtr = nullptr;

  FilterFixture() {
//    cout << "setup" << endl;

    // Filling x vector
    waveLengths.push_back(3560.0);
    waveLengths.push_back(3563.0);
    waveLengths.push_back(3665.0);
    waveLengths.push_back(4000.0);

    // Filling y vector
    filterValues.push_back(0.465);
    filterValues.push_back(0.576);
    filterValues.push_back(0.7868);
    filterValues.push_back(0.231);

    // Create the filter
    filterPtr = new Filter(waveLengths, filterValues, expectedFilterType,
        expectedName);
  }

  FilterFixture(const FilterFixture&) = delete;

  ~FilterFixture() {
//    cout << "teardown" << endl;
    delete filterPtr;
  }

};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Filter_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( constructors_test, FilterFixture ) {
  BOOST_CHECK(filterPtr);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( getter_test, FilterFixture ) {

  double tolerence = 1e-6;

  for (size_t i = 0; i < waveLengths.size(); ++i) {
    BOOST_CHECK_CLOSE(waveLengths.at(i), filterPtr->getWaveLength(i),
        tolerence);
    BOOST_CHECK_CLOSE(filterValues.at(i), filterPtr->getEfficiencyValue(i),
        tolerence);
  }
  BOOST_CHECK_EQUAL(expectedFilterType, filterPtr->getFilterType());
  BOOST_CHECK_EQUAL(expectedName, filterPtr->getFilterName());

}
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( getter_axis_test, FilterFixture ) {

  double tolerence = 1e-6;

  std::vector<double> my_waveLengths  = filterPtr->getWaveLengths();
  std::vector<double> my_filterValues = filterPtr->getEfficiencyValues();

  for (size_t i = 0; i < waveLengths.size(); ++i) {
    BOOST_CHECK_CLOSE(waveLengths.at(i), my_waveLengths.at(i), tolerence);
    BOOST_CHECK_CLOSE(filterValues.at(i), my_filterValues.at(i), tolerence);
  }

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()

