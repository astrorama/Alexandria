/** 
 * @file Matrix_test.cpp
 * @date July 4, 2014
 * @author Nikolaos Apostolakos
 */

#include <vector>
#include <boost/test/unit_test.hpp>
#include <boost/test/test_tools.hpp>
#include "ChMatrix/Matrix.h"

struct Matrix_Fixture {
  typedef ChMatrix::Matrix<std::vector<double>, int, int, int, int> MatrixType;
  typedef ChMatrix::AxisInfo<int> IntAxis;
  IntAxis axis1 {"Axis 1", {1, 2, 3, 4, 5}};
  IntAxis axis2 {"Axis 2", {1, 2, 3}};
  IntAxis axis3 {"Axis 3", {1, 2, 3, 4, 5, 6}};
  IntAxis axis4 {"Axis 4", {1, 2}};
  std::tuple<IntAxis, IntAxis, IntAxis, IntAxis> axes_tuple {axis1, axis2, axis3, axis4};
  size_t total_size = axis1.size() * axis2.size() * axis3.size() * axis4.size();
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Matrix_test)

//-----------------------------------------------------------------------------
// Test construction with AxisInfo objects
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(AxisInfoConstructor, Matrix_Fixture) {
  
  // When
  MatrixType result_matrix {axis1, axis2, axis3, axis4};
  auto& result_data_manager = result_matrix.dataManager();
  auto& result_axes_tuple = result_matrix.axisInfoTuple();
  
  // Then
  BOOST_CHECK_EQUAL(result_data_manager.size(), total_size);
  for (auto& value : result_data_manager) {
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
// Test construction with AxisInfo objects and DataManager
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(AxisInfoDataManagerConstructor, Matrix_Fixture) {
  
  // Given
  std::unique_ptr<std::vector<double>> custom_data_manager {new std::vector<double>(total_size)};
  double custom_value = 0;
  for (size_t i=0; i<total_size; ++i) {
    custom_value += 0.1;
    (*custom_data_manager)[i] = custom_value;
  }
  
  // When
  MatrixType result_matrix {std::move(custom_data_manager), axis1, axis2, axis3, axis4};
  auto& result_data_manager = result_matrix.dataManager();
  auto& result_axes_tuple = result_matrix.axisInfoTuple();
  
  // Then
  BOOST_CHECK_EQUAL(result_data_manager.size(), total_size);
  double expected_value = 0;
  for (auto& value : result_data_manager) {
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
// Test construction with AxisInfo objects and DataManager with wrong size
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(AxisInfoDataManagerConstructorWrongSize, Matrix_Fixture) {
  
  // Given
  std::unique_ptr<std::vector<double>> custom_data_manager {new std::vector<double>(total_size/2)};
  
  // Then
  BOOST_CHECK_THROW(MatrixType(std::move(custom_data_manager), axis1, axis2, axis3, axis4), ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test construction with AxisInfo tuple
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(AxisInfoTupleonstructor, Matrix_Fixture) {
  
  // When
  MatrixType result_matrix {axes_tuple};
  auto& result_data_manager = result_matrix.dataManager();
  auto& result_axes_tuple = result_matrix.axisInfoTuple();
  
  // Then
  BOOST_CHECK_EQUAL(result_data_manager.size(), total_size);
  for (auto& value : result_data_manager) {
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
// Test construction with AxisInfo tuple and DataManager
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(AxisInfoTupleDataManagerConstructor, Matrix_Fixture) {
  
  // Given
  std::unique_ptr<std::vector<double>> custom_data_manager {new std::vector<double>(total_size)};
  double custom_value = 0;
  for (size_t i=0; i<total_size; ++i) {
    custom_value += 0.1;
    (*custom_data_manager)[i] = custom_value;
  }
  
  // When
  MatrixType result_matrix {std::move(custom_data_manager), axes_tuple};
  auto& result_data_manager = result_matrix.dataManager();
  auto& result_axes_tuple = result_matrix.axisInfoTuple();
  
  // Then
  BOOST_CHECK_EQUAL(result_data_manager.size(), total_size);
  double expected_value = 0;
  for (auto& value : result_data_manager) {
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
// Test construction with AxisInfo tuple and DataManager with wrong size
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(AxisInfoTupleDataManagerConstructorWrongSize, Matrix_Fixture) {
  
  // Given
  std::unique_ptr<std::vector<double>> custom_data_manager {new std::vector<double>(total_size/2)};
  
  // Then
  BOOST_CHECK_THROW(MatrixType(std::move(custom_data_manager), axes_tuple), ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test the rank method
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(rank, Matrix_Fixture) {
  
  // When
  MatrixType matrix {axes_tuple};
  
  // Then
  BOOST_CHECK_EQUAL(matrix.rank(), 4);
  
}

//-----------------------------------------------------------------------------
// Test the axisInfo method
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(axisInfo, Matrix_Fixture) {
  
  // When
  MatrixType matrix {axes_tuple};
  
  // Then
  BOOST_CHECK_EQUAL(matrix.axisInfo<0>().name(), axis1.name());
  BOOST_CHECK_EQUAL(matrix.axisInfo<1>().name(), axis2.name());
  BOOST_CHECK_EQUAL(matrix.axisInfo<2>().name(), axis3.name());
  BOOST_CHECK_EQUAL(matrix.axisInfo<3>().name(), axis4.name());
  
}

//-----------------------------------------------------------------------------
// Test the size method
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(size, Matrix_Fixture) {
  
  // When
  MatrixType matrix {axes_tuple};
  
  // Then
  BOOST_CHECK_EQUAL(matrix.size(), total_size);
  
}

//-----------------------------------------------------------------------------
// Test the parenthesis operator
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(parenthesisOperator, Matrix_Fixture) {
  
  // Given
  std::unique_ptr<std::vector<double>> custom_data_manager {new std::vector<double>(total_size)};
  double custom_value = 0;
  for (size_t i=0; i<total_size; ++i) {
    custom_value += 0.1;
    (*custom_data_manager)[i] = custom_value;
  }
  
  // When
  MatrixType matrix {std::move(custom_data_manager), axes_tuple};
  
  // Then
  double expected_value {0};
  for (size_t coord4=0; coord4<axis4.size(); ++coord4) {
    for (size_t coord3=0; coord3<axis3.size(); ++coord3) {
      for (size_t coord2=0; coord2<axis2.size(); ++coord2) {
        for (size_t coord1=0; coord1<axis1.size(); ++coord1) {
          expected_value += 0.1;
          BOOST_CHECK_EQUAL(matrix(coord1, coord2, coord3, coord4), expected_value);
        }
      }
    }
  }
  
}

//-----------------------------------------------------------------------------
// Test the iterator
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(iterator, Matrix_Fixture) {
  
  // Given
  std::unique_ptr<std::vector<double>> custom_data_manager {new std::vector<double>(total_size)};
  double custom_value = 0;
  for (size_t i=0; i<total_size; ++i) {
    custom_value += 0.1;
    (*custom_data_manager)[i] = custom_value;
  }
  
  // When
  MatrixType matrix {std::move(custom_data_manager), axes_tuple};
  
  // Then
  double expected_value {0};
  for (auto& result_value : matrix) {
    expected_value += 0.1;
    BOOST_CHECK_EQUAL(result_value, expected_value);
  }
  
}

//-----------------------------------------------------------------------------
// Test the iterators axisIndex
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(iteratorAxisIndex, Matrix_Fixture) {
  
  // Given
  MatrixType matrix {axes_tuple};
  
  // When
  auto iterator = matrix.begin();
  
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
    
BOOST_FIXTURE_TEST_CASE(iteratorAxisValue, Matrix_Fixture) {
  
  // Given
  MatrixType matrix {axes_tuple};
  
  // When
  auto iterator = matrix.begin();
  
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
    
BOOST_FIXTURE_TEST_CASE(fixIteratorByIndex, Matrix_Fixture) {
  
  // Given
  MatrixType matrix {axes_tuple};
  
  for (size_t fixed_index=0; fixed_index<axis1.size(); ++fixed_index) {
    
    // When
    auto iterator = matrix.begin();
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
    auto iterator = matrix.begin();
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
    auto iterator = matrix.begin();
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
    auto iterator = matrix.begin();
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
    
BOOST_FIXTURE_TEST_CASE(fixIteratorByIndexOutOfBound, Matrix_Fixture) {
  
  // Given
  MatrixType matrix {axes_tuple};
  
  // When
  auto iterator = matrix.begin();
  
  // Then
  BOOST_CHECK_THROW(iterator.fixAxisByIndex<0>(axis1.size()), ElementsException);
  BOOST_CHECK_THROW(iterator.fixAxisByIndex<1>(axis2.size()), ElementsException);
  BOOST_CHECK_THROW(iterator.fixAxisByIndex<2>(axis3.size()), ElementsException);
  BOOST_CHECK_THROW(iterator.fixAxisByIndex<3>(axis4.size()), ElementsException);
  
}

//-----------------------------------------------------------------------------
// Test fixing iterator by value
//-----------------------------------------------------------------------------
    
BOOST_FIXTURE_TEST_CASE(fixIteratorByValue, Matrix_Fixture) {
  
  // Given
  MatrixType matrix {axes_tuple};
  
  for (size_t fixed_index=0; fixed_index<axis1.size(); ++fixed_index) {
    
    // When
    auto iterator = matrix.begin();
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
    auto iterator = matrix.begin();
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
    auto iterator = matrix.begin();
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
    auto iterator = matrix.begin();
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
    
BOOST_FIXTURE_TEST_CASE(fixIteratorByValueNotFound, Matrix_Fixture) {
  
  // Given
  MatrixType matrix {axes_tuple};
  
  // When
  auto iterator = matrix.begin();
  
  // Then
  BOOST_CHECK_THROW(iterator.fixAxisByValue<0>(axis1.size()+1), ElementsException);
  BOOST_CHECK_THROW(iterator.fixAxisByValue<1>(axis2.size()+1), ElementsException);
  BOOST_CHECK_THROW(iterator.fixAxisByValue<2>(axis3.size()+1), ElementsException);
  BOOST_CHECK_THROW(iterator.fixAxisByValue<3>(axis4.size()+1), ElementsException);
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()