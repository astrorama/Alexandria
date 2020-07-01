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
 * @file tests/src/CatalogFixture.h
 *
 * @date May 13, 2014
 * @author Pierre Dubath
 */

#ifndef CATALOGFIXTURE_H_
#define CATALOGFIXTURE_H_

#include <memory>
#include <vector>
#include <utility>
#include "SourceCatalog/Source.h"
#include "SourceCatalog/SourceAttributes/Photometry.h"
#include "SourceCatalog/SourceAttributes/Coordinates.h"
#include "SourceCatalog/SourceAttributes/SpectroscopicRedshift.h"
#include "SourceCatalog/Catalog.h"

namespace Euclid {
namespace SourceCatalog {

struct CatalogFixture {

  double tolerance = 1e-8;
  //
  // Building a photometry attribute mock object
  //
  // Values for building a Photometry object
  const std::string expected_filter_name_1{"COSMOS/g_SDSS"};
  const std::string expected_filter_name_2{"COSMOS/r_SDSS"};
  const double expected_flux_1 = 0.46575674;
  const double expected_error_1 = 0.00001534;
  const double expected_flux_2 = 0.01537575674;
  const double expected_error_2 = 0.00354616;

  // Shared pointer of filter name vector
  std::shared_ptr<std::vector<std::string>> filter_name_vector_ptr{
    new std::vector<std::string>{expected_filter_name_1, expected_filter_name_2}};

  // photometry values vector
  std::vector<FluxErrorPair> photometry_vector{FluxErrorPair(expected_flux_1,
                                                             expected_error_1),
                                               FluxErrorPair(expected_flux_2, expected_error_2)};

  // Photometry
  Photometry photometry{filter_name_vector_ptr, photometry_vector};

  //
  // Building coordinates and spectroscopic redshift attribute mock objects
  //
  double expected_ra_1 = 181.4657;
  double expected_dec_1 = -36.27363;
  double expected_ra_2 = 281.4657;
  double expected_dec_2 = -26.27363;

  double expected_z_value = 3.;
  double expected_z_error = 0.01;

  std::shared_ptr<Attribute> coordinates_1_ptr{new Coordinates{expected_ra_1, expected_dec_1}};
  std::shared_ptr<Attribute> coordinates_2_ptr{new Coordinates{expected_ra_2, expected_dec_2}};

  std::shared_ptr<Attribute> spec_redshift_ptr{new SpectroscopicRedshift{expected_z_value, expected_z_error}};
  std::shared_ptr<Attribute> photometry_ptr{new Photometry{filter_name_vector_ptr, photometry_vector}};
  std::vector<std::shared_ptr<Attribute>> attribute_vector_1{coordinates_1_ptr, spec_redshift_ptr, photometry_ptr};
  std::vector<std::shared_ptr<Attribute>> attribute_vector_2{coordinates_2_ptr, spec_redshift_ptr};

  Source::id_type expected_source_id_1 = 1273684;
  Source::id_type expected_source_id_2 = 2345678;

  Source source_1{expected_source_id_1, attribute_vector_1};
  Source source_2{expected_source_id_2, attribute_vector_2};

  // Store sources in a vector
  std::vector<Source> source_vector{source_1, source_2};

  // create the catalog
  Catalog catalog{source_vector};


  CatalogFixture() {

//    // First source
//    shared_ptr<Coordinates> coordinates_ptr1(new Coordinates(expectedRa1, expectedDec1));
//    shared_ptr<SpectroscopicRedshift> spec_redshift_ptr1(new SpectroscopicRedshift(expectedZvalue1, expectedZerror1));
//    shared_ptr<Photometry> photometry_ptr1(new Photometry{createPhotometryMap()});
//    attribute_vector1.push_back(coordinates_ptr1);
//    attribute_vector1.push_back(spec_redshift_ptr1);
//    attribute_vector1.push_back(photometry_ptr1);
//
//    // Second source
//    shared_ptr<Coordinates> coordinates_ptr2(new Coordinates(expectedRa2, expectedDec2));
//    shared_ptr<SpectroscopicRedshift> spec_redshift_ptr2(new SpectroscopicRedshift(expectedZvalue2, expectedZerror2));
//    attribute_vector2.push_back(coordinates_ptr2);
//    attribute_vector2.push_back(spec_redshift_ptr2);
//
//    // Store sources in a vector
//    source_vector.push_back(Source(expectedSourceId1, attribute_vector1));
//    source_vector.push_back(Source(expectedSourceId2, attribute_vector2));
//
//    catPtr = new Catalog(source_vector);

  }

  virtual ~CatalogFixture() noexcept {
    // teardown
    //delete catPtr;
  }


};

} // end of namespace SourceCatalog
} // end of namespace Euclid

#endif // CATALOGFIXTURE_H_
