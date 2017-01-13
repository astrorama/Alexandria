/** 
 * @file Polynomial.h
 * @date February 19, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATH_POLYNOMIAL_H
#define	CHMATH_POLYNOMIAL_H

#include <vector>
#include "ChMath/function/Function.h"
#include "ChMath/function/Differentiable.h"

namespace ChMath {

class Polynomial : public Differentiable {
public:
  Polynomial(std::vector<double> coefficients);
  virtual ~Polynomial() = default;
  std::vector<double> getCoefficients() const;
  double operator()(const double) const override;
  std::unique_ptr<Function> clone() const override;
  std::shared_ptr<Function> derivative() const override;
  std::shared_ptr<Function> indefiniteIntegral() const override;
private:
  std::vector<double> m_coef;
  mutable std::shared_ptr<Function> m_derivative {};
  mutable std::shared_ptr<Function> m_indefIntegral {};
}; // End of Polynomial

} // End of ChMath

#endif	/* CHMATH_POLYNOMIAL_H */

