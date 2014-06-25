/** 
 * @file ChMath/function/function_tools.h
 * @date February 19, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATH_FUNCTION_TOOLS_H
#define	CHMATH_FUNCTION_TOOLS_H

#include "ChMath/function/Function.h"

namespace ChMath {

double integrate(const Function& function, const double min, const double max);

std::unique_ptr<Function> multiply(const Function&, const Function&);

} // End of ChMath

#endif	/* CHMATH_FUNCTION_TOOLS_H */

