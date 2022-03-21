/*
 * Copyright (C) 2022 Euclid Science Ground Segment
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

#ifndef MATHUTILS_WEIGHTS_H
#define MATHUTILS_WEIGHTS_H

#include "MathUtils/distances/Distances.h"

namespace Euclid {
namespace MathUtils {

struct Likelihood {
  template <typename Scale, typename Iterator>
  static auto weight(Scale scale, Iterator ref_begin, Iterator ref_end, Iterator target_begin)
      -> decltype(ref_begin->getFlux()) {
    auto chi2 = Chi2Distance::distance(scale, ref_begin, ref_end, target_begin);
    return std::exp(-0.5f * chi2);
  }
};

struct InverseChi2 {
  template <typename Scale, typename Iterator>
  static auto weight(Scale scale, Iterator ref_begin, Iterator ref_end, Iterator target_begin)
      -> decltype(ref_begin->getFlux()) {
    return 1.f / Chi2Distance::distance(scale, ref_begin, ref_end, target_begin);
  }
};

struct InverseEuclidean {
  template <typename Scale, typename Iterator>
  static auto weight(Scale scale, Iterator ref_begin, Iterator ref_end, Iterator target_begin)
      -> decltype(ref_begin->getFlux()) {
    return 1.f / EuclideanDistance::distance(scale, ref_begin, ref_end, target_begin);
  }
};

}  // namespace MathUtils
}  // namespace Euclid

#endif  // MATHUTILS_WEIGHTS_H
