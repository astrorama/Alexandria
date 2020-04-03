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

/**
* @file Histogram/Binning/Scott.h
* @date February 11, 2020
* @author Alejandro Alvarez Ayllon
*/

#ifndef ALEXANDRIA_HISTOGRAM_BINNING_SCOTT_H
#define ALEXANDRIA_HISTOGRAM_BINNING_SCOTT_H

#include <cmath>
#include <algorithm>
#include <vector>
#include <boost/accumulators/accumulators.hpp>
#include <boost/accumulators/statistics/stats.hpp>
#include <boost/accumulators/statistics/max.hpp>
#include <boost/accumulators/statistics/min.hpp>
#include <boost/accumulators/statistics/variance.hpp>

#include "Histogram/Histogram.h"

namespace Euclid {
namespace Histogram {
namespace Binning {

/**
 * Bin strategy that estimates the number of bins applying Scott's normal reference rule
 * @details
 *  A proposed bin width is given by \f$ h = \frac{3.5\sigma}{\sqrt[3]{n}} \f$
 *  Where \f$ \sigma \f$ is the standard deviation of the data set
 *
 *  The final number of bins is computed with \f$ k = \left \lceil \frac{\max x - \min x}{h} \right \rceil \f$
 * @see
 *      https://en.wikipedia.org/wiki/Histogram#Scott's_normal_reference_rule
 */
template<typename VarType>
class Scott: public BinStrategy<VarType> {
public:

  template<typename Iterator>
  void computeBins(Iterator begin, Iterator end) {
    using namespace boost::accumulators;

    accumulator_set<VarType, stats<tag::variance, tag::max, tag::min>> acc;
    std::for_each(begin, end, std::bind<void>(std::ref(acc), std::placeholders::_1));

    size_t n = end - begin;

    VarType sigma = std::sqrt(variance(acc));
    VarType h = 3.5 * sigma / std::pow(n, 1. / 3.);
    VarType vmin = min(acc);
    VarType vmax = max(acc);

    if (sigma == 0) {
      vmax += 0.5;
      vmin -= 0.5;
      h = 1;
    }

    VarType range = vmax - vmin;

    m_nbins = std::ceil(range / h);

    m_step = range / m_nbins;
    m_start = vmin;
    m_end = vmax;
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

} // end of namespace Binning
} // end of namespace Histogram
} // end of namespace Euclid

#endif // ALEXANDRIA_HISTOGRAM_BINNING_SCOTT_H
