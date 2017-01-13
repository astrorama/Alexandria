/**
 * @file tests/src/lib/CosmologicalParameters_test.h
 * @date November 29, 2015
 * @author Florian Dubath
 */
#include <cmath>
#include <boost/test/unit_test.hpp>
#include "ElementsKernel/Real.h"
#include "PhysicsUtils/CosmologicalParameters.h"

using namespace Euclid;
using namespace PhysicsUtils;

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (CosmologicalParameters_test)

BOOST_AUTO_TEST_CASE(Constructor) {

  double H_0 = 70;
  for (int i = 0; i < 11; i++) {
    for (int j = 0; j < 11; j++) {
      double omega_m = i * 0.1;
      double omega_lambda = j * 0.1;

      auto cosmologicalParameters = CosmologicalParameters { omega_m,
          omega_lambda, H_0 };
      // check H_0
      BOOST_CHECK(
          Elements::isEqual(H_0, cosmologicalParameters.getHubbleConstant()));

      // Check the Omega parameters
      BOOST_CHECK(
          Elements::isEqual(omega_m, cosmologicalParameters.getOmegaM()));
      BOOST_CHECK(
          Elements::isEqual(omega_lambda,
              cosmologicalParameters.getOmegaLambda()));
      BOOST_CHECK(
          Elements::isEqual(1 - omega_m - omega_lambda,
              cosmologicalParameters.getOmegaK()));

      // check again the sum
      BOOST_CHECK(
          Elements::isEqual(1.0,
              cosmologicalParameters.getOmegaM()
                  + cosmologicalParameters.getOmegaLambda()
                  + cosmologicalParameters.getOmegaK()));
    }
  }

}

BOOST_AUTO_TEST_SUITE_END ()

