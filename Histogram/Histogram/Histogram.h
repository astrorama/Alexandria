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
* @file Histogram/Histogram.h
* @date February 11, 2020
* @author Alejandro Alvarez Ayllon
*/

#ifndef ALEXANDRIA_HISTOGRAM_HISTOGRAM_H
#define ALEXANDRIA_HISTOGRAM_HISTOGRAM_H

#include <cassert>
#include <cmath>
#include <algorithm>
#include <memory>
#include <utility>
#include <tuple>
#include <type_traits>
#include <vector>
#include <ElementsKernel/Exception.h>
#include <AlexandriaKernel/memory_tools.h>

namespace Euclid {
namespace Histogram {

/**
 * Different binning strategies must implement this interface, plus a templated method called computeBins, which
 * should operate over a pair of (begin, end) iterators.
 * @tparam VarType
 *  The type of the continuous variable. Must be an arithmetic type (either integral or floating point)
 */
template<typename VarType>
class BinStrategy {
public:

  /**
   * Constructor.
   * @details
   * m_nbins is to be computed by the concrete implementations
   */
  BinStrategy() : m_nbins(0) {}

  /**
   * Destructor
   */
  virtual ~BinStrategy() = default;

  /**
   * @return The number of bins
   */
  size_t getBinCount() const {
    return m_nbins;
  }

  /**
   * Get the bin index corresponding to the given value
   * @param value
   *    The value to map to a bin
   * @return
   *    The bin index. If value is outside of the bounds, a negative number or a value
   *    bigger or equal to m_nbins can be used to mark the fact
   */
  virtual ssize_t getBinIndex(VarType value) const = 0;

  /**
   * @return The list of bin edges
   * @details
   *    The default implementation is based on getEdge, but the specific implementations
   *    can override an do something more optimal
   */
  virtual std::vector<VarType> getEdges() const {
    std::vector<VarType> edges(m_nbins + 1);
    size_t i = 0;
    std::generate(edges.begin(), edges.end(), [this, &i]() { return getEdge(i++); });
    return edges;
  }

  /**
   * Get the two edges corresponding to the bin i
   * @param i
   *    The bin index
   * @return
   *    The two bin edges
   */
  virtual std::pair<VarType, VarType> getBinEdges(size_t i) const {
    return std::make_pair(getEdge(i), getEdge(i + 1));
  }

  /**
   * Get the edge value e. Note that there are always one more edge than bins:
   * i.e. the bin 0 has the edges (0, 1), the bin 1 the edges (1, 2), etc...
   */
  virtual VarType getEdge(size_t e) const = 0;

  /**
   * Get the center of the bin i
   * @param i
   *    Bin index
   * @return
   *    The value situated at the middle of the bin
   * @details
   *    The default implementation returns the midpoint between the edges. Concrete
   *    implementations can override this with a direct calculation.
   */
  virtual VarType getBin(size_t i) const {
    auto edges = getBinEdges(i);
    return (edges.second + edges.first) / 2;
  }

protected:
  size_t m_nbins;
};

/**
 * Histogram
 * @tparam VarType
 *  The type of the continuous variable. Must be an arithmetic type (either integral or floating point)
 * @tparam WeightType
 *  The type used for the counts, which is the same as the one accepted for the weights.
 */
template<typename VarType, typename WeightType = float>
class Histogram {
public:

  static_assert(std::is_arithmetic<VarType>::value, "Histogram only supports numerical types");
  static_assert(std::is_arithmetic<WeightType>::value, "Histogram only supports numerical weights");

  /**
   * Constructor
   * @tparam IterType
   *    Iterator type for both the edges and the values of the variable
   * @tparam BinType
   *    A concrete movable implementation of BinStrategy
   * @param begin
   *    Beginning of the data
   * @param end
   *    End of the data
   * @param bin_type
   *    An instance of BinType. It will be taken ownership of by the Histogram
   */
  template<typename IterType, typename BinType, typename=typename std::enable_if<std::is_move_constructible<BinType>::value>::type>
  Histogram(IterType begin, IterType end, BinType&& bin_type) {
    auto binning_impl = make_unique<ComputationImpl<BinType>>(std::move(bin_type));
    binning_impl->computeBins(begin, end, ConstantWeight{});
    m_binning_concept = std::move(binning_impl);
  }

  /**
   * Constructor
   * @tparam IterType
   *    Iterator type for both the edges and the values of the variable
   * @tparam WeightIterType
   *    Iterator type for the weights
   * @tparam BinType
   *    A concrete movable implementation of BinStrategy
   * @param begin
   *    Beginning of the data
   * @param end
   *    End of the data
   * @param wbegin
   *    Beginning of the weights
   * @param wend
   *    End of the weights
   * @param bin_type
   *    An instance of BinType. It will be taken ownership of by the Histogram
   * @note
   *    The number of values and weights must match
   */
  template<typename IterType, typename WeightIterType, typename BinType, typename=typename std::enable_if<std::is_move_constructible<BinType>::value>::type>
  Histogram(IterType begin, IterType end, WeightIterType wbegin, WeightIterType wend, BinType&& bin_type) {
    assert(wend - wbegin == end - begin);
    auto binning_impl = make_unique<ComputationImpl<BinType>>(std::move(bin_type));
    binning_impl->computeBins(begin, end, wbegin);
    m_binning_concept = std::move(binning_impl);
  }

  /**
   * Copy constructor
   */
  Histogram(const Histogram& other) {
    m_binning_concept = other.m_binning_concept->clone();
  }

  /**
   * Move constructor
   */
  Histogram(Histogram&&) = default;

  /**
   * Assignment operator
   */
  Histogram& operator=(const Histogram&) = default;

  /**
   * Move assignment operator
   */
  Histogram& operator=(Histogram&&) = default;

  /**
   * @return
   *    The number of bins on the histogram
   */
  size_t size() const {
    return m_binning_concept->size();
  }

  /**
   * @return
   *    The counts of the histogram
   */
  std::vector<WeightType> getCounts() const {
    return std::vector<WeightType>(m_binning_concept->m_counts->begin() + m_binning_concept->m_clip_left,
                                   m_binning_concept->m_counts->begin() + m_binning_concept->m_clip_right + 1);
  }

  /**
   * @return
   *    The edges of the bins
   * @note
   *    The number of edges is equal to the number of bins + 1
   */
  std::vector<VarType> getEdges() const {
    return m_binning_concept->getBinStrategy().getEdges();
  }

  /**
   * @return
   *    The center of the bins
   */
  std::vector<VarType> getBins() const {
    std::vector<VarType> bins(m_binning_concept->m_counts->size());
    size_t i = 0;
    std::generate(bins.begin(), bins.end(), [this, &i]() { return m_binning_concept->getBinStrategy().getBin(i++); });
    return bins;
  }

  /**
   * @param i
   *    Bin index
   * @return
   *    The edges for the given bin
   */
  std::pair<VarType, VarType> getBinEdges(size_t i) const {
    return m_binning_concept->getBinStrategy().getBinEdges(i);
  }

  /**
   * Clip the histogram to the given range
   * @param min
   *    Minimum value to keep
   * @param max
   *    Maximum value to keep
   */
  void clip(VarType min, VarType max) {
    m_binning_concept->clip(min, max);
  }

  /**
   * Compute the mean, the median and the standard deviation of the histogram
   * @details
   *    \f[
   *    \mu = \frac{\sum_{i=0}^{n} \mathit{bin}_i * \mathit{count}_i}{\sum_{i=0}^{n}count_i}
   *    \f]
   *    \f[
   *    \sigma = \sqrt{\frac{\sum_{i=0}^n \mathit{count}_i \times (\mathit{center}_i - \mu)^2}{\sum_{i=0}^n \mathit{count}_i}}
   *    \f]
   *
   *    To find the median, a second pass is done over the bins, computing the cumulative distribution until the bin
   *    where it is greater or equal to 0.5. The median is then interpolated between the lower and higher edges.
   * @return
   *    A tuple (mean, median, sigma)
   */
  std::tuple<VarType, VarType, VarType> getStats() const {
    return m_binning_concept->getStats();
  }


private:
  /**
   * Used internally when no weights are given, which is equivalent to have all weights being 1
   */
  struct ConstantWeight {
    ConstantWeight& operator++() {
      return *this;
    }

    WeightType operator*() const {
      return 1;
    }
  };

  /**
   * This interface is used to do a type erasure of the BinType passed to the constructor of the histogram:
   * calls to an Histogram instance will be forwarded via the virtual methods
   * to a concrete implementation that *knows* the actual type of the binning strategy, which will allow the
   * compiler to optimize (i.e. de-virtualize) calls if the overrides are marked as `final`.
   * This way we can do a single virtual call instead of multiple for things like getStats
   * @see BinStrategy
   */
  struct ComputationInterface {
    std::shared_ptr<std::vector<WeightType>> m_counts;
    ssize_t m_clip_left, m_clip_right;

    virtual ~ComputationInterface() = default;

    ComputationInterface() : m_counts(new std::vector<WeightType>()), m_clip_left(0),
                             m_clip_right(m_counts->size() - 1) {}

    size_t size() const {
      return m_clip_right - m_clip_left + 1;
    }

    virtual const BinStrategy<VarType>& getBinStrategy() const = 0;

    virtual std::unique_ptr<ComputationInterface> clone() const = 0;

    virtual void clip(VarType min, VarType max) = 0;

    virtual std::tuple<VarType, VarType, VarType> getStats() const = 0;
  };

  /**
   * Concrete implementation of ComputationInterface given a BinType
   * @tparam BinType
   *    Type of the binning strategy
   */
  template<typename BinType>
  struct ComputationImpl : public ComputationInterface {
    using ComputationInterface::m_counts;
    using ComputationInterface::m_clip_left;
    using ComputationInterface::m_clip_right;
    BinType m_binning;

    explicit ComputationImpl(BinType&& bin_type): m_binning(std::move(bin_type)) {
    }

    ComputationImpl(const ComputationImpl& other) = default;

    const BinStrategy<VarType>& getBinStrategy() const final {
      return m_binning;
    }

    std::unique_ptr<ComputationInterface> clone() const final {
      return make_unique<ComputationImpl<BinType>>(*this);
    }

    /**
     * Fill the bin counts
     * @tparam IterType
     *    Iterator type for both the edges and the values of the variable
     * @tparam WeightIterType
     *    Iterator type for the weights
     * @param begin
     *    Beginning of the data
     * @param end
     *    End of the data
     * @param wbegin
     *    Beginning of the weights
     */
    template<typename IterType, typename WeightIterType>
    void computeBins(IterType begin, IterType end, WeightIterType wbegin);

    void clip(VarType min, VarType max) final;

    std::tuple<VarType, VarType, VarType> getStats() const final;
  };

  std::unique_ptr<ComputationInterface> m_binning_concept;
};

} // end of namespace Histogram
} // end of namespace Euclid

#include "Histogram/_impl/ComputationImpl.icpp"

#endif // ALEXANDRIA_HISTOGRAM_HISTOGRAM_H
