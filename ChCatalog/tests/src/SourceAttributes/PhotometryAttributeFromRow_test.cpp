/**
 * @file tests/src/SourceAttributes/PhotometryAttributeFromRow_test.cpp
 *
 * @date Apr 17, 2014
 * @author Pierre Dubath
 */

#include <boost/test/unit_test.hpp>
#include <memory>
#include <map>
#include "ChCatalog/SourceAttributes/PhotometryAttributeFromRow.h"
#include "ChCatalog/SourceAttributes/Photometry.h"
#include "ElementsKernel/Exception.h"
#include "ChCatalog/AttributeFromRow.h"

//-----------------------------------------------------------------------------
// Include the TableFixture which contain a complete table mock object use here
// as a test reference
#include "tests/src/TableFixture.h"

using namespace Euclid::ChCatalog;
using namespace std;


//-----------------------------------------------------------------------------
//

BOOST_AUTO_TEST_SUITE (PhotometryAttributeFromRow_test)

//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( createAttribute_test, TableFixture ) {

  BOOST_TEST_MESSAGE("--> createAttribute test ");

  PhotometryAttributeFromRow paft {column_info_ptr, filter_name_mapping};

  unique_ptr<Euclid::ChCatalog::Attribute> attribute_ptr = paft.createAttribute(row1);

  BOOST_CHECK( typeid(*attribute_ptr) == typeid(Euclid::ChCatalog::Photometry) );

  if(typeid(*attribute_ptr) == typeid(Euclid::ChCatalog::Photometry)) {
      Euclid::ChCatalog::Photometry& photometry = dynamic_cast<Euclid::ChCatalog::Photometry&>( *attribute_ptr );
      BOOST_CHECK_CLOSE(photometry.find(v_filter_name)->flux, flux1_row1, tolerance);
      BOOST_CHECK_CLOSE(photometry.find(v_filter_name)->error, error1_row1, tolerance);
      BOOST_CHECK_CLOSE(photometry.find(r_filter_name)->flux, flux2_row1, tolerance);
      BOOST_CHECK_CLOSE(photometry.find(r_filter_name)->error, error2_row1, tolerance);
  }
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


