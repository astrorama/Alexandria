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

#include "NdArray/Operations.h"

namespace Euclid {
namespace NdArray {

std::vector<std::size_t> unravel_index(std::size_t index, const std::vector<std::size_t>& shape) {
  std::vector<std::size_t> coords(shape.size());
  std::size_t              i = coords.size();
  do {
    --i;
    std::size_t stride = shape[i];
    coords[i]          = index % stride;
    index /= stride;
  } while (i > 0);
  if (index > 0) {
    throw std::out_of_range("Index out of bounds");
  }
  return coords;
}

}  // namespace NdArray
}  // namespace Euclid