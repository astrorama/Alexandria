
#include <cmath>
#include <boost/test/unit_test.hpp>
#include "ElementsKernel/Real.h"
#include "PhysicsUtils/Cosmology.h"
#include "MathUtils/numericalIntegration/IntegrationWithMeshRefinement.h"
#include "MathUtils/numericalIntegration/SimpsonsRule.h"
#include "ElementsKernel/PhysConstants.h"

using namespace Euclid;
using namespace PhysicsUtils;
using std::abs;
using std::sqrt;
using std::sin;
using std::sinh;
using Elements::isEqual;

struct Cosmology_Fixture {
  double omega_m =  0.2;
  double omega_lambda =  0.7;
  // so we expect omega_k to be 0.1 !=0
  double H_0=77.0;

  std::vector<double> zs{0,0.001,0.01,0.1,0.5,1.,1.5,2.,4.,6.};
  std::vector<double> hubble_parameters {1.,
                                 1.0004002699919667,
                                 1.0040269916690487,
                                 1.042688831818966,
                                 1.2649110640673518,
                                 1.6431676725154984,
                                 2.1095023109728985,
                                 2.6457513110645907,
                                 5.3103672189407014,
                                 8.6139421869432127
                               };
  std::vector<double> comoving {0.,
                                3892629.7211428746,
                                38856076.082309492,
                                381426775.30670536,
                                1743252275.3547294,
                                3097511958.8287911,
                                4144034048.8586593,
                                4968125488.521699,
                                7037575806.8509665,
                                8185617947.9015932
                               };
  std::vector<double> luminous {10.,
                                4429033.2516768286,
                                44595140.97263521,
                                475341190.49684501,
                                2918477377.0888844,
                                6792421919.9330025,
                                11199033877.97576,
                                15937134721.927008,
                                36706225562.921059 ,
                                59064863879.408623
                               };
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Cosmology_test)

BOOST_FIXTURE_TEST_CASE(Constructor, Cosmology_Fixture) {
 auto cosmology = Cosmology{omega_m,omega_lambda,H_0};

 // Check the Omega parameters
 BOOST_CHECK(isEqual(omega_m, cosmology.getOmegaM()));
 BOOST_CHECK(isEqual(omega_lambda, cosmology.getOmegaLambda()));
 BOOST_CHECK(isEqual(1.0, cosmology.getOmegaM() + cosmology.getOmegaLambda() + cosmology.getOmegaK()));

 // check the Hubble distance
 auto d_h= 2.99792458e+11/H_0; // in [pc]
 BOOST_CHECK(isEqual(d_h, cosmology.getHubbleDistance()));
}




BOOST_FIXTURE_TEST_CASE(hubble_parameter, Cosmology_Fixture) {

  std::vector<double> result_1 {1.,
                                1.0015003749375231,
                                1.0150374377332099,
                                1.1536897329871669,
                                1.8371173070873836,
                                2.8284271247461903,
                                3.9528470752104741,
                                5.196152422706632,
                                11.180339887498949,
                                18.520259177452136
                              };
 // check the limit cases
 auto cosmology = Cosmology{1.,0.,H_0};
 for (size_t i=0; i<zs.size();++i){
   BOOST_CHECK(isEqual(result_1[i], cosmology.hubbleParameter(zs[i])));
 }

 cosmology = Cosmology{0.,0.,H_0};
 for (size_t i=0; i<zs.size();++i){
   BOOST_CHECK(isEqual(1.+zs[i], cosmology.hubbleParameter(zs[i])));
 }

 cosmology = Cosmology{0.,1.,H_0};
 for (size_t i=0; i<zs.size();++i){
   BOOST_CHECK(isEqual(1., cosmology.hubbleParameter(zs[i])));
 }

 cosmology = Cosmology{omega_m,omega_lambda,H_0};
 auto omega_k = cosmology.getOmegaK();
 for (size_t i=0; i<zs.size();++i){
   BOOST_CHECK(isEqual(hubble_parameters[i], cosmology.hubbleParameter(zs[i])));
 }
}


BOOST_FIXTURE_TEST_CASE(comoving_distance, Cosmology_Fixture) {
  auto cosmology = Cosmology{omega_m,omega_lambda,H_0};
  for (size_t i=0; i<zs.size();++i){
    BOOST_CHECK(isEqual(comoving[i],cosmology.comovingDistance(zs[i])));

  }
}

BOOST_FIXTURE_TEST_CASE(transverse_comoving_distance, Cosmology_Fixture) {
  // case with negative omega_k
  auto cosmology = Cosmology{omega_m,1.1-omega_m,H_0};
  BOOST_CHECK(cosmology.getOmegaK()<0);
  BOOST_CHECK(isEqual(4423595310.7368011,cosmology.transverseComovingDistance(1.5)));

  // case with 0 omega_k
  cosmology = Cosmology{omega_m,1.0-omega_m,H_0};
  BOOST_CHECK(isEqual(cosmology.getOmegaK(),0.));
  BOOST_CHECK(isEqual(4319113837.9162245,cosmology.transverseComovingDistance(1.5)));

  // case with positive omega_k
  cosmology = Cosmology{omega_m,0.9-omega_m,H_0};
  BOOST_CHECK(cosmology.getOmegaK()>0);
  BOOST_CHECK(isEqual(4222723848.5923686,cosmology.transverseComovingDistance(1.5)));
}

BOOST_FIXTURE_TEST_CASE(luminous_distance, Cosmology_Fixture) {
  auto cosmology = Cosmology{};
  for (size_t i=0; i<zs.size();++i){
    BOOST_CHECK(isEqual(luminous[i],cosmology.luminousDistance(zs[i])));
  }
}

BOOST_FIXTURE_TEST_CASE(DM_test, Cosmology_Fixture) {
  auto cosmology = Cosmology{};
  BOOST_CHECK(isEqual(44.415392424409184,cosmology.distanceModulus(1.1)));
  BOOST_CHECK_EQUAL(cosmology.distanceModulus(0.),0.);
}

//BOOST_FIXTURE_TEST_CASE(export_data, Cosmology_Fixture) {
//  auto cosmology = Cosmology{0.25,0.75,70.};
//
//
//  std::cout<<cosmology.getHubbleDistance();
//  for (auto z=0;z<6000;z++){
//    std::cout<<z/1000.<<" "<<cosmology.comovingDistance(z/1000.)<<" "<<cosmology.luminousDistance(z/1000.)<< " "<<cosmology.DistanceModulus(z/1000.)<<"\n";
//  }
//}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


