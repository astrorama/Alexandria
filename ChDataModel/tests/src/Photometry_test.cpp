/**
 * @file Photometry_test.cpp
 *
 *  Created on: March 1, 2013
 *      Author: dubath
 */
#include <boost/test/unit_test.hpp>
#include <iostream>
#include "ChDataModel/Source.h"
#include "ChDataModel/Photometry.h"
#include "ChDataModel/Enumerations/FilterNames.h"

using namespace ChDataModel;
using namespace std;

//-----------------------------------------------------------------------------

struct PhotometryFixture {

  Source* sourcePtr;
  Photometry * photometryPtr;
  Photometry * photometryPtr_2;

  const FilterNames expectedFilterName = FilterNames::V_Subaru;
  const PhotometryTypes expectedPhotometryType = PhotometryTypes::AB_MAGNITUDE;
  const double expectedValue = 12.4657;
  const double expectedError = 0.01534;

  PhotometryFixture() {
//    cout << "setup" << endl;
    sourcePtr = new Source();
    photometryPtr = new Photometry(expectedFilterName, expectedPhotometryType,
        expectedValue, expectedError);
    photometryPtr_2 = new Photometry(sourcePtr, expectedFilterName,
        expectedPhotometryType, expectedValue, expectedError);
  }

  ~PhotometryFixture() {
//    cout << "teardown" << endl;
    delete sourcePtr;
    delete photometryPtr;
    delete photometryPtr_2;
  }

  PhotometryFixture(const PhotometryFixture&) = delete;

};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Photometry_test)

// BOOST_GLOBAL_FIXTURE(PV); // this does not work as test case do not have access to PV members!?!?

///BOOST_AUTO_TEST_CASE( constructors_test ) {

//-----------------------------------------------------------------------------

//BOOST_FIXTURE_TEST_CASE( constructors_test, PhotometryFixture ) {
//
//  Photometry* photValueConstructorTest = nullptr;
//  Photometry* photValueDefaultConstructorTest = nullptr;
//  BOOST_CHECK(nullptr == photValueConstructorTest);
//  photValueConstructorTest = new Photometry(expectedFilterName,
//      expectedPhotometryType, expectedValue, expectedError);
//  BOOST_CHECK(photValueConstructorTest);
//  photValueDefaultConstructorTest = new Photometry();
//  FilterNames expectedName = FilterNames::None;
//  BOOST_CHECK(photValueDefaultConstructorTest->getFilterName() == expectedName);
//  delete photValueConstructorTest;
//  delete photValueDefaultConstructorTest;
//}
//
////-----------------------------------------------------------------------------
//
//BOOST_FIXTURE_TEST_CASE( getters_test, PhotometryFixture ) {
//  //
//  FilterNames actualName = photometryPtr->getFilterName();
//  BOOST_CHECK(actualName == expectedFilterName);
//  PhotometryTypes actualType = photometryPtr->getPhotometryType();
//  BOOST_CHECK(actualType == expectedPhotometryType);
//  double tolerence = 0.00001;
//  double actualValue = photometryPtr->getValue();
//  BOOST_CHECK_CLOSE(actualValue, expectedValue, tolerence);
//  double actualError = photometryPtr->getValueError();
//  BOOST_CHECK_CLOSE(actualError, expectedError, tolerence);
//}
//
////-----------------------------------------------------------------------------
//
//BOOST_FIXTURE_TEST_CASE( get_magnitude_test, PhotometryFixture ) {
//  //
//  double tolerence = 0.00001;
//  double actualValue = photometryPtr->getAbMagnitude();
//  BOOST_CHECK_CLOSE(actualValue, expectedValue, tolerence);
//}
//
////-----------------------------------------------------------------------------
//
//BOOST_FIXTURE_TEST_CASE( get_source_back_ptr_test, PhotometryFixture ) {
//  //
//  Source * actualSourcePtr = photometryPtr->getSourcePtr();
//  BOOST_CHECK(actualSourcePtr == nullptr);
//  photometryPtr->setSourcePtr(sourcePtr);
//  // test of the setSourcePtr
//  actualSourcePtr = photometryPtr->getSourcePtr();
//  BOOST_CHECK_EQUAL(actualSourcePtr, sourcePtr);
//  // Test of the constructor which initialized sourcePtr
//  actualSourcePtr = photometryPtr_2->getSourcePtr();
//  BOOST_CHECK_EQUAL(actualSourcePtr, sourcePtr);
//}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
