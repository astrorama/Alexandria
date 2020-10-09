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
 * @file GridContainer/GridAxis.h
 * @date May 12, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef GRIDCONTAINER_GRIDAXIS_H
#define GRIDCONTAINER_GRIDAXIS_H

#include <string>
#include <vector>

namespace Euclid {
namespace GridContainer {

/**
 * @class GridAxis
 *
 * @brief
 * Provides information related with an axis of a GridContainer
 *
 * @details
 * An axis has a name and a set of values, one for each knot of the axis. The
 * GridAxis provides access to the values of the knots by using an iterator or
 * by using the (zero based) index of the knot. Note that the GridAxis is
 * designed to be immutable.
 *
 * @tparam T the type of the axis values
 */
template <typename T>
class GridAxis {

public:
  /// The type of the axis values
  typedef T data_type;

  /// The iterator type of the GridAxis
  typedef typename std::vector<T>::const_iterator const_iterator;

  /// Constructs an GridAxis with the given name and knot values
  GridAxis(std::string name, std::vector<T> values);

  /// Default destructor
  virtual ~GridAxis() = default;

  /// Returns the number of knots of the axis
  size_t size() const;

  /// Returns the name of the axis
  const std::string& name() const;

  /// Returns the value of the knot with the given index
  const T& operator[](size_t index) const;

  /// Returns an iterator at the first knot of the axis
  const_iterator begin() const;

  /// Returns an iterator after the last knot of the axis
  const_iterator end() const;

  /**
   * @brief
   * Compares the axis with another axis
   * @details
   * Two axes are considered equal if they have the same length and equal
   * knots. They do not have to be of the same type. The only requirement is
   * that the operation T == U is valid.
   * @param other
   *    The axis to compare with
   * @return
   *    true if the two axes have the same size and equal knots, false otherwise
   */
  template <typename U>
  bool operator==(const GridAxis<U>& other) const;

  /// The opposite of the == operator
  template <typename U>
  bool operator!=(const GridAxis<U>& other) const;

private:
  std::string    m_name;
  std::vector<T> m_values;
};

}  // end of namespace GridContainer
}  // end of namespace Euclid

#include "GridContainer/_impl/GridAxis.icpp"

#endif /* GRIDCONTAINER_GRIDAXIS_H */
