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
#include <cmath>

#include "Histogram/Histogram.h"
#include "Histogram/Binning/EdgeVector.h"
#include "Histogram/Binning/Sqrt.h"

using namespace Euclid::Histogram;

BOOST_AUTO_TEST_SUITE(Histogram_test)

//-----------------------------------------------------------------------------
// Integer histogram, no weights
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(histogramInt) {
  std::vector<int> data{1, 1, 2, 3, 5, 4, 6};
  std::vector<int> edges{0, 1, 2, 3, 4, 5};
  std::vector<float> expected{0, 2, 1, 1, 2};
  Histogram<int> histo(data.begin(), data.end(), Binning::EdgeVector<int>{edges});

  BOOST_CHECK_EQUAL(histo.size(), 5);
  auto counts = histo.getCounts();
  BOOST_CHECK_EQUAL_COLLECTIONS(expected.begin(), expected.end(), counts.begin(), counts.end());
}

//-----------------------------------------------------------------------------
// Float histogram, no weights
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(histogramFloat) {
  std::vector<float> data{1.10, 1.60, 2.33, 3.01, 5.00, 4.99, 6.00, 5.50};
  std::vector<float> edges{0, 1, 2, 3, 4, 5};
  std::vector<float> expected{0, 2, 1, 1, 2};
  Histogram<float> histo(data.begin(), data.end(), Binning::EdgeVector<float>{edges});

  BOOST_CHECK_EQUAL(histo.size(), 5);
  auto counts = histo.getCounts();
  BOOST_CHECK_EQUAL_COLLECTIONS(expected.begin(), expected.end(), counts.begin(), counts.end());
}

//-----------------------------------------------------------------------------
// Histogram with negative value
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(histogramWithNegatives) {
  std::vector<float> data{-1.20, -2.30, -1.33, 0.00, 1.00, 3.99, 2.00, 6.50};
  std::vector<float> edges{-2, -1, 0, 1, 2, 3};
  std::vector<float> expected{2, 0, 1, 1, 1};
  Histogram<float> histo(data.begin(), data.end(), Binning::EdgeVector<float>{edges});

  BOOST_CHECK_EQUAL(histo.size(), 5);
  auto counts = histo.getCounts();
  BOOST_CHECK_EQUAL_COLLECTIONS(expected.begin(), expected.end(), counts.begin(), counts.end());
}

//-----------------------------------------------------------------------------
// Histogram with weights
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(histogramWeights) {
  std::vector<float> data{1.10, 1.60, 2.33, 3.01, 5.00, 4.99, 6.00, 5.50};
  std::vector<float> weights{1.00, 5.00, 1.10, 0.00, 0.50, 1.00, 2.00, 0.00};
  std::vector<float> edges{0, 1, 2, 3, 4, 5};
  std::vector<float> expected{0.0, 6.0, 1.1, 0.0, 1.5};
  Histogram<float> histo(data.begin(), data.end(), weights.begin(), weights.end(), Binning::EdgeVector<float>{edges});

  BOOST_CHECK_EQUAL(histo.size(), 5);
  auto counts = histo.getCounts();
  BOOST_CHECK_EQUAL_COLLECTIONS(expected.begin(), expected.end(), counts.begin(), counts.end());
}

//-----------------------------------------------------------------------------
// Get the bin midpoints
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(histogramBinsCenter) {
  std::vector<float> data{1.10, 1.60, 2.33, 3.01, 5.00, 4.99, 6.00, 5.50};
  std::vector<float> edges{0, 1, 2, 3, 4, 5};
  std::vector<float> centers{0.5, 1.5, 2.5, 3.5, 4.5};

  Histogram<float> histo(data.begin(), data.end(), Binning::EdgeVector<float>{edges});
  auto bins = histo.getBins();
  BOOST_CHECK_EQUAL_COLLECTIONS(centers.begin(), centers.end(), bins.begin(), bins.end());
}

//-----------------------------------------------------------------------------
// Create an histogram passing a functor to generate the bin edges
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(histogramFunctor) {
  std::vector<float> data{1.10, 1.60, 2.33, 3.01, 5.00, 4.99, 6.00, 5.50};
  Histogram<float> histo(data.begin(), data.end(), Binning::Sqrt<float>{});
  std::vector<float> expected{3, 1, 4};
  std::vector<float> expected_edges{1.1, 2.73333333, 4.36666667, 6};

  BOOST_CHECK_EQUAL(histo.size(), 3);
  auto counts = histo.getCounts();
  BOOST_CHECK_EQUAL_COLLECTIONS(expected.begin(), expected.end(), counts.begin(), counts.end());
  auto ei = expected_edges.begin();
  auto edges = histo.getEdges();

  BOOST_CHECK_EQUAL(expected_edges.size(), edges.size());

  for (auto ai = edges.begin(); ai != edges.end(); ++ei, ++ai) {
    BOOST_CHECK_CLOSE(*ei, *ai, 1e-5);
  }
}

//-----------------------------------------------------------------------------
// Get statistics from the histogram
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(histogramStats) {
/* You can use the following python snipped to verify the values on this test
import numpy as np

values = [1.10, 1.60, 2.33, 3.01, 5.00, 4.99, 6.00, 5.50]
counts, edges = np.histogram(values, bins='sqrt')
centers = 0.5*(edges[1:] + edges[:-1])

mean = np.average(centers, weights=counts)
sigma = np.sqrt(np.sum(counts * (centers - mean)**2) / np.sum(counts))

As for the median, as long as half the values are below, we consider it good
*/

  std::vector<float> data{1.10, 1.60, 2.33, 3.01, 5.00, 4.99, 6.00, 5.50};
  Histogram<float> histo(data.begin(), data.end(), Binning::Sqrt<float>{});

  float mean, median, sigma;
  std::tie(mean, median, sigma) = histo.getStats();

  BOOST_CHECK_CLOSE(mean, 3.7541667, 1e-4);
  auto centers = histo.getBins();
  auto values = histo.getCounts();
  std::transform(centers.begin(), centers.end(), values.begin(), centers.begin(),
                 [median](float v, float c) { return (v < median) * c; });
  auto less_than_median = std::accumulate(centers.begin(), centers.end(), 0);
  BOOST_CHECK_EQUAL(less_than_median, data.size() / 2);

  BOOST_CHECK_CLOSE(sigma, 1.51414, 1e-4);
}

//-----------------------------------------------------------------------------
// Clip an histogram with an inverted min/max
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(clipBadValues) {
  std::vector<float> data{1.10, 1.60, 2.33, 3.01, 5.00, 4.99, 6.00, 5.50};
  std::vector<float> edges{0, 1, 2, 3, 4, 5};

  Histogram<float> histo(data.begin(), data.end(), Binning::EdgeVector<float>{edges});
  BOOST_CHECK_THROW(histo.clip(4, 1), Elements::Exception);

}

//-----------------------------------------------------------------------------
// Clip an histogram
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(clipHistogram) {
  std::vector<float> data{-2, -1, -1, 0, 0, 0, 0, 1, 1, 2};
  std::vector<float> edges{-2.5, -1.5, -0.5, 0.5, 1.5, 2.5};
  std::vector<float> expected{1, 2, 4, 2, 1};
  std::vector<float> centers{-2, -1, 0, 1, 2};

  Histogram<float> histo(data.begin(), data.end(), Binning::EdgeVector<float>{edges});
  BOOST_CHECK_EQUAL(histo.size(), 5);
  auto counts = histo.getCounts();
  BOOST_CHECK_EQUAL_COLLECTIONS(expected.begin(), expected.end(), counts.begin(), counts.end());
  auto bins = histo.getBins();
  BOOST_CHECK_EQUAL_COLLECTIONS(centers.begin(), centers.end(), bins.begin(), bins.end());

  float mean, median, sigma;
  std::tie(mean, median, sigma) = histo.getStats();
  BOOST_CHECK_SMALL(mean, std::numeric_limits<float>::epsilon());
  BOOST_CHECK_SMALL(median, std::numeric_limits<float>::epsilon());
  BOOST_CHECK_CLOSE(sigma, 1.0954451, 1e-5);

  histo.clip(-1.1, 1.1);
  BOOST_CHECK_EQUAL(histo.size(), 3);
  std::tie(mean, median, sigma) = histo.getStats();
  BOOST_CHECK_SMALL(mean, std::numeric_limits<float>::epsilon());
  BOOST_CHECK_SMALL(median, std::numeric_limits<float>::epsilon());
  BOOST_CHECK_CLOSE(sigma, 0.70710678, 1e-5);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(histogramZeroSigma) {
  std::vector<float> data{0, 0, 0, 0};
  std::vector<float> edges{-0.5, +0.5};

  Histogram<float> histo(data.begin(), data.end(), Binning::EdgeVector<float>{edges});
  float mean, median, sigma;
  std::tie(mean, median, sigma) = histo.getStats();
  BOOST_CHECK_SMALL(mean, std::numeric_limits<float>::epsilon());
  BOOST_CHECK_SMALL(median, std::numeric_limits<float>::epsilon());
  BOOST_CHECK_SMALL(sigma, std::numeric_limits<float>::epsilon());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(histogramCopy) {
  std::vector<float> data{-2, -1, -1, 0, 0, 0, 0, 1, 1, 2};
  std::vector<float> edges{-2.5, -1.5, -0.5, 0.5, 1.5, 2.5};
  std::vector<float> expected{1, 2, 4, 2, 1};
  std::vector<float> centers{-2, -1, 0, 1, 2};

  Histogram<float> histo(data.begin(), data.end(), Binning::EdgeVector<float>{edges});
  Histogram<float> histo2(histo);

  histo.clip(-1.1, 1.1);

  float mean, median, sigma;
  std::tie(mean, median, sigma) = histo2.getStats();
  BOOST_CHECK_SMALL(mean, std::numeric_limits<float>::epsilon());
  BOOST_CHECK_SMALL(median, std::numeric_limits<float>::epsilon());
  BOOST_CHECK_CLOSE(sigma, 1.0954451, 1e-5);

  BOOST_CHECK_EQUAL(histo.size(), 3);
  std::tie(mean, median, sigma) = histo.getStats();
  BOOST_CHECK_SMALL(mean, std::numeric_limits<float>::epsilon());
  BOOST_CHECK_SMALL(median, std::numeric_limits<float>::epsilon());
  BOOST_CHECK_CLOSE(sigma, 0.70710678, 1e-5);


}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
