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
 * @file tests/src/ModeExtraction_test.cpp
 * @date 01/22/18
 * @author fdubath
 */

#include <boost/test/unit_test.hpp>

#include "ElementsKernel/Exception.h"
#include "MathUtils/PDF/PdfModeExtraction.h"
#include "XYDataset/XYDataset.h"
#include <cstddef>
#include <tuple>
#include <utility>
#include <vector>

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(ModeExtraction_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(nominal_vector_delta_test) {

  std::vector<double> sampling{0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0};
  std::vector<double> pdf{0.0, 0.0, 5.0, 0.0, 0.0, 4.0, 0.0, 0.0, 1.0, 0.0, 0.0};

  auto modes = Euclid::MathUtils::extractNHighestModes(sampling, pdf, 0.8, 3);

  // position
  BOOST_CHECK_CLOSE(modes[0].getMeanPosition(), 0.2, 0.000001);
  BOOST_CHECK_CLOSE(modes[1].getMeanPosition(), 0.5, 0.000001);
  BOOST_CHECK_CLOSE(modes[2].getMeanPosition(), 0.8, 0.000001);

  // area
  BOOST_CHECK_CLOSE(modes[0].getModeArea(), 0.5, 0.000001);
  BOOST_CHECK_CLOSE(modes[1].getModeArea(), 0.4, 0.000001);
  BOOST_CHECK_CLOSE(modes[2].getModeArea(), 0.1, 0.000001);

  modes = Euclid::MathUtils::extractNBigestModes(sampling, pdf, 0.8, 3);

  // position
  BOOST_CHECK_CLOSE(modes[0].getMeanPosition(), 0.2, 0.000001);
  BOOST_CHECK_CLOSE(modes[1].getMeanPosition(), 0.5, 0.000001);
  BOOST_CHECK_CLOSE(modes[2].getMeanPosition(), 0.8, 0.000001);

  // area
  BOOST_CHECK_CLOSE(modes[0].getModeArea(), 0.5, 0.000001);
  BOOST_CHECK_CLOSE(modes[1].getModeArea(), 0.4, 0.000001);
  BOOST_CHECK_CLOSE(modes[2].getModeArea(), 0.1, 0.000001);
}

BOOST_AUTO_TEST_CASE(nominal_delta_test) {

  std::vector<double> sampling{0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0};
  std::vector<double> pdf{0.0, 0.0, 5.0, 0.0, 0.0, 4.0, 0.0, 0.0, 1.0, 0.0, 0.0};
  auto                full_pdf = Euclid::XYDataset::XYDataset::factory(sampling, pdf);

  auto modes = Euclid::MathUtils::extractNHighestModes(full_pdf, 0.8, 3);

  // position
  BOOST_CHECK_CLOSE(modes[0].getMeanPosition(), 0.2, 0.000001);
  BOOST_CHECK_CLOSE(modes[1].getMeanPosition(), 0.5, 0.000001);
  BOOST_CHECK_CLOSE(modes[2].getMeanPosition(), 0.8, 0.000001);

  // area
  BOOST_CHECK_CLOSE(modes[0].getModeArea(), 0.5, 0.000001);
  BOOST_CHECK_CLOSE(modes[1].getModeArea(), 0.4, 0.000001);
  BOOST_CHECK_CLOSE(modes[2].getModeArea(), 0.1, 0.000001);

  modes = Euclid::MathUtils::extractNBigestModes(full_pdf, 0.8, 3);

  // position
  BOOST_CHECK_CLOSE(modes[0].getMeanPosition(), 0.2, 0.000001);
  BOOST_CHECK_CLOSE(modes[1].getMeanPosition(), 0.5, 0.000001);
  BOOST_CHECK_CLOSE(modes[2].getMeanPosition(), 0.8, 0.000001);

  // area
  BOOST_CHECK_CLOSE(modes[0].getModeArea(), 0.5, 0.000001);
  BOOST_CHECK_CLOSE(modes[1].getModeArea(), 0.4, 0.000001);
  BOOST_CHECK_CLOSE(modes[2].getModeArea(), 0.1, 0.000001);
}

BOOST_AUTO_TEST_CASE(peak_location_test) {
  std::vector<double> sampling{0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0};
  std::vector<double> pdf{0.0, 0.2, 0.5, 0.3, 0.0, 0.0, 0.2, 0.5, 1.0, 0.0, 0.0};
  auto                full_pdf = Euclid::XYDataset::XYDataset::factory(sampling, pdf);
  auto                modes    = Euclid::MathUtils::extractNHighestModes(full_pdf, 0.8, 2);

  /// max sampling
  BOOST_CHECK_CLOSE(modes[0].getHighestSamplePosition(), 0.8, 0.000001);
  BOOST_CHECK_CLOSE(modes[1].getHighestSamplePosition(), 0.2, 0.000001);

  // mean
  BOOST_CHECK_CLOSE(modes[0].getMeanPosition(), 0.7470588235294118, 0.000001);
  BOOST_CHECK_CLOSE(modes[1].getMeanPosition(), 0.21, 0.000001);

  // fitted
  BOOST_CHECK_CLOSE(modes[0].getInterpolatedMaxPosition(), 0.783333333333, 0.000001);
  BOOST_CHECK_CLOSE(modes[1].getInterpolatedMaxPosition(), 0.21, 0.000001);
}

BOOST_AUTO_TEST_CASE(area_test) {

  std::vector<double> sampling{0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0};
  std::vector<double> pdf{0.0, 10., 9.0, 8.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
  auto                full_pdf = Euclid::XYDataset::XYDataset::factory(sampling, pdf);
  auto                modes    = Euclid::MathUtils::extractNHighestModes(full_pdf, 0.8, 1);

  // position
  BOOST_CHECK_CLOSE(modes[0].getMeanPosition(), 0.19259259, 0.001);
  // area
  BOOST_CHECK_CLOSE(modes[0].getModeArea(), 2.7, 0.001);
}

BOOST_AUTO_TEST_CASE(area_limit_test) {

  std::vector<double> sampling{0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0};
  std::vector<double> pdf{0.0, 1, 3, 2, 4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
  auto                full_pdf = Euclid::XYDataset::XYDataset::factory(sampling, pdf);
  auto                modes    = Euclid::MathUtils::extractNHighestModes(full_pdf, 0.8, 1);

  // area
  BOOST_CHECK_CLOSE(modes[0].getModeArea(), 1.0, 0.000001);

  std::vector<double> sampling_2{0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0};
  std::vector<double> pdf_2{10, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
  auto                full_pdf_2 = Euclid::XYDataset::XYDataset::factory(sampling_2, pdf_2);
  modes                          = Euclid::MathUtils::extractNHighestModes(full_pdf_2, 0.8, 1);

  // area
  BOOST_CHECK_CLOSE(modes[0].getModeArea(), 1.0, 0.000001);

  std::vector<double> sampling_3{0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0};
  std::vector<double> pdf_3{20, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
  auto                full_pdf_3 = Euclid::XYDataset::XYDataset::factory(sampling_3, pdf_3);
  modes                          = Euclid::MathUtils::extractNHighestModes(full_pdf_3, 0.8, 1);

  // area
  BOOST_CHECK_CLOSE(modes[0].getModeArea(), 1.0, 0.000001);
}

BOOST_AUTO_TEST_CASE(order_test) {

  std::vector<double> sampling{0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0};
  std::vector<double> pdf{0.0, 10., 0.0, 0.0, 0.0, 0.0, 5.0, 6.0, 5.0, 0.0, 0.0};
  auto                full_pdf = Euclid::XYDataset::XYDataset::factory(sampling, pdf);
  auto                modes    = Euclid::MathUtils::extractNHighestModes(full_pdf, 0.8, 1);

  // position
  BOOST_CHECK_CLOSE(modes[0].getMeanPosition(), 0.1, 0.001);
  // area
  BOOST_CHECK_CLOSE(modes[0].getModeArea(), 1, 0.001);

  modes = Euclid::MathUtils::extractNBigestModes(full_pdf, 0.8, 1);
  // position
  BOOST_CHECK_CLOSE(modes[0].getMeanPosition(), 0.7, 0.001);
  // area
  BOOST_CHECK_CLOSE(modes[0].getModeArea(), 1.6, 0.001);
}

BOOST_AUTO_TEST_CASE(merge_ratio_square_test) {

  std::vector<double> sampling{0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0};
  std::vector<double> pdf{0.0, 0.0, 4.0, 2.0, 5.0, 6.0, 5.0, 2.0, 4.0, 0.0, 0.0};
  auto                full_pdf = Euclid::XYDataset::XYDataset::factory(sampling, pdf);
  auto                modes    = Euclid::MathUtils::extractNHighestModes(full_pdf, 1.0, 1);
  // position
  BOOST_CHECK_CLOSE(modes[0].getMeanPosition(), 0.5, 0.0001);
  // area
  BOOST_CHECK_CLOSE(modes[0].getModeArea(), 2.8, 0.0001);

  modes = Euclid::MathUtils::extractNBigestModes(full_pdf, 1.0, 1);
  // position
  BOOST_CHECK_CLOSE(modes[0].getMeanPosition(), 0.5, 0.0001);
  // area
  BOOST_CHECK_CLOSE(modes[0].getModeArea(), 2.8, 0.0001);
}

BOOST_AUTO_TEST_CASE(merge_ratio_right_test) {

  std::vector<double> sampling{0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0};
  std::vector<double> pdf{0.0, 10., 9.0, 8.5, 8.0, 8.1, 7.0, 7.1, 0.0, 0.0, 0.0};
  auto                full_pdf = Euclid::XYDataset::XYDataset::factory(sampling, pdf);
  auto                modes    = Euclid::MathUtils::extractNHighestModes(full_pdf, 1.0, 1);

  // position
  BOOST_CHECK_CLOSE(modes[0].getMeanPosition(), 0.37729636, 0.0001);
  // area
  BOOST_CHECK_CLOSE(modes[0].getModeArea(), 5.77, 0.0001);

  modes = Euclid::MathUtils::extractNHighestModes(full_pdf, 0.0, 1);
  // position
  BOOST_CHECK_CLOSE(modes[0].getMeanPosition(), 0.240845, 0.0001);
  // area
  BOOST_CHECK_CLOSE(modes[0].getModeArea(), 3.55, 0.0001);

  modes = Euclid::MathUtils::extractNHighestModes(full_pdf, 0.19, 1);
  // position
  BOOST_CHECK_CLOSE(modes[0].getMeanPosition(), 0.240845, 0.0001);
  // area
  BOOST_CHECK_CLOSE(modes[0].getModeArea(), 3.55, 0.0001);

  modes = Euclid::MathUtils::extractNHighestModes(full_pdf, 0.29, 1);
  // position
  BOOST_CHECK_CLOSE(modes[0].getMeanPosition(), 0.3320158, 0.0001);
  // area
  BOOST_CHECK_CLOSE(modes[0].getModeArea(), 5.06, 0.0001);
}

BOOST_AUTO_TEST_CASE(merge_ratio_left_test) {

  std::vector<double> sampling{0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0};
  std::vector<double> pdf{0.0, 8.1, 8.0, 8.5, 9.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0};
  auto                full_pdf = Euclid::XYDataset::XYDataset::factory(sampling, pdf);

  auto modes = Euclid::MathUtils::extractNHighestModes(full_pdf, 1.0, 1);
  // position
  BOOST_CHECK_CLOSE(modes[0].getMeanPosition(), 0.3110092, 0.0001);
  // area
  BOOST_CHECK_CLOSE(modes[0].getModeArea(), 4.36, 0.0001);

  modes = Euclid::MathUtils::extractNHighestModes(full_pdf, 0.0, 1);
  // position
  BOOST_CHECK_CLOSE(modes[0].getMeanPosition(), 0.3591549, 0.0001);
  // area
  BOOST_CHECK_CLOSE(modes[0].getModeArea(), 3.55, 0.0001);
}

BOOST_AUTO_TEST_CASE(getInterpolationAround_nominal_case_test) {
  std::vector<double> sampling{0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0};
  std::vector<double> pdf{0.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0, 0.0, 0.0, 0.0, 0.0};
  auto                full_pdf = Euclid::XYDataset::XYDataset::factory(sampling, pdf);

  auto modes = Euclid::MathUtils::extractNHighestModes(full_pdf, 0.8, 2);

  BOOST_CHECK_CLOSE(modes[0].getInterpolatedMaxPosition(), 0.5166666666666, 0.0001);
  BOOST_CHECK_CLOSE(modes[1].getInterpolatedMaxPosition(), 0.1, 0.0001);
}

BOOST_AUTO_TEST_CASE(getInterpolationAround_border_case_test) {
  std::vector<double> sampling{0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0};
  std::vector<double> pdf{3.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.1};
  auto                full_pdf = Euclid::XYDataset::XYDataset::factory(sampling, pdf);
  auto                modes    = Euclid::MathUtils::extractNHighestModes(full_pdf, 0.8, 2);

  BOOST_CHECK_CLOSE(modes[0].getInterpolatedMaxPosition(), 0.0, 0.0001);
  BOOST_CHECK_CLOSE(modes[1].getInterpolatedMaxPosition(), 0.96111111111, 0.0001);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
