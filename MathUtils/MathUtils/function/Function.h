/** 
 * @file MathUtils/function/Function.h
 * @date February 18, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATH_FUNCTION_H
#define	CHMATH_FUNCTION_H

#include <memory>
#include "ElementsKernel/Exception.h"

namespace Euclid {
namespace ChMath {

/**
 * @interface Function
 * 
 * @brief Interface class representing a function
 * 
 * @details
 * A function is an object which can convert a value from domain X to a value
 * of domain Y. This interface is the root of a hierarchy of classes which
 * perform such conversions, with the parenthesis operator. Because this class
 * is designed for inheritance, it requires the implementation of the clone()
 * method for copying functions when a reference of type Function is used.
 */
class Function {
  
public:
  
  /// Default destructor
  virtual ~Function() = default;
  
  /**
   * Converts the value x from the input domain to the output domain.
   * @param x The value to convert
   * @return The value of the output domain
   */
  virtual double operator()(const double x) const = 0;
  
  /**
   * Creates a clone of the function object. All subclasses must implement this
   * method, to enable copying of Function objects when only a reference to the
   * Function class is available.
   * @return A copy of the Function object
   */
  virtual std::unique_ptr<Function> clone() const = 0;
};

} // End of ChMath
} // end of namespace Euclid

#endif	/* CHMATH_FUNCTION_H */

