/*
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
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

#include "AlexandriaKernel/memory_tools.h"
#include "GridContainer/GridCellManagerVectorOfVectors.h"
#include "GridContainer/GridContainer.h"
#include <boost/test/unit_test.hpp>
#include <numeric>

using Euclid::GridContainer::GridAxis;
using Euclid::GridContainer::GridCellManagerVectorOfVectors;
using Euclid::GridContainer::GridContainer;

struct GridContainerNoDefaultConstructibleFixture {
  typedef GridContainer<GridCellManagerVectorOfVectors<double>, int, int, int, int> GridContainerType;
  typedef GridAxis<int>                                                             IntAxis;
  IntAxis                                                                           axis1{"Axis 1", {1, 2, 3, 4, 5}};
  IntAxis                                                                           axis2{"Axis 2", {1, 2, 3}};
  IntAxis                                                                           axis3{"Axis 3", {1, 2, 3, 4, 5, 6}};
  IntAxis                                                                           axis4{"Axis 4", {1, 2}};
  std::tuple<IntAxis, IntAxis, IntAxis, IntAxis> axes_tuple{axis1, axis2, axis3, axis4};
  const size_t                                   grid_size = axis1.size() * axis2.size() * axis3.size() * axis4.size();
  const int                                      cell_size = 8;
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(GridContainerNoDefaultConstructor_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Construction, GridContainerNoDefaultConstructibleFixture) {
  static_assert(!std::is_default_constructible<GridCellManagerVectorOfVectors<double>>::value,
                "Container must be no default constructible");
  GridContainerType result_grid(std::make_tuple(axis1, axis2, axis3, axis4), cell_size);
  BOOST_CHECK_EQUAL(result_grid.size(), grid_size);
  BOOST_CHECK_EQUAL(result_grid.getCellManager().getTotalSize(), grid_size * cell_size);

  std::vector<double> zeros(cell_size);
  for (auto cell : result_grid) {
    for (auto value : cell) {
      BOOST_CHECK_EQUAL(value, 0);
    }
  }
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Assign, GridContainerNoDefaultConstructibleFixture) {
  GridContainerType result_grid(std::make_tuple(axis1, axis2, axis3, axis4), cell_size);
  double            cell_acc = 0;
  for (auto cell : result_grid) {
    double acc = 0.;
    for (auto& value : cell) {
      value = cell_acc * 100 + acc;
      acc += 1.;
    }
    cell_acc += 1.;
  }

  // First cell
  std::vector<double> cell0(cell_size);
  std::iota(cell0.begin(), cell0.end(), 0.);
  std::vector<double> v = result_grid(0, 0, 0, 0);
  BOOST_CHECK_EQUAL_COLLECTIONS(v.begin(), v.end(), cell0.begin(), cell0.end());

  // 52th cell
  // 0 * 6 * 3 * 5 + 3 * 3 * 5 + 1 * 5 + 2 = 52
  std::vector<double> cell52(cell_size);
  std::iota(cell52.begin(), cell52.end(), 52. * 100.);
  v = result_grid(2, 1, 3, 0);
  BOOST_CHECK_EQUAL_COLLECTIONS(v.begin(), v.end(), cell52.begin(), cell52.end());

  // 179th cell
  // 1 * 6 * 3 * 5 + 5 * 3 * 5 + 2 * 5 + 4 = 179
  std::vector<double> cell179(cell_size);
  std::iota(cell179.begin(), cell179.end(), 179. * 100.);
  v = result_grid(4, 2, 5, 1);
  BOOST_CHECK_EQUAL_COLLECTIONS(v.begin(), v.end(), cell179.begin(), cell179.end());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
