/**
 * @file Source_test.cpp
 *
 *  Created on: Jan 14, 2013
 *      Author: dubath
 */

#include <boost/test/unit_test.hpp>
#include "ChDataModel/Source.h"
// #include "ChDataModel/Photometry.h"
#include "ChDataModel/Attribute.h"
#include "ChDataModel/AttributeName.h"
#include "ChDataModel/SourceAttributes/Coordinates.h"
#include "ChDataModel/SourceAttributes/PhotometryMap.h"
#include "ChDataModel/SourceAttributes/SpectroscopicRedshift.h"

#include "ElementsKernel/ElementsException.h"

#include <iostream>
#include <map>
#include "ChDataModel/Catalog.h"

using namespace ChDataModel;
using namespace std;

//-----------------------------------------------------------------------------

typedef Source* SourcePtr;
typedef Catalog * CatalogPtr;

struct SourceFix {

  int64_t expectedSourceId = 1273684;

  double expectedRa = 181.4657;
  double expectedDec = -36.27363;
  Coordinates coordinate {expectedRa, expectedDec};


//  Photometry photometry_1 = Photometry("V_Subaru", 0.026354, 0.000534);
//  Photometry photometry_2 = Photometry("u_CFHT", 0.5642, 0.001324);

//  map<>

  SourceFix() {
    // setup
  }
  ~SourceFix() {
    // teardown
  }

  SourceFix(const SourceFix&) = delete ;

};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Source_test)

BOOST_AUTO_TEST_CASE( fake_test ) {
  BOOST_CHECK(true);
}

// BOOST_GLOBAL_FIXTURE(PV); // this does not work as test case do not have access to PV members!?!?

// BOOST_AUTO_TEST_CASE( constructors_test ) { // this is a test case that do not depend on fixture

//-----------------------------------------------------------------------------

//BOOST_FIXTURE_TEST_CASE( constructors_test, SourceFix ) {
//  Source* sourceConstructorTest = nullptr;
//  BOOST_CHECK(nullptr == sourceConstructorTest);
//  sourceConstructorTest = new Source(expectedSourceId, expectedRa, expectedDec);
//  BOOST_CHECK(sourceConstructorTest);
//  delete sourceConstructorTest;
//
//}
//
////-----------------------------------------------------------------------------
//
//BOOST_FIXTURE_TEST_CASE( getters_test, SourceFix ) {
//  //
//  int64_t actualSourceId = source_ptr->getSourceId();
//  BOOST_CHECK_EQUAL(actualSourceId, expectedSourceId);
//  double tolerence = 0.00001;
//  double actualRa = source_ptr->getRa();
//  BOOST_CHECK_CLOSE( actualRa, expectedRa, tolerence);
//  double actualDec = source_ptr->getDec();
//  BOOST_CHECK_CLOSE( actualDec, expectedDec, tolerence);
//}
//
////-----------------------------------------------------------------------------
//
//BOOST_FIXTURE_TEST_CASE( getPhotometry_test, SourceFix ) {
//  Photometry photometry = source_ptr->getPhotometry(FilterNames::V_Subaru);
//  BOOST_CHECK_EQUAL(photometry.getSourcePtr()->getSourceId(), expectedSourceId);
//  BOOST_CHECK_EQUAL(photometry.getAbMagnitude(), 13.6452);
//  BOOST_CHECK_EQUAL(photometry.getValue(), 13.6452);
//  BOOST_CHECK_EQUAL(photometry.getValueError(), 0.002534);
//  BOOST_CHECK(photometry.getFilterName() == FilterNames::V_Subaru);
//  BOOST_CHECK(photometry.getPhotometryType() == PhotometryTypes::AB_MAGNITUDE);
//}
//
////-----------------------------------------------------------------------------
//
//BOOST_FIXTURE_TEST_CASE( getPhotometry_test_2, SourceFix ) {
//  Photometry photometry = source_ptr->getPhotometry(FilterNames::u_CFHT);
//  BOOST_CHECK_EQUAL(photometry.getSourcePtr()->getSourceId(), expectedSourceId);
//  BOOST_CHECK_EQUAL(photometry.getValue(), 11.5452);
//}
//
////-----------------------------------------------------------------------------
//
//BOOST_FIXTURE_TEST_CASE( catalog_back_pointer_test, SourceFix ) {
//  BOOST_CHECK(source_ptr->getCatalogPtr() == nullptr);
//  Source insertedSource = catalog_ptr->addSource(*source_ptr);
//  CatalogPtr actual_catalog_ptr = insertedSource.getCatalogPtr();
//  BOOST_CHECK_EQUAL(actual_catalog_ptr, catalog_ptr);
//
//  Source insertedSource2 = catalog_ptr->addSource(*source_ptr_2);
//  actual_catalog_ptr = insertedSource2.getCatalogPtr();
//  BOOST_CHECK_EQUAL(actual_catalog_ptr, catalog_ptr);
//}
//
////-----------------------------------------------------------------------------
//
//BOOST_FIXTURE_TEST_CASE( source_back_pointer_test, SourceFix ) {
//  //
//  Photometry photometry_3 = Photometry(FilterNames::g_Subaru,
//        PhotometryTypes::AB_MAGNITUDE, 10.5452, 0.006324);
// Photometry photom =
//    source_ptr->addPhotometry(photometry_3);
//  BOOST_CHECK_EQUAL(photom.getSourcePtr(), source_ptr);
//}
//
////-----------------------------------------------------------------------------
//
//BOOST_FIXTURE_TEST_CASE( addPhotometry_exception_test, SourceFix ) {
//  //
//  bool exception = false;
//  try {
//    source_ptr->addPhotometry(photometry_1);
//  } catch (const ElementsException & e) {
//    //exception = true;
//    string exception_str = e.what();
//    exception =
//        (exception_str.find(
//            "Source::addPhotometry : Photometry")
//            != string::npos);
//  }
//  BOOST_CHECK(exception);
//}
//
////-----------------------------------------------------------------------------
//
//BOOST_FIXTURE_TEST_CASE( getPhotometry_exception_test, SourceFix ) {
//  //
//  bool exception = false;
//  try {
//    Photometry photometry = source_ptr->getPhotometry(FilterNames::B_Subaru);
//  } catch (const ElementsException & e) {
//    string exception_str = e.what();
//    exception =
//        (exception_str.find("Source::getPhotometry : ") != string::npos);
//  }
//  BOOST_CHECK(exception);
//}
//
////-----------------------------------------------------------------------------
//
//BOOST_FIXTURE_TEST_CASE( add_and_getPhotometricAttribute_test, SourceFix ) {
//  source_ptr->addPhotometricAttribute(expected_photometric_parameter_names_1,
//      expected_photometric_parameter_value_1);
//  source_ptr->addPhotometricAttribute(expected_photometric_parameter_names_2,
//      expected_photometric_parameter_value_2);
//  double tolerence = 0.00001;
//  double actual_photometric_parameter_value_1 =
//      source_ptr->getPhotometricAttribute(
//          expected_photometric_parameter_names_1);
//  BOOST_CHECK_CLOSE( actual_photometric_parameter_value_1,
//      expected_photometric_parameter_value_1, tolerence);
//  double actual_photometric_parameter_value_2 =
//      source_ptr->getPhotometricAttribute(
//          expected_photometric_parameter_names_2);
//  BOOST_CHECK_CLOSE( actual_photometric_parameter_value_2,
//      expected_photometric_parameter_value_2, tolerence);
//}
//
////-----------------------------------------------------------------------------
//
//BOOST_FIXTURE_TEST_CASE( addPhotometricAttribute_exception_test, SourceFix ) {
//  bool exception = false;
//  try {
//    source_ptr->addPhotometricAttribute(expected_photometric_parameter_names_1,
//        expected_photometric_parameter_value_1);
//    source_ptr->addPhotometricAttribute(expected_photometric_parameter_names_1,
//        expected_photometric_parameter_value_1);
//  } catch (const ElementsException & e) {
//    string exception_str = e.what();
//    exception =
//        (exception_str.find("Source::addPhotometricAttribute : a") != string::npos);
//  }
//  BOOST_CHECK(exception);
//}
//
////-----------------------------------------------------------------------------
//
//BOOST_FIXTURE_TEST_CASE( getPhotometricAttribute_exception_test, SourceFix ) {
//  bool exception = false;
//  try {
//    source_ptr->getPhotometricAttribute(expected_photometric_parameter_names_3);
//  } catch (const ElementsException & e) {
//    string exception_str = e.what();
//    exception =
//        (exception_str.find("Source::getPhotometricAttribute :") != string::npos);
//  }
//  BOOST_CHECK(exception);
//}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
