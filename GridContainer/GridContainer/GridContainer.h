/** 
 * @file GridContainer/GridContainer.h
 * @date May 13, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef GRIDCONTAINER_GRIDCONTAINER_H
#define	GRIDCONTAINER_GRIDCONTAINER_H

#include <memory>
#include <tuple>
#include <iterator>
#include <map>
#include "GridContainer/GridCellManagerTraits.h"
#include "GridContainer/GridIndexHelper.h"
#include "_impl/GridConstructionHelper.h"

namespace GridContainer {

/**
 * @class GridContainer
 * 
 * @brief
 * Representation of a multi-dimensional matrix which contains axis information
 * 
 * @details
 * The GridContainer class represents the notion of a multi-dimensional matrix, each
 * axis of is represented by an GridAxis object. Note that this class is not
 * a mathematical tool, but it focuses on providing fast access to the matrix
 * cells and axis information in an efficient way.
 * 
 * In fact, the GridContainer class delegates the handling of the matrix cell values
 * to an instance of a GridCellManager object. The type of this object is given
 * as a template parameter and it can be any type (including mathematical
 * representations of matrices from other libraries). To reduce the requirements
 * on the GridCellManager type, the GridContainer class does not access it directly, but
 * it uses the GridCellManagerTraits. This allows to use as GridCellManager even classes
 * of third party libraries, by defining a specialization of GridCellManagerTraits
 * (for more information refer to the documentation of GridCellManagerTraits).
 * 
 * The axis information of the GridContainer can be accessed by using the method
 * getAxis(). This method gets one integer template parameter, which defines
 * which axis information will be returned. Note that it is zero based. For
 * example, the information of the third axis can be accessed with the
 * following command:
 * 
 * \code {.cpp}
 * auto third_axis = matrix.getAxis<2>();
 * \endcode
 * 
 * The cell values (both for reading and writing) can be accessed in two ways.
 * Either with the parenthesis operator, which gets as parameters the
 * coordinates of the cell, or by using the iterator returned by the begin()
 * method.
 * 
 * Accessing the matrix by using the iterator is optimized for speed and is the
 * recommended way for traversing through the matrix. This way of iteration
 * implies no performance penalty for the axis information management and it
 * is almost as fast as iterating through the GridCellManager containing the data.
 * If the axis information is required, it can be retrieved by using the
 * iterator.axisIndex() and iterator.axisValue() methods (with the implied
 * performance penalty).
 * 
 * Slicing the matrix is supported by the iterator.fixAxisIndex() and
 * iterator.fixAxisValue() methods, which will modify the way the iterator
 * traverses the cells. For example:
 * 
 * @tparam GridCellManager The class to which the handling of the cell values is
 *                     delegated
 * @tparam AxesTypes The types of the matrix axes
 */
template<typename GridCellManager, typename... AxesTypes>
class GridContainer {
  
  // The following aliases are used to simplify the definitions inside the class
  typedef typename GridCellManagerTraits<GridCellManager>::data_type cell_type;
  typedef typename GridCellManagerTraits<GridCellManager>::iterator cell_manager_iter_type;
  // The following is a shortcut to retrieve the type of each axis
  template<int I>
  using axis_type = typename std::tuple_element<I, std::tuple<AxesTypes...>>::type;

public:
  
  // The iterator type of the GridContainer. See at the end of the file for its declaration
  class iterator;
  
  /**
   * @brief Constructs a GridContainer with the given axes
   * @details
   * The GridCellManager type must be given as a template parameter and an instance
   * of it will be created by using the GridCellManagerTraits.factory() method.
   * 
   * @param axes the GridAxis%s describing the axes of the matrix
   */
  GridContainer(GridAxis<AxesTypes>... axes);
  
  /**
   * @brief Constructs a GridContainer with the given axes and data manager
   * @details
   * This constructor will use as GridCellManager the given object and it will not
   * try to create a new one. The values in the data_manager are preserved, so
   * they can be initialized prior the constructor call. If the given data
   * manager does not contain the number of data required for representing the
   * given axes, an exception is thrown.
   * 
   * @param data_manager The data manager instance which keeps the data
   * @param axes the GridAxis%s describing the axes of the matrix
   * @throws ElementsException
   *    if the data_manager has wrong size
   */
  GridContainer(std::unique_ptr<GridCellManager> data_manager, GridAxis<AxesTypes>... axes);
  
  /**
   * @brief Constructs a GridContainer with the given axes
   * @details
   * The GridCellManager type must be given as a template parameter and an instance
   * of it will be created by using the GridCellManagerTraits.factory() method.
   * 
   * @param axes_tuple the GridAxis%s describing the axes of the matrix
   */
  GridContainer(std::tuple<GridAxis<AxesTypes>...> axes_tuple);
  
  /**
   * @brief Constructs a GridContainer with the given axes and data manager
   * @details
   * This constructor will use as GridCellManager the given object and it will not
   * try to create a new one. The values in the data_manager are preserved, so
   * they can be initialized prior the constructor call. If the given data
   * manager does not contain the number of data required for representing the
   * given axes, an exception is thrown.
   * 
   * @param data_manager The data manager instance which keeps the data
   * @param axes_tuple the GridAxis%s describing the axes of the matrix
   * @throws ElementsException
   *    if the data_manager has wrong size
   */
  GridContainer(std::unique_ptr<GridCellManager> data_manager, std::tuple<GridAxis<AxesTypes>...> axes_tuple);
  
  /// Default move constructor
  GridContainer(GridContainer<GridCellManager, AxesTypes...>&&) = default;
  
  GridContainer(const GridContainer<GridCellManager, AxesTypes...>&) = delete;
  
  /// Default destructor
  virtual ~GridContainer() = default;
  
  /// Returns the number of axes of the matrix (dimensionality)
  size_t axisNumber() const;
  
  /**
   * Returns the information of a specific axis.
   * @tparam I The (zero based) index of the axis
   * @return the axis information
   */
  template<int I>
  const GridAxis<axis_type<I>>& getAxis() const;
  
  /// Returns a tuple containing the information of all the matrix axes.
  const std::tuple<GridAxis<AxesTypes>...>& getAxesTuple() const;
  
  /// Returns a reference to the GridCellManager object which handles the cell values
  const GridCellManager& getDataManager() const;
  
  /// Returns an iterator to the first cell of the matrix
  iterator begin();
  
  /// Returns an iterator to the cell after the last of the matrix
  iterator end();
  
  /// Returns the total number of cells of the matrix
  size_t size();
  
  /**
   * Returns a reference to the matrix cell for the given axes indices, to be
   * used both for reading and writing. This method is not bound-checked and
   * out of range indices cause undefined behavior. If the caller cannot
   * guarantee that the indices will be in range, the method at() can be used,
   * which has the same behavior but performs out of range checks.
   * 
   * @param indices The indices of the axes
   * @return A reference to the cell
   */
  cell_type& operator()(decltype(std::declval<GridAxis<AxesTypes>>().size())... indices);
  
  /**
   * Returns a reference to the matrix cell for the given axes indices, to be
   * used both for reading and writing. This method is the bound-checked
   * alternative of the parenthesis operator. Note that if the caller can
   * guarantee that the indices will be in range, the parenthesis operator
   * is a better choice, because it will be faster.
   * 
   * @param indices The indices of the axes
   * @return A reference to the cell
   * @throws ElementsException
   *    if any of the indices is out of range
   */
  cell_type& at(decltype(std::declval<GridAxis<AxesTypes>>().size())... indices);
  
private:
  
  std::tuple<GridAxis<AxesTypes>...> m_axes;
  GridIndexHelper<AxesTypes...> m_index_helper {m_axes};
  std::unique_ptr<GridCellManager> m_cell_manager {
          GridCellManagerTraits<GridCellManager>::factory(
                  GridConstructionHelper<AxesTypes...>::getAxisIndexFactor(
                          m_axes, TemplateLoopCounter<sizeof...(AxesTypes)-1>{}))
  };

}; // end of class GridContainer


/**
 * @class GridContainer::iterator
 * 
 * @brief Class to iterate through the GridContainer cells
 * 
 * @details
 * The GridContainer iterator provides efficient iteration through the cells of a
 * GridContainer. If the axis information is not accessed, the iteration is almost as
 * efficient as directly iterating through the GridCellManager. At any moment, the
 * methods axisIndex() and axisValue() can be used to access the axes
 * information. Slicing can be achieved by using the fixAxisByIndex() and
 * fixAxisByValue() methods.
 */
template<typename GridCellManager, typename... AxesTypes>
class GridContainer<GridCellManager, AxesTypes...>::iterator : public std::iterator<std::forward_iterator_tag, cell_type> {
public:
  
  /**
   * @brief Constructs a new iterator for the given matrix
   * @details
   * The cell on which the iterator points is controlled by the data_iter
   * parameter, which is an iterator to the GridCellManager of the matrix.
   * 
   * @param owner The matrix to iterate through
   * @param data_iter The GridCellManager iterator indicating the cell position
   */
  iterator(const GridContainer<GridCellManager, AxesTypes...>& owner,
           const cell_manager_iter_type& data_iter);
  
  /// Copy operator of the iterator
  iterator& operator=(const iterator& other);
  
  /// Moves the iterator to the next matrix cell
  iterator& operator++();
  
  /// Returns a reference to the cell value
  cell_type& operator*();
  
  /// Compares two iterators for equality. Should be used only for iterators
  /// of the same matrix.
  bool operator==(const iterator& other) const;
  
  /// Compares two iterators for inequality. Should be used only for iterators
  /// of the same matrix.
  bool operator!=(const iterator& other) const;
  
  /// Returns the index (coordinate) of the axis with index I, for the cell
  /// the iterator points
  template<int I>
  size_t axisIndex() const;
  
  /// Returns the value of the axis with index I, for the cell the iterator
  /// points
  template<int I>
  const axis_type<I>& axisValue() const;
  
  /**
   * Modifies the iterator to navigate only through cells with the given axis
   * index. If the current cell does not fulfil this requirement the iterator
   * will be forward to the first that does.
   * 
   * @tparam I the index of the axis to fix
   * @param index the index to fix the axis to
   * @return the iterator over the matrix slice
   * @throws ElementsException
   *    if the given index is out of the bounds of the axis
   */
  template<int I>
  iterator& fixAxisByIndex(size_t index);
  
  /**
   * Modifies the iterator to navigate only through cells with the given axis
   * value. If the current cell does not fulfil this requirement the iterator
   * will be forward to the first that does.
   * 
   * Note that this method will search in the values of the axis, so it implies
   * an overhead when compared with the fixAxisByIndex() method. For this
   * reason the use of fixAxisByIndex() should be favored.
   * 
   * @tparam I the index of the axis to fix
   * @param value the value to fix the axis to
   * @return the iterator over the matrix slice
   * @throws ElementsException
   *    if the axis does not contain the given value
   */
  template<int I>
  iterator& fixAxisByValue(const axis_type<I>& value);
  
private:
  
  const GridContainer<GridCellManager, AxesTypes...>& m_owner;
  cell_manager_iter_type m_data_iter;
  std::map<size_t, size_t> m_fixed_indices;
  void forwardToIndex(size_t axis, size_t fixed_index);
  
}; // end of class iterator

} // end of namespace GridContainer

#include "GridContainer/_impl/GridContainer.icpp"
#include "GridContainer/_impl/GridIterator.icpp"

#endif	/* GRIDCONTAINER_GRIDCONTAINER_H */

