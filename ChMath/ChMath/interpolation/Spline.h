/** 
 * @file ChMath/interpolation/Spline.h
 * @date February 21, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef SPLINE_H
#define	SPLINE_H

#include "ChMath/function/Piecewise.h"

namespace ChMath {

class Spline : public Piecewise {
public:
  Spline(std::vector<double> knots, std::vector<std::shared_ptr<Function>> functions) : Piecewise(knots,functions) { }
  std::unique_ptr<Function> clone() const {
    return std::unique_ptr<Function> (new Spline(this->getKnots(), this->getFunctions()));
  }
};

} // End of ChMath

#endif	/* SPLINE_H */

