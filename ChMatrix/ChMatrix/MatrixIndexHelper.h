/** 
 * @file ChMatrix/MatrixIndexHelper.h
 * @date May 15, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATRIX_MATRIXINDEXHELPER_H
#define	CHMATRIX_MATRIXINDEXHELPER_H

#include <vector>
#include <tuple>
#include "ChMatrix/AxisInfo.h"
#include "_impl/MatrixConstructionHelper.h"

namespace ChMatrix {

/**
 * @class MatrixIndexHelper
 * 
 * @brief Helper class for converting multi-dimensional matrix coordinates to
 * the index of a long data array and vice versa
 * 
 * @details
 * The assumption for the mapping is that the first axis is assumed to vary the
 * fastest and the last the slowest. All indices and coordinates are zero
 * based (start from zero). This class exists mainly to be
 * used internally for the Matrix iterator operations, but it is considered
 * part of the public interface of the ChMatrix module and can be used by
 * any class which wants to perform such conversions. Use of this class in
 * such cases is recommended for performance reasons.
 * 
 * @tparam AxesTypes The types of the Matrix axes
 */
template<typename... AxesTypes>
class MatrixIndexHelper {

public:
  
  /**
   * Constructs a new MatrixIndexHelper instance for making conversions for
   * a Matrix with the given axes. For avoiding the long template syntax
   * consider using the makeMatrixIndexHelper() factory method instead.
   * 
   * @param axes_tuple The information about the axes of the Matrix
   */
  MatrixIndexHelper(const std::tuple<AxisInfo<AxesTypes>...>& axes_tuple)
          : m_axes_sizes { 
                MatrixConstructionHelper<AxesTypes...>::createAxesSizesVector(
                        axes_tuple, TemplateLoopCounter<sizeof...(AxesTypes)>{})
          }, m_axes_index_factors {
                MatrixConstructionHelper<AxesTypes...>::createAxisIndexFactorVector(
                     axes_tuple, TemplateLoopCounter<sizeof...(AxesTypes)>{})
          } { }
  
  /// Default destructor
  virtual ~MatrixIndexHelper() = default;
  
  /**
   * Returns the coordinate of the Matrix axis with the given index which
   * corresponds to the given index of a one dimensional array containing all
   * the Matrix elements.
   * 
   * @param axis The axis to get the index for
   * @param array_index The index of the one dimensional array
   * @return the coordinate of the axis
   */
  size_t axisIndex(size_t axis, size_t array_index) const {
    size_t index = array_index % m_axes_index_factors[axis+1];
    index = index / m_axes_index_factors[axis];
  return index;
  }
  
  /**
   * Returns the index of a one dimensional array which corresponds to the
   * given Matrix coordinates.
   * 
   * @param coords The Matrix coordinates
   * @return the one dimensional array index
   */
  size_t totalIndex(std::initializer_list<size_t> coords) const {
    size_t total {0};
    auto coords_iter = coords.begin();
    auto factors_iter = m_axes_index_factors.begin();
    while (coords_iter != coords.end()) {
      total += (*coords_iter) * (*factors_iter);
      ++coords_iter;
      ++factors_iter;
    }
    return total;
  }
  
  std::vector<size_t> m_axes_sizes;
  std::vector<size_t> m_axes_index_factors;
};

/**
 * Factory method for simplifying the creation of MatrixIndexHelper instances.
 * It is equivalent with using the constructor by specifying the AxesTypes
 * template parameters.
 * 
 * @tparam AxesTypes the types of the Matrix axes
 * @param axes_tuple the information of the Matrix axes
 * @return The MatrixIndexHelper instance
 */
template<typename... AxesTypes>
MatrixIndexHelper<AxesTypes...> makeMatrixIndexHelper(const std::tuple<AxisInfo<AxesTypes>...>& axes_tuple) {
  return MatrixIndexHelper<AxesTypes...>(axes_tuple);
}

} // end of namespace ChMatrix

#endif	/* CHMATRIX_MATRIXINDEXHELPER_H */

