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
 * @file tests/src/SourceAttributes/Photometry_test.cpp
 *
 * Created on: Jan 20, 2014
 *     Author: Pierre Dubath
 */
#include <boost/test/unit_test.hpp>
#include "SourceCatalog/SourceAttributes/Photometry.h"


//-----------------------------------------------------------------------------
// Include the CatalogFixture which comprises a photometry mock object use here
// as a test reference
#include "tests/src/CatalogFixture.h"

using namespace Euclid::SourceCatalog;

//----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Photometry_test)

BOOST_FIXTURE_TEST_CASE( find_test, CatalogFixture ) {

  BOOST_TEST_MESSAGE("--> find test ");

  std::shared_ptr<FluxErrorPair> ptr1 = photometry.find(expected_filter_name_1);
  std::shared_ptr<FluxErrorPair> ptr2 = photometry.find(expected_filter_name_2);

  BOOST_CHECK_CLOSE(expected_flux_1, ptr1->flux, tolerance);
  BOOST_CHECK_CLOSE(expected_error_1, ptr1->error, tolerance);
  BOOST_CHECK_CLOSE(expected_flux_2, ptr2->flux, tolerance);
  BOOST_CHECK_CLOSE(expected_error_2, ptr2->error, tolerance);
}

BOOST_FIXTURE_TEST_CASE( not_found_test, CatalogFixture ) {

  BOOST_TEST_MESSAGE("--> not found find test! ");

  std::unique_ptr<FluxErrorPair> ptr1 = photometry.find("AnotherFilterGroup/AnotherFilterName");
  BOOST_CHECK(ptr1 == nullptr);
}


BOOST_FIXTURE_TEST_CASE( iterator_test, CatalogFixture ) {

  BOOST_TEST_MESSAGE("--> iterator test ");

  // This is to get the expected filter name from the fixture for comparison
  auto expected_filter_name_iter = filter_name_vector_ptr->begin();
  // This is to get the expected fluxes and errors from the fixture for comparison
  auto expected_photo_iter = photometry_vector.begin();

  BOOST_CHECK_EQUAL(photometry.end() - photometry.begin(), photometry_vector.size());

  // loop over the photometry object to check the different filter names, values and errors
  for (auto photo_iter = photometry.begin(); photo_iter != photometry.end(); ++photo_iter) {
    BOOST_CHECK( photo_iter.filterName() ==  *expected_filter_name_iter );
    ++expected_filter_name_iter;
    BOOST_CHECK_CLOSE((*photo_iter).flux, expected_photo_iter->flux, tolerance);
    BOOST_CHECK_CLOSE((*photo_iter).error, expected_photo_iter->error, tolerance);
    ++expected_photo_iter;
  }

}

// This is how to iterate through the photometry values in most cases
BOOST_FIXTURE_TEST_CASE( iterator_getter_test, CatalogFixture ) {

  BOOST_TEST_MESSAGE("--> iterator getter test ");

  // This is to get the expected fluxes and errors from the fixture for comparison
  auto expected_photo_iter = photometry_vector.cbegin();

  // loop over the photometry object to check the different values and errors
  for (auto FluxErrorPair :  photometry) {
    BOOST_CHECK_CLOSE(FluxErrorPair.flux, expected_photo_iter->flux, tolerance);
    BOOST_CHECK_CLOSE(FluxErrorPair.error, expected_photo_iter->error, tolerance);
    ++expected_photo_iter;
  }
}

// Iterate modifying the values
BOOST_FIXTURE_TEST_CASE ( iterator_modify_test, CatalogFixture ) {
  BOOST_TEST_MESSAGE("--> iterator set test ");

  std::vector<FluxErrorPair> new_values {{1.56, 0.3}, {4.4, 1e-3}};

  // Modify the photometries
  size_t i = 0;
  for (auto iter = photometry.begin(); iter != photometry.end(); ++iter, ++i) {
    iter->flux = new_values[i].flux;
    iter->error = new_values[i].error;
  }

  // make sure they have been modified
  i = 0;
  for (auto FluxErrorPair :  photometry) {
    BOOST_CHECK_CLOSE(FluxErrorPair.flux, new_values[i].flux, tolerance);
    BOOST_CHECK_CLOSE(FluxErrorPair.error, new_values[i].error, tolerance);
    ++i;
  }
}

// Cast a non-const iterator to a const iterator
BOOST_FIXTURE_TEST_CASE ( iterator_cast_test, CatalogFixture ) {
  BOOST_TEST_MESSAGE("--> iterator const cast ");

  auto f = [this](Photometry::const_iterator begin, Photometry::const_iterator end){
    BOOST_CHECK_EQUAL(end - begin, 2);
    auto expected_photo_iter = photometry_vector.begin();
    for (auto i = begin; i != end; ++i) {
      BOOST_CHECK_CLOSE(i->flux, expected_photo_iter->flux, tolerance);
      ++expected_photo_iter;
    }
  };

  BOOST_CHECK_EQUAL(photometry.end() - photometry.begin(), 2);
  f(photometry.begin(), photometry.end());
}


BOOST_AUTO_TEST_SUITE_END ()
