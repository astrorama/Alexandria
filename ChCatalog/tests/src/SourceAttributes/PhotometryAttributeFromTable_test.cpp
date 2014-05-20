/**
 * @file PhotometryAttributeFromTable_test.cpp
 *
 * @date Apr 17, 2014
 * @author Pierre Dubath
 */

#include <boost/test/unit_test.hpp>
#include <memory>
#include <map>
#include "ChCatalog/SourceAttributes/PhotometryAttributeFromTable.h"
#include "ChCatalog/SourceAttributes/Photometry.h"
#include "ElementsKernel/ElementsException.h"
#include "ChCatalog/AttributeFromTable.h"

//-----------------------------------------------------------------------------
// Include the TableFixture which contain a complete table mock object use here
// as a test reference
#include "tests/src/TableFixture.h"

using namespace ChCatalog;
using namespace std;


//-----------------------------------------------------------------------------
//

BOOST_AUTO_TEST_SUITE (PhotometryAttributeFromTable_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(constructor_test, TableFixture) {

  BOOST_TEST_MESSAGE("--> constructor test ");

  PhotometryAttributeFromTable paft {column_info_ptr, filter_name_mapping};

  map<string, pair<size_t, size_t>> map = paft.getFilterIndexMapping();
  BOOST_CHECK_EQUAL(map[v_filter_name].first, 5);
  BOOST_CHECK_EQUAL(map[v_filter_name].second, 7);
  BOOST_CHECK_EQUAL(map[r_filter_name].first, 6);
  BOOST_CHECK_EQUAL(map[r_filter_name].second, 8);
}

//-----------------------------------------------------------------------------

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( createAttribute_test, TableFixture ) {

  BOOST_TEST_MESSAGE("--> createAttribute test ");

  PhotometryAttributeFromTable paft {column_info_ptr, filter_name_mapping};

  unique_ptr<ChCatalog::Attribute> attribute_ptr = paft.createAttribute(row1);

  BOOST_CHECK( typeid(*attribute_ptr) == typeid(ChCatalog::Photometry) );

  if(typeid(*attribute_ptr) == typeid(ChCatalog::Photometry)) {
      ChCatalog::Photometry& photometry = dynamic_cast<ChCatalog::Photometry&>( *attribute_ptr );
      BOOST_CHECK_CLOSE(photometry.find(v_filter_name)->flux, flux1_row1, tolerance);
      BOOST_CHECK_CLOSE(photometry.find(v_filter_name)->error, error1_row1, tolerance);
      BOOST_CHECK_CLOSE(photometry.find(r_filter_name)->flux, flux2_row1, tolerance);
      BOOST_CHECK_CLOSE(photometry.find(r_filter_name)->error, error2_row1, tolerance);
  }
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


