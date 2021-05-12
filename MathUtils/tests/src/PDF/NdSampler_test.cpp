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

#include "MathUtils/PDF/NdSampler.h"
//#include "NdArray/io/NpyMmap.h"
#include <boost/test/unit_test.hpp>
#include <chrono>
#include <fstream>

using namespace Euclid::MathUtils;
using namespace Euclid::NdArray;

struct RandomFixture {
  std::mt19937 rng;
  std::size_t  sample_count = 20000;

  RandomFixture() : rng(std::random_device()()) {}
};

// 1D distribution
struct N1DistributionFixture : public RandomFixture {
  NdArray<double>     pdf{{22}, {2.85464796e-04, 1.78549711e-03, 8.00204861e-03, 2.56968795e-02, 5.91302213e-02, 9.75175304e-02,
                             1.15450181e-01, 9.92703248e-02, 6.71295789e-02, 5.13934433e-02, 6.71295789e-02, 9.92703248e-02,
                             1.15450181e-01, 9.75175304e-02, 5.91302213e-02, 2.56968795e-02, 8.00204861e-03, 1.78549711e-03,
                             2.85464796e-04, 3.27025166e-05, 2.68438603e-06, 1.57886115e-07}};
  std::vector<double> knots{-1., 0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11., 12., 13., 14., 15., 16., 17., 18., 19., 20.};
};

// 2D distribution
#include "pdf_2d.icpp"

// 3D distribution
#include "pdf_3d.icpp"

//-----------------------------------------------------------------------------

// Helper function to bin samples
std::vector<int> bin_samples(const NdArray<double>& samples, const std::vector<double>& edges) {
  std::vector<int> result(edges.size() - 1);
  for (auto v : samples) {
    auto bin_max = std::upper_bound(edges.begin(), edges.end(), v);
    auto bin     = (bin_max - edges.begin()) - 1;
    ++result[bin];
  }
  return result;
}

NdArray<int> bin_samples(const NdArray<double>& samples, const std::vector<double>& x0, const std::vector<double>& x1, double& m0,
                         double& m1) {
  NdArray<int> result({x0.size(), x1.size()});
  std::size_t  nsamples = samples.shape()[0];
  m0 = m1 = 0.;
  for (std::size_t i = 0; i < nsamples; ++i) {
    std::size_t bin0 = std::upper_bound(x0.begin(), x0.end(), samples.at(i, 0)) - x0.begin() - 1;
    std::size_t bin1 = std::upper_bound(x1.begin(), x1.end(), samples.at(i, 1)) - x1.begin() - 1;
    if (bin0 >= x0.size())
      bin0 = x0.size() - 1;
    if (bin1 >= x1.size())
      bin1 = x1.size() - 1;
    ++result.at(bin0, bin1);
    m0 += samples.at(i, 0);
    m1 += samples.at(i, 1);
  }
  m0 /= nsamples;
  m1 /= nsamples;
  return result;
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(NdDistribution_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Sample1DSingleCell, RandomFixture) {
  std::vector<double> knots{5, 10};

  // Linear
  NdArray<double> linear_pdf{{2}, {0., 5.}};
  NdSampler<1>    linear_sampler{{knots}, linear_pdf};
  auto            samples = linear_sampler.draw(sample_count, rng);
  double          mean    = std::accumulate(samples.begin(), samples.end(), 0.) / sample_count;
  BOOST_CHECK_GT(mean, 7.8);

  // Uniform
  NdArray<double> uniform_pdf{{2}, {1., 1.}};
  NdSampler<1>    uniform_sampler{{knots}, uniform_pdf};
  auto            uniform_samples = uniform_sampler.draw(sample_count, rng);
  auto            uniform_mean    = std::accumulate(uniform_samples.begin(), uniform_samples.end(), 0.) / sample_count;
  BOOST_CHECK_CLOSE_FRACTION(uniform_mean, 7.5, 0.05);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Sample1D, N1DistributionFixture) {
  NdSampler<1> dist1{knots, pdf};
  auto         samples = dist1.draw(sample_count, rng);
  // Verify output shape
  BOOST_CHECK_EQUAL(samples.shape().size(), 2);
  BOOST_CHECK_EQUAL(samples.shape()[0], sample_count);
  BOOST_CHECK_EQUAL(samples.shape()[1], 1);

  std::ofstream f("/tmp/test1.txt");
  f << samples << std::endl;

  auto counts = bin_samples(samples, knots);
  BOOST_CHECK_EQUAL(std::accumulate(counts.begin(), counts.end(), 0), sample_count);

  // Bimodal!
  auto max = std::max_element(counts.begin(), counts.end()) - counts.begin();
  BOOST_CHECK((max >= 4 && max <= 6) || (max >= 9 || max <= 11));
  BOOST_CHECK_EQUAL(counts.back(), *std::min_element(counts.begin(), counts.end()));

  BOOST_CHECK_LT(counts[0], counts[3]);
  BOOST_CHECK_LT(counts[3], counts[5]);
  BOOST_CHECK_LT(counts[15], counts[13]);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Sample2D, N2DistributionFixture) {
  NdSampler<2> dist2{{knots_x0, knots_x1}, pdf};
  auto         samples = dist2.draw(sample_count, rng);
  // Verify output shape
  BOOST_CHECK_EQUAL(samples.shape().size(), 2);
  BOOST_CHECK_EQUAL(samples.shape()[0], sample_count);
  BOOST_CHECK_EQUAL(samples.shape()[1], 2);

  double mean0, mean1;
  auto   hist2d = bin_samples(samples, knots_x0, knots_x1, mean0, mean1);
  auto   mode   = argmax(hist2d);
  // The mean is in between the two modes
  BOOST_CHECK_CLOSE_FRACTION(mean0, 26.5, 0.1);
  BOOST_CHECK_CLOSE_FRACTION(mean1, 8, 0.1);

  // The mean is in between the two pdf means
  BOOST_CHECK((mode[0] >= 4 && mode[0] <= 8 && mode[1] >= 3 && mode[1] <= 8) ||
              (mode[0] >= 14 && mode[0] <= 18 && mode[1] >= 10 && mode[1] <= 17));

  // std::ofstream f("/tmp/sample2d.txt");
  // f << samples << std::endl;
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Sample2DSingleCell, RandomFixture) {
  std::vector<double> x0{0, 1}, x1{10, 100};
  NdArray<double>     pdf{{2, 2}, {1, 550, 1, 550}};
  NdSampler<2>        dist2{{x0, x1}, pdf};
  auto                sample = dist2.draw(sample_count, rng);
  BOOST_CHECK_EQUAL(sample.shape()[0], sample_count);
  double m0 = 0, m1 = 0;
  for (size_t i = 0; i < sample.shape()[0]; i++) {
    m0 += sample.at(i, 0);
    m1 += sample.at(i, 1);
  }
  m0 /= sample_count;

  BOOST_CHECK_CLOSE_FRACTION(m0, 0.5, 0.1);
  BOOST_CHECK_GT(m1, 60);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Sample3D, N3DistributionFixture) {
  NdSampler<3> dist3{{knots_x0, knots_x1, knots_x2}, pdf};
  auto         samples = dist3.draw(sample_count, rng);
  // Verify output shape
  BOOST_CHECK_EQUAL(samples.shape().size(), 2);
  BOOST_CHECK_EQUAL(samples.shape()[0], sample_count);
  BOOST_CHECK_EQUAL(samples.shape()[1], 3);

  double mean0 = 0, mean1 = 0, mean2 = 0;
  for (std::size_t i = 0; i < sample_count; ++i) {
    mean0 += samples.at(i, 0);
    mean1 += samples.at(i, 1);
    mean2 += samples.at(i, 2);
  }
  mean0 /= sample_count;
  mean1 /= sample_count;
  mean2 /= sample_count;

  // Note that the two PDF combined do not have the same scatter.
  // We compare with the weighted mean and weighted standard deviation computed from the grid itself.
  BOOST_CHECK_CLOSE_FRACTION(mean0, 6.42, 0.5);
  BOOST_CHECK_CLOSE_FRACTION(mean1, 24, 0.2);
  BOOST_CHECK_CLOSE_FRACTION(mean2, 67, 0.3);

  // std::ofstream f("/tmp/sample3d.txt");
  // f << samples << std::endl;
}

//-----------------------------------------------------------------------------

// Comment out this test to do profiling
/*
BOOST_AUTO_TEST_CASE(PerfSample3D) {
  constexpr std::size_t kRepeats     = 10;
  constexpr std::size_t kSampleCount = 10000;
  std::mt19937          rng;

  // Build knots
  std::vector<double> knots_x0(100), knots_x1(80), knots_x2(90);

  for (std::size_t i = 0; i < knots_x0.size(); ++i) {
    knots_x0[i] = -1.0 + i * (20 + 1) / 99.;
  }
  for (std::size_t i = 0; i < knots_x1.size(); ++i) {
    knots_x1[i] = 15.0 + i * (36 - 15) / 79.;
  }
  for (std::size_t i = 0; i < knots_x2.size(); ++i) {
    knots_x2[i] = 44.0 + i * (118 - 44) / 89.;
  }

  // Load data
  auto pdf = mmapNpy<double>("pdf3d.npy");

  // Run tests
  std::chrono::steady_clock clock;
  auto                      start = clock.now();
  for (std::size_t i = 0; i < kRepeats; ++i) {
    if (i % 10 == 0)
      std::cout << i << std::endl;
    NdSampler<3>  dist3{{knots_x0, knots_x1, knots_x2}, pdf};
    auto          samples = dist3.draw(kSampleCount, rng);
    std::ofstream f("/tmp/sample3d.txt");
    f << samples;
    break;
  }
  auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(clock.now() - start).count();
  std::cout << (kSampleCount * kRepeats) / (duration * 1e-3) << " samples / second" << std::endl;
}
*/
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
