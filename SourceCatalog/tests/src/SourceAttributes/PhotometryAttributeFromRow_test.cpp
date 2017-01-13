/**
 * @file tests/src/SourceAttributes/PhotometryAttributeFromRow_test.cpp
 *
 * @date Apr 17, 2014
 * @author Pierre Dubath
 */

#include <boost/test/unit_test.hpp>
#include <memory>
#include <map>
#include "SourceCatalog/SourceAttributes/PhotometryAttributeFromRow.h"
#include "SourceCatalog/SourceAttributes/Photometry.h"
#include "ElementsKernel/Exception.h"
#include "SourceCatalog/AttributeFromRow.h"

//-----------------------------------------------------------------------------
// Include the TableFixture which contain a complete table mock object use here
// as a test reference
#include "tests/src/TableFixture.h"

using namespace Euclid::SourceCatalog;
using namespace std;


//-----------------------------------------------------------------------------
//

BOOST_AUTO_TEST_SUITE (PhotometryAttributeFromRow_test)

//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( createAttribute_test, TableFixture ) {

  BOOST_TEST_MESSAGE("--> createAttribute test ");

  PhotometryAttributeFromRow paft {column_info_ptr, filter_name_mapping, 1.12345e-12};

  unique_ptr<Euclid::SourceCatalog::Attribute> attribute_ptr = paft.createAttribute(row1);

  BOOST_CHECK( typeid(*attribute_ptr) == typeid(Euclid::SourceCatalog::Photometry) );

  if(typeid(*attribute_ptr) == typeid(Euclid::SourceCatalog::Photometry)) {
      Euclid::SourceCatalog::Photometry& photometry = dynamic_cast<Euclid::SourceCatalog::Photometry&>( *attribute_ptr );
      BOOST_CHECK_CLOSE(photometry.find(v_filter_name)->flux, flux1_row1, tolerance);
      BOOST_CHECK_CLOSE(photometry.find(v_filter_name)->error, error1_row1, tolerance);
      BOOST_CHECK(photometry.find(v_filter_name)->missing_photometry_flag);
      BOOST_CHECK_CLOSE(photometry.find(r_filter_name)->flux, flux2_row1, tolerance);
      BOOST_CHECK_CLOSE(photometry.find(r_filter_name)->error, error2_row1, tolerance);
      BOOST_CHECK(!photometry.find(r_filter_name)->missing_photometry_flag);
  }
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


