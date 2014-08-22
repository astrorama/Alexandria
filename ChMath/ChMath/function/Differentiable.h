/**
 * @file ChMath/function/Differentiable.h
 * @date February 18, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATH_DIFFERENTIABLE_H
#define	CHMATH_DIFFERENTIABLE_H

#include <memory>

#include "ElementsKernel/Export.h"

#include "ChMath/function/Integrable.h"

namespace Euclid {
namespace ChMath {

/**
 * @interface Differentiable
 *
 * @brief Interface representing a differentiable function
 *
 * @details
 * A function is differentiable if its derivative and indefinite integrals can
 * be calculated in a fast, analytical way. The implementations of this
 * interface should implement the derivative() and indefiniteIntegral() functions
 * accordingly. Note that the Differentiable class implements the Integrable
 * interface by using the indefiniteIntegral().
 */
class ELEMENTS_API Differentiable : public Integrable {

public:

  /// Default destructor
  virtual ~Differentiable() {}

  /// Returns a Function representing the derivative
  virtual std::shared_ptr<Function> derivative() const = 0;

  /// Returns a Function representing the indefiniteIntegral
  virtual std::shared_ptr<Function> indefiniteIntegral() const = 0;

  /**
   * Calculates the integral in the range [x1,x2], by using the indefinite
   * integral.
   * @param x1 The lower bound of the integration
   * @param x2 The upper bound of the integration
   * @return The integral in the range [x1,x2]
   */
  double integrate(const double x1, const double x2) const override final;
};

} // End of ChMath
} // end of namespace Euclid

#endif	/* CHMATH_DIFFERENTIABLE_H */

