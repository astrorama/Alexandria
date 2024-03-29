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
 * @file src/lib/CosmologicalDistances.h
 * @date November 29, 2015
 * @author Florian Dubath
 */
#include <cmath>

#include "ElementsKernel/PhysConstants.h"
#include "ElementsKernel/Real.h"

#include "MathUtils/function/FunctionAdapter.h"
#include "MathUtils/function/function_tools.h"
#include "MathUtils/numericalIntegration/AdaptativeIntegration.h"
#include "MathUtils/numericalIntegration/SimpsonsRule.h"

#include "PhysicsUtils/CosmologicalDistances.h"

namespace Euclid {
namespace PhysicsUtils {

double CosmologicalDistances::hubbleDistance(const CosmologicalParameters& parameters) const {
  return Elements::Units::c_light * 1.0E3 / parameters.getHubbleConstant();  // in [pc]
}

double CosmologicalDistances::hubbleParameter(double z, const CosmologicalParameters& parameters) const {
  double square = (1. + z) * (1. + z);
  double cube   = square * (1. + z);
  return std::sqrt(parameters.getOmegaM() * cube + parameters.getOmegaK() * square + parameters.getOmegaLambda());
}

double CosmologicalDistances::comovingDistance(double z, const CosmologicalParameters& parameters,
                                               double relative_precision) const {
  if (Elements::isEqual(0., z)) {
    return 0.;
  }

  std::unique_ptr<MathUtils::NumericalIntegrationScheme> integrationScheme{
      new MathUtils::AdaptativeIntegration<MathUtils::SimpsonsRule>(relative_precision,
                                                                    MathUtils::SimpsonsRule::minimal_order)};

  MathUtils::FunctionAdapter adpater([&parameters, this](double x) { return 1. / hubbleParameter(x, parameters); });

  return hubbleDistance(parameters) * integrate(adpater, 0., z, std::move(integrationScheme));
}

double CosmologicalDistances::transverseComovingDistance(double z, const CosmologicalParameters& parameters) const {
  double comoving = comovingDistance(z, parameters);
  if (Elements::isEqual(0., parameters.getOmegaK())) {
    return comoving;
  }

  double dHOverSqrtOmegaK = hubbleDistance(parameters) / std::sqrt(std::abs(parameters.getOmegaK()));

  if (parameters.getOmegaK() > 0) {
    return dHOverSqrtOmegaK * std::sinh(comoving / dHOverSqrtOmegaK);
  } else {
    return dHOverSqrtOmegaK * std::sin(comoving / dHOverSqrtOmegaK);
  }
}

double CosmologicalDistances::luminousDistance(double z, const CosmologicalParameters& parameters) const {
  if (Elements::isEqual(0., z)) {
    return 10.;
  } else {
    return (1. + z) * transverseComovingDistance(z, parameters);
  }
}

double CosmologicalDistances::distanceModulus(double z, const CosmologicalParameters& parameters) const {
  return 5. * std::log10(luminousDistance(z, parameters) / 10.);
}

double CosmologicalDistances::dimensionlessComovingVolumeElement(double                        z,
                                                                 const CosmologicalParameters& parameters) const {
  double D_H = hubbleDistance(parameters);
  double E   = hubbleParameter(z, parameters);
  double D_M = transverseComovingDistance(z, parameters);
  return D_M * D_M / (E * D_H * D_H);
}

}  // namespace PhysicsUtils
}  // namespace Euclid
