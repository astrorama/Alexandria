/**
 * @file tests/src/CatalogFromTable_test.cpp
 *
 * @date Apr 15, 2014
 * @author Pierre Dubath
 */

#include <boost/test/unit_test.hpp>
#include "SourceCatalog/CatalogFromTable.h"
#include "SourceCatalog/AttributeFromRow.h"
#include "SourceCatalog/SourceAttributes/PhotometryAttributeFromRow.h"


//-----------------------------------------------------------------------------
// Include the TableFixture which contain a complete table mock object use here
// as a test reference
#include "tests/src/TableFixture.h"

using namespace Euclid::SourceCatalog;
using namespace std;

namespace Euclid {
namespace SourceCatalog {

//-----------------------------------------------------------------------------
//

BOOST_AUTO_TEST_SUITE (CatalogFromTable_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(createCatalog_test, TableFixture) {


  unique_ptr<AttributeFromRow> photmetryAft_ptr {new PhotometryAttributeFromRow {column_info_ptr, filter_name_mapping, -99.} };

  vector<shared_ptr<AttributeFromRow>> attribute_from_table_vector;

  attribute_from_table_vector.push_back( move(photmetryAft_ptr) );

  CatalogFromTable cft {table.getColumnInfo(), source_id_name, move(attribute_from_table_vector)};

  Euclid::SourceCatalog::Catalog catalog = cft.createCatalog(table);


  BOOST_CHECK_EQUAL(catalog.find(source_id_1)->getId(),  source_id_1 );
  BOOST_CHECK_CLOSE(catalog.find(source_id_2)->getAttribute<Photometry>()->find(r_filter_name)->flux,  flux2_row1, tolerance );

}


BOOST_AUTO_TEST_SUITE_END ()

} // namespace SourceCatalog
} // end of namespace Euclid
