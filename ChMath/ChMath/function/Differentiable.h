/** 
 * @file ChMath/function/Differentiable.h
 * @date February 18, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATH_DIFFERENTIABLE_H
#define	CHMATH_DIFFERENTIABLE_H

#include <memory>
#include "ChMath/function/Function.h"
#include "ChMath/function/Integrable.h"

namespace ChMath {

class Differentiable : public Integrable {
public:
  virtual ~Differentiable() {}
  virtual std::shared_ptr<Function> derivative() const = 0;
  virtual std::shared_ptr<Function> indefiniteIntegral() const = 0;
  double integrate(const double x1, const double x2) const override final;
};

} // End of ChMath

#endif	/* CHMATH_DIFFERENTIABLE_H */

