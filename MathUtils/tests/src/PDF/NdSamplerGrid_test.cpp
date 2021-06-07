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

#include "ElementsKernel/Auxiliary.h"
#include "GridContainer/GridAxis.h"
#include "GridContainer/GridContainer.h"
#include "GridContainer/serialize.h"
#include "MathUtils/PDF/NdSampler.h"
#include "MathUtils/PDF/NdSamplerFromGrid.h"
#include "NdArray/NdArray.h"
#include "XYDataset/serialize.h"
#include <boost/archive/text_iarchive.hpp>
#include <boost/archive/text_oarchive.hpp>
#include <boost/test/unit_test.hpp>

using namespace Euclid::MathUtils;
using namespace Euclid::NdArray;
using Euclid::GridContainer::GridAxis;
using Euclid::GridContainer::GridContainer;
using Euclid::GridContainer::gridExport;
using Euclid::GridContainer::gridImport;
using Euclid::XYDataset::QualifiedName;

//-----------------------------------------------------------------------------

struct RandomFixture {
  std::mt19937 rng;
  std::size_t  sample_count = 20000;

  RandomFixture() : rng(std::random_device()()) {}
};

//-----------------------------------------------------------------------------

static std::size_t scaleMax(const std::map<std::size_t, std::size_t>& scale_count) {
  typedef std::map<std::size_t, std::size_t>::value_type scale_pair_t;
  auto                                                   max_i = std::max_element(scale_count.begin(), scale_count.end(),
                                [](const scale_pair_t& a, const scale_pair_t& b) { return a.second < b.second; });
  return max_i->first;
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(NdSamplerGrid_test)

//-----------------------------------------------------------------------------

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
  std::tuple<double, double, QualifiedName, QualifiedName> default_tuple(0., 0., default_qn, default_qn);
  std::vector<decltype(default_tuple)>                     sample(sample_count, default_tuple);
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
  BOOST_CHECK_CLOSE_FRACTION(sed_mean_z[sed0], 0.8, 0.11);
  // Second follows a Gaussian centered at 1.5 and a std of 1
  BOOST_CHECK_CLOSE_FRACTION(sed_mean_z[sed1], 1.5, 0.11);
  // And the third follows a Gaussian centered at 3 and a std of 1
  BOOST_CHECK_CLOSE_FRACTION(sed_mean_z[sed2], 3.0, 0.11);
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(FromGridVectorContainer, RandomFixture) {
  using PhzGrid = GridContainer<std::vector<std::vector<double>>, double, double, QualifiedName, QualifiedName>;

  const QualifiedName sed0("CosmosSp/new_name"), sed1("CosmosSp/Sa_A_0"), sed2("CosmosSp/Sa_A_1");
  const QualifiedName default_qn({}, "dummy");

  // Load grid. It follows the same schema as Phosphoros' grids, with a mock content of three SEDs,
  // a single reddening curve, a single E(B-V), and 61 knots for Z
  // Each SED has a Z probability that follows a Gaussian centered at 0, 1.5 and 3 respectively
  // Cells are vector of doubles, representing an additional axis corresponding to the scale
  // The scale for the first sed follows a Gaussian centered at 10
  // For the second, centered at 5
  // And for the third, centered at ~3
  // Check the image Grid_TEST_vector.png for an intuition
  auto          grid_path = Elements::getAuxiliaryPath("MathUtils/Grid_TEST_vector.txt");
  std::ifstream grid_stream(grid_path.native());
  auto          grid = gridImport<PhzGrid, boost::archive::text_iarchive>(grid_stream);

  // Make sure using an user-defined axis works
  std::vector<double> scale_axis(10);
  for (std::size_t i = 0; i < scale_axis.size(); ++i) {
    scale_axis[i] = i * 0.01;
  }

  auto dsampler = createSamplerFromGrid(grid, scale_axis);
  BOOST_CHECK(dsampler);

  std::vector<std::tuple<double, double, double, QualifiedName, QualifiedName>> dsample(
      1, std::make_tuple(0, 0, 0, default_qn, default_qn));
  dsampler->draw(1, rng, dsample);

  // For testing, use the default conversion (discrete axis), which is Phosphoros' use case
  auto sampler = createSamplerFromGrid(grid);
  BOOST_CHECK(sampler);

  std::vector<std::tuple<std::size_t, double, double, QualifiedName, QualifiedName>> sample(
      sample_count, std::make_tuple(0, 0, 0, default_qn, default_qn));
  sampler->draw(sample_count, rng, sample);

  // Verify that the sample statistics match the known distribution
  std::map<QualifiedName, std::size_t>                        sed_count;
  std::map<QualifiedName, double>                             sed_mean_z;
  std::map<QualifiedName, std::map<std::size_t, std::size_t>> sed_scale;
  std::map<QualifiedName, std::size_t>                        red_count;
  double                                                      ebv_sum = 0.;

  for (auto& s : sample) {
    double        z, ebv;
    std::size_t   scale;
    QualifiedName red(default_qn), sed(default_qn);

    std::tie(scale, z, ebv, red, sed) = s;

    ++sed_count[sed];
    ++red_count[red];
    sed_mean_z[sed] += z;
    ++sed_scale[sed][scale];
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

  // There are three SEDs, with a marginal probability of 0.36, 0.47, 0.17
  BOOST_CHECK_EQUAL(sed_count.size(), 3);
  BOOST_CHECK_GT(sed_count[sed1], 1.1 * sed_count[sed0]);
  BOOST_CHECK_GT(sed_count[sed1], 2.5 * sed_count[sed2]);
  BOOST_CHECK_GT(sed_count[sed0], 2. * sed_count[sed2]);

  // First SED has PDZ following a half-normal distribution located at 0, so has a mean of ~0.8
  BOOST_CHECK_CLOSE_FRACTION(sed_mean_z[sed0], 0.8, 0.05);
  // Second follows a Gaussian centered at 1.5 and a std of 1
  BOOST_CHECK_CLOSE_FRACTION(sed_mean_z[sed1], 1.6, 0.05);
  // And the third follows a Gaussian centered at 3 and a std of 1
  BOOST_CHECK_CLOSE_FRACTION(sed_mean_z[sed2], 3.0, 0.05);

  // First SED has an independent scale factor following a half-normal located at position 9
  BOOST_CHECK_EQUAL(scaleMax(sed_scale[sed0]), 9ul);
  // Second SED has a scale factor following a normal located at position 4
  BOOST_CHECK_EQUAL(scaleMax(sed_scale[sed1]), 4ul);
  // And third SED follows a normal located at position 2
  BOOST_CHECK_EQUAL(scaleMax(sed_scale[sed2]), 2ul);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
