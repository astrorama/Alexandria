/*
 * Copyright (C) 2022 Euclid Science Ground Segment
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

#include "MathUtils/distances/Weights.h"
#include "SourceCatalog/SourceAttributes/Photometry.h"
#include <boost/test/unit_test.hpp>

using namespace Euclid::MathUtils;
using Euclid::SourceCatalog::FluxErrorPair;

struct WeightFixture {
  std::vector<FluxErrorPair> ref_obj, target_obj;

  WeightFixture() : ref_obj{{1.0, 0.01}, {2.0, 0.02}, {3.0, 0.03}}, target_obj{{1.1, 0.1}, {1.9, 0.2}, {3.1, 0.3}} {}
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(Weights_tests)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(EuclideanWeight_test, WeightFixture) {
  auto weight = InverseEuclidean::weight(1., ref_obj.begin(), ref_obj.end(), target_obj.begin());
  static_assert(std::is_same<decltype(weight), double>::value, "Weight must match the photometry value");
  BOOST_CHECK_CLOSE(weight, 5.773502691896255, 1e-7);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Chi2Weight_test, WeightFixture) {
  auto weight = InverseChi2::weight(1., ref_obj.begin(), ref_obj.end(), target_obj.begin());
  static_assert(std::is_same<decltype(weight), double>::value, "Weight must match the photometry value");
  BOOST_CHECK_CLOSE(weight, 0.7420408163265294, 1e-7);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(LikelihoodWeight_test, WeightFixture) {
  auto weight = Likelihood::weight(1., ref_obj.begin(), ref_obj.end(), target_obj.begin());
  static_assert(std::is_same<decltype(weight), double>::value, "Weight must match the photometry value");
  BOOST_CHECK_CLOSE(weight, 0.5097589144785925, 1e-7);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
