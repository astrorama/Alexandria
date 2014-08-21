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

namespace Grid {

/**
 * @class GridContainer
 * 
 * @brief
 * Representation of a multi-dimensional grid which contains axis information
 * 
 * @details
 * The GridContainer class represents the notion of a multi-dimensional grid, each
 * axis of is represented by an GridAxis object. Note that this class is not
 * a mathematical tool, but it focuses on providing fast access to the grid
 * cells and axis information in an efficient way.
 * 
 * In fact, the GridContainer class delegates the handling of the grid cell values
 * to an instance of a GridCellManager object. The type of this object is given
 * as a template parameter and it can be any type (including mathematical
 * representations of grids from other libraries). To reduce the requirements
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
 * auto third_axis = grid.getAxis<2>();
 * \endcode
 * 
 * The cell values (both for reading and writing) can be accessed in two ways.
 * Either with the parenthesis operator, which gets as parameters the
 * coordinates of the cell, or by using the iterator returned by the begin()
 * method.
 * 
 * Accessing the grid by using the iterator is optimized for speed and is the
 * recommended way for traversing through the grid. This way of iteration
 * implies no performance penalty for the axis information management and it
 * is almost as fast as iterating through the GridCellManager containing the data.
 * If the axis information is required, it can be retrieved by using the
 * iterator.axisIndex() and iterator.axisValue() methods (with the implied
 * performance penalty).
 * 
 * Slicing the grid is supported by the iterator.fixAxisIndex() and
 * iterator.fixAxisValue() methods, which will modify the way the iterator
 * traverses the cells. For example:
 * 
 * @tparam GridCellManager The class to which the handling of the cell values is
 *                     delegated
 * @tparam AxesTypes The types of the grid axes
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
  template<typename CellType>
  class iter;
  
  typedef iter<cell_type> iterator;
  typedef iter<cell_type const> const_iterator;
  
  /**
   * @brief Constructs a GridContainer with the given axes
   * @details
   * The GridCellManager type must be given as a template parameter and an instance
   * of it will be created by using the GridCellManagerTraits.factory() method.
   * 
   * @param axes the GridAxis%es describing the axes of the grid
   */
  GridContainer(GridAxis<AxesTypes>... axes);
  
  /**
   * @brief Constructs a GridContainer with the given axes and cell manager
   * @details
   * This constructor will use as GridCellManager the given object and it will not
   * try to create a new one. The values in the cell_manager are preserved, so
   * they can be initialized prior the constructor call. If the given data
   * manager does not contain the number of data required for representing the
   * given axes, an exception is thrown.
   * 
   * @param cell_manager The cell manager instance which keeps the data
   * @param axes the GridAxis%es describing the axes of the grid
   * @throws ElementsException
   *    if the cell_manager has wrong size
   */
  GridContainer(std::unique_ptr<GridCellManager> cell_manager, GridAxis<AxesTypes>... axes);
  
  /**
   * @brief Constructs a GridContainer with the given axes
   * @details
   * The GridCellManager type must be given as a template parameter and an instance
   * of it will be created by using the GridCellManagerTraits.factory() method.
   * 
   * @param axes_tuple the GridAxis%es describing the axes of the grid
   */
  GridContainer(std::tuple<GridAxis<AxesTypes>...> axes_tuple);
  
  /**
   * @brief Constructs a GridContainer with the given axes and cell manager
   * @details
   * This constructor will use as GridCellManager the given object and it will not
   * try to create a new one. The values in the cell_manager are preserved, so
   * they can be initialized prior the constructor call. If the given data
   * manager does not contain the number of data required for representing the
   * given axes, an exception is thrown.
   * 
   * @param cell_manager The cell manager instance which keeps the data
   * @param axes_tuple the GridAxis%es describing the axes of the grid
   * @throws ElementsException
   *    if the cell_manager has wrong size
   */
  GridContainer(std::unique_ptr<GridCellManager> cell_manager, std::tuple<GridAxis<AxesTypes>...> axes_tuple);
  
  /// Default move constructor
  GridContainer(GridContainer<GridCellManager, AxesTypes...>&&) = default;
  
  GridContainer(const GridContainer<GridCellManager, AxesTypes...>&) = delete;
  
  /// Default destructor
  virtual ~GridContainer() = default;
  
  /// Returns the number of axes of the grid (dimensionality)
  size_t axisNumber() const;
  
  /**
   * Returns the information of a specific axis.
   * @tparam I The (zero based) index of the axis
   * @return the axis information
   */
  template<int I>
  const GridAxis<axis_type<I>>& getAxis() const;
  
  /// Returns a tuple containing the information of all the grid axes.
  const std::tuple<GridAxis<AxesTypes>...>& getAxesTuple() const;
  
  /// Returns a reference to the GridCellManager object which handles the cell values
  const GridCellManager& getCellManager() const;
  
  /// Returns an iterator to the first cell of the grid
  iterator begin();
  
  /// @copydoc begin()
  const_iterator begin() const;
  
  /// Returns an iterator to the cell after the last of the grid
  iterator end();
  
  /// @copydoc end()
  const_iterator end() const;
  
  /// Returns the total number of cells of the grid
  size_t size() const;
  
  /**
   * Returns a reference to the grid cell for the given axes indices, to be
   * used both for reading and writing. This method is not bound-checked and
   * out of range indices cause undefined behavior. If the caller cannot
   * guarantee that the indices will be in range, the method at() can be used,
   * which has the same behavior but performs out of range checks.
   * 
   * @param indices The indices of the axes
   * @return A reference to the cell
   */
  const cell_type& operator()(decltype(std::declval<GridAxis<AxesTypes>>().size())... indices) const;
  
  /// @copydoc operator() (decltype(std::declval<GridAxis<AxesTypes>>().size())...) const
  cell_type& operator()(decltype(std::declval<GridAxis<AxesTypes>>().size())... indices);
  
  /**
   * Returns a reference to the grid cell for the given axes indices, to be
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
  const cell_type& at(decltype(std::declval<GridAxis<AxesTypes>>().size())... indices) const;
  
  /// @copydoc at(decltype(std::declval<GridAxis<AxesTypes>>().size())...) const
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
 * @class GridContainer::iter
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
template<typename CellType>
class GridContainer<GridCellManager, AxesTypes...>::iter : public std::iterator<std::forward_iterator_tag, CellType> {
public:
  
  /**
   * @brief Constructs a new iterator for the given grid
   * @details
   * The cell on which the iterator points is controlled by the data_iter
   * parameter, which is an iterator to the GridCellManager of the grid.
   * 
   * @param owner The grid to iterate through
   * @param data_iter The GridCellManager iterator indicating the cell position
   */
  iter(const GridContainer<GridCellManager, AxesTypes...>& owner,
           const cell_manager_iter_type& data_iter);
  
  /// Copy operator of the iterator
  iter& operator=(const iter& other);
  
  /// Moves the iterator to the next grid cell
  iter& operator++();
  
  /// Returns a reference to the cell value
  CellType& operator*();
  
  /// Compares two iterators for equality. Should be used only for iterators
  /// of the same grid.
  bool operator==(const iter& other) const;
  
  /// Compares two iterators for inequality. Should be used only for iterators
  /// of the same grid.
  bool operator!=(const iter& other) const;
  
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
   * @return the iterator over the grid slice
   * @throws ElementsException
   *    if the given index is out of the bounds of the axis
   */
  template<int I>
  iter& fixAxisByIndex(size_t index);
  
  /**
   * Modifies the iterator to navigate only through cells with the given axis
   * value. If the current cell does not fulfill this requirement the iterator
   * will be forward to the first that does.
   * 
   * Note that this method will search in the values of the axis, so it implies
   * an overhead when compared with the fixAxisByIndex() method. For this
   * reason the use of fixAxisByIndex() should be favored.
   * 
   * @tparam I the index of the axis to fix
   * @param value the value to fix the axis to
   * @return the iterator over the grid slice
   * @throws ElementsException
   *    if the axis does not contain the given value
   */
  template<int I>
  iter& fixAxisByValue(const axis_type<I>& value);
  
private:
  
  const GridContainer<GridCellManager, AxesTypes...>& m_owner;
  cell_manager_iter_type m_data_iter;
  std::map<size_t, size_t> m_fixed_indices;
  void forwardToIndex(size_t axis, size_t fixed_index);
  
}; // end of class iter

} // end of namespace Grid

#include "GridContainer/_impl/GridContainer.icpp"
#include "GridContainer/_impl/GridIterator.icpp"

#endif	/* GRIDCONTAINER_GRIDCONTAINER_H */

