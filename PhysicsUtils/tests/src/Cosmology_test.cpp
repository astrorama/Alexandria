
#include <cmath>
#include <boost/test/unit_test.hpp>
#include "ElementsKernel/Real.h"
#include "PhysicsUtils/Cosmology.h"
#include "MathUtils/numericalIntegration/IntegrationWithMeshRefinement.h"
#include "MathUtils/numericalIntegration/SimpsonsRule.h"
#include "ElementsKernel/PhysConstants.h"

using namespace Euclid;
using namespace PhysicsUtils;


struct Cosmology_Fixture {
  double omega_m =  0.2;
  double omega_lambda =  0.7;
  // so we expect omega_k to be 0.1 !=0
  double H_0=77.0;

  double E(double O_m, double O_l, double O_k, double z){
    return sqrt(pow(1.+z,3)*O_m+pow(1.+z,2)*O_k+O_l);
  }


};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Cosmology_test)

//-----------------------------------------------------------------------------
// Test that the integration uses the indefinite integral
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Constructor, Cosmology_Fixture) {
 auto cosmology = Cosmology{omega_m,omega_lambda,H_0};

 // Check the Omega parameters
 BOOST_CHECK(Elements::isEqual(omega_m,cosmology.getOmegaM()));
 BOOST_CHECK(Elements::isEqual(omega_lambda,cosmology.getOmegaLambda()));
 BOOST_CHECK(Elements::isEqual(1.0,cosmology.getOmegaM()+cosmology.getOmegaLambda()+cosmology.getOmegaK()));

 // check the Hubble distance
 auto H_0_pc = H_0*(Elements::Units::kilometer/3600.)/(1.0E6); // H_O in [(m/s)/pc]
 auto d_h= Elements::Units::c_light/H_0_pc; // in [pc]

 BOOST_CHECK(Elements::isEqual(d_h,cosmology.getHubbleDistance()));
}

BOOST_FIXTURE_TEST_CASE(hubble_parameter, Cosmology_Fixture) {

 // check the limit cases
 auto cosmology = Cosmology{1.,0.,H_0};
 for (auto z=0;z<6000;z++){
     BOOST_CHECK(Elements::isEqual(pow(1.+z/1000.,1.5),cosmology.hubbleParameter(z/1000.)));
 }

 cosmology = Cosmology{0.,0.,H_0};
 for (auto z=0;z<6000;z++){
      BOOST_CHECK(Elements::isEqual(1.+z/1000.,cosmology.hubbleParameter(z/1000.)));
 }

 cosmology = Cosmology{0.,1.,H_0};
 for (auto z=0;z<6000;z++){
      BOOST_CHECK(Elements::isEqual(1.,cosmology.hubbleParameter(z/1000.)));
 }

 cosmology = Cosmology{omega_m,omega_lambda,H_0};
 auto omega_k = cosmology.getOmegaK();
 for (auto z=0;z<6000;z++){
   BOOST_CHECK(Elements::isEqual(E(omega_m,omega_lambda,omega_k,z/1000.),cosmology.hubbleParameter(z/1000.)));
 }

}


BOOST_FIXTURE_TEST_CASE(comoving_distance, Cosmology_Fixture) {
  auto cosmology = Cosmology{omega_m,omega_lambda,H_0};
  for (auto z=0;z<6000;z++){

    auto comovingDistance_z=cosmology.comovingDistance(z/1000.);

    double omega_k= cosmology.getOmegaK();
    Euclid::MathUtils::IntegrationWithMeshRefinement<Euclid::MathUtils::SimpsonsRule> integrator{0.0000001,3};

    double integral = integrator([this,&omega_k](double x) { return 1/sqrt(pow(1.+x,3)*omega_m+pow(1.+x,2)*omega_k+omega_lambda);},0.,z/1000.);
    double expected = integral*cosmology.getHubbleDistance();
    BOOST_CHECK(Elements::isEqual(comovingDistance_z,expected));
  }

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


