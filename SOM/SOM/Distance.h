/*
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
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
#include <cassert>  // for assert
#include <cmath>    // for sqrt

#include "ElementsKernel/Exception.h"

namespace Euclid {
namespace SOM {
namespace Distance {

class Interface {

public:
  virtual ~Interface() = default;

  virtual double distance(const std::vector<double>& left, const std::vector<double>& right) const = 0;

  virtual double distance(const std::vector<double>&, const std::vector<double>&, const std::vector<double>&) const {
    throw Elements::Exception() << "Distance with uncertainties is not supported "
                                << "for this type of distance";
  }
};

class L2 : public Interface {

public:
  virtual ~L2() = default;

  double distance(const std::vector<double>& left, const std::vector<double>& right) const override {
    assert(left.size() == right.size());
    double result = 0;
    for (auto li = left.begin(), ri = right.begin(); li < left.end(); ++li, ++ri) {
      double diff = (*li - *ri);
      result += diff * diff;
    }
    return std::sqrt(result);
  }

  double distance(const std::vector<double>& left, const std::vector<double>& right,
                  const std::vector<double>& uncertainties) const override {
    assert(left.size() == right.size() && left.size() == uncertainties.size());

    double result = 0;
    for (auto li = left.begin(), ri = right.begin(), ui = uncertainties.begin(); li < left.end(); ++li, ++ri, ++ui) {
      double diff = *li - *ri;
      double up   = diff * diff;
      double down = *ui * *ui;
      result += up / down;
    }
    return std::sqrt(result);
  }
};

}  // namespace Distance
}  // namespace SOM
}  // namespace Euclid

#endif /* SOM_DISTANCE_H */
