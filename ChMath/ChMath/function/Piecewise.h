/**
 * @file ChMath/function/Piecewise.h
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATH_PIECEWISE_H
#define	CHMATH_PIECEWISE_H

#include <vector>
#include <memory>

#include "ElementsKernel/Export.h"

#include "ChMath/function/Integrable.h"

namespace Euclid {
namespace ChMath {

/**
 * @class Piecewise
 *
 * @brief Represents a piecewise function
 *
 * @details
 * A Piecewise function is defined by multiple sub functions, each applied to an
 * interval defined by the piecewise knots. Outside of the knots range the
 * Piecewise evaluates zero.
 */
class ELEMENTS_API Piecewise : public Integrable {

public:

  /**
   * Creates a new Piecewise instance with the given knots and functions between
   * them. The functions vector must have size one less than the knots. The
   * sub-function with index 0 corresponds to the range [knot0,knot1], the one
   * with index 1 to the range [knot1,knot2], etc.
   * @param knots The knots of the piecewise function
   * @param functions The sub-functions in the knot ranges
   * @throws Elements::Exception
   *    if the size of the sub-functions vector is not ine less than the knots
   *    vector size
   * @throws Elements::Exception
   *    if the knots are not strictly increasing
   */
  Piecewise(std::vector<double> knots, std::vector<std::shared_ptr<Function>> functions);

  /// Default destructor
  virtual ~Piecewise() = default;

  /// Returns the knots of the piecewise function
  const std::vector<double>& getKnots() const;

  /// Returns the functions in the ranges between the knots
  const std::vector<std::shared_ptr<Function>>& getFunctions() const;

  /// Returns the value of the piecewise function for the given value, by using
  /// the correct sub-function. Values outside of the knots evaluate to zero.
  double operator()(const double) const override;

  /// Creates a Piecewise function with the same knots and sub-functions. Note
  /// that the sub-functions are not cloned, but just a pointer is copied.
  std::unique_ptr<Function> clone() const override;

  /**
   * Calculates the integral in the range [x1,x2], by delegating the integration
   * in the sub-functions.
   * @param x1 The lower bound of the integration
   * @param x2 The upper bound of the integration
   * @return The integral in the range [x1,x2]
   */
  double integrate(const double x1, const double x2) const override;

private:

  /// A vector where the knots are kept
  std::vector<double> m_knots;
  /// A vector where the sub-functions are kept
  std::vector<std::shared_ptr<Function>> m_functions;

};

} // End of ChMath
} // end of namespace Euclid

#endif	/* CHMATH_PIECEWISE_H */

