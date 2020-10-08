/*
 * Copyright (C) 2012-2020 Euclid Science Ground Segment
 *
 * This library is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free
 * Software Foundation; either version 3.0 of the License, or (at your option)
 * any later version.
 *
 * This library is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
 * details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this library; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 */

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
class CosmologicalParameters {
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

}  // namespace PhysicsUtils
}  // namespace Euclid
#endif /* PHYSICSUTILS_PHYSICSUTILS_COSMOLOGICALPARAMETERS_H_ */
