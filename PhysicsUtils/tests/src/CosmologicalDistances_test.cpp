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

/**
 * @file tests/src/lib/CosmologicalDistances_test.h
 * @date November 29, 2015
 * @author Florian Dubath
 */
#include "ElementsKernel/Real.h"
#include "PhysicsUtils/CosmologicalDistances.h"
#include <boost/test/unit_test.hpp>
#include <cmath>

using namespace Euclid;
using namespace PhysicsUtils;

struct CosmologicalDistances_Fixture {
  double omega_m      = 0.2;
  double omega_lambda = 0.7;
  // so we expect omega_k to be 0.1 !=0
  double H_0 = 77.0;

  std::vector<double> zs{0, 0.001, 0.01, 0.1, 0.5, 1., 1.5, 2., 4., 6.};
  std::vector<double> hubble_parameters{1.,
                                        1.0004002699919667,
                                        1.0040269916690487,
                                        1.042688831818966,
                                        1.2649110640673518,
                                        1.6431676725154984,
                                        2.1095023109728985,
                                        2.6457513110645907,
                                        5.3103672189407014,
                                        8.6139421869432127};
  std::vector<double> comoving{0.,
                               3892629.7211428746,
                               38856076.082309492,
                               381426775.30670536,
                               1743252275.3547294,
                               3097511958.8287911,
                               4144034048.8586593,
                               4968125488.521699,
                               7037575806.8509665,
                               8185617947.9015932};
  std::vector<double> luminous{10.,
                               4429033.2516768286,
                               44595140.97263521,
                               475341190.49684501,
                               2918477377.0888844,
                               6792421919.9330025,
                               11199033877.97576,
                               15937134721.927008,
                               36706225562.921059,
                               59064863879.408623};

  std::vector<double> volumeElement{0.0,
                                    9.990733333168602e-07,
                                    9.907367503391648e-05,
                                    0.009081033159604667,
                                    0.14679118615652445,
                                    0.33115915506673393,
                                    0.4361667073426341,
                                    0.47945673110160303,
                                    0.43890675385247246,
                                    0.35200068850695454};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(CosmologicalDistances_test)

BOOST_FIXTURE_TEST_CASE(hubble_distance, CosmologicalDistances_Fixture) {

  CosmologicalDistances distances{};

  for (double h_0 = 65.; h_0 < 100.; h_0 += 2.1) {
    CosmologicalParameters parameters{omega_m, omega_lambda, h_0};
    double                 expected = 2.99792458e+11 / h_0;  // in [pc]
    BOOST_CHECK(Elements::isEqual(expected, distances.hubbleDistance(parameters)));
  }
}

BOOST_FIXTURE_TEST_CASE(hubble_parameter, CosmologicalDistances_Fixture) {
  std::vector<double>   result_1{1.,
                               1.0015003749375231,
                               1.0150374377332099,
                               1.1536897329871669,
                               1.8371173070873836,
                               2.8284271247461903,
                               3.9528470752104741,
                               5.196152422706632,
                               11.180339887498949,
                               18.520259177452136};
  CosmologicalDistances distances{};

  // check the limit cases
  CosmologicalParameters parameters_1{1., 0., H_0};

  for (size_t i = 0; i < zs.size(); ++i) {
    BOOST_CHECK(Elements::isEqual(result_1[i], distances.hubbleParameter(zs[i], parameters_1)));
  }

  CosmologicalParameters parameters_2{0., 0., H_0};
  for (size_t i = 0; i < zs.size(); ++i) {
    BOOST_CHECK(Elements::isEqual(1. + zs[i], distances.hubbleParameter(zs[i], parameters_2)));
  }

  CosmologicalParameters parameters_3{0., 1., H_0};
  for (size_t i = 0; i < zs.size(); ++i) {
    BOOST_CHECK(Elements::isEqual(1., distances.hubbleParameter(zs[i], parameters_3)));
  }

  CosmologicalParameters parameters_4{omega_m, omega_lambda, H_0};
  for (size_t i = 0; i < zs.size(); ++i) {
    BOOST_CHECK(Elements::isEqual(hubble_parameters[i], distances.hubbleParameter(zs[i], parameters_4)));
  }
}

BOOST_FIXTURE_TEST_CASE(comoving_distance, CosmologicalDistances_Fixture) {
  CosmologicalDistances  distances{};
  CosmologicalParameters parameters{omega_m, omega_lambda, H_0};
  for (size_t i = 0; i < zs.size(); ++i) {
    BOOST_CHECK(Elements::isEqual(comoving[i], distances.comovingDistance(zs[i], parameters)));
  }
}

BOOST_FIXTURE_TEST_CASE(transverse_comoving_distance, CosmologicalDistances_Fixture) {
  CosmologicalDistances distances{};

  // case with negative omega_k
  CosmologicalParameters parameters_1{omega_m, 1.1 - omega_m, H_0};
  BOOST_CHECK(Elements::isEqual(4423595310.7368011, distances.transverseComovingDistance(1.5, parameters_1)));

  // case with 0 omega_k
  CosmologicalParameters parameters_2{omega_m, 1.0 - omega_m, H_0};
  BOOST_CHECK(Elements::isEqual(4319113837.9162245, distances.transverseComovingDistance(1.5, parameters_2)));

  // case with positive omega_k
  CosmologicalParameters parameters_3{omega_m, 0.9 - omega_m, H_0};
  BOOST_CHECK(Elements::isEqual(4222723848.5923686, distances.transverseComovingDistance(1.5, parameters_3)));
}

BOOST_FIXTURE_TEST_CASE(luminous_distance, CosmologicalDistances_Fixture) {
  CosmologicalDistances  distances{};
  CosmologicalParameters parameters{};
  for (size_t i = 0; i < zs.size(); ++i) {
    BOOST_CHECK(Elements::isEqual(luminous[i], distances.luminousDistance(zs[i], parameters)));
  }
}

BOOST_FIXTURE_TEST_CASE(DM_test, CosmologicalDistances_Fixture) {
  CosmologicalDistances  distances{};
  CosmologicalParameters parameters{};
  BOOST_CHECK(Elements::isEqual(44.415392424409184, distances.distanceModulus(1.1, parameters)));
  BOOST_CHECK_EQUAL(0., distances.distanceModulus(0., parameters));
}

BOOST_FIXTURE_TEST_CASE(VE_test, CosmologicalDistances_Fixture) {
  CosmologicalDistances  distances{};
  CosmologicalParameters parameters{};
  for (size_t i = 0; i < zs.size(); ++i) {
    BOOST_CHECK_CLOSE(volumeElement[i], distances.dimensionlessComovingVolumeElement(zs[i], parameters), 0.00001);
  }
}

// BOOST_FIXTURE_TEST_CASE(export_data, CosmologicalDistances_Fixture) {
//  CosmologicalDistances distances{};
//  CosmologicalParameters parameters{0.25,0.75,70.};
//
//
//  std::cout<<distances.hubbleDistance(parameters);
//  for (auto z=0;z<6000;z++){
//    std::cout<< z/1000. << " "
//             << distances.comovingDistance(z/1000., parameters)
//             << " "
//             << distances.luminousDistance(z/1000., parameters)
//             << " "
//             << distances.distanceModulus(z/1000., parameters)
//             << "\n";
//  }
//}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
