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

#include "GridContainer/GridContainerToTable.h"
#include <boost/test/unit_test.hpp>
#include <cmath>
#include <string>
#include <tuple>
#include <vector>

using namespace Euclid::GridContainer;

struct SimpleGridContainer_Fixture {
  typedef GridContainer<std::vector<double>, int, int, std::string, float> GridContainerType;
  typedef GridAxis<int>                                                    IntAxis;
  typedef GridAxis<std::string>                                            StrAxis;
  typedef GridAxis<float>                                                  FloatAxis;
  IntAxis                                                                  axis1{"Axis 1", {1, 2, 3, 4, 5}};
  IntAxis                                                                  axis2{"Axis 2", {1, 2, 3}};
  StrAxis                                                                  axis3{"Axis 3", {"a", "b", "c", "d", "e", "f"}};
  FloatAxis                                                                axis4{"Axis 4", {1, 2}};
  std::tuple<IntAxis, IntAxis, StrAxis, FloatAxis>                         axes_tuple{axis1, axis2, axis3, axis4};

  GridContainerType grid{axis1, axis2, axis3, axis4};

  double Fx(int ax1, int ax2, const std::string& ax3, float ax4) {
    return ax1 * 1000 + ax2 * 100 + (ax3[0] - 'a') * 10 + ax4;
  }

  SimpleGridContainer_Fixture() {
    for (size_t a1 = 0; a1 < axis1.size(); ++a1) {
      for (size_t a2 = 0; a2 < axis2.size(); ++a2) {
        for (size_t a3 = 0; a3 < axis3.size(); ++a3) {
          for (size_t a4 = 0; a4 < axis4.size(); ++a4) {
            grid.at(a1, a2, a3, a4) = Fx(axis1[a1], axis2[a2], axis3[a3], axis4[a4]);
          }
        }
      }
    }
  }
};

struct CellWithAttributes {
  double      flux, error;
  std::string description;
};

namespace Euclid {
namespace GridContainer {
template <>
struct GridCellToTable<CellWithAttributes> {
  static void addColumnDescriptions(const CellWithAttributes&, std::vector<Euclid::Table::ColumnDescription>& columns) {
    columns.emplace_back("MyFlux", typeid(double));
    columns.emplace_back("MyError", typeid(double));
    columns.emplace_back("MyDescription", typeid(std::string));
  }

  static void addCells(const CellWithAttributes& c, std::vector<Euclid::Table::Row::cell_type>& row) {
    row.emplace_back(c.flux);
    row.emplace_back(c.error);
    row.emplace_back(c.description);
  }
};
}  // namespace GridContainer
}  // namespace Euclid

struct ComposedGridContainer_Fixture {
  typedef GridContainer<std::vector<CellWithAttributes>, int, int, std::string, float> GridContainerType;
  typedef GridAxis<int>                                                                IntAxis;
  typedef GridAxis<std::string>                                                        StrAxis;
  typedef GridAxis<float>                                                              FloatAxis;
  IntAxis                                                                              axis1{"Axis 1", {1, 2, 3, 4, 5}};
  IntAxis                                                                              axis2{"Axis 2", {1, 2, 3}};
  StrAxis                                          axis3{"Axis 3", {"a", "b", "c", "d", "e", "f"}};
  FloatAxis                                        axis4{"Axis 4", {1, 2}};
  std::tuple<IntAxis, IntAxis, StrAxis, FloatAxis> axes_tuple{axis1, axis2, axis3, axis4};

  GridContainerType grid{axis1, axis2, axis3, axis4};

  double Fx(int ax1, int ax2, const std::string& ax3, float ax4) {
    return ax1 * 1000 + ax2 * 100 + (ax3[0] - 'a') * 10 + ax4;
  }

  ComposedGridContainer_Fixture() {
    for (size_t a1 = 0; a1 < axis1.size(); ++a1) {
      for (size_t a2 = 0; a2 < axis2.size(); ++a2) {
        for (size_t a3 = 0; a3 < axis3.size(); ++a3) {
          for (size_t a4 = 0; a4 < axis4.size(); ++a4) {
            CellWithAttributes c;
            c.flux                  = Fx(axis1[a1], axis2[a2], axis3[a3], axis4[a4]);
            c.error                 = std::sqrt(c.flux);
            c.description           = std::string(a4 + 1, 'x');
            grid.at(a1, a2, a3, a4) = c;
          }
        }
      }
    }
  }
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(GridToTable_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(SimpleToTable, SimpleGridContainer_Fixture) {
  auto table = gridContainerToTable(grid);

  BOOST_CHECK_EQUAL(grid.size(), table.size());

  auto column_info = table.getColumnInfo();

  auto axis1_col = column_info->getDescription("Axis_1");
  BOOST_CHECK(std::type_index(typeid(int)) == axis1_col.type);

  auto axis2_col = column_info->getDescription("Axis_2");
  BOOST_CHECK(std::type_index(typeid(int)) == axis2_col.type);

  auto axis3_col = column_info->getDescription("Axis_3");
  BOOST_CHECK(std::type_index(typeid(std::string)) == axis3_col.type);

  auto axis4_col = column_info->getDescription("Axis_4");
  BOOST_CHECK(std::type_index(typeid(float)) == axis4_col.type);

  auto cell_col = column_info->getDescription("value");
  BOOST_CHECK(std::type_index(typeid(double)) == cell_col.type);

  // The order is not so important as to keep the proper values together!
  for (auto& row : table) {
    auto   ax1 = boost::get<int>(row["Axis_1"]);
    auto   ax2 = boost::get<int>(row["Axis_2"]);
    auto   ax3 = boost::get<std::string>(row["Axis_3"]);
    auto   ax4 = boost::get<float>(row["Axis_4"]);
    double v   = Fx(ax1, ax2, ax3, ax4);
    BOOST_CHECK_CLOSE(boost::get<double>(row["value"]), v, 1e-7);
  }
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ComposedToTable, ComposedGridContainer_Fixture) {
  auto table = gridContainerToTable(grid);

  BOOST_CHECK_EQUAL(grid.size(), table.size());

  auto column_info = table.getColumnInfo();

  auto axis1_col = column_info->getDescription("Axis_1");
  BOOST_CHECK(std::type_index(typeid(int)) == axis1_col.type);

  auto axis2_col = column_info->getDescription("Axis_2");
  BOOST_CHECK(std::type_index(typeid(int)) == axis2_col.type);

  auto axis3_col = column_info->getDescription("Axis_3");
  BOOST_CHECK(std::type_index(typeid(std::string)) == axis3_col.type);

  auto axis4_col = column_info->getDescription("Axis_4");
  BOOST_CHECK(std::type_index(typeid(float)) == axis4_col.type);

  auto flux_col = column_info->getDescription("MyFlux");
  BOOST_CHECK(std::type_index(typeid(double)) == flux_col.type);

  auto fluxerr_col = column_info->getDescription("MyError");
  BOOST_CHECK(std::type_index(typeid(double)) == fluxerr_col.type);

  auto descr_col = column_info->getDescription("MyDescription");
  BOOST_CHECK(std::type_index(typeid(std::string)) == descr_col.type);

  // The order is not so important as to keep the proper values together!
  for (auto& row : table) {
    auto   ax1 = boost::get<int>(row["Axis_1"]);
    auto   ax2 = boost::get<int>(row["Axis_2"]);
    auto   ax3 = boost::get<std::string>(row["Axis_3"]);
    auto   ax4 = boost::get<float>(row["Axis_4"]);
    double v   = Fx(ax1, ax2, ax3, ax4);
    BOOST_CHECK_CLOSE(boost::get<double>(row["MyFlux"]), v, 1e-7);
    BOOST_CHECK_CLOSE(boost::get<double>(row["MyError"]), std::sqrt(v), 1e-7);
  }
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
