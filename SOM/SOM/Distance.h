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
#include "ElementsKernel/Unused.h"

namespace Euclid {
namespace SOM {
namespace Distance {

class Interface {

public:
  using const_iterator = std::vector<double>::const_iterator;

  virtual ~Interface() = default;

  virtual double distance(const_iterator begin1, const_iterator end1, const_iterator begin2) const = 0;

  virtual double distance(const_iterator ELEMENTS_UNUSED begin1, const_iterator ELEMENTS_UNUSED end1,
                          const_iterator ELEMENTS_UNUSED begin2,
                          const_iterator ELEMENTS_UNUSED begin_uncertainties) const {
    throw Elements::Exception() << "Distance with uncertainties is not supported "
                                << "for this type of distance";
  }
};

class L2 final : public Interface {

public:
  virtual ~L2() = default;

  double distance(const_iterator begin1, const_iterator end1, const_iterator begin2) const override {
    double result = 0;
    for (; begin1 < end1; ++begin1, ++begin2) {
      double diff = (*begin1 - *begin2);
      result += diff * diff;
    }
    return std::sqrt(result);
  }

  double distance(const_iterator begin1, const_iterator end1, const_iterator begin2,
                  const_iterator begin_uncertainties) const override {

    double result = 0;
    for (; begin1 < end1; ++begin1, ++begin2, ++begin_uncertainties) {
      double diff = *begin1 - *begin2;
      double up   = diff * diff;
      double down = *begin_uncertainties * *begin_uncertainties;
      result += up / down;
    }
    return std::sqrt(result);
  }
};

}  // namespace Distance
}  // namespace SOM
}  // namespace Euclid

#endif /* SOM_DISTANCE_H */
