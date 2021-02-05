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

/**
 * @file tests/src/serialization/DefaultConstructibleClass.h
 * @date June 27, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef GRIDCONTAINER_DEFAULTCONSTRUCTIBLECLASS_H
#define GRIDCONTAINER_DEFAULTCONSTRUCTIBLECLASS_H

class DefaultConstructibleClass {
public:
  DefaultConstructibleClass() {}
  double value = 0;
};

namespace boost {
namespace serialization {

template <typename Archive>
void serialize(Archive& ar, DefaultConstructibleClass& c, const unsigned int) {
  ar& c.value;
}

}  // namespace serialization
}  // namespace boost

#endif /* GRIDCONTAINER_DEFAULTCONSTRUCTIBLECLASS_H */
