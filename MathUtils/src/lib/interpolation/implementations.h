/** 
 * @file src/lib/interpolation/implementations.h
 * @date February 21, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef MATHUTILS_IMPLEMENTATIONS_H
#define	MATHUTILS_IMPLEMENTATIONS_H

namespace Euclid {
namespace MathUtils {

/// Performs linear interpolation for the given set of data points
std::unique_ptr<Function> linearInterpolation(const std::vector<double>& x, const std::vector<double>& y);

/// Performs cubic spline interpolation for the given set of data points
std::unique_ptr<Function> splineInterpolation(const std::vector<double>& x, const std::vector<double>& y);

} // End of MathUtils
} // end of namespace Euclid

#endif	/* MATHUTILS_IMPLEMENTATIONS_H */

