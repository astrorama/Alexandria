/**
 * @file Source_test.cpp
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

#include "ElementsKernel/ElementsException.h"

#include <iostream>
#include <map>

using namespace ChCatalog;
using namespace std;


struct SourceFix {

  double tolerence = 1e-8;

  //SpectroscopicRedshift* spectroscopicRedshift;

  const FilterName expectedFilterName { "COSMOS", "V_band" };
  double expectedFlux  = 0.46575674;
  double expectedError = 0.00001534;

  int64_t expectedSourceId     = 1273684;
  int64_t expectedSourceIdMiss = 2345678;

  double expectedRa      = 181.4657;
  double expectedDec     = -36.27363;
  double expectedMissRa  = 281.4657;
  double expectedMissDec = -26.27363;

  double expectedZvalue = 3.;
  double expectedZerror = 0.01;

  vector<shared_ptr<Attribute>> attribute_vector {};
  vector<shared_ptr<Attribute>> attribute_miss_vector {};

  Source* sourcePtr{};
  Source* sourceMissAttrPtr{};

  SourceFix() {

    // setup
    shared_ptr<Coordinates> coordinates_ptr(new Coordinates(expectedRa, expectedDec));
    shared_ptr<SpectroscopicRedshift> spec_redshift_ptr(new SpectroscopicRedshift(expectedZvalue, expectedZerror));
    shared_ptr<Photometry> photometry_ptr(new Photometry{createPhotometryMap()});
    attribute_vector.push_back(coordinates_ptr);
    attribute_vector.push_back(spec_redshift_ptr);
    attribute_vector.push_back(photometry_ptr);

    sourcePtr = new Source(expectedSourceId, attribute_vector);

    // Missing Photometry attibute for the second source
    shared_ptr<Coordinates> coordinates_ptr2(new Coordinates(expectedMissRa, expectedMissDec));
    shared_ptr<SpectroscopicRedshift> spec_redshift_ptr2(new SpectroscopicRedshift(expectedZvalue, expectedZerror));
    attribute_miss_vector.push_back(coordinates_ptr2);
    attribute_miss_vector.push_back(spec_redshift_ptr2);

    sourceMissAttrPtr = new Source(expectedSourceIdMiss, attribute_miss_vector);
 }

  ~SourceFix() {
    // teardown
    delete(sourcePtr);
  }

  SourceFix(const SourceFix&) = delete;

  map< FilterName, pair<double, double> > createPhotometryMap() {
    map< FilterName, pair<double, double> > phot_map {};
    phot_map.insert(make_pair(expectedFilterName, make_pair(expectedFlux, expectedError)));
    return phot_map;
  }

};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Source_test)

BOOST_FIXTURE_TEST_CASE( getAttribute_test, SourceFix ) {

   BOOST_TEST_MESSAGE("--> getAttribute test ");

   shared_ptr<Photometry> ptrPhoto(sourcePtr->getAttribute<Photometry>());
//   cout << " Flux  : " << (ptrPhoto->find(expectedFilterName))->first
//        << " Error : " << (ptrPhoto->find(expectedFilterName))->second
//        << endl;
   BOOST_CHECK_CLOSE(expectedFlux,(ptrPhoto->find(expectedFilterName))->first, tolerence);
   BOOST_CHECK_CLOSE(expectedError,(ptrPhoto->find(expectedFilterName))->second, tolerence);

   shared_ptr<Coordinates> ptrCoord(sourcePtr->getAttribute<Coordinates>());
//   cout << " Ra  : " << ptrCoord->getRa()
//        << " Dec : " << ptrCoord->getDec()
//        << endl;
   BOOST_CHECK_CLOSE(expectedRa, ptrCoord->getRa(), tolerence);
   BOOST_CHECK_CLOSE(expectedDec,ptrCoord->getDec(), tolerence);

   shared_ptr<SpectroscopicRedshift> ptrRedshift(sourcePtr->getAttribute<SpectroscopicRedshift>());
//   cout << " Zvalue : " << ptrRedshift->getValue()
//        << " Error  : " << ptrRedshift->getError()
//        << endl;
   BOOST_CHECK_CLOSE(expectedZvalue, ptrRedshift->getValue(), tolerence);
   BOOST_CHECK_CLOSE(expectedZerror, ptrRedshift->getError(), tolerence);

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( getId_test, SourceFix ) {

   BOOST_TEST_MESSAGE("--> getId test ");
   uint64_t sourceID = sourcePtr->getId();
   BOOST_CHECK_EQUAL(expectedSourceId, sourceID);

}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( missing_attribute_test, SourceFix ) {

   BOOST_TEST_MESSAGE("--> missing_attribute test ");
   shared_ptr<Photometry> ptrPhoto(sourceMissAttrPtr->getAttribute<Photometry>());
   BOOST_CHECK(nullptr == ptrPhoto);

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
