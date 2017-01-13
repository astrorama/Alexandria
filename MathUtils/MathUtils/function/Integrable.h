/** 
 * @file MathUtils/function/Integrable.h
 * @date February 18, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef MATHUTILS_INTEGRABLE_H
#define	MATHUTILS_INTEGRABLE_H

#include "MathUtils/function/Function.h"

namespace Euclid {
namespace MathUtils {

/**
 * @interface Integrable
 * 
 * @brief Interface representing an integrable function
 * 
 * @details
 * A function is integrable when there is a fast analytical way to calculate
 * its integral (as opposed to a numerical calculation). The implementations
 * of this interface should provide this calculation by implementing the
 * integrate() method.
 */
class Integrable : public Function {
  
public:
  
  /// Default destructor
  virtual ~Integrable() = default;
  
  /**
   * Calculates the integral of the function in the range [a,b].
   * @param a The lower bound of the integration
   * @param b The upper bound of the integration
   * @return The integral of the function in the range [a,b]
   */
  virtual double integrate(const double a, const double b) const = 0;
};

} // End of MathUtils
} // end of namespace Euclid

#endif	/* MATHUTILS_INTEGRABLE_H */

