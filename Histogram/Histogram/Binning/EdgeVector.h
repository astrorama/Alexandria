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
* @file Histogram/Binning/EdgeVector.h
* @date February 17, 2020
* @author Alejandro Alvarez Ayllon
*/

#ifndef ALEXANDRIA_HISTOGRAM_BINNING_EDGEVECTOR_H
#define ALEXANDRIA_HISTOGRAM_BINNING_EDGEVECTOR_H

#include "Histogram/Histogram.h"
#include <utility>
#include <vector>

namespace Euclid {
namespace Histogram {
namespace Binning {

/**
 * Bin strategy based on a fixed set of edges given by the user.
 * The number of bins is equal to the number of edges minus one.
 * Each interval is open to the right, except the last one, which is closed.
 * So, \f[
 *  \mathit{bin}_i = [\mathit{edge}_{i}, \mathit{edge}_{i+i}) \\
 *  ... \\
 * \mathit{bin}_n= [\mathit{edge}_{n}, \mathit{edge}_{n+i}]
*  \f]
 */
template<typename VarType>
class EdgeVector : public BinStrategy<VarType> {
public:
  virtual ~EdgeVector() = default;

  EdgeVector(EdgeVector&&) = default;

  template<typename... Args>
  explicit EdgeVector(Args&& ... args): m_edges(std::forward<Args>(args)...) {
    m_nbins = m_edges.size() - 1;
  }

  EdgeVector(const EdgeVector&) = default;

  ssize_t getBinIndex(VarType value) const final {
    if (value < m_edges.front() || value > m_edges.back())
      return -1;
    auto next_edge = std::find_if(m_edges.begin(), m_edges.end(), [value](const VarType edge) { return edge > value; });
    if (next_edge == m_edges.end())
      --next_edge;
    return next_edge - m_edges.begin() - 1;
  }

  std::pair<VarType, VarType> getBinEdges(size_t i) const final {
    return std::make_pair(m_edges[i], m_edges[i + 1]);
  }

  VarType getEdge(size_t i) const final {
    return m_edges[i];
  }

private:
  using BinStrategy<VarType>::m_nbins;
  std::vector<VarType> m_edges;
};

} // end of namespace Binning
} // end of namespace Histogram
} // end of namespace Euclid

#endif // ALEXANDRIA_HISTOGRAM_BINNING_EDGEVECTOR_H
