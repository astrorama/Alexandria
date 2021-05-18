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

#include "AlexandriaKernel/index_sequence.h"
#include "ElementsKernel/Auxiliary.h"
#include "GridContainer/serialize.h"
#include "MathUtils/PDF/NdSampler.h"
#include "NdArray/io/NpyMmap.h"
#include "SourceCatalog/SourceAttributes/Photometry.h"
#include "XYDataset/QualifiedName.h"
#include "XYDataset/serialize.h"
#include <boost/archive/text_iarchive.hpp>
#include <boost/test/unit_test.hpp>
#include <chrono>
#include <fstream>

using namespace Euclid::MathUtils;
using namespace Euclid::NdArray;
using Euclid::GridContainer::GridAxis;
using Euclid::GridContainer::GridContainer;
using Euclid::GridContainer::gridImport;
using Euclid::SourceCatalog::Photometry;
using Euclid::XYDataset::QualifiedName;

/// Used for discrete axes
enum class MyEnum { A, B, C, D, E, F, G, H, I, J, K };

std::ostream& operator<<(std::ostream& out, const MyEnum e) {
  out << "MyEnum::" << 'A' + static_cast<int>(e) - static_cast<int>(MyEnum::A);
  return out;
}

typedef std::map<MyEnum, std::size_t>::value_type counter_t;
BOOST_TEST_DONT_PRINT_LOG_VALUE(counter_t)

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
std::vector<int> bin_samples(const std::vector<std::tuple<double>>& samples, const std::vector<double>& edges) {
  std::vector<int> result(edges.size() - 1);
  for (auto v : samples) {
    auto bin_max = std::upper_bound(edges.begin(), edges.end(), std::get<0>(v));
    auto bin     = (bin_max - edges.begin()) - 1;
    ++result[bin];
  }
  return result;
}

std::vector<int> bin_samples(const std::vector<std::tuple<std::string>>& samples, const std::vector<std::string>& bins) {
  std::vector<int> result(bins.size());
  for (auto v : samples) {
    auto bin = std::find(bins.begin(), bins.end(), std::get<0>(v)) - bins.begin();
    ++result[bin];
  }
  return result;
}

NdArray<int> bin_samples(const std::vector<std::tuple<double, double>>& samples, const std::vector<double>& x0,
                         const std::vector<double>& x1, double& m0, double& m1) {
  NdArray<int> result({x0.size(), x1.size()});
  std::size_t  nsamples = samples.size();
  m0 = m1 = 0.;
  for (auto& sample : samples) {
    auto        v0   = std::get<0>(sample);
    auto        v1   = std::get<1>(sample);
    std::size_t bin0 = std::upper_bound(x0.begin(), x0.end(), v0) - x0.begin() - 1;
    std::size_t bin1 = std::upper_bound(x1.begin(), x1.end(), v1) - x1.begin() - 1;
    if (bin0 >= x0.size())
      bin0 = x0.size() - 1;
    if (bin1 >= x1.size())
      bin1 = x1.size() - 1;
    ++result.at(bin0, bin1);
    m0 += v0;
    m1 += v1;
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
  NdArray<double>   linear_pdf{{2}, {0., 5.}};
  NdSampler<double> linear_sampler{{knots}, linear_pdf};
  auto              samples = linear_sampler.draw(sample_count, rng);
  double            mean    = 0.;
  for (auto& s : samples) {
    mean += std::get<0>(s);
  }
  mean /= sample_count;
  BOOST_CHECK_GT(mean, 7.8);

  // Uniform
  NdArray<double>   uniform_pdf{{2}, {1., 1.}};
  NdSampler<double> uniform_sampler{{knots}, uniform_pdf};
  auto              uniform_samples = uniform_sampler.draw(sample_count, rng);
  auto              uniform_mean    = 0.;
  for (auto& s : uniform_samples) {
    uniform_mean += std::get<0>(s);
  }
  uniform_mean /= sample_count;
  BOOST_CHECK_CLOSE_FRACTION(uniform_mean, 7.5, 0.05);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Sample1D, N1DistributionFixture) {
  NdSampler<double> dist1{knots, pdf};
  auto              samples = dist1.draw(sample_count, rng);
  BOOST_CHECK_EQUAL(samples.size(), sample_count);

  // std::ofstream f("/tmp/test1.txt");
  // f << samples << std::endl;

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

BOOST_FIXTURE_TEST_CASE(Sample1DDiscrete, N1DistributionFixture) {
  std::vector<std::string> sknots{"-1", "0",  "1",  "2",  "3",  "4",  "5",  "6",  "7",  "8",  "9",
                                  "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"};
  NdSampler<std::string>   dist1{sknots, pdf};
  auto                     samples = dist1.draw(sample_count, rng);
  BOOST_CHECK_EQUAL(samples.size(), sample_count);

  auto counts = bin_samples(samples, sknots);
  BOOST_CHECK_EQUAL(std::accumulate(counts.begin(), counts.end(), 0), sample_count);

  auto max_i = std::max_element(counts.begin(), counts.end()) - counts.begin();
  auto min_i = std::min_element(counts.begin(), counts.end()) - counts.begin();

  // Bimodal!
  BOOST_CHECK(sknots[max_i] == "5" || sknots[max_i] == "11");
  BOOST_CHECK(min_i <= 1 || min_i >= 18);
  BOOST_CHECK_GT(counts[4], counts[3]);
  BOOST_CHECK_GT(counts[6], counts[7]);
  BOOST_CHECK_GT(counts[13], counts[15]);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Sample2D, N2DistributionFixture) {
  NdSampler<double, double> dist2{{knots_x0, knots_x1}, pdf};
  auto                      samples = dist2.draw(sample_count, rng);
  // Verify output shape
  BOOST_CHECK_EQUAL(samples.size(), sample_count);

  double mean0, mean1;
  auto   hist2d = bin_samples(samples, knots_x0, knots_x1, mean0, mean1);
  auto   mode   = argmax(hist2d);
  // The mean is in between the two modes
  BOOST_CHECK_CLOSE_FRACTION(mean0, 26.5, 0.1);
  BOOST_CHECK_CLOSE_FRACTION(mean1, 8, 0.1);

  // The mean is in between the two pdf means
  BOOST_CHECK((mode[0] >= 4 && mode[0] <= 8 && mode[1] >= 3 && mode[1] <= 8) ||
              (mode[0] >= 14 && mode[0] <= 18 && mode[1] >= 10 && mode[1] <= 17));
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Sample2DSingleCell, RandomFixture) {
  std::vector<double>       x0{0, 1}, x1{10, 100};
  NdArray<double>           pdf{{2, 2}, {1, 550, 1, 550}};
  NdSampler<double, double> dist2{{x0, x1}, pdf};
  auto                      sample = dist2.draw(sample_count, rng);
  BOOST_CHECK_EQUAL(sample.size(), sample_count);
  double m0 = 0, m1 = 0;
  for (auto& s : sample) {
    m0 += std::get<0>(s);
    m1 += std::get<1>(s);
  }
  m0 /= sample_count;

  BOOST_CHECK_CLOSE_FRACTION(m0, 0.5, 0.1);
  BOOST_CHECK_GT(m1, 60);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Sample3D, N3DistributionFixture) {
  NdSampler<double, double, double> dist3{{knots_x0, knots_x1, knots_x2}, pdf};
  auto                              sample = dist3.draw(sample_count, rng);
  // Verify output shape
  BOOST_CHECK_EQUAL(sample.size(), sample_count);

  double mean0 = 0, mean1 = 0, mean2 = 0;
  for (auto& s : sample) {
    mean0 += std::get<0>(s);
    mean1 += std::get<1>(s);
    mean2 += std::get<2>(s);
  }
  mean0 /= sample_count;
  mean1 /= sample_count;
  mean2 /= sample_count;

  // Note that the two PDF combined do not have the same scatter.
  // We compare with the weighted mean and weighted standard deviation computed from the grid itself.
  BOOST_CHECK_CLOSE_FRACTION(mean0, 6.42, 0.1);
  BOOST_CHECK_CLOSE_FRACTION(mean1, 24, 0.1);
  BOOST_CHECK_CLOSE_FRACTION(mean2, 67, 0.1);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Sample3DDiscrete, N3DistributionFixture) {
  std::vector<MyEnum> knots_enum0;
  for (std::size_t i = 0; i <= 'K' - 'A'; ++i) {
    knots_enum0.emplace_back(static_cast<MyEnum>(static_cast<int>(MyEnum::A) + i));
  }

  NdSampler<MyEnum, double, double> dist3{{knots_enum0, knots_x1, knots_x2}, pdf};
  auto                              sample = dist3.draw(sample_count, rng);

  // This will not compile if the output sample type is not what we expect
  static_assert(std::is_same<std::remove_reference<decltype(sample[0])>::type, std::tuple<MyEnum, double, double>>::value,
                "Compile time check!");

  BOOST_CHECK_EQUAL(sample.size(), sample_count);

  double                        mean1 = 0, mean2 = 0;
  std::map<MyEnum, std::size_t> counter0;

  for (auto& s : sample) {
    ++counter0[std::get<0>(s)];
    mean1 += std::get<1>(s);
    mean2 += std::get<2>(s);
  }
  mean1 /= sample_count;
  mean2 /= sample_count;

  // Continuous axes
  BOOST_CHECK_CLOSE_FRACTION(mean1, 24, 0.1);
  BOOST_CHECK_CLOSE_FRACTION(mean2, 67, 0.1);

  // Discrete axis. According to the marginalization, the mode is at the third position : that's C
  auto max_i = std::max_element(counter0.begin(), counter0.end(),
                                [](const counter_t& a, const counter_t& b) { return a.second < b.second; });
  BOOST_CHECK_EQUAL(max_i->first, MyEnum::C);

  // E is the second mode
  BOOST_CHECK_GT(counter0[MyEnum::E], counter0[MyEnum::A]);
  BOOST_CHECK_GT(counter0[MyEnum::E], counter0[MyEnum::B]);
  BOOST_CHECK_LT(counter0[MyEnum::E], counter0[MyEnum::C]);  // First mode!
  BOOST_CHECK_GT(counter0[MyEnum::E], counter0[MyEnum::D]);
  BOOST_CHECK_GT(counter0[MyEnum::E], counter0[MyEnum::F]);
  BOOST_CHECK_GT(counter0[MyEnum::E], counter0[MyEnum::G]);
  BOOST_CHECK_GT(counter0[MyEnum::E], counter0[MyEnum::H]);
  BOOST_CHECK_GT(counter0[MyEnum::E], counter0[MyEnum::I]);
  BOOST_CHECK_GT(counter0[MyEnum::E], counter0[MyEnum::J]);
  BOOST_CHECK_GT(counter0[MyEnum::E], counter0[MyEnum::K]);

  // G should be greater than I, J and K, might be the same as H
  BOOST_CHECK_GT(counter0[MyEnum::G], counter0[MyEnum::I]);
  BOOST_CHECK_GT(counter0[MyEnum::G], counter0[MyEnum::J]);
  BOOST_CHECK_GT(counter0[MyEnum::G], counter0[MyEnum::K]);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(SingleDiscreteValue, RandomFixture) {
  std::vector<MyEnum> knots0{MyEnum::A};
  std::vector<double> knots1{0., 1., 2., 3.};
  NdArray<double>     pdf{{1, 4}, {0.5, 1., 3., 1.5}};

  NdSampler<MyEnum, double> dist2{{knots0, knots1}, pdf};
  auto                      sample = dist2.draw(sample_count, rng);

  double      mean    = 0;
  std::size_t count_a = 0;
  for (auto& s : sample) {
    mean += std::get<1>(s);
    count_a += std::get<0>(s) == MyEnum::A;
  }
  mean /= sample_count;

  // 1.916667 is the weighted average
  BOOST_CHECK_CLOSE_FRACTION(mean, 1.916667, 0.06);
  BOOST_CHECK_EQUAL(count_a, sample_count);

  // Swap axes
  NdSampler<double, MyEnum> dist2p{{knots1, knots0}, pdf.reshape(4, 1)};
  auto                      samplep = dist2p.draw(sample_count, rng);

  mean    = 0;
  count_a = 0;
  for (auto& s : samplep) {
    mean += std::get<0>(s);
    count_a += std::get<1>(s) == MyEnum::A;
  }
  mean /= sample_count;

  // 1.916667 is the weighted average
  BOOST_CHECK_CLOSE_FRACTION(mean, 1.916667, 0.06);
  BOOST_CHECK_EQUAL(count_a, sample_count);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(SingleContinuousValue, RandomFixture) {
  std::vector<MyEnum> knots0{MyEnum::A, MyEnum::B, MyEnum::C};
  std::vector<double> knots1{2.};
  NdArray<double>     pdf{{3, 1}, {0.60, 0.30, 0.10}};

  NdSampler<MyEnum, double> dist2{{knots0, knots1}, pdf};
  auto                      sample = dist2.draw(sample_count, rng);

  double                        mean = 0;
  std::map<MyEnum, std::size_t> counts;
  for (auto& s : sample) {
    mean += std::get<1>(s);
    ++counts[std::get<0>(s)];
  }
  mean /= sample_count;

  BOOST_CHECK_EQUAL(mean, 2.);
  BOOST_CHECK_GT(counts[MyEnum::A], counts[MyEnum::B]);
  BOOST_CHECK_GT(counts[MyEnum::B], counts[MyEnum::C]);

  // Swap axes
  NdSampler<double, MyEnum> dist2p{{knots1, knots0}, pdf.reshape(1, 3)};
  auto                      samplep = dist2p.draw(sample_count, rng);
  mean                              = 0;
  counts.clear();

  for (auto& s : samplep) {
    mean += std::get<0>(s);
    ++counts[std::get<1>(s)];
  }
  mean /= sample_count;

  BOOST_CHECK_EQUAL(mean, 2.);
  BOOST_CHECK_GT(counts[MyEnum::A], counts[MyEnum::B]);
  BOOST_CHECK_GT(counts[MyEnum::B], counts[MyEnum::C]);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(RepeatedContiguousDiscrete, RandomFixture) {
  std::vector<MyEnum> knots0{MyEnum::A, MyEnum::B, MyEnum::B, MyEnum::C};
  std::vector<double> knots1{0., 1., 2.};

  NdArray<double> pdf{{4, 3},
                      {                   //
                       0.60, 0.30, 0.10,  //
                       0.00, 0.50, 0.50,  //
                       0.33, 0.33, 0.33,  //
                       0.00, 0.00, 1.00}};

  NdSampler<MyEnum, double> dist2({knots0, knots1}, pdf);
  auto                      sample = dist2.draw(sample_count, rng);

  double                        mean = 0.;
  std::map<MyEnum, std::size_t> counts;
  for (auto& s : sample) {
    mean += std::get<1>(s);
    ++counts[std::get<0>(s)];
  }
  mean /= sample_count;

  // All discrete are roughly equivalent, but B is repeated twice, which means ~2x more likely
  BOOST_CHECK_GT(counts[MyEnum::A], 0);
  BOOST_CHECK_GT(counts[MyEnum::C], 0);
  BOOST_CHECK_GT(counts[MyEnum::B], 1.8 * counts[MyEnum::A]);
  BOOST_CHECK_GT(counts[MyEnum::B], 1.8 * counts[MyEnum::C]);

  // This ~1.13 was computed numerically using numpy:
  // interp_prob = np.interp(np.linspace(0, 2, 1000), [0, 1, 2], pdf.sum(axis=0))
  // np.random.choice(np.linspace(0, 2, 1000), p=interp_prob/interp_prob.sum(), size=20000).mean()
  BOOST_CHECK_CLOSE_FRACTION(mean, 1.13, 0.04);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(RepeatedNonContiguousDiscrete, RandomFixture) {
  // Note that this is like the previous case, but B is now not contiguous
  std::vector<MyEnum> knots0{MyEnum::A, MyEnum::B, MyEnum::C, MyEnum::B};
  std::vector<double> knots1{0., 1., 2.};

  // The PDF has been permuted accordingly
  NdArray<double> pdf{{4, 3},
                      {
                          //
                          0.60, 0.30, 0.10,  //
                          0.00, 0.50, 0.50,  //
                          0.00, 0.00, 1.00,  //
                          0.33, 0.33, 0.33,  //
                      }};

  NdSampler<MyEnum, double> dist2({knots0, knots1}, pdf);
  auto                      sample = dist2.draw(sample_count, rng);

  double                        mean = 0.;
  std::map<MyEnum, std::size_t> counts;
  for (auto& s : sample) {
    mean += std::get<1>(s);
    ++counts[std::get<0>(s)];
  }
  mean /= sample_count;

  // All discrete are roughly equivalent, but B is repeated twice, which means ~2x more likely
  BOOST_CHECK_GT(counts[MyEnum::A], 0);
  BOOST_CHECK_GT(counts[MyEnum::C], 0);
  BOOST_CHECK_GT(counts[MyEnum::B], 1.8 * counts[MyEnum::A]);
  BOOST_CHECK_GT(counts[MyEnum::B], 1.8 * counts[MyEnum::C]);

  BOOST_CHECK_CLOSE_FRACTION(mean, 1.13, 0.04);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(RepeatedContiguousContinous, RandomFixture) {
  std::vector<MyEnum> knots0{MyEnum::A, MyEnum::B, MyEnum::C};
  std::vector<double> knots1{0., 1., 2., 2., 3.};
  NdArray<double>     pdf{{3, 5},
                      {
                          //
                          0.00, 0.15, 0.20, 0.30, 0.20,  //
                          0.05, 0.10, 0.10, 0.40, 0.10,  //
                          0.05, 0.08, 0.00, 0.00, 0.30,  //
                      }};

  NdSampler<MyEnum, double> dist2({knots0, knots1}, pdf);
  auto                      sample = dist2.draw(sample_count, rng);

  double                        mean = 0.;
  std::map<MyEnum, std::size_t> counts;
  for (auto& s : sample) {
    mean += std::get<1>(s);
    ++counts[std::get<0>(s)];
  }
  mean /= sample_count;

  // Marginal for discrete axis: 0.85, 0.75, 0.43
  BOOST_CHECK_GT(counts[MyEnum::A], counts[MyEnum::B]);
  BOOST_CHECK_GT(counts[MyEnum::B], counts[MyEnum::C]);
  BOOST_CHECK_GT(counts[MyEnum::C], 0);

  // This ~1.8783 was computed numerically using numpy:
  // interp_prob = np.interp(np.linspace(0, 3, 1000), [0, 1, 2, 2, 3], pdf.sum(axis=0))
  // np.random.choice(np.linspace(0, 3, 1000), p=interp_prob/interp_prob.sum(), size=20000).mean()
  BOOST_CHECK_CLOSE_FRACTION(mean, 1.8783, 0.01);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(RepeatedNonContiguousContinuous, RandomFixture) {
  std::vector<MyEnum> knots0{MyEnum::A, MyEnum::B, MyEnum::C};
  // This simply can not be handled
  std::vector<double> knots1{0., 1., 2., 3., 2.};
  NdArray<double>     pdf{{3, 5}};

  try {
    NdSampler<MyEnum, double> dist2({knots0, knots1}, pdf);
    dist2.draw(sample_count, rng);
    BOOST_FAIL("Should have thrown");
  } catch (const Elements::Exception&) {
  }

  // Swap axes
  try {
    NdSampler<double, MyEnum> dist2({knots1, knots0}, pdf.reshape(5, 3));
    dist2.draw(sample_count, rng);
    BOOST_FAIL("Should have thrown");
  } catch (const Elements::Exception&) {
  }
}

//-----------------------------------------------------------------------------

template <typename Seq>
struct ExtractKnots {};

template <std::size_t... Is>
struct ExtractKnots<Euclid::_index_sequence<Is...>> {
  template <typename... Axes>
  static std::tuple<std::vector<Axes>...> extract(const std::tuple<GridAxis<Axes>...>& axes) {
    return std::tuple<std::vector<Axes>...>{{std::get<Is>(axes).begin(), std::get<Is>(axes).end()}...};
  }

  template <typename... Axes>
  static std::vector<std::size_t> extractShape(const std::tuple<GridAxis<Axes>...>& axes) {
    return std::vector<std::size_t>{std::get<Is>(axes).size()...};
  }
};

template <typename... Axes>
std::unique_ptr<NdSampler<Axes...>> createSamplerFromGrid(const GridContainer<std::vector<double>, Axes...>& grid) {
  auto            knots     = ExtractKnots<Euclid::_make_index_sequence<sizeof...(Axes)>>::extract(grid.getAxesTuple());
  auto            pdf_shape = ExtractKnots<Euclid::_make_index_sequence<sizeof...(Axes)>>::extractShape(grid.getAxesTuple());
  NdArray<double> pdf(pdf_shape, grid.begin(), grid.end());
  return Euclid::make_unique<NdSampler<Axes...>>(std::move(knots), std::move(pdf));
}

BOOST_FIXTURE_TEST_CASE(FromGridContainer, RandomFixture) {
  using PhzGrid = GridContainer<std::vector<double>, double, double, QualifiedName, QualifiedName>;

  const QualifiedName sed0("CosmosSp/new_name"), sed1("CosmosSp/Sa_A_0"), sed2("CosmosSp/Sa_A_1");
  const QualifiedName default_qn({}, "dummy");

  // Load grid. It follows the same schema as Phosphoros' grids, with a mock content of three SEDs,
  // a single reddening curve, a single E(B-V), and 61 knots for Z
  // Each SED has a Z probability that follows a Gaussian centered at 0, 1.5 and 3 respectively
  auto          grid_path = Elements::getAuxiliaryPath("MathUtils/Grid_TEST_param_MADAU.txt");
  std::ifstream grid_stream(grid_path.native());
  auto          grid = gridImport<PhzGrid, boost::archive::text_iarchive>(grid_stream);

  // Initialize the sampler from the grid
  auto sampler = createSamplerFromGrid(grid);

  // Draw samples
  // Since QualifiedName is not default constructible, we allocate the output area here with
  // a default value
  std::vector<std::tuple<double, double, QualifiedName, QualifiedName>> sample(sample_count, {0., 0., default_qn, default_qn});
  sampler->draw(sample_count, rng, sample);

  // Verify that the sample statistics match the known distribution
  std::map<QualifiedName, std::size_t> sed_count;
  std::map<QualifiedName, double>      sed_mean_z;
  std::map<QualifiedName, std::size_t> red_count;
  double                               ebv_sum = 0.;

  for (auto& s : sample) {
    double        z, ebv;
    QualifiedName red(default_qn), sed(default_qn);

    std::tie(z, ebv, red, sed) = s;

    ++sed_count[sed];
    ++red_count[red];
    sed_mean_z[sed] += z;
    ebv_sum += ebv;
  }
  sed_mean_z[sed0] /= sed_count[sed0];
  sed_mean_z[sed1] /= sed_count[sed1];
  sed_mean_z[sed2] /= sed_count[sed2];

  // The grid has E(B-V) fixed to 0
  BOOST_CHECK_EQUAL(ebv_sum, 0.);

  // The reddening curve is fixed to SB_calzetti
  BOOST_CHECK_EQUAL(red_count.size(), 1);
  BOOST_CHECK_EQUAL(red_count[QualifiedName({}, "SB_calzetti")], sample_count);

  // There are three SEDs, with a marginal probability of 0.45, 0.41, 0.14
  BOOST_CHECK_EQUAL(sed_count.size(), 3);
  BOOST_CHECK_GT(sed_count[sed0], 1.05 * sed_count[sed1]);
  BOOST_CHECK_GT(sed_count[sed1], 2.5 * sed_count[sed2]);
  BOOST_CHECK_GT(sed_count[sed2], 0);

  // First SED has PDZ following a half-normal distribution located at 0, so has a mean of ~0.8
  BOOST_CHECK_CLOSE_FRACTION(sed_mean_z[sed0], 0.8, 0.1);
  // Second follows a Gaussian centered at 1.5 and a std of 1
  BOOST_CHECK_CLOSE_FRACTION(sed_mean_z[sed1], 1.5, 0.1);
  // And the third follows a Gaussian centered at 3 and a std of 1
  BOOST_CHECK_CLOSE_FRACTION(sed_mean_z[sed2], 3.0, 0.1);
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
    NdSampler<double, double, double> dist3{{knots_x0, knots_x1, knots_x2}, pdf};
    dist3.draw(kSampleCount, rng);
  }
  auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(clock.now() - start).count();
  std::cout << (kSampleCount * kRepeats) / (duration * 1e-3) << " samples / second" << std::endl;
}
*/
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
