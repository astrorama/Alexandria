/*
 * SimpsonsRule.h
 *
 *  Created on: Jul 2, 2015
 *      Author: fdubath
 */

#ifndef MATHUTILS_MATHUTILS_NUMERCALINTEGRATION_SIMPSONSRULE_H_
#define MATHUTILS_MATHUTILS_NUMERCALINTEGRATION_SIMPSONSRULE_H_

#include <functional>

namespace Euclid {
namespace MathUtils {

/**
 * @class SimpsonsRule
 * @details
 * Implement numerical integration based on the fit of a polynom of degree 3 on
 * 4 successive dots. For polynom of degree 3 the integration is exact even at low order.
 * The formula is taken from "Numerical Recipes" (Third edition)
 * W.H.Press, S.A.Teukolsky, A.T. Vetterling & B.P. Flannery. p160 Equ 4.1.14.
 * With a shift in the notation N-1 -> N. As we use N = 2^m where we call m the order.
 * One may compute the approximation at order = m+1 by adding only the missing
 * terms and thus deducting by ~2 the computational cost.
 *
 */
class SimpsonsRule {

public:
  const static int minimal_order =3;
  /**
   * @breif
   * Integrate a function between x_min and x_max using a mesh of 2^order steps. order>=3
   *
   * @param f
   * the R-valued function to be integrated.
   *
   * @param x_min
   * the lower bound of the integration domain
   *
   * @param x_max
   * the upper bound of the integration domain
   *
   * @param order
   * the order of the approximation the mesh used to compute the integration will have 2^order step
   */
  double operator()(const std::function<double(double)>& f,double x_min, double x_max, int order);

  /**
   * Integrate a function between x_min and x_max using a mesh of 2^order steps
   * based on the value at the previous order order>=4
   */
  double operator()(const std::function<double(double)>& f,double x_min, double x_max, double previous_value, int order);

};

}
}


#endif /* MATHUTILS_MATHUTILS_NUMERCALINTEGRATION_SIMPSONSRULE_H_ */
