/**
 * @file InterpolationFactory.cpp
 * @date Dec 11, 2013
 * @author Nicolas Morisset
 */

#include "ElementsKernel/ElementsException.h"
#include "ProtoZ/InterpolationFactory.h"

using namespace std;

////////////////////////////////////////////////////////////////////////////////
//                            InterpolationFactory class
////////////////////////////////////////////////////////////////////////////////

std::unique_ptr<BaseInterpolation> InterpolationFactory::getInterpolationFunction(const std::string& method, const std::vector<double>& x, const std::vector<double>& y)
{
  if (method == "CUBIC") {
    return ( unique_ptr<BaseInterpolation> (new CubicSplineInterpolation(x, y)) );
 }
 else if (method == "LINEAR") {
    return ( unique_ptr<BaseInterpolation> (new LinearInterpolation(x, y)) );
 }
 else {
   throw ElementsException(
       "InterpolationFactory::get_interpolation_function: unknown interpolation method!!!");
 }
}
