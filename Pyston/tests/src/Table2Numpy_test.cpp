/*
 * Copyright (C) 2022 Euclid Science Ground Segment
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

#include "Pyston/Table2Numpy.h"
#include <boost/python/def.hpp>
#include <boost/python/exec.hpp>
#include <boost/python/import.hpp>
#include <boost/python/numpy.hpp>
#include <boost/test/unit_test.hpp>
#include <boost/test/unit_test_monitor.hpp>

using namespace Pyston;
using namespace Euclid::Table;
namespace py = boost::python;
namespace np = boost::python::numpy;

struct TablePyFixture {
  struct SinglePython {
    SinglePython() {
      Py_Initialize();
      np::initialize();
    }
  };

  static py::object getTable() {
    auto             column_info = std::make_shared<ColumnInfo>(std::vector<ColumnDescription>{
        {"ID", typeid(int32_t)}, {"STR", typeid(std::string)}, {"VF", typeid(std::vector<float>)}});
    std::vector<Row> rows;
    for (int32_t i = 0; i < 10; ++i) {
      auto f = static_cast<float>(i);
      rows.emplace_back(Row({i, std::to_string(i), std::vector<float>{f, f * 2, std::sqrt(f)}}, column_info));
    }
    Table table(std::move(rows));
    return table2numpy(table);
  }

  TablePyFixture() {
    static SinglePython single_python;
    gil_state                   = PyGILState_Ensure();
    auto main_module            = py::import("__main__");
    main_namespace              = main_module.attr("__dict__");
    main_namespace["np"]        = py::import("numpy");
    main_namespace["get_table"] = py::make_function(&getTable);
  }

  ~TablePyFixture() {
    PyGILState_Release(gil_state);
  }

  boost::python::object main_namespace;
  PyGILState_STATE      gil_state;
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(TablePy_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(TableToNumpy_test, TablePyFixture) {
  py::exec(R"PYCODE(
table = get_table()
assert table is not None

# Structure
assert len(table) == 10
assert len(table.dtype) == 3
assert table.dtype.names == ('ID', 'STR', 'VF'), table.dtype.names
assert table['ID'].dtype == np.int32, table['ID'].dtype
assert table['STR'].dtype == np.dtype('|S2'), table['STR'].dtype
assert table['VF'].dtype == np.float32, table['VF'].dtype
assert table['VF'].shape == (10, 3), table['VF'].shape

# Content
for i in range(10):
  assert table[i]['ID'] == i, table[i]
  assert table[i]['STR'] == str(i).encode('ascii'), table[i]
  np.testing.assert_allclose(table[i]['VF'], [i, i*2, np.sqrt(i)])
)PYCODE",
           main_namespace);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
