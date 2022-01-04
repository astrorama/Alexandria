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
#include "GridContainer/GridContainer.h"
#include <boost/test/unit_test.hpp>
#include <numeric>

/**
 * No default constructible container.
 * It allocates as a single vector a grid of arrays of doubles.
 */
struct Container {
  /**
   * Iterator that strides over the underlying vector, so +1 actually steps n positions
   */
  struct StrideIterator {
    StrideIterator(std::vector<double>::iterator start, int stride) : m_i(start), m_stride(stride) {}

    bool operator!=(const StrideIterator& other) const {
      return m_i != other.m_i;
    }

    bool operator>(const StrideIterator& other) const {
      return m_i > other.m_i;
    }

    StrideIterator& operator++() {
      m_i += m_stride;
      return *this;
    }

    StrideIterator& operator+=(int diff) {
      m_i += diff;
      return *this;
    }

    ptrdiff_t operator-(const StrideIterator& other) const {
      return (m_i - other.m_i) / m_stride;
    }

    double& operator*() {
      return *m_i;
    }

  private:
    std::vector<double>::iterator m_i;
    int                           m_stride;
  };

  Container(size_t size, int nested_values) : m_values(size * nested_values), m_cell_size(nested_values) {}
  ~Container() = default;

  Container(const Container&) = delete;

  double& operator[](int i) {
    return m_values[i * m_cell_size];
  }

  std::vector<double> m_values;
  int                 m_cell_size;
};

/**
 * GridCellManagerTraits specialization
 */
namespace Euclid {
namespace GridContainer {
template <>
struct GridCellManagerTraits<Container> {
  typedef double                    data_type;
  typedef double&                   reference_type;
  typedef double*                   pointer_type;
  typedef Container::StrideIterator iterator;

  static std::unique_ptr<Container> factory(size_t size, size_t nested_values) {
    return Euclid::make_unique<Container>(size, nested_values);
  }

  static iterator begin(Container& c) {
    return {c.m_values.begin(), c.m_cell_size};
  }

  static iterator end(Container& c) {
    return {c.m_values.end(), c.m_cell_size};
  }
};

}  // namespace GridContainer
}  // namespace Euclid

struct GridContainerNoDefaultConstructibleFixture {
  typedef Euclid::GridContainer::GridContainer<Container, int, int, int, int> GridContainerType;
  typedef Euclid::GridContainer::GridAxis<int>                                IntAxis;
  IntAxis                                                                     axis1{"Axis 1", {1, 2, 3, 4, 5}};
  IntAxis                                                                     axis2{"Axis 2", {1, 2, 3}};
  IntAxis                                                                     axis3{"Axis 3", {1, 2, 3, 4, 5, 6}};
  IntAxis                                                                     axis4{"Axis 4", {1, 2}};
  std::tuple<IntAxis, IntAxis, IntAxis, IntAxis>                              axes_tuple{axis1, axis2, axis3, axis4};
  const size_t total_size = axis1.size() * axis2.size() * axis3.size() * axis4.size();
  const int    cell_size  = 8;
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(GridContainerNoDefaultConstructor_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Construction, GridContainerNoDefaultConstructibleFixture) {
  static_assert(!std::is_default_constructible<Container>::value, "Container must be no default constructible");
  GridContainerType result_grid(std::make_tuple(axis1, axis2, axis3, axis4), cell_size);
  BOOST_CHECK_EQUAL(result_grid.size(), total_size);
  BOOST_CHECK_EQUAL(result_grid.getCellManager().m_values.size(), total_size * cell_size);

  std::vector<double> zeros(cell_size);
  for (auto& v : result_grid) {
    BOOST_CHECK_EQUAL_COLLECTIONS(&v, &v + cell_size, zeros.begin(), zeros.end());
  }
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Assign, GridContainerNoDefaultConstructibleFixture) {
  GridContainerType result_grid(std::make_tuple(axis1, axis2, axis3, axis4), cell_size);
  double            cell = 0;
  for (auto& v : result_grid) {
    double value = 0.;
    for (double* ptr = &v; ptr < &v + cell_size; ++ptr) {
      *ptr = cell * 100 + value;
      value += 1.;
    }
    cell += 1.;
  }

  // First cell
  std::vector<double> cell0(cell_size);
  std::iota(cell0.begin(), cell0.end(), 0.);
  double* v = &result_grid(0, 0, 0, 0);
  BOOST_CHECK_EQUAL_COLLECTIONS(v, v + cell_size, cell0.begin(), cell0.end());

  // 52th cell
  // 0 * 6 * 3 * 5 + 3 * 3 * 5 + 1 * 5 + 2 = 52
  std::vector<double> cell52(cell_size);
  std::iota(cell52.begin(), cell52.end(), 52. * 100.);
  v = &result_grid(2, 1, 3, 0);
  BOOST_CHECK_EQUAL_COLLECTIONS(v, v + cell_size, cell52.begin(), cell52.end());

  // 179th cell
  // 1 * 6 * 3 * 5 + 5 * 3 * 5 + 2 * 5 + 4 = 179
  std::vector<double> cell179(cell_size);
  std::iota(cell179.begin(), cell179.end(), 179. * 100.);
  v = &result_grid(4, 2, 5, 1);
  BOOST_CHECK_EQUAL_COLLECTIONS(v, v + cell_size, cell179.begin(), cell179.end());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()

//-----------------------------------------------------------------------------
