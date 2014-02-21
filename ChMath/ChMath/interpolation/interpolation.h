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

enum class InterpolationType {
  LINEAR, CUBIC_SPLINE
};

std::unique_ptr<Function> interpolate(const std::vector<double>& x, const std::vector<double>& y, InterpolationType type);

} // End of ChMath

#endif	/* INTERPOLATION_H */

