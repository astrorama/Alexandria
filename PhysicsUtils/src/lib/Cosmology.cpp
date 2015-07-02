/*
 * Cosmology.cpp
 *
 *  Created on: Jul 1, 2015
 *      Author: fdubath
 */
#include <cmath>
#include "PhysicsUtils/Cosmology.h"
#include "ElementsKernel/PhysConstants.h"
#include "MathUtils/numericalIntegration/IntegrationWithMeshRefinement.h"
#include "MathUtils/numericalIntegration/SimpsonsRule.h"

namespace Euclid {
namespace PhysicsUtils {


Cosmology::Cosmology(double omega_m,
                     double omega_lambda,
                     double hubble_constant) : m_omega_m{omega_m},
                                               m_omega_lambda{omega_lambda},
                                               m_omega_k{1.0-omega_m-omega_lambda}{

 m_d_H = Elements::Units::c_light * 3.6E6 / hubble_constant;
}


double Cosmology::getOmegaM(){
  return m_omega_m;
}

double Cosmology::getOmegaLambda(){
  return m_omega_lambda;
}

double Cosmology::getOmegaK(){
  return m_omega_k;
}

double Cosmology::getHubbleDistance(){
  return m_d_H;
}

double Cosmology::hubbleParameter(double z){
  auto sqr=(1.+z)*(1.+z);
  return sqrt(m_omega_m*sqr*(1.+z)+m_omega_k*sqr+m_omega_lambda);
}

double Cosmology::comovingDistance(double z){
   MathUtils::IntegrationWithMeshRefinement<Euclid::MathUtils::SimpsonsRule> integraton_functor{m_relative_precision,Euclid::MathUtils::SimpsonsRule::minimal_order};

   return m_d_H*integraton_functor([this](double x) {return 1./hubbleParameter(x);},0.,z);
}

double Cosmology::transverseComovingDistance(double z){
  return 1.;
}

double Cosmology::luminousDistance(double z){
  return 1.;
}



}
}
