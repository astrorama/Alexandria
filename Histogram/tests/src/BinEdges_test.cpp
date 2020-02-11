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

#include <boost/test/unit_test.hpp>

#include "Histogram/Binning/Scott.h"
#include "Histogram/Binning/Sqrt.h"

using namespace Euclid::Histogram;

struct BinEdgesFixture {
  std::vector<float> values{1, 2, 8, 4, 5, 4, 3, 2, 1, 5};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(ScalarBinEdges_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(scottsBinEdges, BinEdgesFixture) {
  std::vector<float> eedges{1., 3.333333, 5.66666667, 8.};

  Binning::Scott<float> binning;
  binning.computeBins(values.begin(), values.end());
  auto edges = binning.getEdges();
  BOOST_CHECK_EQUAL(edges.size(), eedges.size());

  auto eei = eedges.begin();
  auto ei = edges.begin();
  for (; eei != eedges.end(); ++eei, ++ei) {
    BOOST_CHECK_CLOSE(*ei, *eei, 1e-4);
  }
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(sqrtBinEdges, BinEdgesFixture) {
  std::vector<float> eedges{1., 2.75, 4.5, 6.25, 8.};

  Binning::Sqrt<float> binning;
  binning.computeBins(values.begin(), values.end());
  auto edges = binning.getEdges();
  BOOST_CHECK_EQUAL(edges.size(), eedges.size());

  auto eei = eedges.begin();
  auto ei = edges.begin();
  for (; eei != eedges.end(); ++eei, ++ei) {
    BOOST_CHECK_CLOSE(*ei, *eei, 1e-4);
  }
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(scottZeros) {
  std::vector<float> values{0., 0., 0.};

  Binning::Scott<float> binning;
  binning.computeBins(values.begin(), values.end());
  auto edges = binning.getEdges();
  BOOST_CHECK_EQUAL(edges.size(), 2);
  BOOST_CHECK_EQUAL(edges[0], -0.5);
  BOOST_CHECK_EQUAL(edges[1], +0.5);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------