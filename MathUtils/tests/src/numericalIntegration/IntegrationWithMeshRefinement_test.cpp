/**
 * @file tests/src/interpolation/Linear_test.cpp
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Real.h"
#include "MathUtils/numericalIntegration/IntegrationWithMeshRefinement.h"
#include "MathUtils/numericalIntegration/SimpsonsRule.h"

struct IntegrationWithMeshRefinement_Fixture {
  double precision = 0.00000001;
  Euclid::MathUtils::IntegrationWithMeshRefinement<Euclid::MathUtils::SimpsonsRule> integrator_functor{precision,3};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (IntegrationWithMeshRefinement_test)

BOOST_FIXTURE_TEST_CASE(error_test, IntegrationWithMeshRefinement_Fixture) {
    Euclid::MathUtils::SimpsonsRule simpsons_rule_functor{};
    double result = integrator_functor([](double x) { return exp(-x); },0.,1.);
    double expected = (1.-exp(-1.));
    BOOST_CHECK((result-expected)/expected<precision);

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
