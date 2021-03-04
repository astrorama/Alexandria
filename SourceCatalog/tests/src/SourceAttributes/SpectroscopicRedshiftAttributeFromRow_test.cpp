/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
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
 * @file tests/src/SourceAttributes/SpectroscopicRedshiftAttributeFromRow_test.cpp
 *
 * @date Apr 17, 2014
 * @author Pierre Dubath
 */

#include "ElementsKernel/Exception.h"
#include "SourceCatalog/AttributeFromRow.h"
#include "SourceCatalog/SourceAttributes/SpectroscopicRedshift.h"
#include "SourceCatalog/SourceAttributes/SpectroscopicRedshiftAttributeFromRow.h"
#include <boost/test/unit_test.hpp>
#include <map>
#include <memory>

//-----------------------------------------------------------------------------
// Include the TableFixture which contain a complete table mock object use here
// as a test reference
#include "tests/src/TableFixture.h"

using namespace Euclid::SourceCatalog;

//-----------------------------------------------------------------------------
//

BOOST_AUTO_TEST_SUITE(SpectroscopicRedshiftAttributeFromRow_test)

//-----------------------------------------------------------------------------

// BOOST_FIXTURE_TEST_CASE(createAttribute_test, TableFixture) {
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

BOOST_FIXTURE_TEST_CASE(createAttribute_test, TableFixture) {

  BOOST_TEST_MESSAGE("--> createAttribute test ");

  SpectroscopicRedshiftAttributeFromRow srafr{column_info_ptr, spec_z_val_col_name, spec_z_err_col_name};

  //  unique_ptr<Euclid::SourceCatalog::Attribute> attribute_ptr_0 = srafr.createAttribute(row0);
  //
  //  BOOST_CHECK( typeid(*attribute_ptr_0) == typeid(Euclid::SourceCatalog::SpectroscopicRedshift) );
  //
  //  if(typeid(*attribute_ptr_0) == typeid(Euclid::SourceCatalog::SpectroscopicRedshift)) {
  //      Euclid::SourceCatalog::SpectroscopicRedshift& spectroscopicRedshift =
  //      dynamic_cast<Euclid::SourceCatalog::SpectroscopicRedshift&>( *attribute_ptr_0 );
  //      BOOST_CHECK_CLOSE(spectroscopicRedshift.getValue(), spec_z_val_row0 , tolerance);
  //      BOOST_CHECK_CLOSE(spectroscopicRedshift.getError(), spec_z_err_row0 , tolerance);
  //  }

  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_ptr_1 = srafr.createAttribute(row1);
  Euclid::SourceCatalog::SpectroscopicRedshift*     spectroscopicRedshift =
      dynamic_cast<Euclid::SourceCatalog::SpectroscopicRedshift*>(attribute_ptr_1.get());
  BOOST_CHECK(spectroscopicRedshift != nullptr);
  BOOST_CHECK_CLOSE(spectroscopicRedshift->getValue(), spec_z_val_row1, tolerance);
  BOOST_CHECK_CLOSE(spectroscopicRedshift->getError(), spec_z_err_row1, tolerance);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
