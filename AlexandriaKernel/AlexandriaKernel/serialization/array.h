
/*
 * Copyright (C) 2012-2020 Euclid Science Ground Segment
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

#ifndef ALEXANDRIA_KERNEL_SERIALIZATION_ARRAY_H
#define ALEXANDRIA_KERNEL_SERIALIZATION_ARRAY_H

// Boost, starting from version 1.56, provides serialization for the templated
// std::array. This file provides basic serialization support for versions
// before that. Note that if the boost version exists it is used instead.

#include <boost/version.hpp>

#if (BOOST_VERSION / 100000) <= 1 && ((BOOST_VERSION / 100) % 1000) < 56

#include <array>

namespace boost {
namespace serialization {

template <class Archive, std::size_t ND, typename CellType>
void serialize(Archive& archive, std::array<CellType, ND>& array, const unsigned int) {
  for (int i = 0; i < ND; ++i) {
    archive& array[i];
  }
}

}  // namespace serialization
}  // namespace boost

#else

#include <boost/serialization/array.hpp>

#endif

#endif /* ALEXANDRIA_KERNEL_SERIALIZATION_ARRAY_H */
