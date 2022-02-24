/** Copyright © 2021 Université de Genève, LMU Munich - Faculty of Physics, IAP-CNRS/Sorbonne Université
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

#ifndef _KDTREE_KDTREE_H_
#define _KDTREE_KDTREE_H_

#include <algorithm>
#include <memory>
#include <vector>

namespace KdTree {

template <typename T>
struct KdTreeTraits {
  /**
   * @return the number of dimensions
   */
  static std::size_t getDimensions(const T& t);

  /**
   * @return the value for the coordinate `index`
   */
  static double getCoord(const T& t, size_t index);
};

/**
 * Euclidean distance
 * @tparam T
 */
template <typename T>
struct EuclideanDistance {
  static bool isCloserThan(const T& a, const T& b, double distance);
};

/**
 * Chebyshev Distance: max(|x_i - y_i|)
 * @tparam T
 */
template <typename T>
struct ChebyshevDistance {
  static bool isCloserThan(const T& a, const T& b, double distance);
};

/**
 * @class KdTree
 * @brief A simple N-dimensional KdTree for speeding-up elements within range types of queries.
 *
 * template arguments: T type, a traits implementation to access coordinates must be provided
 *                     DistanceMethod type, a class providing a static method indicating if two points
 *                                    are closer than a given distance
 */

template <typename T, typename DistanceMethod = EuclideanDistance<T>>
class KdTree {
public:
  using Traits = KdTreeTraits<T>;

  explicit KdTree(const std::vector<T>& data, std::size_t leaf_size = 100);

  /**
   * Return the points that are within the given radius from the coordinate `coord`
   * @param coord
   * @param radius
   * @return
   */
  std::vector<T> findPointsWithinRadius(const T& coord, double radius) const;

  /**
   * Count how many points are within the given radius from the coordonate `coord`
   * @param coord
   * @param radius
   * @return
   */
  std::size_t countPointsWithinRadius(const T& coord, double radius) const;

private:
  class Node;
  class Leaf;
  class Split;

  std::size_t           m_dimensionality;
  std::shared_ptr<Node> m_root;
};

/**
 * Trait specialization for std::vector
 */
template <typename U>
struct KdTreeTraits<std::vector<U>> {
  static std::size_t getDimensions(const std::vector<U>& t) {
    return t.size();
  }

  static double getCoord(const std::vector<U>& t, size_t index) {
    return t[index];
  }
};

/**
 * Trait specialization for std::array
 */
template <typename U, std::size_t S>
struct KdTreeTraits<std::array<U, S>> {
  static std::size_t getDimensions(const std::array<U, S>& t) {
    return S;
  }

  static double getCoord(const std::array<U, S>& t, size_t index) {
    return t[index];
  }
};

}  // namespace KdTree

#include "_impl/KdTree.icpp"

#endif /* _KDTREE_KDTREE_H_ */
