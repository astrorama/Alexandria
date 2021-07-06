/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
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
 * @file PhysicsUtils/CosmologicalDistances.h
 * @date November 29, 2015
 * @author Florian Dubath
 */

#ifndef PHYSICSUTILS_PHYSICSUTILS_COSMOLOGICALDISTANCES_H_
#define PHYSICSUTILS_PHYSICSUTILS_COSMOLOGICALDISTANCES_H_

#include "PhysicsUtils/CosmologicalParameters.h"

namespace Euclid {
namespace PhysicsUtils {

/**
 * @class CosmologicalDistance
 *
 * @brief Compute the distances according to it. See http://xxx.lanl.gov/abs/astro-ph/9905116
 */
class CosmologicalDistances {
public:
  virtual ~CosmologicalDistances() = default;

  /**
   * @brief Get the computed Hubble distance for the cosmology.
   *
   * @param parameters The cosmological parameters the distance has to be computed for.
   *
   * @return the Hubble distance in [pc]
   */
  double hubbleDistance(const CosmologicalParameters& parameters) const;

  /**
   * @brief Returns the (unit-less) Hubble parameter E(z)
   *
   * @param z The redshift for which the distance has to be computed.
   *
   * @param parameters The cosmological parameters the distance has to be computed for.
   */
  double hubbleParameter(double z, const CosmologicalParameters& parameters) const;

  /**
   * @brief return the comoving distance in [pc]. This value is obtained
   * through a numerical integration. The relative precision of the integration
   * can be specified and is defaulted to 0.00001%.
   *
   * @param z The redshift for which the distance has to be computed.
   *
   * @param parameters The cosmological parameters the distance has to be computed for.
   *
   * @param relative_precision The requested precision.
   *
   */
  double comovingDistance(double z, const CosmologicalParameters& parameters,
                          double relative_precision = 0.0000001) const;

  /**
   * @brief return the transverse comoving distance in [pc]
   *
   * @param z The redshift for which the distance has to be computed.
   *
   * @param parameters The cosmological parameters the distance has to be computed for.
   */
  double transverseComovingDistance(double z, const CosmologicalParameters& parameters) const;

  /**
   * @brief return the luminous distance in [pc]. For z=0 the returned value is 10pc.
   *
   * @param z The redshift for which the distance has to be computed.
   *
   * @param parameters The cosmological parameters the distance has to be computed for.
   */
  double luminousDistance(double z, const CosmologicalParameters& parameters) const;

  /**
   * @brief return the correction for the Magnitude due to the distance:
   * DM =5*log_10(DL/10pc)
   *
   * @param z The redshift for which the distance modulus has to be computed.
   *
   * @param parameters The cosmological parameters the distance has to be computed for.
   */
  double distanceModulus(double z, const CosmologicalParameters& parameters) const;

  /**
   * @brief return the dimensionless comoving volume element.
   *
   * @param z The redshift for which the volume element has to be computed.
   *
   * @param parameters The cosmological parameters the distance has to be computed for.
   */
  double dimensionlessComovingVolumeElement(double z, const CosmologicalParameters& parameters) const;
};

}  // namespace PhysicsUtils
}  // namespace Euclid
#endif /* PHYSICSUTILS_PHYSICSUTILS_COSMOLOGICALDISTANCES_H_ */
