/**
 * @file SpectroscopicRedshiftAttributeFromRow_test.cpp
 *
 * @date Apr 17, 2014
 * @author Pierre Dubath
 */

#include <boost/test/unit_test.hpp>
#include <memory>
#include <map>
#include "ChCatalog/SourceAttributes/SpectroscopicRedshiftAttributeFromRow.h"
#include "ChCatalog/SourceAttributes/SpectroscopicRedshift.h"
#include "ElementsKernel/ElementsException.h"
#include "ChCatalog/AttributeFromRow.h"

//-----------------------------------------------------------------------------
// Include the TableFixture which contain a complete table mock object use here
// as a test reference
#include "tests/src/TableFixture.h"

using namespace ChCatalog;
using namespace std;


//-----------------------------------------------------------------------------
//

BOOST_AUTO_TEST_SUITE (SpectroscopicRedshiftAttributeFromRow_test)

//-----------------------------------------------------------------------------

//BOOST_FIXTURE_TEST_CASE(createAttribute_test, TableFixture) {
//
//  BOOST_TEST_MESSAGE("--> createAttribute test ");
//
//  SpectroscopicRedshiftAttributeFromRow srafr {column_info_ptr, spec_z_val_col_name, spec_z_err_col_name};
//
//  BOOST_CHECK_EQUAL(srafr.first, 5);
//  BOOST_CHECK_EQUAL(map[v_filter_name].second, 7);
//  BOOST_CHECK_EQUAL(map[r_filter_name].first, 6);
//  BOOST_CHECK_EQUAL(map[r_filter_name].second, 8);
//}

//-----------------------------------------------------------------------------

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( createAttribute_test, TableFixture ) {

  BOOST_TEST_MESSAGE("--> createAttribute test ");

  SpectroscopicRedshiftAttributeFromRow srafr {column_info_ptr, spec_z_val_col_name, spec_z_err_col_name};

//  unique_ptr<ChCatalog::Attribute> attribute_ptr_0 = srafr.createAttribute(row0);
//
//  BOOST_CHECK( typeid(*attribute_ptr_0) == typeid(ChCatalog::SpectroscopicRedshift) );
//
//  if(typeid(*attribute_ptr_0) == typeid(ChCatalog::SpectroscopicRedshift)) {
//      ChCatalog::SpectroscopicRedshift& spectroscopicRedshift = dynamic_cast<ChCatalog::SpectroscopicRedshift&>( *attribute_ptr_0 );
//      BOOST_CHECK_CLOSE(spectroscopicRedshift.getValue(), spec_z_val_row0 , tolerance);
//      BOOST_CHECK_CLOSE(spectroscopicRedshift.getError(), spec_z_err_row0 , tolerance);
//  }

  unique_ptr<ChCatalog::Attribute> attribute_ptr_1 = srafr.createAttribute(row1);

  BOOST_CHECK( typeid(*attribute_ptr_1) == typeid(ChCatalog::SpectroscopicRedshift) );

   if(typeid(*attribute_ptr_1) == typeid(ChCatalog::SpectroscopicRedshift)) {
       ChCatalog::SpectroscopicRedshift& spectroscopicRedshift = dynamic_cast<ChCatalog::SpectroscopicRedshift&>( *attribute_ptr_1 );
       BOOST_CHECK_CLOSE(spectroscopicRedshift.getValue(), spec_z_val_row1 , tolerance);
       BOOST_CHECK_CLOSE(spectroscopicRedshift.getError(), spec_z_err_row1 , tolerance);
   }

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


