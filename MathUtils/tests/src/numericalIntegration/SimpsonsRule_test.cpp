/**
 * @file tests/src/interpolation/Linear_test.cpp
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Real.h"
#include "MathUtils/numericalIntegration/SimpsonsRule.h"

struct simpsonsRule_Fixture {
  Euclid::MathUtils::SimpsonsRule integrator_functor{};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (simpsonsRule_test)

BOOST_FIXTURE_TEST_CASE(error_test, simpsonsRule_Fixture) {
  BOOST_CHECK_THROW(integrator_functor([](double) { return 1.; },0.,1.,0), Elements::Exception );
  BOOST_CHECK_THROW(integrator_functor([](double) { return 1.; },0.,1.,1), Elements::Exception );
  BOOST_CHECK_THROW(integrator_functor([](double) { return 1.; },0.,1.,2), Elements::Exception );
  BOOST_CHECK_NO_THROW(integrator_functor([](double) { return 1.; },0.,1.,3));
  BOOST_CHECK_NO_THROW(integrator_functor([](double) { return 1.; },0.,1.,4));
  BOOST_CHECK_NO_THROW(integrator_functor([](double) { return 1.; },0.,1.,5));


  BOOST_CHECK_THROW(integrator_functor([](double) { return 1.; },0.,1.,1.,2), Elements::Exception );
  BOOST_CHECK_THROW(integrator_functor([](double) { return 1.; },0.,1.,1.,3), Elements::Exception );
  BOOST_CHECK_NO_THROW(integrator_functor([](double) { return 1.; },0.,1.,1.,4));
  BOOST_CHECK_NO_THROW(integrator_functor([](double) { return 1.; },0.,1.,1.,5));
}


BOOST_FIXTURE_TEST_CASE(Linear, simpsonsRule_Fixture) {
  double result = integrator_functor([](double) { return 1.; },0.,1.,3);
  BOOST_CHECK(Elements::isEqual(result,1.));

  result = integrator_functor([](double x) { return x; },0.,1.,3);
  BOOST_CHECK(Elements::isEqual(result,0.5));

  result = integrator_functor([](double x) { return x; },-1.,1.,3);
  BOOST_CHECK(Elements::isEqual(result,0.));
}

BOOST_FIXTURE_TEST_CASE(quadratic, simpsonsRule_Fixture) {
  double result = integrator_functor([](double x) { return x*x; },0.,1.,3);
  BOOST_CHECK(Elements::isEqual(result,1./3.));
}

BOOST_FIXTURE_TEST_CASE(cubic, simpsonsRule_Fixture) {
  double result = integrator_functor([](double x) { return x*x*x; },0.,1.,3);
  BOOST_CHECK(Elements::isEqual(result,1./4.));
}

BOOST_FIXTURE_TEST_CASE(recursion, simpsonsRule_Fixture) {
  double result_3 = integrator_functor([](double x) { return x*x*x; },0.,1.,3);
  double result_4 = integrator_functor([](double x) { return x*x*x; },0.,1.,4);
  double result_rec = integrator_functor([](double x) { return x*x*x; },0.,1.,result_3,4);
  BOOST_CHECK(Elements::isEqual(result_rec,result_4));
}

BOOST_FIXTURE_TEST_CASE(exp_decr, simpsonsRule_Fixture) {
  double result = integrator_functor([](double x) { return exp(-x); },0.,1.,3);
  double expected = (1.-exp(-1.));
  BOOST_CHECK((result-expected)/expected<0.00001);
  result = integrator_functor([](double x) { return exp(-x); },0.,1.,4);
  BOOST_CHECK((result-expected)/expected<0.000001);
}


//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
