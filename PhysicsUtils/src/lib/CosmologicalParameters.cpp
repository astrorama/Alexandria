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
 * @file src/lib/CosmologicalParameters.h
 * @date November 29, 2015
 * @author Florian Dubath
 */

#include "PhysicsUtils/CosmologicalParameters.h"

namespace Euclid {
namespace PhysicsUtils {

CosmologicalParameters::CosmologicalParameters(double omega_m, double omega_lambda, double hubble_constant)
    : m_omega_m{omega_m}, m_omega_lambda{omega_lambda}, m_omega_k{1.0 - omega_m - omega_lambda}, m_H_0{hubble_constant} {}

double CosmologicalParameters::getOmegaM() const {
  return m_omega_m;
}

double CosmologicalParameters::getOmegaLambda() const {
  return m_omega_lambda;
}

double CosmologicalParameters::getOmegaK() const {
  return m_omega_k;
}

double CosmologicalParameters::getHubbleConstant() const {
  return m_H_0;
}

}  // namespace PhysicsUtils
}  // namespace Euclid
