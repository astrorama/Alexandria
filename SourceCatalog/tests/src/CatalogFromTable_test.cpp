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

  BOOST_TEST_MESSAGE("Create Catalog test");
  unique_ptr<AttributeFromRow> photmetryAft_ptr {new PhotometryAttributeFromRow {column_info_ptr, filter_name_mapping, true, -99., true, threshold_mapping, -99} };
  vector<shared_ptr<AttributeFromRow>> attribute_from_table_vector;

  attribute_from_table_vector.push_back( move(photmetryAft_ptr) );

  CatalogFromTable cft {table.getColumnInfo(), source_id_name, move(attribute_from_table_vector)};

  Euclid::SourceCatalog::Catalog catalog = cft.createCatalog(table);

  BOOST_CHECK_EQUAL(catalog.size(),2);
  BOOST_CHECK_EQUAL(boost::get<int64_t>(catalog.find(source_id_1)->getId()),  source_id_1 );
  BOOST_CHECK_CLOSE(catalog.find(source_id_2)->getAttribute<Photometry>()->find(r_filter_name)->flux,  flux2_row1, tolerance );

}

BOOST_FIXTURE_TEST_CASE(createCatalogWithStringId_test, TableFixture) {

  BOOST_TEST_MESSAGE("Create Catalog with string ID test");
  unique_ptr<AttributeFromRow> photmetryAft_ptr {new PhotometryAttributeFromRow {column_info_ptr, filter_name_mapping, true, -99., true, threshold_mapping, -99} };
  vector<shared_ptr<AttributeFromRow>> attribute_from_table_vector;

  attribute_from_table_vector.push_back( move(photmetryAft_ptr) );

  CatalogFromTable cft {table.getColumnInfo(), source_id_str_name, move(attribute_from_table_vector)};

  Euclid::SourceCatalog::Catalog catalog = cft.createCatalog(table);

  BOOST_CHECK_EQUAL(catalog.size(),2);
  BOOST_CHECK_EQUAL(boost::get<std::string>(catalog.find(source_str_id_1)->getId()),  source_str_id_1 );
  BOOST_CHECK_CLOSE(catalog.find(source_str_id_2)->getAttribute<Photometry>()->find(r_filter_name)->flux,  flux2_row1, tolerance );

}

BOOST_AUTO_TEST_SUITE_END ()

} // namespace SourceCatalog
} // end of namespace Euclid
