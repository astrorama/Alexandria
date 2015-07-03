/*
 * Cosmology.h
 *
 *  Created on: Jul 1, 2015
 *      Author: fdubath
 */

#ifndef PHYSICSUTILS_PHYSICSUTILS_COSMOLOGY_H_
#define PHYSICSUTILS_PHYSICSUTILS_COSMOLOGY_H_

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
  double getOmegaM();

  /**
   * @brief Get Omega Lambda for the cosmology
   */
  double getOmegaLambda();

  /**
   * @brief Get the (computed) Omega curvature for the cosmology
   */
  double getOmegaK();

  /**
   * @brief Get the computed Hubble distance for the cosmology.
   * @return the Hubble distance in [pc]
   */
  double getHubbleDistance();

  /**
   * @brief Returns the (unit-less) Hubble parameter E(z)
   */
  double hubbleParameter(double z);

  /**
   * @brief return the comoving distance in [pc]
   */
  double comovingDistance(double z);

  /**
    * @brief return the transverse comoving distance in [pc]
    */
  double transverseComovingDistance(double z);

  /**
    * @brief return the luminous distance in [pc]
    */
  double luminousDistance(double z);

  /**
   * @brief return the correction for the Magnitude due to the distance:
   * DM =5*log_10(DL/10pc)
   */
  double DM(double z);

private:
  double m_omega_m;
  double m_omega_lambda;
  double m_omega_k;
  double m_d_H;

  // for the integration
  double m_relative_precision = 0.0000001;
};

}
}
#endif /* PHYSICSUTILS_PHYSICSUTILS_COSMOLOGY_H_ */
