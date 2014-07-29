/** 
 * @file ChMath/interpolation/interpolation.h
 * @date February 20, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef INTERPOLATION_H
#define	INTERPOLATION_H

#include <memory>
#include <vector>
#include <XYDataset/XYDataset.h>
#include "ChMath/function/Function.h"

namespace ChMath {

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
 * @throws ElementsException
 *    if the x and y vectors do not have the same size
 * @throws ElementsException
 *    if the x values are not strictly increasing
 */
std::unique_ptr<Function> interpolate(const std::vector<double>& x, const std::vector<double>& y, InterpolationType type);

/**
 * Returns a Function which performs interpolation for the data points of the
 * given dataset.
 * @param dataset The dataset containing the data points
 * @param type The type of the interpolation to perform
 * @return A function representing the interpolation
 * @throws ElementsException
 *    if the x and y vectors do not have the same size
 * @throws ElementsException
 *    if the x values are not strictly increasing
 */
std::unique_ptr<Function> interpolate(const XYDataset::XYDataset& dataset, InterpolationType type);

} // End of ChMath

#endif	/* INTERPOLATION_H */

