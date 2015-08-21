/*
 * Cosmology.cpp
 *
 *  Created on: Jul 1, 2015
 *      Author: fdubath
 */
#include <cmath>
#include "PhysicsUtils/Cosmology.h"
#include "ElementsKernel/PhysConstants.h"
#include "ElementsKernel/Real.h"
#include "MathUtils/numericalIntegration/IntegrationWithMeshRefinement.h"
#include "MathUtils/numericalIntegration/SimpsonsRule.h"
using std::abs;
using std::sqrt;
using std::sinh;
using std::sin;

namespace Euclid {
namespace PhysicsUtils {


Cosmology::Cosmology(double omega_m,
                     double omega_lambda,
                     double hubble_constant) : m_omega_m{omega_m},
                                               m_omega_lambda{omega_lambda},
                                               m_omega_k{1.0-omega_m-omega_lambda}{

 m_d_H = Elements::Units::c_light * 1E3 / hubble_constant; // in [pc]
}


double Cosmology::getOmegaM() const{
  return m_omega_m;
}

double Cosmology::getOmegaLambda() const{
  return m_omega_lambda;
}

double Cosmology::getOmegaK() const{
  return m_omega_k;
}

double Cosmology::getHubbleDistance() const{
  return m_d_H;
}

double Cosmology::hubbleParameter(double z) const{
  auto sqr=(1.+z)*(1.+z);
  return sqrt(m_omega_m*sqr*(1.+z)+m_omega_k*sqr+m_omega_lambda);
}

double Cosmology::comovingDistance(double z) const{
   MathUtils::IntegrationWithMeshRefinement<Euclid::MathUtils::SimpsonsRule> integraton_functor{m_relative_precision,Euclid::MathUtils::SimpsonsRule::minimal_order};

   return m_d_H*integraton_functor([this](double x) {return 1./hubbleParameter(x);},0.,z);
}

double Cosmology::transverseComovingDistance(double z) const{
  double comoving = comovingDistance(z);
  if (Elements::isEqual(0.,m_omega_k)){
    return comoving;
  }

  double dHOverSqrtOmegaK = m_d_H/sqrt(abs(m_omega_k));

  if (m_omega_k>0){
    return dHOverSqrtOmegaK*sinh(comoving/dHOverSqrtOmegaK);
  } else {
    return dHOverSqrtOmegaK*sin(comoving/dHOverSqrtOmegaK);
  }
}

double Cosmology::luminousDistance(double z) {
  auto map_iter = m_Luminous_distance_cache.find(z);
   if (map_iter != m_Luminous_distance_cache.end()){
     return map_iter->second;
   }

   double ld = (1.+z)*transverseComovingDistance(z);

   m_Luminous_distance_cache.insert(std::make_pair(z,ld));

   return ld;
}


double Cosmology::DistanceModulus(double z){
  auto map_iter = m_distance_modulus_cache.find(z);
  if (map_iter != m_distance_modulus_cache.end()){
    return map_iter->second;
  }

  double dm = 5.*std::log10(luminousDistance(z)/10);

  m_distance_modulus_cache.insert(std::make_pair(z,dm));

  return dm;
}


}
}
