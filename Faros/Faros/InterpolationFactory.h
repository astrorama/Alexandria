/*
 * InterpolationFactory.h
 *
 *  Created on: Oct 17, 2013
 *      Author: admin
 */

#ifndef INTERPOLATIONFACTORY_H_
#define INTERPOLATIONFACTORY_H_

#include "Faros/Interpolation.h"

class InterpolationFactory
{
 public:
  InterpolationFactory() {;}

  BaseInterpolation* getInterpolationFunction(const InterpolationMethod& method, const std::vector<double>& x, const std::vector<double>& y);

 private:

};


#endif /* INTERPOLATIONFACTORY_H_ */
