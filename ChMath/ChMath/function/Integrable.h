/** 
 * @file ChMath/function/Integrable.h
 * @date February 18, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATH_INTEGRABLE_H
#define	CHMATH_INTEGRABLE_H

#include "ChMath/function/Function.h"

namespace ChMath {

class Integrable : public Function {
public:
  virtual ~Integrable() = default;
  virtual double integrate(const double, const double) const = 0;
};

} // End of ChMath

#endif	/* CHMATH_INTEGRABLE_H */

