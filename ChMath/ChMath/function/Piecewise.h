/** 
 * @file ChMath/function/Piecewise.h
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATH_PIECEWISE_H
#define	CHMATH_PIECEWISE_H

#include <vector>
#include <memory>
#include "ChMath/function/Integrable.h"

namespace ChMath {

class Piecewise : public Integrable {
public:
  Piecewise(std::vector<double> knots, std::vector<std::shared_ptr<Function>> functions);
  virtual ~Piecewise() = default;
  std::vector<double> getKnots() const;
  std::vector<std::shared_ptr<Function>> getFunctions() const;
  double operator()(const double) const override;
  std::unique_ptr<Function> clone() const override;
  double integrate(const double, const double) const override;
private:
  std::vector<double> m_knots;
  std::vector<std::shared_ptr<Function>> m_functions;
};

} // End of ChMath

#endif	/* CHMATH_PIECEWISE_H */

