/** 
 * @file ChMath/function/Function.h
 * @date February 18, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATH_FUNCTION_H
#define	CHMATH_FUNCTION_H

#include <memory>
#include "ElementsKernel/ElementsException.h"

namespace ChMath {

class Function {
public:
  virtual ~Function() = default;
  virtual double operator()(const double) const = 0;
  virtual std::unique_ptr<Function> clone() const = 0;
};

} // End of ChMath

#endif	/* CHMATH_FUNCTION_H */

