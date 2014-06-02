/** 
 * @file Matrix.h
 * @date May 13, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATRIX_MATRIX_H
#define	CHMATRIX_MATRIX_H

#include <memory>
#include <tuple>
#include <iterator>
#include <map>
#include "ChMatrix/DataManagerTraits.h"
#include "ChMatrix/MatrixIndexHelper.h"
#include "_impl/MatrixConstructionHelper.h"

namespace ChMatrix {

template<typename DataManager, typename... AxesTypes>
class Matrix {
  
  // The following aliases are used to simplify the definitions in the class
  typedef typename DataManagerTraits<DataManager>::data_type data_type;
  typedef typename DataManagerTraits<DataManager>::iterator data_iter_type;
  // The following can be used to retrieve the type type of each axis
  template<int I>
  using axis_type = typename std::tuple_element<I, std::tuple<AxesTypes...>>::type;

public:
  
  class iterator : public std::iterator<std::forward_iterator_tag, data_type> {
  public:
    iterator(const Matrix<DataManager, AxesTypes...>& owner,
             const data_iter_type& data_iter);
    iterator& operator=(const iterator& other);
    iterator& operator++();
    data_type& operator*();
    bool operator==(const iterator& other) const;
    bool operator!=(const iterator& other) const;
    template<int I>
    size_t axisIndex() const;
    template<int I>
    const axis_type<I>& axisValue() const;
    template<int I>
    iterator& fixAxis(size_t index);
  private:
    const Matrix<DataManager, AxesTypes...>& m_owner;
    data_iter_type m_data_iter;
    std::map<size_t, size_t> m_fixed_indices;
    void forwardToIndex(size_t axis, size_t fixed_index);
  }; // end of class iterator
  
  Matrix(AxisInfo<AxesTypes>... axes);
  
  Matrix(std::unique_ptr<DataManager> data_manager, AxisInfo<AxesTypes>... axes);
  
  Matrix(std::tuple<AxisInfo<AxesTypes>...> axes_tuple);
  
  Matrix(std::unique_ptr<DataManager> data_manager, std::tuple<AxisInfo<AxesTypes>...> axes_tuple);
  
  virtual ~Matrix() = default;
  
  size_t rank() const;
  
  template<int I>
  const AxisInfo<axis_type<I>>& axisInfo() const;
  
  const std::tuple<AxisInfo<AxesTypes>...>& axisInfoTuple() const;
  
  const DataManager& dataManager() const;
  
  iterator begin();
  
  iterator end();
  
  size_t size();
  
  data_type& operator()(decltype(std::declval<AxisInfo<AxesTypes>>().size())... indices);
  
private:
  
  std::tuple<AxisInfo<AxesTypes>...> m_axes;
  MatrixIndexHelper<AxesTypes...> m_index_helper {m_axes};
  std::unique_ptr<DataManager> m_data_manager {
          DataManagerTraits<DataManager>::factory(
                  MatrixConstructionHelper<AxesTypes...>::getAxisIndexFactor(
                          m_axes, TemplateLoopCounter<sizeof...(AxesTypes)-1>{}))
  };

}; // end of class Matrix

} // end of namespace ChMatrix

#include "ChMatrix/_impl/Matrix.icpp"
#include "ChMatrix/_impl/MatrixIterator.icpp"

#endif	/* CHMATRIX_MATRIX_H */

