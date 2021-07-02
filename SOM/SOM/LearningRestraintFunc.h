/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
 *
 * This library is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free
 * Software Foundation; either version 3.0 of the License, or (at your option)
 * any later version.
 *
 * This library is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
 * details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this library; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 */

/*
 * @file LearningRestraintFunc.h
 * @author nikoapos
 */

#ifndef SOM_LEARNINGRESTRAINTFUNC_H
#define SOM_LEARNINGRESTRAINTFUNC_H

#include <ElementsKernel/Export.h>
#include <functional>

namespace Euclid {
namespace SOM {
namespace LearningRestraintFunc {

using Signature = std::function<double(std::size_t iteration, std::size_t total_iterations)>;

ELEMENTS_API Signature linear();

ELEMENTS_API Signature exponentialDecay(double initial_rate);

}  // namespace LearningRestraintFunc
}  // namespace SOM
}  // namespace Euclid

#endif /* SOM_LEARNINGRESTRAINTFUNC_H */
