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

#ifndef MATHUTILS_DISTANCES_H
#define MATHUTILS_DISTANCES_H

#include <cmath>

namespace Euclid {
namespace MathUtils {

/**
 * Implement the distance (with scale factor), partial derivative of the distance wrt scale factor,
 * and scale guessing for the χ^2 distance
 */
struct Chi2Distance {

  /**
   * χ^2 distance
   * @tparam Scale
   * @tparam Iterator
   * @param scale
   * @param ref_begin
   * @param ref_end
   * @param target_begin
   * @return
   */
  template <typename Scale, typename Iterator>
  static auto distance(Scale scale, Iterator ref_begin, Iterator ref_end, Iterator target_begin)
      -> decltype(ref_begin->getFlux()) {
    decltype(ref_begin->getFlux()) acc = 0.;

    for (auto ri = ref_begin, ti = target_begin; ri != ref_end; ++ri, ++ti) {
      auto ref_val = scale * ri->getFlux();
      auto ref_err = scale * ri->getError();
      auto tar_val = ti->getFlux();
      auto tar_err = ti->getError();
      auto nom     = (ref_val - tar_val) * (ref_val - tar_val);
      auto den     = ref_err * ref_err + tar_err * tar_err;
      acc += nom / den;
    }

    return acc;
  }

  /**
   * Guess the scale factor for the reference object
   * @tparam Iterator
   * @param ref_begin
   * @param ref_end
   * @param target_begin
   * @return
   */
  template <typename Iterator>
  static auto guessScale(Iterator ref_begin, Iterator ref_end, Iterator target_begin) -> decltype(ref_begin->getFlux()) {
    decltype(ref_begin->getFlux()) nom = 0., den = 0.;

    for (auto ri = ref_begin, ti = target_begin; ri != ref_end; ++ri, ++ti) {
      auto err_sqr = (ti->getError() * ti->getError());
      nom += (ri->getFlux() * ti->getFlux()) / err_sqr;
      den += (ri->getFlux() * ri->getFlux()) / err_sqr;
    }

    return nom / den;
  }

  /**
   * Implement the derivative of the chi2 distance
   *\f[
   *    \frac{\delta}{\delta a}\left[ \frac{(a f_{ref} - f_{target})^2}{(a e_{ref})^2 + e_{target}^2}\right] = \frac{2
   *(a f_{ref} - f_{target}) (e_{ref}^2 a f_{target} + f_{ref} e_{target}^2)}{(e_{ref}^2 a^2 + e_{target}^2)^2} \f]
   */
  template <typename Scale, typename Iterator>
  static auto daDistance(Scale scale, Iterator ref_begin, Iterator ref_end, Iterator target_begin)
      -> decltype(ref_begin->getFlux()) {
    decltype(ref_begin->getFlux()) acc = 0.;

    for (auto ri = ref_begin, ti = target_begin; ri != ref_end; ++ri, ++ti) {
      auto ref_val = ri->getFlux();
      auto ref_err = ri->getError();
      auto tar_val = ti->getFlux();
      auto tar_err = ti->getError();

      auto ref_err_sq = ref_err * ref_err;
      auto tar_err_sq = tar_err * tar_err;

      auto nom = 2 * (scale * ref_val - tar_val) * (ref_err_sq * scale * tar_val + ref_val * tar_err_sq);
      auto den = ref_err_sq * scale * scale + tar_err_sq;
      acc += nom / (den * den);
    }

    return acc;
  }
};

/**
 * Implement the distance (with scale factor), partial derivative of the distance wrt scale factor,
 * and scale guessing for the Euclidean distance
 */
struct EuclideanDistance {
  template <typename Scale, typename Iterator>
  static auto distance(Scale scale, Iterator ref_begin, Iterator ref_end, Iterator target_begin)
      -> decltype(ref_begin->getFlux()) {
    decltype(ref_begin->getFlux()) acc = 0.;

    for (auto ri = ref_begin, ti = target_begin; ri != ref_end; ++ri, ++ti) {
      auto d = (scale * ri->getFlux()) - (ti->getFlux());
      acc += d * d;
    }

    return std::sqrt(acc);
  }

  /**
   * Guess the scale factor for the reference object
   * @tparam Iterator
   * @param ref_begin
   * @param ref_end
   * @param target_begin
   * @return
   */
  template <typename Iterator>
  static auto guessScale(Iterator ref_begin, Iterator ref_end, Iterator target_begin) -> decltype(ref_begin->getFlux()) {
    decltype(ref_begin->getFlux()) nom = 0., den = 0.;

    for (auto ri = ref_begin, ti = target_begin; ri != ref_end; ++ri, ++ti) {
      nom += (ti->getFlux() * ti->getFlux());
      den += (ri->getFlux() * ri->getFlux());
    }

    return std::sqrt(nom) / std::sqrt(den);
  }

  /**
   *\f[
   * \frac{\delta}{\delta a}\left[ \sqrt{\sum_i^n (a f_{ref} - f_{target})^2} \right] = \frac{a \left(\sum_i^n
   *f_{ref}^2\right) - \left( \sum_i^n f_{ref} \times f_{target} \right)}{\sqrt{\sum_i^n (a f_{ref} - f_{target})^2}}
   *\f]
   */
  template <typename Scale, typename Iterator>
  static auto daDistance(Scale scale, Iterator ref_begin, Iterator ref_end, Iterator target_begin)
      -> decltype(ref_begin->getFlux()) {
    decltype(ref_begin->getFlux()) den = 0., nom_sum_sqr = 0., nom_sum_prod = 0.;

    for (auto ri = ref_begin, ti = target_begin; ri != ref_end; ++ri, ++ti) {
      nom_sum_sqr += ri->getFlux() * ri->getFlux();
      nom_sum_prod += ri->getFlux() * ti->getFlux();
      den += (ti->getFlux() - scale * ri->getFlux()) * (ti->getFlux() - scale * ri->getFlux());
    }

    return (scale * nom_sum_sqr - nom_sum_prod) / std::sqrt(den);
  }
};
}  // namespace MathUtils
}  // namespace Euclid

#endif  // MATHUTILS_DISTANCES_H
