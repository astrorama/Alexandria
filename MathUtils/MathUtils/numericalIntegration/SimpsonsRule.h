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
 * @file MathUtils/numericalIntegration/SimpsonsRule.h
 * @date July 2, 2015
 * @author Florian Dubath
 */

#ifndef MATHUTILS_MATHUTILS_NUMERCALINTEGRATION_SIMPSONSRULE_H_
#define MATHUTILS_MATHUTILS_NUMERCALINTEGRATION_SIMPSONSRULE_H_

#include "MathUtils/function/Function.h"

namespace Euclid {
namespace MathUtils {

/**
 * @class SimpsonsRule
 *
 * @details
 * Implement numerical integration (quadrature) based on the fit of a polynom of
 * degree 3 on 4 successive points.
 * For polynome of degree 3 the integration is exact even at low order.
 * The formula is taken from "Numerical Recipes" (Third edition)
 * W.H.Press, S.A.Teukolsky, A.T. Vetterling & B.P. Flannery. p160 Equ 4.1.14.
 * With a shift in the notation N-1 -> N. As we use N = 2^m where we call m the order.
 * One may compute the approximation at order = m+1 by adding only the missing
 * terms and thus deducting by ~2 the computational cost.
 * Note that at order m there is (2^m)+1 evaluations of the function for the direct case
 * and (2^(m-1))+4 in the case where the result of the previous order is provided.
 */
class SimpsonsRule {

public:
  const static int minimal_order = 3;
  /**
   * @brief Integrate a function between min and max using a mesh of 2^order steps. order>=3
   *
   * @param function
   * the R-valued function to be integrated.
   *
   * @param min
   * the lower bound of the integration domain
   *
   * @param max
   * the upper bound of the integration domain
   *
   * @param order
   * the order of the approximation.
   * The mesh used to compute the integration will have 2^order steps.
   */
  double operator()(const Function& function, double min, double max, int order);

  /**
   * @detail
   * Integrate a function between min and max using a mesh of 2^order steps
   * based on the value at the previous order (order>=4) by adding only the
   * difference between the integrals.
   *
   * @param function
   * the R-valued function to be integrated.
   *
   * @param min
   * the lower bound of the integration domain
   *
   * @param max
   * the upper bound of the integration domain
   *
   * @param order
   * the order of the approximation.
   * The mesh used to compute the integration will have 2^order steps.
   *
   * @param previous_value
   * The value of the integration at the previous order.
   */
  double operator()(const Function& function, double min, double max, double previous_value, int order);
};

}  // namespace MathUtils
}  // namespace Euclid

#endif /* MATHUTILS_MATHUTILS_NUMERCALINTEGRATION_SIMPSONSRULE_H_ */
