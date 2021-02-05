/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
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

/**
 * @file GridContainer_test.cpp
 * @date July 4, 2014
 * @author Nikolaos Apostolakos
 */

#include "GridContainer/GridContainer.h"
#include <ElementsKernel/Real.h>
#include <boost/test/test_tools.hpp>
#include <boost/test/unit_test.hpp>
#include <vector>

using Elements::isEqual;

struct GridContainer_Fixture {
  typedef Euclid::GridContainer::GridContainer<std::vector<double>, int, int, int, int> GridContainerType;
  typedef Euclid::GridContainer::GridAxis<int>                                          IntAxis;
  IntAxis                                                                               axis1{"Axis 1", {1, 2, 3, 4, 5}};
  IntAxis                                                                               axis2{"Axis 2", {1, 2, 3}};
  IntAxis                                                                               axis3{"Axis 3", {1, 2, 3, 4, 5, 6}};
  IntAxis                                                                               axis4{"Axis 4", {1, 2}};
  std::tuple<IntAxis, IntAxis, IntAxis, IntAxis>                                        axes_tuple{axis1, axis2, axis3, axis4};
  size_t total_size = axis1.size() * axis2.size() * axis3.size() * axis4.size();
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(GridContainer_test)

//-----------------------------------------------------------------------------
// Test construction with GridAxis objects
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(GridAxisConstructor, GridContainer_Fixture) {

  // When
  GridContainerType result_grid{axis1, axis2, axis3, axis4};
  auto&             result_axes_tuple = result_grid.getAxesTuple();

  // Then
  BOOST_CHECK_EQUAL(result_grid.size(), total_size);
  for (auto& value : result_grid) {
    BOOST_CHECK_EQUAL(value, 0.);
  }
  BOOST_CHECK_EQUAL(std::get<0>(result_axes_tuple).name(), axis1.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(std::get<0>(result_axes_tuple).begin(), std::get<0>(result_axes_tuple).end(), axis1.begin(),
                                axis1.end());
  BOOST_CHECK_EQUAL(std::get<1>(result_axes_tuple).name(), axis2.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(std::get<1>(result_axes_tuple).begin(), std::get<1>(result_axes_tuple).end(), axis2.begin(),
                                axis2.end());
  BOOST_CHECK_EQUAL(std::get<2>(result_axes_tuple).name(), axis3.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(std::get<2>(result_axes_tuple).begin(), std::get<2>(result_axes_tuple).end(), axis3.begin(),
                                axis3.end());
  BOOST_CHECK_EQUAL(std::get<3>(result_axes_tuple).name(), axis4.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(std::get<3>(result_axes_tuple).begin(), std::get<3>(result_axes_tuple).end(), axis4.begin(),
                                axis4.end());
}

//-----------------------------------------------------------------------------
// Test construction with GridAxis tuple
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(GridAxisTupleonstructor, GridContainer_Fixture) {

  // When
  GridContainerType result_grid{axes_tuple};
  auto&             result_axes_tuple = result_grid.getAxesTuple();

  // Then
  BOOST_CHECK_EQUAL(result_grid.size(), total_size);
  for (auto& value : result_grid) {
    BOOST_CHECK_EQUAL(value, 0.);
  }
  BOOST_CHECK_EQUAL(std::get<0>(result_axes_tuple).name(), axis1.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(std::get<0>(result_axes_tuple).begin(), std::get<0>(result_axes_tuple).end(), axis1.begin(),
                                axis1.end());
  BOOST_CHECK_EQUAL(std::get<1>(result_axes_tuple).name(), axis2.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(std::get<1>(result_axes_tuple).begin(), std::get<1>(result_axes_tuple).end(), axis2.begin(),
                                axis2.end());
  BOOST_CHECK_EQUAL(std::get<2>(result_axes_tuple).name(), axis3.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(std::get<2>(result_axes_tuple).begin(), std::get<2>(result_axes_tuple).end(), axis3.begin(),
                                axis3.end());
  BOOST_CHECK_EQUAL(std::get<3>(result_axes_tuple).name(), axis4.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(std::get<3>(result_axes_tuple).begin(), std::get<3>(result_axes_tuple).end(), axis4.begin(),
                                axis4.end());
}

//-----------------------------------------------------------------------------
// Test the rank method
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(rank, GridContainer_Fixture) {

  // When
  GridContainerType grid{axes_tuple};

  // Then
  BOOST_CHECK_EQUAL(grid.axisNumber(), 4u);
}

//-----------------------------------------------------------------------------
// Test the getAxis method
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getAxis, GridContainer_Fixture) {

  // When
  GridContainerType grid{axes_tuple};

  // Then
  BOOST_CHECK_EQUAL(grid.getAxis<0>().name(), axis1.name());
  BOOST_CHECK_EQUAL(grid.getAxis<1>().name(), axis2.name());
  BOOST_CHECK_EQUAL(grid.getAxis<2>().name(), axis3.name());
  BOOST_CHECK_EQUAL(grid.getAxis<3>().name(), axis4.name());
}

//-----------------------------------------------------------------------------
// Test the size method
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(size, GridContainer_Fixture) {

  // When
  GridContainerType grid{axes_tuple};

  // Then
  BOOST_CHECK_EQUAL(grid.size(), total_size);
}

//-----------------------------------------------------------------------------
// Test the parenthesis operator
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(parenthesisOperator, GridContainer_Fixture) {

  // Given
  GridContainerType        grid{axes_tuple};
  const GridContainerType& const_grid = grid;

  // When
  double custom_value = 0;
  for (auto& cell : grid) {
    custom_value += 0.1;
    cell = custom_value;
  }

  // Then
  double expected_value{0};
  for (size_t coord4 = 0; coord4 < axis4.size(); ++coord4) {
    for (size_t coord3 = 0; coord3 < axis3.size(); ++coord3) {
      for (size_t coord2 = 0; coord2 < axis2.size(); ++coord2) {
        for (size_t coord1 = 0; coord1 < axis1.size(); ++coord1) {
          expected_value += 0.1;
          BOOST_CHECK_CLOSE(grid(coord1, coord2, coord3, coord4), expected_value, 1e-6);
          BOOST_CHECK_CLOSE(const_grid(coord1, coord2, coord3, coord4), expected_value, 1e-6);
        }
      }
    }
  }
}

//-----------------------------------------------------------------------------
// Test the at method
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(at, GridContainer_Fixture) {

  // Given
  GridContainerType        grid{axes_tuple};
  const GridContainerType& const_grid = grid;

  // When
  double custom_value = 0;
  for (auto& cell : grid) {
    custom_value += 0.1;
    cell = custom_value;
  }

  // Then
  double expected_value{0};
  for (size_t coord4 = 0; coord4 < axis4.size(); ++coord4) {
    for (size_t coord3 = 0; coord3 < axis3.size(); ++coord3) {
      for (size_t coord2 = 0; coord2 < axis2.size(); ++coord2) {
        for (size_t coord1 = 0; coord1 < axis1.size(); ++coord1) {
          expected_value += 0.1;
          BOOST_CHECK_CLOSE(grid.at(coord1, coord2, coord3, coord4), expected_value, 1e-6);
          BOOST_CHECK_CLOSE(const_grid.at(coord1, coord2, coord3, coord4), expected_value, 1e-6);
        }
      }
    }
  }
}

//-----------------------------------------------------------------------------
// Test the at method throws for out of bound
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(atOutOfBound, GridContainer_Fixture) {

  // Given
  GridContainerType        grid{axes_tuple};
  const GridContainerType& const_grid = grid;

  // When
  double custom_value = 0;
  for (auto& cell : grid) {
    custom_value += 0.1;
    cell = custom_value;
  }

  // Then
  BOOST_CHECK_THROW(grid.at(axis1.size(), 0, 0, 0), Elements::Exception);
  BOOST_CHECK_THROW(grid.at(0, axis2.size(), 0, 0), Elements::Exception);
  BOOST_CHECK_THROW(grid.at(0, 0, axis3.size(), 0), Elements::Exception);
  BOOST_CHECK_THROW(grid.at(0, 0, 0, axis4.size()), Elements::Exception);
  BOOST_CHECK_THROW(const_grid.at(axis1.size(), 0, 0, 0), Elements::Exception);
  BOOST_CHECK_THROW(const_grid.at(0, axis2.size(), 0, 0), Elements::Exception);
  BOOST_CHECK_THROW(const_grid.at(0, 0, axis3.size(), 0), Elements::Exception);
  BOOST_CHECK_THROW(const_grid.at(0, 0, 0, axis4.size()), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test the iterator
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(iterator, GridContainer_Fixture) {

  // Given
  GridContainerType        grid{axes_tuple};
  const GridContainerType& const_grid = grid;

  // When
  double custom_value = 0;
  for (auto& cell : grid) {
    custom_value += 0.1;
    cell = custom_value;
  }

  // Then
  double expected_value{0};
  for (auto& result_value : grid) {
    expected_value += 0.1;
    BOOST_CHECK_CLOSE(result_value, expected_value, 1e-6);
  }
  expected_value = 0;
  for (auto& result_value : const_grid) {
    expected_value += 0.1;
    BOOST_CHECK_CLOSE(result_value, expected_value, 1e-6);
  }
}

//-----------------------------------------------------------------------------
// Test the iterators axisIndex
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(iteratorAxisIndex, GridContainer_Fixture) {

  // Given
  GridContainerType        grid{axes_tuple};
  const GridContainerType& const_grid = grid;

  // When
  auto iterator       = grid.begin();
  auto const_iterator = const_grid.begin();

  // Then
  for (size_t coord4 = 0; coord4 < axis4.size(); ++coord4) {
    for (size_t coord3 = 0; coord3 < axis3.size(); ++coord3) {
      for (size_t coord2 = 0; coord2 < axis2.size(); ++coord2) {
        for (size_t coord1 = 0; coord1 < axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(iterator.axisIndex<0>(), coord1);
          BOOST_CHECK_EQUAL(iterator.axisIndex<1>(), coord2);
          BOOST_CHECK_EQUAL(iterator.axisIndex<2>(), coord3);
          BOOST_CHECK_EQUAL(iterator.axisIndex<3>(), coord4);
          ++iterator;
        }
      }
    }
  }
  for (size_t coord4 = 0; coord4 < axis4.size(); ++coord4) {
    for (size_t coord3 = 0; coord3 < axis3.size(); ++coord3) {
      for (size_t coord2 = 0; coord2 < axis2.size(); ++coord2) {
        for (size_t coord1 = 0; coord1 < axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<0>(), coord1);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<1>(), coord2);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<2>(), coord3);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<3>(), coord4);
          ++const_iterator;
        }
      }
    }
  }
}

//-----------------------------------------------------------------------------
// Test the iterators axisValue
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(iteratorAxisValue, GridContainer_Fixture) {

  // Given
  GridContainerType        grid{axes_tuple};
  const GridContainerType& const_grid = grid;

  // When
  auto iterator       = grid.begin();
  auto const_iterator = const_grid.begin();

  // Then
  for (size_t coord4 = 0; coord4 < axis4.size(); ++coord4) {
    for (size_t coord3 = 0; coord3 < axis3.size(); ++coord3) {
      for (size_t coord2 = 0; coord2 < axis2.size(); ++coord2) {
        for (size_t coord1 = 0; coord1 < axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(iterator.axisValue<0>(), axis1[coord1]);
          BOOST_CHECK_EQUAL(iterator.axisValue<1>(), axis2[coord2]);
          BOOST_CHECK_EQUAL(iterator.axisValue<2>(), axis3[coord3]);
          BOOST_CHECK_EQUAL(iterator.axisValue<3>(), axis4[coord4]);
          ++iterator;
        }
      }
    }
  }
  for (size_t coord4 = 0; coord4 < axis4.size(); ++coord4) {
    for (size_t coord3 = 0; coord3 < axis3.size(); ++coord3) {
      for (size_t coord2 = 0; coord2 < axis2.size(); ++coord2) {
        for (size_t coord1 = 0; coord1 < axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(const_iterator.axisValue<0>(), axis1[coord1]);
          BOOST_CHECK_EQUAL(const_iterator.axisValue<1>(), axis2[coord2]);
          BOOST_CHECK_EQUAL(const_iterator.axisValue<2>(), axis3[coord3]);
          BOOST_CHECK_EQUAL(const_iterator.axisValue<3>(), axis4[coord4]);
          ++const_iterator;
        }
      }
    }
  }
}

//-----------------------------------------------------------------------------
// Test fixing iterator by index
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(fixIteratorByIndex, GridContainer_Fixture) {

  // Given
  GridContainerType        grid{axes_tuple};
  const GridContainerType& const_grid = grid;

  for (size_t fixed_index = 0; fixed_index < axis1.size(); ++fixed_index) {

    // When
    auto iterator = grid.begin();
    iterator.fixAxisByIndex<0>(fixed_index);
    auto const_iterator = const_grid.begin();
    const_iterator.fixAxisByIndex<0>(fixed_index);

    // Then
    for (size_t coord4 = 0; coord4 < axis4.size(); ++coord4) {
      for (size_t coord3 = 0; coord3 < axis3.size(); ++coord3) {
        for (size_t coord2 = 0; coord2 < axis2.size(); ++coord2) {
          BOOST_CHECK_EQUAL(iterator.axisIndex<0>(), fixed_index);
          BOOST_CHECK_EQUAL(iterator.axisIndex<1>(), coord2);
          BOOST_CHECK_EQUAL(iterator.axisIndex<2>(), coord3);
          BOOST_CHECK_EQUAL(iterator.axisIndex<3>(), coord4);
          ++iterator;
        }
      }
    }
    for (size_t coord4 = 0; coord4 < axis4.size(); ++coord4) {
      for (size_t coord3 = 0; coord3 < axis3.size(); ++coord3) {
        for (size_t coord2 = 0; coord2 < axis2.size(); ++coord2) {
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<0>(), fixed_index);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<1>(), coord2);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<2>(), coord3);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<3>(), coord4);
          ++const_iterator;
        }
      }
    }
  }

  for (size_t fixed_index = 0; fixed_index < axis2.size(); ++fixed_index) {

    // When
    auto iterator = grid.begin();
    iterator.fixAxisByIndex<1>(fixed_index);
    auto const_iterator = const_grid.begin();
    const_iterator.fixAxisByIndex<1>(fixed_index);

    // Then
    for (size_t coord4 = 0; coord4 < axis4.size(); ++coord4) {
      for (size_t coord3 = 0; coord3 < axis3.size(); ++coord3) {
        for (size_t coord1 = 0; coord1 < axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(iterator.axisIndex<0>(), coord1);
          BOOST_CHECK_EQUAL(iterator.axisIndex<1>(), fixed_index);
          BOOST_CHECK_EQUAL(iterator.axisIndex<2>(), coord3);
          BOOST_CHECK_EQUAL(iterator.axisIndex<3>(), coord4);
          ++iterator;
        }
      }
    }
    for (size_t coord4 = 0; coord4 < axis4.size(); ++coord4) {
      for (size_t coord3 = 0; coord3 < axis3.size(); ++coord3) {
        for (size_t coord1 = 0; coord1 < axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<0>(), coord1);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<1>(), fixed_index);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<2>(), coord3);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<3>(), coord4);
          ++const_iterator;
        }
      }
    }
  }

  for (size_t fixed_index = 0; fixed_index < axis3.size(); ++fixed_index) {

    // When
    auto iterator = grid.begin();
    iterator.fixAxisByIndex<2>(fixed_index);
    auto const_iterator = const_grid.begin();
    const_iterator.fixAxisByIndex<2>(fixed_index);

    // Then
    for (size_t coord4 = 0; coord4 < axis4.size(); ++coord4) {
      for (size_t coord2 = 0; coord2 < axis2.size(); ++coord2) {
        for (size_t coord1 = 0; coord1 < axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(iterator.axisIndex<0>(), coord1);
          BOOST_CHECK_EQUAL(iterator.axisIndex<1>(), coord2);
          BOOST_CHECK_EQUAL(iterator.axisIndex<2>(), fixed_index);
          BOOST_CHECK_EQUAL(iterator.axisIndex<3>(), coord4);
          ++iterator;
        }
      }
    }
    for (size_t coord4 = 0; coord4 < axis4.size(); ++coord4) {
      for (size_t coord2 = 0; coord2 < axis2.size(); ++coord2) {
        for (size_t coord1 = 0; coord1 < axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<0>(), coord1);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<1>(), coord2);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<2>(), fixed_index);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<3>(), coord4);
          ++const_iterator;
        }
      }
    }
  }

  for (size_t fixed_index = 0; fixed_index < axis4.size(); ++fixed_index) {

    // When
    auto iterator = grid.begin();
    iterator.fixAxisByIndex<3>(fixed_index);
    auto const_iterator = const_grid.begin();
    const_iterator.fixAxisByIndex<3>(fixed_index);

    // Then
    for (size_t coord3 = 0; coord3 < axis3.size(); ++coord3) {
      for (size_t coord2 = 0; coord2 < axis2.size(); ++coord2) {
        for (size_t coord1 = 0; coord1 < axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(iterator.axisIndex<0>(), coord1);
          BOOST_CHECK_EQUAL(iterator.axisIndex<1>(), coord2);
          BOOST_CHECK_EQUAL(iterator.axisIndex<2>(), coord3);
          BOOST_CHECK_EQUAL(iterator.axisIndex<3>(), fixed_index);
          ++iterator;
        }
      }
    }
    for (size_t coord3 = 0; coord3 < axis3.size(); ++coord3) {
      for (size_t coord2 = 0; coord2 < axis2.size(); ++coord2) {
        for (size_t coord1 = 0; coord1 < axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<0>(), coord1);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<1>(), coord2);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<2>(), coord3);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<3>(), fixed_index);
          ++const_iterator;
        }
      }
    }
  }
}

//-----------------------------------------------------------------------------
// Test fixing iterator index out of bound exception
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(fixIteratorByIndexOutOfBound, GridContainer_Fixture) {

  // Given
  GridContainerType        grid{axes_tuple};
  const GridContainerType& const_grid = grid;

  // When
  auto iterator       = grid.begin();
  auto const_iterator = const_grid.begin();

  // Then
  BOOST_CHECK_THROW(iterator.fixAxisByIndex<0>(axis1.size()), Elements::Exception);
  BOOST_CHECK_THROW(iterator.fixAxisByIndex<1>(axis2.size()), Elements::Exception);
  BOOST_CHECK_THROW(iterator.fixAxisByIndex<2>(axis3.size()), Elements::Exception);
  BOOST_CHECK_THROW(iterator.fixAxisByIndex<3>(axis4.size()), Elements::Exception);
  BOOST_CHECK_THROW(const_iterator.fixAxisByIndex<0>(axis1.size()), Elements::Exception);
  BOOST_CHECK_THROW(const_iterator.fixAxisByIndex<1>(axis2.size()), Elements::Exception);
  BOOST_CHECK_THROW(const_iterator.fixAxisByIndex<2>(axis3.size()), Elements::Exception);
  BOOST_CHECK_THROW(const_iterator.fixAxisByIndex<3>(axis4.size()), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test fixing iterator by index twice for same axis throws exception
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(fixIteratorByIndexTwiceForSameAxis, GridContainer_Fixture) {

  // Given
  GridContainerType        grid{axes_tuple};
  const GridContainerType& const_grid = grid;

  // When
  auto iterator       = grid.begin().fixAxisByIndex<0>(0).fixAxisByIndex<1>(0).fixAxisByIndex<2>(0).fixAxisByIndex<3>(0);
  auto const_iterator = const_grid.begin().fixAxisByIndex<0>(0).fixAxisByIndex<1>(0).fixAxisByIndex<2>(0).fixAxisByIndex<3>(0);

  // Then
  iterator.fixAxisByIndex<0>(0);
  iterator.fixAxisByIndex<1>(0);
  BOOST_CHECK_THROW(iterator.fixAxisByIndex<2>(1), Elements::Exception);
  BOOST_CHECK_THROW(iterator.fixAxisByIndex<3>(1), Elements::Exception);
  const_iterator.fixAxisByIndex<0>(0);
  const_iterator.fixAxisByIndex<1>(0);
  BOOST_CHECK_THROW(const_iterator.fixAxisByIndex<2>(1), Elements::Exception);
  BOOST_CHECK_THROW(const_iterator.fixAxisByIndex<3>(1), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test fixing iterator by value
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(fixIteratorByValue, GridContainer_Fixture) {

  // Given
  GridContainerType        grid{axes_tuple};
  const GridContainerType& const_grid = grid;

  for (size_t fixed_index = 0; fixed_index < axis1.size(); ++fixed_index) {

    // When
    auto iterator = grid.begin();
    iterator.fixAxisByValue<0>(axis1[fixed_index]);
    auto const_iterator = const_grid.begin();
    const_iterator.fixAxisByValue<0>(axis1[fixed_index]);

    // Then
    for (size_t coord4 = 0; coord4 < axis4.size(); ++coord4) {
      for (size_t coord3 = 0; coord3 < axis3.size(); ++coord3) {
        for (size_t coord2 = 0; coord2 < axis2.size(); ++coord2) {
          BOOST_CHECK_EQUAL(iterator.axisIndex<0>(), fixed_index);
          BOOST_CHECK_EQUAL(iterator.axisIndex<1>(), coord2);
          BOOST_CHECK_EQUAL(iterator.axisIndex<2>(), coord3);
          BOOST_CHECK_EQUAL(iterator.axisIndex<3>(), coord4);
          ++iterator;
        }
      }
    }
    for (size_t coord4 = 0; coord4 < axis4.size(); ++coord4) {
      for (size_t coord3 = 0; coord3 < axis3.size(); ++coord3) {
        for (size_t coord2 = 0; coord2 < axis2.size(); ++coord2) {
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<0>(), fixed_index);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<1>(), coord2);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<2>(), coord3);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<3>(), coord4);
          ++const_iterator;
        }
      }
    }
  }

  for (size_t fixed_index = 0; fixed_index < axis2.size(); ++fixed_index) {

    // When
    auto iterator = grid.begin();
    iterator.fixAxisByValue<1>(axis2[fixed_index]);
    auto const_iterator = const_grid.begin();
    const_iterator.fixAxisByValue<1>(axis2[fixed_index]);

    // Then
    for (size_t coord4 = 0; coord4 < axis4.size(); ++coord4) {
      for (size_t coord3 = 0; coord3 < axis3.size(); ++coord3) {
        for (size_t coord1 = 0; coord1 < axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(iterator.axisIndex<0>(), coord1);
          BOOST_CHECK_EQUAL(iterator.axisIndex<1>(), fixed_index);
          BOOST_CHECK_EQUAL(iterator.axisIndex<2>(), coord3);
          BOOST_CHECK_EQUAL(iterator.axisIndex<3>(), coord4);
          ++iterator;
        }
      }
    }
    for (size_t coord4 = 0; coord4 < axis4.size(); ++coord4) {
      for (size_t coord3 = 0; coord3 < axis3.size(); ++coord3) {
        for (size_t coord1 = 0; coord1 < axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<0>(), coord1);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<1>(), fixed_index);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<2>(), coord3);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<3>(), coord4);
          ++const_iterator;
        }
      }
    }
  }

  for (size_t fixed_index = 0; fixed_index < axis3.size(); ++fixed_index) {

    // When
    auto iterator = grid.begin();
    iterator.fixAxisByValue<2>(axis3[fixed_index]);
    auto const_iterator = const_grid.begin();
    const_iterator.fixAxisByValue<2>(axis3[fixed_index]);

    // Then
    for (size_t coord4 = 0; coord4 < axis4.size(); ++coord4) {
      for (size_t coord2 = 0; coord2 < axis2.size(); ++coord2) {
        for (size_t coord1 = 0; coord1 < axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(iterator.axisIndex<0>(), coord1);
          BOOST_CHECK_EQUAL(iterator.axisIndex<1>(), coord2);
          BOOST_CHECK_EQUAL(iterator.axisIndex<2>(), fixed_index);
          BOOST_CHECK_EQUAL(iterator.axisIndex<3>(), coord4);
          ++iterator;
        }
      }
    }
    for (size_t coord4 = 0; coord4 < axis4.size(); ++coord4) {
      for (size_t coord2 = 0; coord2 < axis2.size(); ++coord2) {
        for (size_t coord1 = 0; coord1 < axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<0>(), coord1);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<1>(), coord2);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<2>(), fixed_index);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<3>(), coord4);
          ++const_iterator;
        }
      }
    }
  }

  for (size_t fixed_index = 0; fixed_index < axis4.size(); ++fixed_index) {

    // When
    auto iterator = grid.begin();
    iterator.fixAxisByValue<3>(axis4[fixed_index]);
    auto const_iterator = const_grid.begin();
    const_iterator.fixAxisByValue<3>(axis4[fixed_index]);

    // Then
    for (size_t coord3 = 0; coord3 < axis3.size(); ++coord3) {
      for (size_t coord2 = 0; coord2 < axis2.size(); ++coord2) {
        for (size_t coord1 = 0; coord1 < axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(iterator.axisIndex<0>(), coord1);
          BOOST_CHECK_EQUAL(iterator.axisIndex<1>(), coord2);
          BOOST_CHECK_EQUAL(iterator.axisIndex<2>(), coord3);
          BOOST_CHECK_EQUAL(iterator.axisIndex<3>(), fixed_index);
          ++iterator;
        }
      }
    }
    for (size_t coord3 = 0; coord3 < axis3.size(); ++coord3) {
      for (size_t coord2 = 0; coord2 < axis2.size(); ++coord2) {
        for (size_t coord1 = 0; coord1 < axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<0>(), coord1);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<1>(), coord2);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<2>(), coord3);
          BOOST_CHECK_EQUAL(const_iterator.axisIndex<3>(), fixed_index);
          ++const_iterator;
        }
      }
    }
  }
}

//-----------------------------------------------------------------------------
// Test fixing iterator value not found exception
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(fixIteratorByValueNotFound, GridContainer_Fixture) {

  // Given
  GridContainerType        grid{axes_tuple};
  const GridContainerType& const_grid = grid;

  // When
  auto iterator       = grid.begin();
  auto const_iterator = const_grid.begin();

  // Then
  BOOST_CHECK_THROW(iterator.fixAxisByValue<0>(axis1.size() + 1), Elements::Exception);
  BOOST_CHECK_THROW(iterator.fixAxisByValue<1>(axis2.size() + 1), Elements::Exception);
  BOOST_CHECK_THROW(iterator.fixAxisByValue<2>(axis3.size() + 1), Elements::Exception);
  BOOST_CHECK_THROW(iterator.fixAxisByValue<3>(axis4.size() + 1), Elements::Exception);
  BOOST_CHECK_THROW(const_iterator.fixAxisByValue<0>(axis1.size() + 1), Elements::Exception);
  BOOST_CHECK_THROW(const_iterator.fixAxisByValue<1>(axis2.size() + 1), Elements::Exception);
  BOOST_CHECK_THROW(const_iterator.fixAxisByValue<2>(axis3.size() + 1), Elements::Exception);
  BOOST_CHECK_THROW(const_iterator.fixAxisByValue<3>(axis4.size() + 1), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test fixing iterator by value twice for same axis throws exception
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(fixIteratorByValueTwiceForSameAxis, GridContainer_Fixture) {

  // Given
  GridContainerType        grid{axes_tuple};
  const GridContainerType& const_grid = grid;

  // When
  auto iterator       = grid.begin().fixAxisByValue<0>(1).fixAxisByValue<1>(1).fixAxisByValue<2>(1).fixAxisByValue<3>(1);
  auto const_iterator = const_grid.begin().fixAxisByValue<0>(1).fixAxisByValue<1>(1).fixAxisByValue<2>(1).fixAxisByValue<3>(1);

  // Then
  iterator.fixAxisByValue<0>(1);
  iterator.fixAxisByValue<1>(1);
  BOOST_CHECK_THROW(iterator.fixAxisByValue<2>(2), Elements::Exception);
  BOOST_CHECK_THROW(iterator.fixAxisByValue<3>(2), Elements::Exception);
  const_iterator.fixAxisByValue<0>(1);
  const_iterator.fixAxisByValue<1>(1);
  BOOST_CHECK_THROW(const_iterator.fixAxisByValue<2>(2), Elements::Exception);
  BOOST_CHECK_THROW(const_iterator.fixAxisByValue<3>(2), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test fixing all exes of iterator by other iterator
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(fixIteratorAllAxes, GridContainer_Fixture) {

  // Given
  GridContainerType grid1{axes_tuple};
  auto              iter1 = grid1.begin();
  GridContainerType grid2{axes_tuple};
  auto              iter2 = grid2.begin();

  // When
  iter1.fixAxisByIndex<0>(3).fixAxisByIndex<1>(2).fixAxisByIndex<2>(1).fixAxisByIndex<3>(0);
  iter2.fixAllAxes(iter1);

  // Then
  BOOST_CHECK_EQUAL(iter2.axisIndex<0>(), 3u);
  BOOST_CHECK_EQUAL(iter2.axisIndex<1>(), 2u);
  BOOST_CHECK_EQUAL(iter2.axisIndex<2>(), 1u);
  BOOST_CHECK_EQUAL(iter2.axisIndex<3>(), 0u);
}

//-----------------------------------------------------------------------------
// Test slicing using index out of bound exception
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(sliceByIndexOutOfBound, GridContainer_Fixture) {

  // Given
  GridContainerType        grid{axes_tuple};
  const GridContainerType& const_grid = grid;

  // Then
  BOOST_CHECK_THROW(grid.fixAxisByIndex<0>(axis1.size()), Elements::Exception);
  BOOST_CHECK_THROW(grid.fixAxisByIndex<1>(axis2.size()), Elements::Exception);
  BOOST_CHECK_THROW(grid.fixAxisByIndex<2>(axis3.size()), Elements::Exception);
  BOOST_CHECK_THROW(grid.fixAxisByIndex<3>(axis4.size()), Elements::Exception);
  BOOST_CHECK_THROW(const_grid.fixAxisByIndex<0>(axis1.size()), Elements::Exception);
  BOOST_CHECK_THROW(const_grid.fixAxisByIndex<1>(axis2.size()), Elements::Exception);
  BOOST_CHECK_THROW(const_grid.fixAxisByIndex<2>(axis3.size()), Elements::Exception);
  BOOST_CHECK_THROW(const_grid.fixAxisByIndex<3>(axis4.size()), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test slicing using index twice at the same axis throws exception
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(sliceByIndexTwiceSameAxis, GridContainer_Fixture) {

  // Given
  GridContainerType        grid{axes_tuple};
  const GridContainerType& const_grid = grid;

  // When
  auto  slice0       = grid.fixAxisByIndex<0>(0);
  auto  slice1       = grid.fixAxisByIndex<1>(0);
  auto  slice2       = grid.fixAxisByIndex<2>(0);
  auto  slice3       = grid.fixAxisByIndex<3>(0);
  auto& const_slice0 = const_grid.fixAxisByIndex<0>(0);
  auto& const_slice1 = const_grid.fixAxisByIndex<1>(0);
  auto& const_slice2 = const_grid.fixAxisByIndex<2>(0);
  auto& const_slice3 = const_grid.fixAxisByIndex<3>(0);

  // Then
  BOOST_CHECK_THROW(slice0.fixAxisByIndex<0>(0), Elements::Exception);
  BOOST_CHECK_THROW(slice1.fixAxisByIndex<1>(0), Elements::Exception);
  BOOST_CHECK_THROW(slice2.fixAxisByIndex<2>(1), Elements::Exception);
  BOOST_CHECK_THROW(slice3.fixAxisByIndex<3>(1), Elements::Exception);
  BOOST_CHECK_THROW(const_slice0.fixAxisByIndex<0>(0), Elements::Exception);
  BOOST_CHECK_THROW(const_slice1.fixAxisByIndex<1>(0), Elements::Exception);
  BOOST_CHECK_THROW(const_slice2.fixAxisByIndex<2>(1), Elements::Exception);
  BOOST_CHECK_THROW(const_slice3.fixAxisByIndex<3>(1), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test slicing using value not found exception
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(sliceByValueNotFound, GridContainer_Fixture) {

  // Given
  GridContainerType        grid{axes_tuple};
  const GridContainerType& const_grid = grid;

  // Then
  BOOST_CHECK_THROW(grid.fixAxisByValue<0>(axis1.size() + 1), Elements::Exception);
  BOOST_CHECK_THROW(grid.fixAxisByValue<1>(axis2.size() + 1), Elements::Exception);
  BOOST_CHECK_THROW(grid.fixAxisByValue<2>(axis3.size() + 1), Elements::Exception);
  BOOST_CHECK_THROW(grid.fixAxisByValue<3>(axis4.size() + 1), Elements::Exception);
  BOOST_CHECK_THROW(const_grid.fixAxisByValue<0>(axis1.size() + 1), Elements::Exception);
  BOOST_CHECK_THROW(const_grid.fixAxisByValue<1>(axis2.size() + 1), Elements::Exception);
  BOOST_CHECK_THROW(const_grid.fixAxisByValue<2>(axis3.size() + 1), Elements::Exception);
  BOOST_CHECK_THROW(const_grid.fixAxisByValue<3>(axis4.size() + 1), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test slicing using value twice at the same axis throws exception
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(sliceByValueTwiceSameAxis, GridContainer_Fixture) {

  // Given
  GridContainerType        grid{axes_tuple};
  const GridContainerType& const_grid = grid;

  // When
  auto  slice0       = grid.fixAxisByValue<0>(1);
  auto  slice1       = grid.fixAxisByValue<1>(1);
  auto  slice2       = grid.fixAxisByValue<2>(1);
  auto  slice3       = grid.fixAxisByValue<3>(1);
  auto& const_slice0 = const_grid.fixAxisByValue<0>(1);
  auto& const_slice1 = const_grid.fixAxisByValue<1>(1);
  auto& const_slice2 = const_grid.fixAxisByValue<2>(1);
  auto& const_slice3 = const_grid.fixAxisByValue<3>(1);

  // Then
  BOOST_CHECK_THROW(slice0.fixAxisByValue<0>(1), Elements::Exception);
  BOOST_CHECK_THROW(slice1.fixAxisByValue<1>(1), Elements::Exception);
  BOOST_CHECK_THROW(slice2.fixAxisByValue<2>(2), Elements::Exception);
  BOOST_CHECK_THROW(slice3.fixAxisByValue<3>(2), Elements::Exception);
  BOOST_CHECK_THROW(const_slice0.fixAxisByValue<0>(1), Elements::Exception);
  BOOST_CHECK_THROW(const_slice1.fixAxisByValue<1>(1), Elements::Exception);
  BOOST_CHECK_THROW(const_slice2.fixAxisByValue<2>(2), Elements::Exception);
  BOOST_CHECK_THROW(const_slice3.fixAxisByValue<3>(2), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test that modifications to the slices are reflected to the original
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(sliceChancesReflected, GridContainer_Fixture) {

  // Given
  GridContainerType grid{axes_tuple};
  auto              slice_index = grid.fixAxisByIndex<0>(2).fixAxisByIndex<1>(2).fixAxisByIndex<2>(2).fixAxisByIndex<3>(1);
  auto              slice_value = grid.fixAxisByValue<0>(2).fixAxisByValue<1>(2).fixAxisByValue<2>(2).fixAxisByValue<3>(1);

  // When
  *slice_index.begin() = -10;
  *slice_value.begin() = -20;

  // Then
  BOOST_CHECK_EQUAL(grid(2, 2, 2, 1), -10);
  BOOST_CHECK_EQUAL(grid(1, 1, 1, 0), -20);
}

//-----------------------------------------------------------------------------
// Test that slices have correct axes and size
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(sliceAxes, GridContainer_Fixture) {

  // Given
  GridContainerType        grid{axes_tuple};
  const GridContainerType& const_grid          = grid;
  std::vector<int>         expected_fixed_axis = {2};

  // When
  auto  slice       = grid.fixAxisByIndex<1>(1);
  auto& const_slice = const_grid.fixAxisByIndex<1>(1);

  // Then
  BOOST_CHECK_EQUAL(slice.size(), grid.size() / axis2.size());
  BOOST_CHECK_EQUAL(slice.getAxis<0>().name(), axis1.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(slice.getAxis<0>().begin(), slice.getAxis<0>().end(), axis1.begin(), axis1.end());
  BOOST_CHECK_EQUAL(slice.getAxis<1>().name(), axis2.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(slice.getAxis<1>().begin(), slice.getAxis<1>().end(), expected_fixed_axis.begin(),
                                expected_fixed_axis.end());
  BOOST_CHECK_EQUAL(slice.getAxis<2>().name(), axis3.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(slice.getAxis<2>().begin(), slice.getAxis<2>().end(), axis3.begin(), axis3.end());
  BOOST_CHECK_EQUAL(slice.getAxis<3>().name(), axis4.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(slice.getAxis<3>().begin(), slice.getAxis<3>().end(), axis4.begin(), axis4.end());
  BOOST_CHECK_EQUAL(const_slice.size(), grid.size() / axis2.size());
  BOOST_CHECK_EQUAL(const_slice.getAxis<0>().name(), axis1.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(const_slice.getAxis<0>().begin(), const_slice.getAxis<0>().end(), axis1.begin(), axis1.end());
  BOOST_CHECK_EQUAL(const_slice.getAxis<1>().name(), axis2.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(const_slice.getAxis<1>().begin(), const_slice.getAxis<1>().end(), expected_fixed_axis.begin(),
                                expected_fixed_axis.end());
  BOOST_CHECK_EQUAL(const_slice.getAxis<2>().name(), axis3.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(const_slice.getAxis<2>().begin(), const_slice.getAxis<2>().end(), axis3.begin(), axis3.end());
  BOOST_CHECK_EQUAL(const_slice.getAxis<3>().name(), axis4.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(const_slice.getAxis<3>().begin(), const_slice.getAxis<3>().end(), axis4.begin(), axis4.end());
}

//-----------------------------------------------------------------------------
// Test that slices iterator works fine
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(sliceIterator, GridContainer_Fixture) {

  // Given
  GridContainerType        grid{axes_tuple};
  const GridContainerType& const_grid = grid;

  // When
  auto  slice            = grid.fixAxisByIndex<1>(1).fixAxisByIndex<3>(0);
  auto  slice_iter       = slice.begin();
  auto  grid_iter        = grid.begin().fixAxisByIndex<1>(1).fixAxisByIndex<3>(0);
  auto& const_slice      = const_grid.fixAxisByIndex<1>(1).fixAxisByIndex<3>(0);
  auto  const_slice_iter = const_slice.begin();
  auto  const_grid_iter  = const_grid.begin().fixAxisByIndex<1>(1).fixAxisByIndex<3>(0);

  // Then
  for (; slice_iter != slice.end(); ++slice_iter, ++grid_iter) {
    BOOST_CHECK_EQUAL(*slice_iter, *grid_iter);
    BOOST_CHECK_EQUAL(slice_iter.axisValue<0>(), grid_iter.axisValue<0>());
    BOOST_CHECK_EQUAL(slice_iter.axisValue<1>(), grid_iter.axisValue<1>());
    BOOST_CHECK_EQUAL(slice_iter.axisValue<2>(), grid_iter.axisValue<2>());
    BOOST_CHECK_EQUAL(slice_iter.axisValue<3>(), grid_iter.axisValue<3>());
  }
  BOOST_CHECK(grid_iter == grid.end());
  for (; const_slice_iter != const_slice.end(); ++const_slice_iter, ++const_grid_iter) {
    BOOST_CHECK_EQUAL(*const_slice_iter, *const_grid_iter);
    BOOST_CHECK_EQUAL(const_slice_iter.axisValue<0>(), const_grid_iter.axisValue<0>());
    BOOST_CHECK_EQUAL(const_slice_iter.axisValue<1>(), const_grid_iter.axisValue<1>());
    BOOST_CHECK_EQUAL(const_slice_iter.axisValue<2>(), const_grid_iter.axisValue<2>());
    BOOST_CHECK_EQUAL(const_slice_iter.axisValue<3>(), const_grid_iter.axisValue<3>());
  }
  BOOST_CHECK(const_grid_iter == const_grid.end());
}

//-----------------------------------------------------------------------------
// Test that slices parenthesis operator works fine
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(sliceParenthesisOperator, GridContainer_Fixture) {

  // Given
  GridContainerType grid{axes_tuple};
  double            custom_value = 0;
  for (auto& cell : grid) {
    custom_value += 0.1;
    cell = custom_value;
  }

  // When
  auto slice = grid.fixAxisByIndex<1>(2).fixAxisByIndex<3>(1);

  // Then
  for (size_t coord1 = 0; coord1 < axis1.size(); ++coord1) {
    for (size_t coord3 = 0; coord3 < axis3.size(); ++coord3) {
      BOOST_CHECK_EQUAL(slice(coord1, 0, coord3, 0), grid(coord1, 2, coord3, 1));
    }
  }
}

//-----------------------------------------------------------------------------
// Test that slices at works fine
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(sliceAtOperator, GridContainer_Fixture) {

  // Given
  GridContainerType grid{axes_tuple};
  double            custom_value = 0;
  for (auto& cell : grid) {
    custom_value += 0.1;
    cell = custom_value;
  }

  // When
  auto slice = grid.fixAxisByIndex<1>(2).fixAxisByIndex<3>(1);

  // Then
  for (size_t coord1 = 0; coord1 < axis1.size(); ++coord1) {
    for (size_t coord3 = 0; coord3 < axis3.size(); ++coord3) {
      BOOST_CHECK_EQUAL(slice.at(coord1, 0, coord3, 0), grid(coord1, 2, coord3, 1));
    }
  }
}

//-----------------------------------------------------------------------------
// Test that slices fixed axes throw exception for non zero indices when at is used
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(sliceFixAxisNonZeroIndexAccess, GridContainer_Fixture) {

  // Given
  GridContainerType grid{axes_tuple};

  // When
  auto slice = grid.fixAxisByIndex<0>(0).fixAxisByIndex<1>(2).fixAxisByIndex<2>(2).fixAxisByIndex<3>(1);

  // Then
  BOOST_CHECK_EQUAL(slice.at(0, 0, 0, 0), 0.);
  BOOST_CHECK_THROW(slice.at(1, 0, 0, 0), Elements::Exception);
  BOOST_CHECK_THROW(slice.at(0, 1, 0, 0), Elements::Exception);
  BOOST_CHECK_THROW(slice.at(0, 0, 1, 0), Elements::Exception);
  BOOST_CHECK_THROW(slice.at(0, 0, 0, 1), Elements::Exception);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
