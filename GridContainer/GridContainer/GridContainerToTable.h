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

#ifndef GRIDCONTAINER_GRIDCONTAINERTOTABLE_H
#define GRIDCONTAINER_GRIDCONTAINERTOTABLE_H

#include <vector>
#include "GridContainer/GridContainer.h"
#include "Table/Table.h"
#include "XYDataset/QualifiedName.h"

namespace Euclid {
namespace GridContainer {

/**
 * Trait used to map internal C++ types to types known by Alexandria's Table implementation.
 * This is the generic case: identity mapping
 * @tparam T
 *  Type to be mapped
 */
template<typename T>
struct GridAxisToTable {
  typedef T table_cell_t;

  static T serialize(T v) {
    return v;
  }
};

/**
 * Specialization for mapping a qualified name into a string
 */
template<>
struct GridAxisToTable<Euclid::XYDataset::QualifiedName> {
  typedef std::string table_cell_t;

  static table_cell_t serialize(const Euclid::XYDataset::QualifiedName& qn) {
    return qn.qualifiedName();
  }
};

/**
 * Trait used to map the grid cell type into an Alexandria's table set of cells.
 * @tparam T
 *  Type to be mapped
 */
template<typename T, typename Enable=void>
struct GridCellToTable {
  static_assert(!std::is_same<T, T>::value, "Specialization of GridCellToTable required");

  /**
   * Get the column descriptions of the values of the cell. The element passed will be one
   * reference cell from the grid (i.e. the first one)
   * @param c
   *    A cell instance
   * @param columns
   *    The column description(s) for the cell type. New columns must be *appended*
   */
  static void addColumnDescriptions(const T& c, std::vector<Table::ColumnDescription>& columns);

  /**
   * Add the cell values into the row
   * @param c
   *    A cell instance to be serialized
   * @param row
   *    Destination row. New cells must be *appended* on the same order as the column descriptions.
   */
  static void addCells(const T& c, std::vector<Table::Row::cell_type>& row);
};

/**
 * Specialization for scalar types
 */
template<typename T>
struct GridCellToTable<T, typename std::enable_if<std::is_arithmetic<T>::value>::type> {

  static void addColumnDescriptions(const T&, std::vector<Table::ColumnDescription>& columns) {
    columns.emplace_back("value", typeid(T));
  }

  static void addCells(const T& c, std::vector<Table::Row::cell_type>& row) {
    row.emplace_back(c);
  }
};

/**
 * Transform a GridContainer into a Table, with an entry for each
 * cell. The content will be unfolded, so the knot values will be repeated.
 */
template<typename GridCellManager, typename ...AxesTypes>
Table::Table gridContainerToTable(const GridContainer<GridCellManager, AxesTypes...>& grid);

} // end of namespace GridContainer
} // end of namespace Euclid

#include "GridContainer/_impl/GridContainerToTable.icpp"

#endif // GRIDCONTAINER_GRIDCONTAINERTOTABLE_H
