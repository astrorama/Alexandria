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
#include <type_traits>
#include "GridContainer/GridCellManagerTraits.h"
#include "GridContainer/GridIndexHelper.h"
#include "_impl/GridConstructionHelper.h"

namespace Euclid {
namespace GridContainer {

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
 * Slicing the grid is supported by two ways. The iterator.fixAxisIndex() and
 * iterator.fixAxisValue() methods modify the way an iterator traverses through
 * a grid object. The GridContainer.fixAxisIndex() and GridContainer.fisAxisValue()
 * methods return grid objects representing silces of the original grid. Note that
 * these slices share the same underling data with the original grid and any
 * modifications will be reflected. For more information see the documentation
 * of the related methods.
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

public:

  // The following is a shortcut to retrieve the type of each axis
  template<int I>
  using axis_type = typename std::tuple_element<I, std::tuple<AxesTypes...>>::type;

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
   * @brief Constructs a GridContainer with the given axes
   * @details
   * The GridCellManager type must be given as a template parameter and an instance
   * of it will be created by using the GridCellManagerTraits.factory() method.
   *
   * @param axes_tuple the GridAxis%es describing the axes of the grid
   */
  GridContainer(std::tuple<GridAxis<AxesTypes>...> axes_tuple);

  /// Default move constructor
  GridContainer(GridContainer<GridCellManager, AxesTypes...>&&) = default;

  // Do not allow copying of GridContainer objects. This is done because these
  // objects will most of the time be very big and copying them will be a
  // bottleneck. To avoid unvoluntary copy constructor calls, this constructor
  // is deleted.
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

  /// Returns an iterator to the first cell of the grid
  iterator begin();

  /// @copydoc begin()
  const_iterator begin() const;

  /// Returns a constant iterator to the first cell of the grid
  const_iterator cbegin();

  /// Returns an iterator to the cell after the last of the grid
  iterator end();

  /// @copydoc end()
  const_iterator end() const;

  /// Returns a constant iterator to the cell after the last of the grid
  const_iterator cend();

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
   * @throws Elements::Exception
   *    if any of the indices is out of range
   */
  const cell_type& at(decltype(std::declval<GridAxis<AxesTypes>>().size())... indices) const;

  /// @copydoc at(decltype(std::declval<GridAxis<AxesTypes>>().size())...) const
  cell_type& at(decltype(std::declval<GridAxis<AxesTypes>>().size())... indices);
  
  /**
   * @brief Returns a slice of the grid based on an axis index
   * @details
   * The returned GridContainer has the same number of axes with the original,
   * with the fixed axis having a single value. The two grids (original and shared)
   * share the same data and any modifications are reflected to both.
   * 
   * @tparam I
   *    the (zero based) index of the axis to fix
   * @param index
   *    the index (zero based) to fix the axis to
   * @return
   *    A GridContainer representing the slice
   * @throws Elements::Exception 
   *    if the given index is out of the bounds of the axis
   * @throws Elements::Exception
   *    if the grid container is a slice and has this axis already fixed
   */
  template <int I>
  GridContainer<GridCellManager, AxesTypes...> fixAxisByIndex(size_t index);
  
  /**
   * @brief
   * const version of the fixAxisByIndex(size_t) method
   * @details
   * <b>Important note:</b> Because the returned GridContainer shares the same
   * underlying data with the original one, the returned object is a constant
   * grid (othewise it could be used for modifying the original object, which is
   * constant). This, with combination that the GridContainer does not have a
   * copy constructor (to avoid performance pitfalls), does not allow for creating
   * a new object from the returned rvalue. For example the following are wrong:
   * 
   * \code {.cpp}
   * const GridContainer grid1 = ...;
   * GridContainer grid2 = grid1.fixAxisByIndex<0>(0); // WRONG - DO NOT DO THAT
   * const GridContainer grid3 = grid1.fixAxisByIndex<0>(0); // WRONG - DO NOT DO THAT
   * auto grid3 = grid4.fixAxisByIndex<0>(0); // WRONG - DO NOT DO THAT
   * \endcode
   * 
   * All the above will try to create a new GridContainer object by using the
   * deleted copy constructor, which will result to the compilation failing with
   * the related message.
   * 
   * The way to use the object returned by this method is to assign a constant
   * reference to it. This action will extend the life of the temporary rvalue
   * object to the lifetime of the reference. For example:
   * 
   * \code {.cpp}
   * const GridContainer grid1 = ...;
   * const GridContainer& grid2 = grid1.fixAxisByIndex<0>(0); // CORRECT
   * auto& grid3 = grid1.fixAxisByIndex<0>(0); // CORRECT
   * \endcode
   */
  template <int I>
  const GridContainer<GridCellManager, AxesTypes...> fixAxisByIndex(size_t index) const;
  
  /**
   * @brief Returns a slice of the grid based on an axis value
   * @details
   * The returned GridContainer has the same number of axes with the original,
   * with the fixed axis having a single value. The two grids (original and shared)
   * share the same data and any modifications are reflected to both.
   * 
   * @tparam I
   *    the (zero based) index of the axis to fix
   * @param value
   *    the value to fix the axis to
   * @return
   *    A GridContainer representing the slice
   * @throws Elements::Exception 
   *    if the axis does not contain the given value
   * @throws Elements::Exception
   *    if the grid container is a slice and has this axis already fixed
   */
  template <int I>
  GridContainer<GridCellManager, AxesTypes...> fixAxisByValue(const axis_type<I>& value);
  
  /**
   * @brief
   * const version of the fixAxisByValue(const axis_type<I>&) method
   * @details
   * <b>Important note:</b> Because the returned GridContainer shares the same
   * underlying data with the original one, the returned object is a constant
   * grid (othewise it could be used for modifying the original object, which is
   * constant). This, with combination that the GridContainer does not have a
   * copy constructor (to avoid performance pitfalls), does not allow for creating
   * a new object from the returned rvalue. For example the following are wrong:
   * 
   * \code {.cpp}
   * const GridContainer grid1 = ...;
   * GridContainer grid2 = grid1.fixAxisByValue<0>(0); // WRONG - DO NOT DO THAT
   * const GridContainer grid3 = grid1.fixAxisByValue<0>(0); // WRONG - DO NOT DO THAT
   * auto grid3 = grid4.fixAxisByValue<0>(0); // WRONG - DO NOT DO THAT
   * \endcode
   * 
   * All the above will try to create a new GridContainer object by using the
   * deleted copy constructor, which will result to the compilation failing with
   * the related message.
   * 
   * The way to use the object returned by this method is to assign a constant
   * reference to it. This action will extend the life of the temporary rvalue
   * object to the lifetime of the reference. For example:
   * 
   * \code {.cpp}
   * const GridContainer grid1 = ...;
   * const GridContainer& grid2 = grid1.fixAxisByValue<0>(0); // CORRECT
   * auto& grid3 = grid1.fixAxisByValue<0>(0); // CORRECT
   * \endcode
   */
  template <int I>
  const GridContainer<GridCellManager, AxesTypes...> fixAxisByValue(const axis_type<I>& value) const;

private:

  /// A tuple containing the axes of the grid
  std::tuple<GridAxis<AxesTypes>...> m_axes;
  /// A helper class used for calculations of the axes indices
  GridIndexHelper<AxesTypes...> m_index_helper {m_axes};
  /// a tuple containing the original axes of the full grid, if this grid is a slice
  std::tuple<GridAxis<AxesTypes>...> m_axes_fixed {m_axes};
  /// a helper class for calculations of the original axes indices
  GridIndexHelper<AxesTypes...> m_index_helper_fixed {m_axes_fixed};
  /// A map containing the axes which have been fixed, if this grid is a slice
  std::map<size_t, size_t> m_fixed_indices {};
  /// A pointer to the data of the grid
  std::shared_ptr<GridCellManager> m_cell_manager {
          GridCellManagerTraits<GridCellManager>::factory(
                  GridConstructionHelper<AxesTypes...>::getAxisIndexFactor(
                          m_axes, TemplateLoopCounter<sizeof...(AxesTypes)-1>{}))
  };
  
  /**
   * @brief Slice constructor
   * @details
   * This constructor creates a GridContainer which represents a slice of the
   * given one. It is private and it should be used only by the fixAxisByIndex
   * and fixAxisByValue methods.
   * @param other The original grid
   * @param axis The axis to fix (zero based)
   * @param index The index to fix the axis to (zero based)
   */
  GridContainer(const GridContainer<GridCellManager, AxesTypes...>& other, size_t axis, size_t index);
  
  /// Returns the original axis. This behaves the same like the getAxis() with
  /// exception the case that the grid is a slice. In that case, it will return
  /// the original axes and not the single value fixed ones.
  template<int I>
  const GridAxis<axis_type<I>>& getOriginalAxis() const;

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

  /// Returns a reference to the cell value (const version)
  typename std::add_const<CellType>::type& operator*() const;

  /// Returns a pointer to the cell value
  CellType* operator->();

  /// Returns a pointer to the cell value (const version)
  typename std::add_const<CellType>::type* operator->() const;

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
   * @throws Elements::Exception
   *    if the given index is out of the bounds of the axis
   * @throws Elements::Exception
   *    if the axis has already been fixed for this iterator
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
   * @throws Elements::Exception
   *    if the axis does not contain the given value
   * @throws Elements::Exception
   *    if the axis has already been fixed for this iterator
   */
  template<int I>
  iter& fixAxisByValue(const axis_type<I>& value);
  
  /**
   * Fixes all the axes of this iterator to the values of the axes of the given
   * iterator. The given iterator is assumed to be an iterator of a grid with
   * the same number of axes, with the same names. It is the responsibility of
   * the caller to guarantee that.
   * @tparam OtherIter The type of the other iterator
   * @param other The iterator to get the axes values from
   * @return the iterator with all its axes fixed
   */
  template<typename OtherIter>
  iter& fixAllAxes(const OtherIter& other);
  
private:

  const GridContainer<GridCellManager, AxesTypes...>& m_owner;
  cell_manager_iter_type m_data_iter;
  std::map<size_t, size_t> m_fixed_indices;
  void forwardToIndex(size_t axis, size_t fixed_index);

}; // end of class iter

} // end of namespace GridContainer
} // end of namespace Euclid

#include "GridContainer/_impl/GridContainer.icpp"
#include "GridContainer/_impl/GridIterator.icpp"

#endif	/* GRIDCONTAINER_GRIDCONTAINER_H */

