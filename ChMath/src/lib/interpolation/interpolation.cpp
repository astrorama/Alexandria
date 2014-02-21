/** 
 * @file interpolation.cpp
 * @date February 21, 2014
 * @author Nikolaos Apostolakos
 */

#include "ChMath/interpolation/interpolation.h"
#include "implementations.h"

namespace ChMath {

std::unique_ptr<Function> interpolate(const std::vector<double>& x, const std::vector<double>& y, InterpolationType type) {
  switch (type) {
  case InterpolationType::LINEAR:
    return linearInterpolation(x, y);
  case InterpolationType::CUBIC_SPLINE:
    return splineInterpolation(x, y);
  }
  return nullptr;
}

} // End of ChMath