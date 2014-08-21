/** 
 * @file GridContainer_test.cpp
 * @date July 4, 2014
 * @author Nikolaos Apostolakos
 */

#include <vector>
#include <boost/test/unit_test.hpp>
#include <boost/test/test_tools.hpp>
#include "GridContainer/GridContainer.h"

struct GridContainer_Fixture {
  typedef Grid::GridContainer<std::vector<double>, int, int, int, int> GridContainerType;
  typedef Grid::GridAxis<int> IntAxis;
  IntAxis axis1 {"Axis 1", {1, 2, 3, 4, 5}};
  IntAxis axis2 {"Axis 2", {1, 2, 3}};
  IntAxis axis3 {"Axis 3", {1, 2, 3, 4, 5, 6}};
  IntAxis axis4 {"Axis 4", {1, 2}};
  std::tuple<IntAxis, IntAxis, IntAxis, IntAxis> axes_tuple {axis1, axis2, axis3, axis4};
  size_t total_size = axis1.size() * axis2.size() * axis3.size() * axis4.size();
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (GridContainer_test)

//-----------------------------------------------------------------------------
// Test construction with GridAxis objects
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(GridAxisConstructor, GridContainer_Fixture) {
  
  // When
  GridContainerType result_grid {axis1, axis2, axis3, axis4};
  auto& result_cell_manager = result_grid.getCellManager();
  auto& result_axes_tuple = result_grid.getAxesTuple();
  
  // Then
  BOOST_CHECK_EQUAL(result_cell_manager.size(), total_size);
  for (auto& value : result_cell_manager) {
    BOOST_CHECK_EQUAL(value, 0.);
  }
  BOOST_CHECK_EQUAL(std::get<0>(result_axes_tuple).name(), axis1.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(
      std::get<0>(result_axes_tuple).begin(), std::get<0>(result_axes_tuple).end(),
      axis1.begin(), axis1.end());
  BOOST_CHECK_EQUAL(std::get<1>(result_axes_tuple).name(), axis2.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(
      std::get<1>(result_axes_tuple).begin(), std::get<1>(result_axes_tuple).end(),
      axis2.begin(), axis2.end());
  BOOST_CHECK_EQUAL(std::get<2>(result_axes_tuple).name(), axis3.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(
      std::get<2>(result_axes_tuple).begin(), std::get<2>(result_axes_tuple).end(),
      axis3.begin(), axis3.end());
  BOOST_CHECK_EQUAL(std::get<3>(result_axes_tuple).name(), axis4.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(
      std::get<3>(result_axes_tuple).begin(), std::get<3>(result_axes_tuple).end(),
      axis4.begin(), axis4.end());
  
}

//-----------------------------------------------------------------------------
// Test construction with GridAxis objects and GridCellManager
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(GridAxisCellManagerConstructor, GridContainer_Fixture) {
  
  // Given
  std::unique_ptr<std::vector<double>> custom_cell_manager {new std::vector<double>(total_size)};
  double custom_value = 0;
  for (size_t i=0; i<total_size; ++i) {
    custom_value += 0.1;
    (*custom_cell_manager)[i] = custom_value;
  }
  
  // When
  GridContainerType result_grid {std::move(custom_cell_manager), axis1, axis2, axis3, axis4};
  auto& result_cell_manager = result_grid.getCellManager();
  auto& result_axes_tuple = result_grid.getAxesTuple();
  
  // Then
  BOOST_CHECK_EQUAL(result_cell_manager.size(), total_size);
  double expected_value = 0;
  for (auto& value : result_cell_manager) {
    expected_value += 0.1;
    BOOST_CHECK_EQUAL(value, expected_value);
  }
  BOOST_CHECK_EQUAL(std::get<0>(result_axes_tuple).name(), axis1.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(
      std::get<0>(result_axes_tuple).begin(), std::get<0>(result_axes_tuple).end(),
      axis1.begin(), axis1.end());
  BOOST_CHECK_EQUAL(std::get<1>(result_axes_tuple).name(), axis2.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(
      std::get<1>(result_axes_tuple).begin(), std::get<1>(result_axes_tuple).end(),
      axis2.begin(), axis2.end());
  BOOST_CHECK_EQUAL(std::get<2>(result_axes_tuple).name(), axis3.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(
      std::get<2>(result_axes_tuple).begin(), std::get<2>(result_axes_tuple).end(),
      axis3.begin(), axis3.end());
  BOOST_CHECK_EQUAL(std::get<3>(result_axes_tuple).name(), axis4.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(
      std::get<3>(result_axes_tuple).begin(), std::get<3>(result_axes_tuple).end(),
      axis4.begin(), axis4.end());
  
}

//-----------------------------------------------------------------------------
// Test construction with GridAxis objects and GridCellManager with wrong size
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(GridAxisCellManagerConstructorWrongSize, GridContainer_Fixture) {
  
  // Given
  std::unique_ptr<std::vector<double>> custom_cell_manager {new std::vector<double>(total_size/2)};
  
  // Then
  BOOST_CHECK_THROW(GridContainerType(std::move(custom_cell_manager), axis1, axis2, axis3, axis4), ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test construction with GridAxis tuple
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(GridAxisTupleonstructor, GridContainer_Fixture) {
  
  // When
  GridContainerType result_grid {axes_tuple};
  auto& result_cell_manager = result_grid.getCellManager();
  auto& result_axes_tuple = result_grid.getAxesTuple();
  
  // Then
  BOOST_CHECK_EQUAL(result_cell_manager.size(), total_size);
  for (auto& value : result_cell_manager) {
    BOOST_CHECK_EQUAL(value, 0.);
  }
  BOOST_CHECK_EQUAL(std::get<0>(result_axes_tuple).name(), axis1.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(
      std::get<0>(result_axes_tuple).begin(), std::get<0>(result_axes_tuple).end(),
      axis1.begin(), axis1.end());
  BOOST_CHECK_EQUAL(std::get<1>(result_axes_tuple).name(), axis2.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(
      std::get<1>(result_axes_tuple).begin(), std::get<1>(result_axes_tuple).end(),
      axis2.begin(), axis2.end());
  BOOST_CHECK_EQUAL(std::get<2>(result_axes_tuple).name(), axis3.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(
      std::get<2>(result_axes_tuple).begin(), std::get<2>(result_axes_tuple).end(),
      axis3.begin(), axis3.end());
  BOOST_CHECK_EQUAL(std::get<3>(result_axes_tuple).name(), axis4.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(
      std::get<3>(result_axes_tuple).begin(), std::get<3>(result_axes_tuple).end(),
      axis4.begin(), axis4.end());
  
}

//-----------------------------------------------------------------------------
// Test construction with GridAxis tuple and GridCellManager
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(GridAxisTupleCellManagerConstructor, GridContainer_Fixture) {
  
  // Given
  std::unique_ptr<std::vector<double>> custom_cell_manager {new std::vector<double>(total_size)};
  double custom_value = 0;
  for (size_t i=0; i<total_size; ++i) {
    custom_value += 0.1;
    (*custom_cell_manager)[i] = custom_value;
  }
  
  // When
  GridContainerType result_grid {std::move(custom_cell_manager), axes_tuple};
  auto& result_cell_manager = result_grid.getCellManager();
  auto& result_axes_tuple = result_grid.getAxesTuple();
  
  // Then
  BOOST_CHECK_EQUAL(result_cell_manager.size(), total_size);
  double expected_value = 0;
  for (auto& value : result_cell_manager) {
    expected_value += 0.1;
    BOOST_CHECK_EQUAL(value, expected_value);
  }
  BOOST_CHECK_EQUAL(std::get<0>(result_axes_tuple).name(), axis1.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(
      std::get<0>(result_axes_tuple).begin(), std::get<0>(result_axes_tuple).end(),
      axis1.begin(), axis1.end());
  BOOST_CHECK_EQUAL(std::get<1>(result_axes_tuple).name(), axis2.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(
      std::get<1>(result_axes_tuple).begin(), std::get<1>(result_axes_tuple).end(),
      axis2.begin(), axis2.end());
  BOOST_CHECK_EQUAL(std::get<2>(result_axes_tuple).name(), axis3.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(
      std::get<2>(result_axes_tuple).begin(), std::get<2>(result_axes_tuple).end(),
      axis3.begin(), axis3.end());
  BOOST_CHECK_EQUAL(std::get<3>(result_axes_tuple).name(), axis4.name());
  BOOST_CHECK_EQUAL_COLLECTIONS(
      std::get<3>(result_axes_tuple).begin(), std::get<3>(result_axes_tuple).end(),
      axis4.begin(), axis4.end());
  
}

//-----------------------------------------------------------------------------
// Test construction with GridAxis tuple and GridCellManager with wrong size
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(GridAxisTupleCellManagerConstructorWrongSize, GridContainer_Fixture) {
  
  // Given
  std::unique_ptr<std::vector<double>> custom_cell_manager {new std::vector<double>(total_size/2)};
  
  // Then
  BOOST_CHECK_THROW(GridContainerType(std::move(custom_cell_manager), axes_tuple), ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the rank method
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(rank, GridContainer_Fixture) {
  
  // When
  GridContainerType grid {axes_tuple};
  
  // Then
  BOOST_CHECK_EQUAL(grid.axisNumber(), 4);
  
}

//-----------------------------------------------------------------------------
// Test the getAxis method
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(getAxis, GridContainer_Fixture) {
  
  // When
  GridContainerType grid {axes_tuple};
  
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
  GridContainerType grid {axes_tuple};
  
  // Then
  BOOST_CHECK_EQUAL(grid.size(), total_size);
  
}

//-----------------------------------------------------------------------------
// Test the parenthesis operator
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(parenthesisOperator, GridContainer_Fixture) {
  
  // Given
  std::unique_ptr<std::vector<double>> custom_cell_manager {new std::vector<double>(total_size)};
  double custom_value = 0;
  for (size_t i=0; i<total_size; ++i) {
    custom_value += 0.1;
    (*custom_cell_manager)[i] = custom_value;
  }
  
  // When
  GridContainerType grid {std::move(custom_cell_manager), axes_tuple};
  const GridContainerType& const_grid = grid;
  
  // Then
  double expected_value {0};
  for (size_t coord4=0; coord4<axis4.size(); ++coord4) {
    for (size_t coord3=0; coord3<axis3.size(); ++coord3) {
      for (size_t coord2=0; coord2<axis2.size(); ++coord2) {
        for (size_t coord1=0; coord1<axis1.size(); ++coord1) {
          expected_value += 0.1;
          BOOST_CHECK_EQUAL(grid(coord1, coord2, coord3, coord4), expected_value);
          BOOST_CHECK_EQUAL(const_grid(coord1, coord2, coord3, coord4), expected_value);
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
  std::unique_ptr<std::vector<double>> custom_cell_manager {new std::vector<double>(total_size)};
  double custom_value = 0;
  for (size_t i=0; i<total_size; ++i) {
    custom_value += 0.1;
    (*custom_cell_manager)[i] = custom_value;
  }
  
  // When
  GridContainerType grid {std::move(custom_cell_manager), axes_tuple};
  const GridContainerType& const_grid = grid;
  
  // Then
  double expected_value {0};
  for (size_t coord4=0; coord4<axis4.size(); ++coord4) {
    for (size_t coord3=0; coord3<axis3.size(); ++coord3) {
      for (size_t coord2=0; coord2<axis2.size(); ++coord2) {
        for (size_t coord1=0; coord1<axis1.size(); ++coord1) {
          expected_value += 0.1;
          BOOST_CHECK_EQUAL(grid.at(coord1, coord2, coord3, coord4), expected_value);
          BOOST_CHECK_EQUAL(const_grid.at(coord1, coord2, coord3, coord4), expected_value);
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
  std::unique_ptr<std::vector<double>> custom_cell_manager {new std::vector<double>(total_size)};
  double custom_value = 0;
  for (size_t i=0; i<total_size; ++i) {
    custom_value += 0.1;
    (*custom_cell_manager)[i] = custom_value;
  }
  
  // When
  GridContainerType grid {std::move(custom_cell_manager), axes_tuple};
  const GridContainerType& const_grid = grid;
  
  // Then
  BOOST_CHECK_THROW(grid.at(axis1.size(), 0, 0, 0), ElementsException);
  BOOST_CHECK_THROW(grid.at(0, axis2.size(), 0, 0), ElementsException);
  BOOST_CHECK_THROW(grid.at(0, 0, axis3.size(), 0), ElementsException);
  BOOST_CHECK_THROW(grid.at(0, 0, 0, axis4.size()), ElementsException);
  BOOST_CHECK_THROW(const_grid.at(axis1.size(), 0, 0, 0), ElementsException);
  BOOST_CHECK_THROW(const_grid.at(0, axis2.size(), 0, 0), ElementsException);
  BOOST_CHECK_THROW(const_grid.at(0, 0, axis3.size(), 0), ElementsException);
  BOOST_CHECK_THROW(const_grid.at(0, 0, 0, axis4.size()), ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the iterator
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(iterator, GridContainer_Fixture) {
  
  // Given
  std::unique_ptr<std::vector<double>> custom_cell_manager {new std::vector<double>(total_size)};
  double custom_value = 0;
  for (size_t i=0; i<total_size; ++i) {
    custom_value += 0.1;
    (*custom_cell_manager)[i] = custom_value;
  }
  
  // When
  GridContainerType grid {std::move(custom_cell_manager), axes_tuple};
  
  // Then
  double expected_value {0};
  for (auto& result_value : grid) {
    expected_value += 0.1;
    BOOST_CHECK_EQUAL(result_value, expected_value);
  }
  
}

//-----------------------------------------------------------------------------
// Test the iterators axisIndex
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(iteratorAxisIndex, GridContainer_Fixture) {
  
  // Given
  GridContainerType grid {axes_tuple};
  
  // When
  auto iterator = grid.begin();
  
  // Then
  for (size_t coord4=0; coord4<axis4.size(); ++coord4) {
    for (size_t coord3=0; coord3<axis3.size(); ++coord3) {
      for (size_t coord2=0; coord2<axis2.size(); ++coord2) {
        for (size_t coord1=0; coord1<axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(iterator.axisIndex<0>(), coord1);
          BOOST_CHECK_EQUAL(iterator.axisIndex<1>(), coord2);
          BOOST_CHECK_EQUAL(iterator.axisIndex<2>(), coord3);
          BOOST_CHECK_EQUAL(iterator.axisIndex<3>(), coord4);
          ++iterator;
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
  GridContainerType grid {axes_tuple};
  
  // When
  auto iterator = grid.begin();
  
  // Then
  for (size_t coord4=0; coord4<axis4.size(); ++coord4) {
    for (size_t coord3=0; coord3<axis3.size(); ++coord3) {
      for (size_t coord2=0; coord2<axis2.size(); ++coord2) {
        for (size_t coord1=0; coord1<axis1.size(); ++coord1) {
          BOOST_CHECK_EQUAL(iterator.axisValue<0>(), axis1[coord1]);
          BOOST_CHECK_EQUAL(iterator.axisValue<1>(), axis2[coord2]);
          BOOST_CHECK_EQUAL(iterator.axisValue<2>(), axis3[coord3]);
          BOOST_CHECK_EQUAL(iterator.axisValue<3>(), axis4[coord4]);
          ++iterator;
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
  GridContainerType grid {axes_tuple};
  
  for (size_t fixed_index=0; fixed_index<axis1.size(); ++fixed_index) {
    
    // When
    auto iterator = grid.begin();
    iterator.fixAxisByIndex<0>(fixed_index);
    
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
    
  }
  
  for (size_t fixed_index=0; fixed_index<axis2.size(); ++fixed_index) {
    
    // When
    auto iterator = grid.begin();
    iterator.fixAxisByIndex<1>(fixed_index);
    
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
    
  }
  
  for (size_t fixed_index=0; fixed_index<axis3.size(); ++fixed_index) {
    
    // When
    auto iterator = grid.begin();
    iterator.fixAxisByIndex<2>(fixed_index);
    
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
    
  }
  
  for (size_t fixed_index=0; fixed_index<axis4.size(); ++fixed_index) {
    
    // When
    auto iterator = grid.begin();
    iterator.fixAxisByIndex<3>(fixed_index);
    
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
    
  }
  
}

//-----------------------------------------------------------------------------
// Test fixing iterator index out of bound exception
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(fixIteratorByIndexOutOfBound, GridContainer_Fixture) {
  
  // Given
  GridContainerType grid {axes_tuple};
  
  // When
  auto iterator = grid.begin();
  
  // Then
  BOOST_CHECK_THROW(iterator.fixAxisByIndex<0>(axis1.size()), ElementsException);
  BOOST_CHECK_THROW(iterator.fixAxisByIndex<1>(axis2.size()), ElementsException);
  BOOST_CHECK_THROW(iterator.fixAxisByIndex<2>(axis3.size()), ElementsException);
  BOOST_CHECK_THROW(iterator.fixAxisByIndex<3>(axis4.size()), ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test fixing iterator by value
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(fixIteratorByValue, GridContainer_Fixture) {
  
  // Given
  GridContainerType grid {axes_tuple};
  
  for (size_t fixed_index=0; fixed_index<axis1.size(); ++fixed_index) {
    
    // When
    auto iterator = grid.begin();
    iterator.fixAxisByValue<0>(axis1[fixed_index]);
    
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
    
  }
  
  for (size_t fixed_index=0; fixed_index<axis2.size(); ++fixed_index) {
    
    // When
    auto iterator = grid.begin();
    iterator.fixAxisByValue<1>(axis2[fixed_index]);
    
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
    
  }
  
  for (size_t fixed_index=0; fixed_index<axis3.size(); ++fixed_index) {
    
    // When
    auto iterator = grid.begin();
    iterator.fixAxisByValue<2>(axis3[fixed_index]);
    
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
    
  }
  
  for (size_t fixed_index=0; fixed_index<axis4.size(); ++fixed_index) {
    
    // When
    auto iterator = grid.begin();
    iterator.fixAxisByValue<3>(axis4[fixed_index]);
    
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
    
  }
  
}

//-----------------------------------------------------------------------------
// Test fixing iterator value not found exception
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(fixIteratorByValueNotFound, GridContainer_Fixture) {
  
  // Given
  GridContainerType grid {axes_tuple};
  
  // When
  auto iterator = grid.begin();
  
  // Then
  BOOST_CHECK_THROW(iterator.fixAxisByValue<0>(axis1.size()+1), ElementsException);
  BOOST_CHECK_THROW(iterator.fixAxisByValue<1>(axis2.size()+1), ElementsException);
  BOOST_CHECK_THROW(iterator.fixAxisByValue<2>(axis3.size()+1), ElementsException);
  BOOST_CHECK_THROW(iterator.fixAxisByValue<3>(axis4.size()+1), ElementsException);
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()