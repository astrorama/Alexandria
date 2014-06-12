/** 
 * @file implementations.h
 * @date February 21, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATH_IMPLEMENTATIONS_H
#define	CHMATH_IMPLEMENTATIONS_H

namespace ChMath {

std::unique_ptr<Function> linearInterpolation(const std::vector<double>& x, const std::vector<double>& y);

std::unique_ptr<Function> splineInterpolation(const std::vector<double>& x, const std::vector<double>& y);

} // End of ChMath

#endif	/* CHMATH_IMPLEMENTATIONS_H */

