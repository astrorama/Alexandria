/*
 * Copyright (C) 2012-2020 Euclid Science Ground Segment
 *
 * This library is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free
 * Software Foundation; either version 3.0 of the License, or (at your option)
 * any later version.
 *
 * This library is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
 * details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this library; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 */

 /**
 * @file tests/src/Source_test.cpp
 *
 *  Created on: Jan 14, 2013
 *      Author: dubath
 */

#include <boost/test/unit_test.hpp>
#include "SourceCatalog/Source.h"
#include "SourceCatalog/Attribute.h"
#include "SourceCatalog/SourceAttributes/Coordinates.h"
#include "SourceCatalog/SourceAttributes/Photometry.h"
#include "SourceCatalog/SourceAttributes/SpectroscopicRedshift.h"

#include "ElementsKernel/Exception.h"

#include <iostream>
#include <map>

//-----------------------------------------------------------------------------
// Include the CatalogFixture which include a photometry mock object we use here for the test
#include "tests/src/CatalogFixture.h"


using namespace Euclid::SourceCatalog;
using namespace std;




//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Source_test)

BOOST_FIXTURE_TEST_CASE( getAttribute_test, CatalogFixture ) {

   BOOST_TEST_MESSAGE("--> getAttribute test ");

   shared_ptr<Photometry> photometry_ptr(source_1.getAttribute<Photometry>());
//   cout << " Flux  : " << (ptrPhoto->find(expectedFilterName))->flux
//        << " Error : " << (ptrPhoto->find(expectedFilterName))->error
//        << endl;
   BOOST_CHECK_CLOSE(expected_flux_1, (photometry_ptr->find(expected_filter_name_1))->flux, tolerance);
   BOOST_CHECK_CLOSE(expected_error_2, (photometry_ptr->find(expected_filter_name_2))->error, tolerance);

   shared_ptr<Coordinates> coordinate_ptr(source_1.getAttribute<Coordinates>());
//   cout << " Ra  : " << ptrCoord->getRa()
//        << " Dec : " << ptrCoord->getDec()
//        << endl;
   BOOST_CHECK_CLOSE(expected_ra_1, coordinate_ptr->getRa(), tolerance);
   BOOST_CHECK_CLOSE(expected_dec_1, coordinate_ptr->getDec(), tolerance);

   shared_ptr<SpectroscopicRedshift> redshift_ptr(source_1.getAttribute<SpectroscopicRedshift>());
//   cout << " Zvalue : " << ptrRedshift->getValue()
//        << " Error  : " << ptrRedshift->getError()
//        << endl;
   BOOST_CHECK_CLOSE(expected_z_value, redshift_ptr->getValue(), tolerance);
   BOOST_CHECK_CLOSE(expected_z_error, redshift_ptr->getError(), tolerance);

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( getId_test, CatalogFixture ) {

   BOOST_TEST_MESSAGE("--> getId test ");
   auto sourceId = source_1.getId();
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
