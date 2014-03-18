/*
 * InterpolationFactory.cpp
 *
 *  Created on: Oct 17, 2013
 *      Author: admin
 */

#include "ElementsKernel/ElementsException.h"
#include "Faros/InterpolationFactory.h"

////////////////////////////////////////////////////////////////////////////////
//                            InterpolationFactory class
////////////////////////////////////////////////////////////////////////////////

BaseInterpolation* InterpolationFactory::getInterpolationFunction(const InterpolationMethod& method, const std::vector<double>& x, const std::vector<double>& y)
{
 // Todo how to use shared pointer
 BaseInterpolation* ptr = nullptr;

 switch(method)
 {
 case (InterpolationMethod::CUBIC):
    ptr = new CubicSplineInterpolation(x, y);
    break;
 case (InterpolationMethod::LINEAR):
    ptr = new LinearInterpolation(x, y);
    break;
 default:
   throw ElementsException(
       "InterpolationFactory::get_interpolation_function: unkonwn interpolation method!!!");
 }

 return (ptr);
}
