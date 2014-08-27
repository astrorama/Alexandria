/** 
 * @file GridContainer/GridAxis.h
 * @date May 12, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef GRIDCONTAINER_GRIDAXIS_H
#define	GRIDCONTAINER_GRIDAXIS_H

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
template<typename T>
class GridAxis {

public:
  
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

private:
  
  std::string m_name;
  std::vector<T> m_values;
  
};

} // end of namespace GridContainer
} // end of namespace Euclid

#include "GridContainer/_impl/GridAxis.icpp"

#endif	/* GRIDCONTAINER_GRIDAXIS_H */
