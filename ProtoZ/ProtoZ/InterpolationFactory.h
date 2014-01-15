/**
 * @file InterpolationFactory.h
 * @date Dec 11, 2013
 * @author Nicolas Morisset
 */

#ifndef PROTOZ_INTERPOLATIONFACTORY_H_
#define PROTOZ_INTERPOLATIONFACTORY_H_

#include "ProtoZ/Interpolation.h"
#include <memory>



class InterpolationFactory
{
 public:

  /**
   * @brief Constructor
   */
  InterpolationFactory() {;}

  /**
   * @brief getInterpolationFunction
   * Get the interpolation function pointer (F) such as  y=F(x)
   *
   * @details
   *
   * @param method
   *  String containing the name of the method to be used (CUBIC or LINEAR)
   *
   * @param x
   * vector of double values
   * @param y
   *  vector of double values
   *
   * @return
   * A unique pointer (of BaseInterpolation type) to the function F
   *
   * @throws ElementsException
       unknown interpolation method
   *
   */

  std::unique_ptr<BaseInterpolation>  getInterpolationFunction(const std::string& method, const std::vector<double>& x, const std::vector<double>& y);

 private:

};


#endif /* PROTOZ_INTERPOLATIONFACTORY_H_ */
