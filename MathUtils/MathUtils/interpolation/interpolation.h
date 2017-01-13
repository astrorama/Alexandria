/**
 * @file MathUtils/interpolation/interpolation.h
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef INTERPOLATION_H
#define	INTERPOLATION_H

#include <memory>
#include <vector>

#include "ElementsKernel/Export.h"

#include "XYDataset/XYDataset.h"
#include "MathUtils/function/Function.h"

namespace Euclid {
namespace MathUtils {

/// Enumeration of the different supported interpolation types
enum class InterpolationType {
  LINEAR, CUBIC_SPLINE
};

/**
 * Returns a Function which performs interpolation for the given set of data
 * points.
 * @param x The x values of the data points
 * @param y The y values of the data points
 * @param type The type of the interpolation to perform
 * @return A function representing the interpolation
 * @throws Elements::Exception
 *    if the x and y vectors do not have the same size
 * @throws Elements::Exception
 *    if the x values are not strictly increasing
 */
ELEMENTS_API std::unique_ptr<Function> interpolate(const std::vector<double>& x, const std::vector<double>& y, InterpolationType type);

/**
 * Returns a Function which performs interpolation for the data points of the
 * given dataset.
 * @param dataset The dataset containing the data points
 * @param type The type of the interpolation to perform
 * @return A function representing the interpolation
 * @throws Elements::Exception
 *    if the x and y vectors do not have the same size
 * @throws Elements::Exception
 *    if the x values are not strictly increasing
 */
ELEMENTS_API std::unique_ptr<Function> interpolate(const Euclid::XYDataset::XYDataset& dataset, InterpolationType type);

} // End of MathUtils
} // end of namespace Euclid

#endif	/* INTERPOLATION_H */
