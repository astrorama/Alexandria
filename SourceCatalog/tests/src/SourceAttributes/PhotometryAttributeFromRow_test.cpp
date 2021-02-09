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
 * @file tests/src/SourceAttributes/PhotometryAttributeFromRow_test.cpp
 *
 * @date Apr 17, 2014
 * @author Pierre Dubath
 */

#include "SourceCatalog/SourceAttributes/PhotometryAttributeFromRow.h"
#include <boost/test/unit_test.hpp>
#include <map>
#include <memory>

#include "../../../SourceCatalog/PhotometryParsingException.h"
#include "ElementsKernel/Exception.h"
#include "SourceCatalog/AttributeFromRow.h"
#include "SourceCatalog/SourceAttributes/Photometry.h"
#include "tests/src/TableFixture.h"

using namespace Euclid::SourceCatalog;

//-----------------------------------------------------------------------------
//

BOOST_AUTO_TEST_SUITE(PhotometryAttributeFromRow_test)

//-----------------------------------------------------------------------------
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(createAttribute_test, TableFixture) {
  BOOST_TEST_MESSAGE("--> createAttribute test ");

  PhotometryAttributeFromRow paft{column_info_ptr, filter_name_mapping, true, 1.12345e-12, true, threshold_mapping, -99};

  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_ptr = paft.createAttribute(row1);

  BOOST_CHECK(dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_ptr.get()) != nullptr);

  Euclid::SourceCatalog::Photometry* photometry = dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_ptr.get());
  if (photometry) {
    BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->flux, flux1_row1, tolerance);
    BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->error, 0,
                      tolerance);  // When the missing photometry is set the error is 0
    BOOST_CHECK(photometry->find(v_filter_name)->missing_photometry_flag);
    BOOST_CHECK_CLOSE(photometry->find(r_filter_name)->flux, flux2_row1, tolerance);
    BOOST_CHECK_CLOSE(photometry->find(r_filter_name)->error, error2_row1, tolerance);
    BOOST_CHECK(!photometry->find(r_filter_name)->missing_photometry_flag);
  }
}


BOOST_FIXTURE_TEST_CASE(convert_from_mag_test, TableFixture) {
  BOOST_TEST_MESSAGE("--> convertion from mag test ");

  PhotometryAttributeFromRow paft{column_info_ptr, filter_name_mapping, true, -99, true, threshold_mapping, -98, true};

  // simple case
  auto converted_1 = paft.convertFromMag(24.,0.1);
  BOOST_CHECK_CLOSE(converted_1.first, 0.91207, 1e-3);
  BOOST_CHECK_CLOSE(converted_1.second, 0.084004, 1e-3);

  auto converted_2 = paft.convertFromMag(20.,0.2);
  BOOST_CHECK_CLOSE(converted_2.first, 36.31, 1e-3);
  BOOST_CHECK_CLOSE(converted_2.second, 6.688549, 1e-3);

  // missing data
  auto converted_3 = paft.convertFromMag(-99,0.1);
  BOOST_CHECK_CLOSE(converted_3.first, -99, tolerance);
  BOOST_CHECK_CLOSE(converted_3.second, 0., 1e-3);

  // upper limit (negative error)
  auto converted_4 = paft.convertFromMag(20.,-0.2);
  BOOST_CHECK_CLOSE(converted_4.first, 36.31, 1e-3);
  BOOST_CHECK_CLOSE(converted_4.second, -6.688549, 1e-3);

  // upper limit (flag)
  auto converted_5 = paft.convertFromMag(20.,-98);
  BOOST_CHECK_CLOSE(converted_5.first, 36.31, 1e-3);
  BOOST_CHECK_CLOSE(converted_5.second, -98, tolerance);

}









BOOST_FIXTURE_TEST_CASE(exceptionalCaseNoMissingNoUpper_test, TableFixture) {
  BOOST_TEST_MESSAGE("--> No Missing Data, No Upper Limit ");
  PhotometryAttributeFromRow paft_nn{column_info_ptr, filter_name_mapping, false, -99., false, threshold_mapping, -99};

  // nominal: read as it, no flags
  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_nn_nom_ptr = paft_nn.createAttribute(row_nominal_case);
  Euclid::SourceCatalog::Photometry* photometry = dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_nn_nom_ptr.get());
  BOOST_CHECK(photometry != nullptr);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->flux, 1., tolerance);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->error, 0.5, tolerance);
  BOOST_CHECK(!photometry->find(v_filter_name)->missing_photometry_flag);
  BOOST_CHECK(!photometry->find(v_filter_name)->upper_limit_flag);

  // flux zero: read as it, no flags
  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_nn_f0_ptr = paft_nn.createAttribute(row_zero_flux);
  photometry = dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_nn_f0_ptr.get());
  BOOST_CHECK(photometry != nullptr);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->flux, 0., tolerance);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->error, 0.5, tolerance);
  BOOST_CHECK(!photometry->find(v_filter_name)->missing_photometry_flag);
  BOOST_CHECK(!photometry->find(v_filter_name)->upper_limit_flag);

  // flux negatif: read as it, no flags
  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_nn_fm_ptr = paft_nn.createAttribute(row_flag_flux);
  photometry = dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_nn_fm_ptr.get());
  BOOST_CHECK(photometry != nullptr);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->flux, -99., tolerance);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->error, 0.5, tolerance);
  BOOST_CHECK(!photometry->find(v_filter_name)->missing_photometry_flag);
  BOOST_CHECK(!photometry->find(v_filter_name)->upper_limit_flag);

  // error 0: error
  BOOST_CHECK_THROW(paft_nn.createAttribute(row_zero_error), PhotometryParsingException);
  // error negatif: error
  BOOST_CHECK_THROW(paft_nn.createAttribute(row_neg_error), PhotometryParsingException);
}

BOOST_FIXTURE_TEST_CASE(exceptionalCaseMissingNoUpper_test, TableFixture) {
  BOOST_TEST_MESSAGE("--> Missing Data, No Upper Limit ");
  PhotometryAttributeFromRow paft_yn{column_info_ptr, filter_name_mapping, true, -99., false, threshold_mapping, -99};
  // nominal: read as it, no flags
  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_yn_nom_ptr = paft_yn.createAttribute(row_nominal_case);
  Euclid::SourceCatalog::Photometry* photometry = dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_yn_nom_ptr.get());
  BOOST_CHECK(photometry != nullptr);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->flux, 1., tolerance);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->error, 0.5, tolerance);
  BOOST_CHECK(!photometry->find(v_filter_name)->missing_photometry_flag);
  BOOST_CHECK(!photometry->find(v_filter_name)->upper_limit_flag);

  // flux zero: read as it, no flags
  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_yn_f0_ptr = paft_yn.createAttribute(row_zero_flux);
  photometry = dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_yn_f0_ptr.get());
  BOOST_CHECK(photometry != nullptr);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->flux, 0., tolerance);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->error, 0.5, tolerance);
  BOOST_CHECK(!photometry->find(v_filter_name)->missing_photometry_flag);
  BOOST_CHECK(!photometry->find(v_filter_name)->upper_limit_flag);

  // flux negatif: read as it, no flags
  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_yn_fm_ptr = paft_yn.createAttribute(row_neg_flux);
  photometry = dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_yn_fm_ptr.get());
  BOOST_CHECK(photometry != nullptr);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->flux, -1., tolerance);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->error, 0.5, tolerance);
  BOOST_CHECK(!photometry->find(v_filter_name)->missing_photometry_flag);
  BOOST_CHECK(!photometry->find(v_filter_name)->upper_limit_flag);

  // flux =Flag: Missing photometry Flag Error=0
  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_yn_fF_ptr = paft_yn.createAttribute(row_flag_flux);
  photometry = dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_yn_fF_ptr.get());
  BOOST_CHECK(photometry != nullptr);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->error, 0., tolerance);
  BOOST_CHECK(photometry->find(v_filter_name)->missing_photometry_flag);
  BOOST_CHECK(!photometry->find(v_filter_name)->upper_limit_flag);

  // flux =Flag error<0: Missing photometry Flag Error=0
  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_yn_fFem_ptr = paft_yn.createAttribute(row_flag_flux_neg_error);
  photometry = dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_yn_fFem_ptr.get());
  BOOST_CHECK(photometry != nullptr);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->error, 0., tolerance);
  BOOST_CHECK(photometry->find(v_filter_name)->missing_photometry_flag);
  BOOST_CHECK(!photometry->find(v_filter_name)->upper_limit_flag);

  BOOST_TEST_MESSAGE("--> Error <= 0");
  // error 0: error
  BOOST_CHECK_THROW(paft_yn.createAttribute(row_zero_error), PhotometryParsingException);
  // error negatif: error
  BOOST_CHECK_THROW(paft_yn.createAttribute(row_neg_error), PhotometryParsingException);
}

BOOST_FIXTURE_TEST_CASE(exceptionalCaseNoMissingUpper_test, TableFixture) {
  BOOST_TEST_MESSAGE("--> No Missing Data, Upper Limit ");
  PhotometryAttributeFromRow paft_ny{column_info_ptr, filter_name_mapping, false, -99., true, threshold_mapping, -99};
  // nominal: read as it, no flags
  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_ny_nom_ptr = paft_ny.createAttribute(row_nominal_case);
  Euclid::SourceCatalog::Photometry* photometry = dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_ny_nom_ptr.get());
  BOOST_CHECK(photometry != nullptr);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->flux, 1., tolerance);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->error, 0.5, tolerance);
  BOOST_CHECK(!photometry->find(v_filter_name)->missing_photometry_flag);
  BOOST_CHECK(!photometry->find(v_filter_name)->upper_limit_flag);

  // flux zero: read as it, no flags
  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_ny_f0_ptr = paft_ny.createAttribute(row_zero_flux);
  photometry = dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_ny_f0_ptr.get());
  BOOST_CHECK(photometry != nullptr);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->flux, 0., tolerance);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->error, 0.5, tolerance);
  BOOST_CHECK(!photometry->find(v_filter_name)->missing_photometry_flag);
  BOOST_CHECK(!photometry->find(v_filter_name)->upper_limit_flag);

  // flux negatif: read as it, no flags
  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_ny_fm_ptr = paft_ny.createAttribute(row_neg_flux);
  photometry = dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_ny_fm_ptr.get());
  BOOST_CHECK(photometry != nullptr);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->flux, -1., tolerance);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->error, 0.5, tolerance);
  BOOST_CHECK(!photometry->find(v_filter_name)->missing_photometry_flag);
  BOOST_CHECK(!photometry->find(v_filter_name)->upper_limit_flag);

  // Error==0: error
  BOOST_CHECK_THROW(paft_ny.createAttribute(row_zero_error), PhotometryParsingException);
  // Error<0 Flux<0: error
  BOOST_CHECK_THROW(paft_ny.createAttribute(row_flag_flux_neg_error), PhotometryParsingException);
  // Error<0 Flux=0: error
  BOOST_CHECK_THROW(paft_ny.createAttribute(row_zero_flux_neg_error), PhotometryParsingException);

  // error negative: flag as upper limit Error = |Error|
  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_ny_em_ptr = paft_ny.createAttribute(row_neg_error);
  photometry = dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_ny_em_ptr.get());
  BOOST_CHECK(photometry != nullptr);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->flux, 1., tolerance);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->error, 0.5, tolerance);
  BOOST_CHECK(!photometry->find(v_filter_name)->missing_photometry_flag);
  BOOST_CHECK(photometry->find(v_filter_name)->upper_limit_flag);

  // error negative = Threshold Flag: flag as upper limit,  Error = |Error|, Flux=Flux/n
  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_ny_em_fl_ptr = paft_ny.createAttribute(row_neg_error_flag);
  photometry = dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_ny_em_fl_ptr.get());
  BOOST_CHECK(photometry != nullptr);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->flux, 1., tolerance);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->error, 1. / 3., tolerance);
  BOOST_CHECK(!photometry->find(v_filter_name)->missing_photometry_flag);
  BOOST_CHECK(photometry->find(v_filter_name)->upper_limit_flag);

  BOOST_CHECK_CLOSE(photometry->find(r_filter_name)->flux, 3., tolerance);
  BOOST_CHECK_CLOSE(photometry->find(r_filter_name)->error, 3. / 5., tolerance);
  BOOST_CHECK(!photometry->find(r_filter_name)->missing_photometry_flag);
  BOOST_CHECK(photometry->find(r_filter_name)->upper_limit_flag);
}

BOOST_FIXTURE_TEST_CASE(exceptionalCaseMissingUpper_test, TableFixture) {
  BOOST_TEST_MESSAGE("-->Missing Data, Upper Limit ");
  PhotometryAttributeFromRow paft_yy{column_info_ptr, filter_name_mapping, true, -99., true, threshold_mapping, -99};
  // nominal: read as it, no flags
  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_yy_nom_ptr = paft_yy.createAttribute(row_nominal_case);
  Euclid::SourceCatalog::Photometry* photometry = dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_yy_nom_ptr.get());
  BOOST_CHECK(photometry != nullptr);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->flux, 1., tolerance);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->error, 0.5, tolerance);
  BOOST_CHECK(!photometry->find(v_filter_name)->missing_photometry_flag);
  BOOST_CHECK(!photometry->find(v_filter_name)->upper_limit_flag);

  // flux zero: read as it, no flags
  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_yy_f0_ptr = paft_yy.createAttribute(row_zero_flux);
  photometry = dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_yy_f0_ptr.get());
  BOOST_CHECK(photometry != nullptr);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->flux, 0., tolerance);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->error, 0.5, tolerance);
  BOOST_CHECK(!photometry->find(v_filter_name)->missing_photometry_flag);
  BOOST_CHECK(!photometry->find(v_filter_name)->upper_limit_flag);

  // flux negatif: read as it, no flags
  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_yy_fm_ptr = paft_yy.createAttribute(row_neg_flux);
  photometry = dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_yy_fm_ptr.get());
  BOOST_CHECK(photometry != nullptr);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->flux, -1., tolerance);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->error, 0.5, tolerance);
  BOOST_CHECK(!photometry->find(v_filter_name)->missing_photometry_flag);
  BOOST_CHECK(!photometry->find(v_filter_name)->upper_limit_flag);

  // Error==0: error
  BOOST_CHECK_THROW(paft_yy.createAttribute(row_zero_error), PhotometryParsingException);

  // flux =Flag: Missing photometry Flag Error=0
  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_yy_fF_ptr = paft_yy.createAttribute(row_flag_flux);
  photometry = dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_yy_fF_ptr.get());
  BOOST_CHECK(photometry != nullptr);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->error, 0., tolerance);
  BOOST_CHECK(photometry->find(v_filter_name)->missing_photometry_flag);
  BOOST_CHECK(!photometry->find(v_filter_name)->upper_limit_flag);

  // flux = Flag error<0: Missing photometry Flag Error=0
  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_yy_fFem_ptr = paft_yy.createAttribute(row_flag_flux_neg_error);
  photometry = dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_yy_fFem_ptr.get());
  BOOST_CHECK(photometry != nullptr);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->error, 0., tolerance);
  BOOST_CHECK(photometry->find(v_filter_name)->missing_photometry_flag);
  BOOST_CHECK(!photometry->find(v_filter_name)->upper_limit_flag);

  // error negatif: flag as upper limit Error = |Error|
  std::unique_ptr<Euclid::SourceCatalog::Attribute> attribute_yy_em_ptr = paft_yy.createAttribute(row_neg_error);
  photometry = dynamic_cast<Euclid::SourceCatalog::Photometry*>(attribute_yy_em_ptr.get());
  BOOST_CHECK(photometry != nullptr);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->flux, 1., tolerance);
  BOOST_CHECK_CLOSE(photometry->find(v_filter_name)->error, 0.5, tolerance);
  BOOST_CHECK(!photometry->find(v_filter_name)->missing_photometry_flag);
  BOOST_CHECK(photometry->find(v_filter_name)->upper_limit_flag);

  // Error<0 Flux=0: error
  BOOST_CHECK_THROW(paft_yy.createAttribute(row_zero_flux_neg_error), PhotometryParsingException);
  // Error<0 Flux<0: error
  BOOST_CHECK_THROW(paft_yy.createAttribute(row_neg_flux_neg_error), PhotometryParsingException);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
