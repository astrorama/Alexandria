/**
 * @file src/lib/CosmologicalParameters.h
 * @date November 29, 2015
 * @author Florian Dubath
 */

#include "PhysicsUtils/CosmologicalParameters.h"

namespace Euclid {
namespace PhysicsUtils {

CosmologicalParameters::CosmologicalParameters(double omega_m,
                     double omega_lambda,
                     double hubble_constant) : m_omega_m{omega_m},
                                               m_omega_lambda{omega_lambda},
                                               m_omega_k{1.0-omega_m-omega_lambda},
                                               m_H_0{hubble_constant}{
}

double CosmologicalParameters::getOmegaM() const{
  return m_omega_m;
}

double CosmologicalParameters::getOmegaLambda() const{
  return m_omega_lambda;
}

double CosmologicalParameters::getOmegaK() const{
  return m_omega_k;
}

double CosmologicalParameters::getHubbleConstant() const{
  return m_H_0;
}


}
}
