/*
 * Cosmology.h
 *
 *  Created on: Jul 1, 2015
 *      Author: fdubath
 */

#ifndef PHYSICSUTILS_PHYSICSUTILS_COSMOLOGY_H_
#define PHYSICSUTILS_PHYSICSUTILS_COSMOLOGY_H_

#include <map>

namespace Euclid {
namespace PhysicsUtils {



/**
 * @class Cosmology
 *
 * @brief Model the cosmology and compute the distances according to it.
 */
class Cosmology{
public:
  /**
   * @brief Constructor taking the cosmology parameters
   *
   * @param omega_m
   * Omega Matter
   *
   * @param omega_lambda
   * Omega Lambda
   *
   * @param hubble_constant
   * H_0 in (km/s)/Mpc
   */
  Cosmology(double omega_m = 0.3089, double omega_lambda = 0.6911, double hubble_constant = 67.74);

  virtual ~Cosmology() = default;

  /**
   * @brief Get Omega matter for the cosmology
   */
  double getOmegaM() const;

  /**
   * @brief Get Omega Lambda for the cosmology
   */
  double getOmegaLambda() const;

  /**
   * @brief Get the (computed) Omega curvature for the cosmology
   */
  double getOmegaK() const;

  /**
   * @brief Get the computed Hubble distance for the cosmology.
   * @return the Hubble distance in [pc]
   */
  double getHubbleDistance() const;

  /**
   * @brief Returns the (unit-less) Hubble parameter E(z)
   */
  double hubbleParameter(double z) const;

  /**
   * @brief return the comoving distance in [pc]
   */
  double comovingDistance(double z) const;

  /**
    * @brief return the transverse comoving distance in [pc]
    */
  double transverseComovingDistance(double z) const;

  /**
    * @brief return the luminous distance in [pc]
    */
  double luminousDistance(double z) const;

  /**
   * @brief return the correction for the Magnitude due to the distance:
   * DM =5*log_10(DL/10pc)
   */
  double DistanceModulus(double z) const;

private:
  size_t m_hash;
  double m_omega_m;
  double m_omega_lambda;
  double m_omega_k;
  double m_d_H;

  // for the integration
  double m_relative_precision = 0.0000001;

//  mutable std::map<double,double> m_Luminous_distance_cache{{0.,10.}};
//  mutable std::map<double,double> m_distance_modulus_cache{{0.,0.}};


};

}
}
#endif /* PHYSICSUTILS_PHYSICSUTILS_COSMOLOGY_H_ */
