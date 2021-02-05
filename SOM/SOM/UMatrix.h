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
 * @file UMatrix.h
 * @author nikoapos
 */

#ifndef SOM_UMATRIX_H
#define SOM_UMATRIX_H

#include "GridContainer/GridContainer.h"
#include "SOM/SOM.h"

namespace Euclid {
namespace SOM {

using UMatrix = GridContainer::GridContainer<std::vector<double>, std::size_t, std::size_t>;

enum class UMatrixType { MIN, MAX, MEAN };

template <std::size_t ND, typename DistFunc = Distance::L2<ND>>
UMatrix computeUMatrix(const SOM<ND, DistFunc>& som, UMatrixType type = UMatrixType::MEAN);

}  // namespace SOM
}  // namespace Euclid

#include "SOM/_impl/UMatrix.icpp"

#endif /* SOM_UMATRIX_H */
