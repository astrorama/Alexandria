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
 * @file Histogram/Binning/Sqrt.h
 * @date February 11, 2020
 * @author Alejandro Alvarez Ayllon
 */

#ifndef ALEXANDRIA_HISTOGRAM_BINNING_SQRT_H
#define ALEXANDRIA_HISTOGRAM_BINNING_SQRT_H

#include <algorithm>
#include <cmath>
#include <numeric>
#include <vector>

#include "Histogram/Histogram.h"

namespace Euclid {
namespace Histogram {
namespace Binning {

/**
 * Bin strategy that estimates the number of bins as \f$ \sqrt{n} \f$
 */
template <typename VarType>
class Sqrt : public BinStrategy<VarType> {
public:
  template <typename Iterator>
  void computeBins(Iterator begin, Iterator end) {
    m_nbins     = std::ceil(std::sqrt(end - begin));
    auto minmax = std::minmax_element(begin, end);
    m_step      = (*minmax.second - *minmax.first) / m_nbins;
    m_start     = *minmax.first;
    m_end       = *minmax.second;
  }

  ssize_t getBinIndex(VarType value) const final {
    if (value == m_end)
      return m_nbins - 1;
    return (value - m_start) / m_step;
  }

  std::pair<VarType, VarType> getBinEdges(size_t i) const final {
    return std::make_pair(i * m_step + m_start, (i + 1) * m_step + m_start);
  }

  VarType getEdge(size_t i) const final {
    return i * m_step + m_start;
  }

private:
  using BinStrategy<VarType>::m_nbins;
  VarType m_start, m_step, m_end;
};

}  // end of namespace Binning
}  // end of namespace Histogram
}  // end of namespace Euclid

#endif  // ALEXANDRIA_HISTOGRAM_BINNING_SQRT_H
