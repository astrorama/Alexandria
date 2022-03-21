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

#include "MathUtils/distances/Distances.h"
#include "SourceCatalog/SourceAttributes/Photometry.h"
#include <boost/test/unit_test.hpp>

using namespace Euclid::MathUtils;
using Euclid::SourceCatalog::FluxErrorPair;

struct DistancesFixture {
  std::vector<FluxErrorPair> ref_obj, target_obj;

  DistancesFixture() : ref_obj{{1.0, 0.01}, {2.0, 0.02}, {3.0, 0.03}}, target_obj{{1.1, 0.1}, {1.9, 0.2}, {3.1, 0.3}} {}
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(Distances_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(EuclideanDistance_test, DistancesFixture) {
  auto distance = EuclideanDistance::distance(1., ref_obj.begin(), ref_obj.end(), target_obj.begin());
  static_assert(std::is_same<decltype(distance), double>::value, "Distance must match the photometry value");
  BOOST_CHECK_CLOSE(distance, 0.1732050807568878, 1e-7);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(EuclideanScaleGuess_test, DistancesFixture) {
  std::vector<FluxErrorPair> new_target(ref_obj);
  std::transform(ref_obj.begin(), ref_obj.end(), new_target.begin(), [](FluxErrorPair fe) {
    fe.flux *= 2.;
    return fe;
  });

  auto scale = EuclideanDistance::guessScale(ref_obj.begin(), ref_obj.end(), new_target.begin());
  static_assert(std::is_same<decltype(scale), double>::value, "Scale must match the photometry value");
  BOOST_CHECK_CLOSE(scale, 2.0, 1e-7);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(EuclideanScaleDerivative_test, DistancesFixture) {
  double x         = 1.1;
  double h         = 1e-10;
  auto   dx        = EuclideanDistance::daDistance(x, ref_obj.begin(), ref_obj.end(), target_obj.begin());
  auto   fx        = EuclideanDistance::distance(x, ref_obj.begin(), ref_obj.end(), target_obj.begin());
  auto   fxh       = EuclideanDistance::distance(x + h, ref_obj.begin(), ref_obj.end(), target_obj.begin());
  auto   dx_approx = (fxh - fx) / h;
  BOOST_CHECK_CLOSE(dx, dx_approx, 1e-4);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Chi2Distance_test, DistancesFixture) {
  auto distance = Chi2Distance::distance(1., ref_obj.begin(), ref_obj.end(), target_obj.begin());
  static_assert(std::is_same<decltype(distance), double>::value, "Distance must match the photometry value");
  BOOST_CHECK_CLOSE(distance, 1.3476347634763499, 1e-7);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Chi2Scale_test, DistancesFixture) {
  std::vector<FluxErrorPair> new_target(ref_obj);
  std::transform(ref_obj.begin(), ref_obj.end(), new_target.begin(), [](FluxErrorPair fe) {
    fe.flux *= 8.;
    return fe;
  });

  auto scale = Chi2Distance::guessScale(ref_obj.begin(), ref_obj.end(), new_target.begin());
  static_assert(std::is_same<decltype(scale), double>::value, "Scale must match the photometry value");
  BOOST_CHECK_CLOSE(scale, 8.0, 1e-7);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Chi2ScaleDerivative_test, DistancesFixture) {
  double x         = 1.4;
  double h         = 1e-10;
  auto   dx        = Chi2Distance::daDistance(x, ref_obj.begin(), ref_obj.end(), target_obj.begin());
  auto   fx        = Chi2Distance::distance(x, ref_obj.begin(), ref_obj.end(), target_obj.begin());
  auto   fxh       = Chi2Distance::distance(x + h, ref_obj.begin(), ref_obj.end(), target_obj.begin());
  auto   dx_approx = (fxh - fx) / h;
  BOOST_CHECK_CLOSE(dx, dx_approx, 1e-4);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
