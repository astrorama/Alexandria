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
 * @file InitFunc.h
 * @author nikoapos
 */

#ifndef SOM_INITFUNC_H
#define SOM_INITFUNC_H

#include <ElementsKernel/Export.h>
#include <functional>

namespace Euclid {
namespace SOM {

namespace InitFunc {

using Signature = std::function<double()>;

extern Signature zero;

ELEMENTS_API Signature normalDistribution(double sigma, double mu);

ELEMENTS_API Signature uniformRandom(double min, double max);

}  // namespace InitFunc

}  // namespace SOM
}  // namespace Euclid

#endif /* SOM_INITFUNC_H */
