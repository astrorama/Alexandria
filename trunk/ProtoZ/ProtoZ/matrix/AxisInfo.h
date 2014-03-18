/** 
 * @file AxisInfo.h
 * @date December 4, 2013
 * @author Nikolaos Apostolakos
 */

#ifndef AXISINFO_H
#define	AXISINFO_H

#include <string>
#include <vector>
#include <cstdint>

namespace ProtoZ {
namespace matrix {

/**
 * @class AxisInfo
 * @brief
 *      Represents an axis of a multidimensional matrix.
 * @details
 *      Each axis has a name and a size, which shows the size of the matrix in
 *      the dimension of the axis. The conversion between the axis knot indexes
 *      (which are used for accessing the matrix) and the axis world values is
 *      done with the methods indexToValue() and valueToIndex().
 * 
 * @tparam T
 *      The type of the axis world values
 */
template<typename T>
class AxisInfo {

  // Allow direct access to the members to facilitate boost serialization
  template <typename Archive,typename U>
  friend void boost::serialization::serialize(Archive&, AxisInfo<U>&,
                                              const unsigned int);

public:

  /**
   * @brief
   *    Default constructor
   * @details
   *    To be used for boost serialization. For normal usage use one of the
   *    other constructors.
   */
  AxisInfo() = default;

  /**
   * @brief
   *    Constructs a new AxisInfo instance with the given name and values.
   * @details
   *    The name as well as the values are copied internally. This requires that
   *    the T type implements the copy assignment. Any further modifications
   *    to the name or values parameters are not reflected to the AxisInfo
   *    object.
   * 
   * @param name
   *    The name of the axis
   * @param values
   *    The world values of the axis
   */
  AxisInfo(const std::string& name, const std::vector<T>& values);

  /**
   * @brief Destructor
   */
  virtual ~AxisInfo() = default;

  /**
   * @brief
   *    Returns the number of knots (number of values) of the axis.
   * 
   * @return
   *    The number of knots of the axis
   */
  uint32_t size() const;

  /**
   * @brief
   *    Returns the name of the axis.
   * 
   * @return 
   *    The name of the axis
   */
  const std::string& name() const;

  /**
   * @brief
   *    Converts an axis index to the world value
   * @details
   *    The axis indexes are zero based and represent the coordinate of the
   *    matrix. The world value is the axis real value represented by this index.
   * 
   * @param index
   *    The axis index (zero based)
   * @return 
   *    The axis world value
   * @throws
   *    std::out_of_range, if the index is grater or equal than the axis size
   */
  const T& indexToValue(uint32_t index) const;

  /**
   * @brief
   *    Converts an axis world value to its index
   * @details
   *    This method converts only world values which are exact representations
   *    of the axis knots (does not return "closest" knot). If there is no knot
   *    representing the exact given value -1 is returned. The equality is
   *    checked using the equality operator.
   * @param value
   *    The value to convert to index
   * @return
   *    The (zero based) index of the knot representing the given value or -1
   *    if there is no such knot
   */
  int64_t valueToIndex(const T& value) const;
  
private:
  
  std::string m_name;
  std::vector<T> m_values;
  
};

} /* namespace matrix */
} /* namespace ProtoZ */

#define AXISINFO_IMPL
#include "ProtoZ/matrix/_impl/AxisInfo.icpp"
#undef AXISINFO_IMPL

#endif	/* AXISINFO_H */

