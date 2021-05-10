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

#ifndef _FUNCTIONUTILS_NDSAMPLER_H
#define _FUNCTIONUTILS_NDSAMPLER_H

#include "MathUtils/function/Function.h"
#include "NdArray/NdArray.h"
#include <array>
#include <functional>
#include <vector>

namespace Euclid {
namespace MathUtils {

/**
 * Multidimensional sampler
 * Inspired on
 * - S. Dolgov, K. Anaya-Izquierdo, C. Fox, and R. Scheichl,
 *   "Approximation and sampling of multivariate probability distributions in the tensor train decomposition”
 * See Section 2
 *
 * @details
 *  NdSampler recursively decomposes the sampling of a N dimensional space into
 *  sampling from an N-1 dimensional space (marginalized), and then sampling the N dimension
 *  according to p(x_n|x_1,...,x{n-1})
 *  As specified on the cited paper, the conditional can be approximated by p(x_1,...,x{n-1},x_n), which is
 *  computed using the N-dimensional interpolation of the grid for each $x_n \in knots_n$.
 * @tparam N
 *  The number of dimensions
 */
template <std::size_t N>
class NdSampler {
public:
  /**
   * Constructor
   * @param knots
   *    Dimensions of the n-dimensional grid. Coordinates must follow the same order as the grid
   *    axes: first set of coordinates correspond to axis0, second to axis1, and so on
   * @param grid
   *    Values of the PDF at each grid intersection.
   */
  NdSampler(std::array<std::vector<double>, N> knots, const NdArray::NdArray<double>& grid);

  /**
   * Draw samples from the n-dimensional distribution
   * @tparam Generator
   *    Type of the random number generator (i.e std::mt19937)
   * @param ndraws
   *    Number of samples
   * @param rng
   *    Instance of the random number generator
   * @return
   *    An NdArray, where the first axis corresponds to the number of draws, and the second to the number of dimensions
   */
  template <typename Generator>
  NdArray::NdArray<double> draw(std::size_t ndraws, Generator& rng) const;

  template<typename Generator>
  void draw(std::size_t ndraws, Generator &rng, NdArray::NdArray<double>& output) const;

private:
  std::unique_ptr<NdSampler<N - 1>> m_subsampler;
  std::unique_ptr<NAryFunction<N>>  m_interpolation;
  std::vector<double>               m_knots;
};

}  // namespace MathUtils
}  // namespace Euclid

#define NDSAMPLER_IMPL
#include "MathUtils/PDF/_impl/NdSampler.icpp"
#undef NDSAMPLER_IMPL

#endif  // _FUNCTIONUTILS_NDSAMPLER_H
