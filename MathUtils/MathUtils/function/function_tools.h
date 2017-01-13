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
 * Returns the integral of the given function inside the range [min,max]. This
 * method will take advantage of Function%s which also implement the
 * Integrable interface. Note that at the moment there is no default numerical
 * implementation yet, so if the given function is not Integrable an exception
 * will be thrown.
 * @param function The function to integrate
 * @param min The minimum range of the integration
 * @param max The maximum range of the integration
 * @return The integral in the range [min,max]
 */
ELEMENTS_API double integrate(const Function& function, const double min, const double max);

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

