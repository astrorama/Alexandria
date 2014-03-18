/**
 * @file Matrix.h
 * @date December 4, 2013
 * @author Nikolaos Apostolakos
 */

#ifndef MATRIX_H
#define	MATRIX_H

#include <cstdint>
#include <tuple>
#include <vector>
#include <boost/serialization/access.hpp>
#include "ProtoZ/matrix/AxisInfo.h"

namespace ProtoZ {
namespace matrix {

/**
 * @class Matrix
 * @brief
 *      A multidimensional matrix containing its data and information about its
 *      axes
 * @details
 *      This class implements the different dimensionalities by using variadic
 *      templates. The axes information can be retrieved by using the axesInfo()
 *      method. Access to the matrix data is done by using the setValue() and 
 *      getValue() methods.
 * 
 * @tparam T
 *      The type of the matrix values
 * @tparam Axes
 *      The types of the matrix axes world values
 */
template<typename T, typename... Axes>
class Matrix {
  
  // Allow direct access to the members to facilitate boost serialization
  template <typename Archive, typename U, typename... Z>
  friend void boost::serialization::serialize(Archive&, Matrix<U,Z...>&, const unsigned int);
  
  // Allow direct access to the members to facilitated export to ASCII table
  friend class MatrixAsciiExporter;
  friend class MatrixFitsExporter;

public:
  
  /**
   * @brief
   *    Default constructor
   * @details
   *    To be used for boost serialization. For normal usage use one of the
   *    other constructors.
   */
  Matrix() = default;

  /**
   * @brief
   *    Constructs a new Matrix instance with the given axes
   * @details
   *    This constructor recognizes from the number and sizes of the given axes
   *    the dimensionality and total size of the matrix. The total amount of
   *    memory to store the matrix data is allocated during construction. All
   *    matrix elements are created with the default constructor.
   * 
   * @param axes
   *    The axes of the matrix
   */
  Matrix(const AxisInfo<Axes>&... axes);
  
  // Because the matrix instances will be very big, we forbid copying and allow
  // moving. The default moving is enough because vectors implement it in a
  // fast way.
  Matrix(const Matrix&) = delete;
  Matrix& operator=(const Matrix&) = delete;
  
  Matrix(Matrix&&) = default;
  Matrix& operator=(Matrix&&) = default;

  /**
   * @brief Destructor
   */
  virtual ~Matrix() = default;

  /**
   * @brief
   *    Returns the rank (or dimensionality or number of axes) of the matrix
   * 
   * @return 
   *    The rank of the matrix
   */
  uint32_t rank() const;

  /**
   * @brief
   *    Return the information about the matrix axes
   * 
   * @return 
   *    The information about the matrix axes
   */
  const std::tuple<AxisInfo<Axes>...>& axesInfo() const;

  /**
   * @brief
   *    Sets the value of the matrix cell
   * 
   * @param coords
   *    The coordinates of the matrix cell to set
   * @param value
   *    The new value of the cell
   * @throws std::out_of_range
   *    If any of the indexes is out of range
   */
  void setValue(const uint32_t (&coords)[sizeof...(Axes)], const T& value);

  /**
   * @brief
   *    Returns the value of a matrix cell
   * 
   * @param coords
   *    The coordinates of the matrix cell
   * @return 
   *    The matrix cell value
   * @throws std::out_of_range
   *    If any of the indexes is out of range
   */
  const T& getValue(const uint32_t (&coords)[sizeof...(Axes)]) const;

private:
  
  /// A tuple where the matrix axes information is stored
  std::tuple<AxisInfo<Axes>...> m_axes;
  
  /// A (long) vector where the matrix data are stored
  std::vector<T> m_data;
  
  /// A helper vector which keeps the sizes of all the axes for quick reference
  std::vector<uint32_t> m_axis_sizes;
  
  /// A helper vector which keeps the factors with which each axis index needs
  /// to be multiplied to calculate the index of the vector where the data are
  /// stored
  std::vector<uint64_t> m_axis_index_factors;
  
  /**
   * @class MatrixIndexHelper
   * @brief
   *    An internal helper class which calculates the indexes of the vector where
   *    the data are stored, using variadic template loops.
   */
  class MatrixIndexHelper;
  
};

} /* namespace matrix */
} /* namespace ProtoZ */

#define MATRIX_IMPL
#include "ProtoZ/matrix/_impl/Matrix.icpp"
#undef MATRIX_IMPL

#endif	/* MATRIX_H */

