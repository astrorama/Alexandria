/**
 * @file CatalogFixture.h
 *
 * @date May 13, 2014
 * @author Pierre Dubath
 */

#ifndef CATALOGFIXTURE_H_
#define CATALOGFIXTURE_H_

#include <memory>
#include <vector>
#include <utility>
#include "ChCatalog/SourceAttributes/Photometry.h"
#include "ChCatalog/FilterName.h"

using namespace ChCatalog;
using namespace std;

struct CatalogFixture {

  double tolerence = 1e-8;

//  Source* sourcePtr1{};
//  Source* sourcePtr2{};
//
//  size_t expected_cat_size = 2;
//

//
// Building a photometry mock object
//
  // Values for building a Photometry object
  const FilterName expected_filter_name_1 { "COSMOS", "g_SDSS" };
  const FilterName expected_filter_name_2 { "COSMOS", "r_SDSS" };
  const double expected_flux_1 = 0.46575674;
  const double expected_error_1 = 0.00001534;
  const double expected_flux_2 = 0.01537575674;
  const double expected_error_2 = 0.00354616;

  // Shared pointer of filter name vector
  shared_ptr<vector<FilterName>> filter_name_vector_ptr {
      new vector<FilterName> { expected_filter_name_1, expected_filter_name_2 } };

  // photometry values vector
  vector<Photometry::ValuePair> photometry_vector { Photometry::ValuePair(expected_flux_1,
      expected_error_1), Photometry::ValuePair(expected_flux_2, expected_error_2) };

  // Photometry
  Photometry photometry {filter_name_vector_ptr, photometry_vector};


//
//  int64_t expectedSourceId1 = 1273684;
//  int64_t expectedSourceId2 = 2345678;
//
//  double expectedRa1  = 181.4657;
//  double expectedDec1 = -36.27363;
//  double expectedRa2  = 281.4657;
//  double expectedDec2 = -26.27363;
//
//  double expectedZvalue1 = 3.;
//  double expectedZerror1 = 0.01;
//  double expectedZvalue2 = 2.;
//  double expectedZerror2 = 0.01;
//
//  vector<shared_ptr<Attribute>> attribute_vector1 {};
//  vector<shared_ptr<Attribute>> attribute_vector2 {};
//
//  vector<Source> source_vector {};
//
//  Catalog* catPtr {};

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
  ~CatalogFixture() {
    // teardown
    //delete catPtr;
  }

//  map< FilterName, pair<double, double> > createPhotometryMap() {
//    map< FilterName, pair<double, double> > phot_map {};
//    phot_map.insert(make_pair(expectedFilterName, make_pair(expectedFlux, expectedError)));
//    return phot_map;
//  }

};

#endif // CATALOGFIXTURE_H_ 
