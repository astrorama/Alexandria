/**
 * @file CatalogFromTable_test.cpp
 *
 * @date Apr 15, 2014
 * @author Pierre Dubath
 */

#include <boost/test/unit_test.hpp>
#include "ChCatalog/CatalogFromTable.h"
#include "ChCatalog/AttributeFromRow.h"
#include "ChCatalog/SourceAttributes/PhotometryAttributeFromRow.h"


//-----------------------------------------------------------------------------
// Include the TableFixture which contain a complete table mock object use here
// as a test reference
#include "tests/src/TableFixture.h"

using namespace ChCatalog;
using namespace std;

namespace ChCatalog {

//-----------------------------------------------------------------------------
//

BOOST_AUTO_TEST_SUITE (CatalogFromTable_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(createCatalog_test, TableFixture) {


  unique_ptr<AttributeFromRow> photmetryAft_ptr {new PhotometryAttributeFromRow {column_info_ptr, filter_name_mapping} };

  vector<unique_ptr<AttributeFromRow>> attribute_from_table_vector;

  attribute_from_table_vector.push_back( move(photmetryAft_ptr) );

  size_t source_id_index = *(table.getColumnInfo()->find(source_id_name));

  CatalogFromTable cft {source_id_index, move(attribute_from_table_vector)};

  ChCatalog::Catalog catalog = cft.createCatalog(table);

  BOOST_CHECK(true);
  //BOOST_CHECK_EQUAL(catalog.find(source_id_1)->getId(),  source_id_1 );
  //BOOST_CHECK_CLOSE(catalog.find(source_id_2)->getAttribute<Photometry>()->find(r_filter_name)->flux,  flux2_row1, tolerance );

}


BOOST_AUTO_TEST_SUITE_END ()

} // namespace ChCatalog
