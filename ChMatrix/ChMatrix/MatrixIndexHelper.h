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

template<typename... AxesTypes>
class MatrixIndexHelper {

public:
  
  MatrixIndexHelper(std::tuple<AxisInfo<AxesTypes>...> axes_tuple)
          : m_axes_sizes { 
                MatrixConstructionHelper<AxesTypes...>::createAxesSizesVector(
                        axes_tuple, TemplateLoopCounter<sizeof...(AxesTypes)>{})
          }, m_axes_index_factors {
                MatrixConstructionHelper<AxesTypes...>::createAxisIndexFactorVector(
                     axes_tuple, TemplateLoopCounter<sizeof...(AxesTypes)>{})
          } { }
  
  virtual ~MatrixIndexHelper() = default;
  
  size_t axisIndex(size_t axis, size_t total_index) const {
    size_t index = total_index % m_axes_index_factors[axis+1];
    index = index / m_axes_index_factors[axis];
  return index;
  }
  
  size_t totalIndex(std::initializer_list<size_t> indices) const {
    size_t total {0};
    auto indices_iter = indices.begin();
    auto factors_iter = m_axes_index_factors.begin();
    while (indices_iter != indices.end()) {
      total += (*indices_iter) * (*factors_iter);
      ++indices_iter;
      ++factors_iter;
    }
    return total;
  }
  
  std::vector<size_t> m_axes_sizes;
  std::vector<size_t> m_axes_index_factors;
};

template<typename... AxesTypes>
MatrixIndexHelper<AxesTypes...> makeMatrixIndexHelper(std::tuple<AxisInfo<AxesTypes>...> axes_tuple) {
  return MatrixIndexHelper<AxesTypes...>(axes_tuple);
}

} // end of namespace ChMatrix

#endif	/* CHMATRIX_MATRIXINDEXHELPER_H */

