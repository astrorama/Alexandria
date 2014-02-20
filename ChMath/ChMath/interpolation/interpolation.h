/** 
 * @file interpolation.h
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef INTERPOLATION_H
#define	INTERPOLATION_H

#include <memory>
#include <vector>
#include "ChMath/function/Function.h"

namespace ChMath {

std::unique_ptr<Function> linearInterpolation(const std::vector<double>& x, const std::vector<double>& y);

std::unique_ptr<Function> splineInterpolation(const std::vector<double>& x, const std::vector<double>& y);

} // End of ChMath

#endif	/* INTERPOLATION_H */

