/**
 * @file tests/src/Source_test.cpp
 *
 *  Created on: Jan 14, 2013
 *      Author: dubath
 */

#include <boost/test/unit_test.hpp>
#include "ChCatalog/Source.h"
#include "ChCatalog/Attribute.h"
#include "ChCatalog/SourceAttributes/Coordinates.h"
#include "ChCatalog/SourceAttributes/Photometry.h"
#include "ChCatalog/SourceAttributes/SpectroscopicRedshift.h"

#include "ElementsKernel/Exception.h"

#include <iostream>
#include <map>

//-----------------------------------------------------------------------------
// Include the CatalogFixture which include a photometry mock object we use here for the test
#include "tests/src/CatalogFixture.h"


using namespace Euclid::ChCatalog;
using namespace std;




//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Source_test)

BOOST_FIXTURE_TEST_CASE( getAttribute_test, CatalogFixture ) {

   BOOST_TEST_MESSAGE("--> getAttribute test ");

   shared_ptr<Photometry> photometry_ptr(source_1.getAttribute<Photometry>());
//   cout << " Flux  : " << (ptrPhoto->find(expectedFilterName))->flux
//        << " Error : " << (ptrPhoto->find(expectedFilterName))->error
//        << endl;
   BOOST_CHECK_CLOSE(expected_flux_1,(photometry_ptr->find(expected_filter_name_1))->flux, tolerence);
   BOOST_CHECK_CLOSE(expected_error_2,(photometry_ptr->find(expected_filter_name_2))->error, tolerence);

   shared_ptr<Coordinates> coordinate_ptr(source_1.getAttribute<Coordinates>());
//   cout << " Ra  : " << ptrCoord->getRa()
//        << " Dec : " << ptrCoord->getDec()
//        << endl;
   BOOST_CHECK_CLOSE(expected_ra_1, coordinate_ptr->getRa(), tolerence);
   BOOST_CHECK_CLOSE(expected_dec_1,coordinate_ptr->getDec(), tolerence);

   shared_ptr<SpectroscopicRedshift> redshift_ptr(source_1.getAttribute<SpectroscopicRedshift>());
//   cout << " Zvalue : " << ptrRedshift->getValue()
//        << " Error  : " << ptrRedshift->getError()
//        << endl;
   BOOST_CHECK_CLOSE(expected_z_value, redshift_ptr->getValue(), tolerence);
   BOOST_CHECK_CLOSE(expected_z_error, redshift_ptr->getError(), tolerence);

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( getId_test, CatalogFixture ) {

   BOOST_TEST_MESSAGE("--> getId test ");
   int64_t sourceId = source_1.getId();
   BOOST_CHECK_EQUAL(expected_source_id_1, sourceId);

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( missing_attribute_test, CatalogFixture ) {

   BOOST_TEST_MESSAGE("--> missing_attribute test ");
   shared_ptr<Photometry> ptrPhoto(source_2.getAttribute<Photometry>());
   BOOST_CHECK(nullptr == ptrPhoto);

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
