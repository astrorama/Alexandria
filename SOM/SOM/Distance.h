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
 * @file Distance.h
 * @author nikoapos
 */

#ifndef SOM_DISTANCE_H
#define SOM_DISTANCE_H

#include <array>
#include <cmath>  // for sqrt

#include "ElementsKernel/Exception.h"

namespace Euclid {
namespace SOM {
namespace Distance {

template <typename std::size_t ND>
class Interface {

public:
  virtual ~Interface() = default;

  virtual double distance(const std::array<double, ND>& left, const std::array<double, ND>& right) const = 0;

  virtual double distance(const std::array<double, ND>&, const std::array<double, ND>&,
                          const std::array<double, ND>&) const {
    throw Elements::Exception() << "Distance with uncertainties is not supported "
                                << "for this type of distance";
  }
};

template <typename std::size_t ND>
class L2 : public Interface<ND> {

public:
  virtual ~L2() = default;

  double distance(const std::array<double, ND>& left, const std::array<double, ND>& right) const override {
    double result = 0;
    for (std::size_t i = 0; i < ND; ++i) {
      result += (left[i] - right[i]) * (left[i] - right[i]);
    }
    return std::sqrt(result);
  }

  double distance(const std::array<double, ND>& left, const std::array<double, ND>& right,
                  const std::array<double, ND>& uncertainties) const override {
    double result = 0;
    for (std::size_t i = 0; i < ND; ++i) {
      double up   = (left[i] - right[i]) * (left[i] - right[i]);
      double down = uncertainties[i] * uncertainties[i];
      result += up / down;
    }
    return std::sqrt(result);
  }
};

}  // namespace Distance
}  // namespace SOM
}  // namespace Euclid

#endif /* SOM_DISTANCE_H */
