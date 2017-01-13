/**
 * @file MathUtils/function/function_tools.h
 * @date February 19, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef MATHUTILS_FUNCTION_TOOLS_H
#define	MATHUTILS_FUNCTION_TOOLS_H

#include "ElementsKernel/Export.h"

#include "MathUtils/function/Function.h"

namespace Euclid {
namespace MathUtils {

/**
 * @interface NumericalIntegrationScheme
 *
 * @brief Interface class representing a numerical integration scheme
 *
 * @details
 * A NumericalIntegrationScheme is an object which can return the definite
 * integral of a Function object over the range [min,max].
 */
class NumericalIntegrationScheme {

public:
  /// Default destructor
  virtual ~NumericalIntegrationScheme() = default;

  /**
   * Compute (numerically) the integral of the function on the provided interval.
   * @param function the Function to integrate.
   * @param min The minimum range of the integration.
   * @param max The maximum range of the integration.
   */
  virtual double operator()(const Function& function, double min, double max) = 0;
};

/**
 * Returns the integral of the given function inside the range [min,max]. This
 * method will take advantage of Function%s which also implement the
 * Integrable interface. For other Function the integration will be delegated to
 * the NumericalIntegrationScheme. Note that at the moment there is no default
 * numerical implementation, so if the given function is not Integrable and
 * no numerical integration scheme is provided an exception will be thrown.
 * @param function The function to integrate
 * @param min The minimum range of the integration
 * @param max The maximum range of the integration
 * @param numericalIntegrationScheme The class in charge of the numerical
 * integration (if the function do not implement the Integrable interface).
 * @return The integral in the range [min,max]
 */
ELEMENTS_API double integrate(const Function& function,
                              const double min,
                              const double max,
                              std::unique_ptr<NumericalIntegrationScheme> numericalIntegrationScheme = nullptr);

/**
 * Returns a function which represents the multiplication of the two parameters.
 * This method makes use of the multiplySpecificSpecificMap and multiplySpecificGenericMap
 * maps for detecting efficient ways of multiplying the parameters.
 * @param f1 The first function to multiply
 * @param f2 The second function to multiply
 * @return A function representing the multiplication of the parameters
 */
ELEMENTS_API std::unique_ptr<Function> multiply(const Function& f1, const Function& f2);

} // End of MathUtils
} // end of namespace Euclid

#endif	/* MATHUTILS_FUNCTION_TOOLS_H */

