/**
 * @file PhysicsUtils/CosmologicalParameters.h
 * @date November 29, 2015
 * @author Florian Dubath
 */

#ifndef PHYSICSUTILS_PHYSICSUTILS_COSMOLOGICALPARAMETERS_H_
#define PHYSICSUTILS_PHYSICSUTILS_COSMOLOGICALPARAMETERS_H_

namespace Euclid {
namespace PhysicsUtils {

/**
 * @class CosmologicalParameters
 *
 * @brief Model the cosmological parameters.
 * Omega_m, Omega_lambda, Omega_k and hubble_constant.
 * Guarantee that the sum of the Omegas is 1
 */
class CosmologicalParameters{
public:
  /**
   * @brief Constructor taking the cosmologycal parameters
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
  CosmologicalParameters(double omega_m = 0.3089, double omega_lambda = 0.6911, double hubble_constant = 67.74);

  virtual ~CosmologicalParameters() = default;

  /**
   * @brief Get Omega matter for the cosmology
   */
  double getOmegaM() const;

  /**
   * @brief Get Omega Lambda for the cosmology
   */
  double getOmegaLambda() const;

  /**
   * @brief Get the Omega curvature (computed as 1 - Omega_m - Omega_L) for the cosmology
   */
  double getOmegaK() const;

  /**
   * @brief Get the Hubble constant H_0 in (km/s)/Mpc
   */
  double getHubbleConstant() const;


private:
  double m_omega_m;
  double m_omega_lambda;
  double m_omega_k;
  double m_H_0;
};

}
}
#endif /* PHYSICSUTILS_PHYSICSUTILS_COSMOLOGICALPARAMETERS_H_ */
