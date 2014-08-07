/** 
 * @file serialize_test.cpp
 * @date July 7, 2014
 * @author Nikolaos Apostolakos
 */

#include <sstream>
#include <boost/test/unit_test.hpp>
#include <boost/test/test_tools.hpp>
#include "GridContainer/serialize.h"
#include "serialization/DefaultConstructibleClass.h"
#include "serialization/NonDefaultConstructibleClass.h"

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (serialize_test)

//-----------------------------------------------------------------------------
// Test serialization of default constructible cell values
//-----------------------------------------------------------------------------
    
BOOST_AUTO_TEST_CASE(GridContainerSerializationDefaultConstructibleCells) {
  
  typedef DefaultConstructibleClass DCC;
  typedef NonDefaultConstructibleClass NDCC;
  typedef GridContainer::GridContainer<std::vector<DCC>, double, DCC, NDCC> GridContainerType;
  
  // Given
  std::string name0 = "FundamentalAxis";
  std::vector<double> knots0 {0., 3.4, 12E-15};
  GridContainer::GridAxis<double> axis_info0 {name0, knots0};
  std::string name1 = "DefaultConstructibleAxis";
  std::vector<DCC> knots1 {DCC{}, DCC{}, DCC{}};
  knots1[0].value = 0.;
  knots1[1].value = 3.4;
  knots1[2].value = 12E-15;
  GridContainer::GridAxis<DCC> axis_info1 {name1, knots1};
  std::string name2 = "NonDefaultConstructibleAxis";
  std::vector<NDCC> knots2 {};
  knots2.push_back(NDCC{0.});
  knots2.push_back(NDCC{3.4});
  knots2.push_back(NDCC{12E-15});
  GridContainer::GridAxis<NDCC> axis_info2 {name2, knots2};
  std::unique_ptr<std::vector<DCC>> data_manager {new std::vector<DCC>{}};
  double value {0.};
  for (size_t i=0; i<knots0.size()*knots1.size()*knots2.size(); ++i) {
    data_manager->push_back({});
    data_manager->back().value = value;
    value += 0.1;
  }
  GridContainerType matrix {std::move(data_manager), axis_info0, axis_info1, axis_info2};
  
  // When
  std::stringstream stream {};
  GridContainer::binaryExport(stream, matrix);
  GridContainerType result = GridContainer::binaryImport<std::vector<DCC>, double, DCC, NDCC>(stream);
  
  // Then
  BOOST_CHECK_EQUAL(result.axisNumber(), 3);
  BOOST_CHECK_EQUAL(result.getAxis<0>().name(), name0);
  BOOST_CHECK_EQUAL_COLLECTIONS(
      result.getAxis<0>().begin(), result.getAxis<0>().end(),
      knots0.begin(), knots0.end());
  BOOST_CHECK_EQUAL(result.getAxis<1>().name(), name1);
  BOOST_CHECK_EQUAL(result.getAxis<1>().size(), knots1.size());
  auto result_iter1 = result.getAxis<1>().begin();
  auto knots_iter1 = knots1.begin();
  while (result_iter1 != result.getAxis<1>().end()) {
    BOOST_CHECK_EQUAL(result_iter1->value, knots_iter1->value);
    ++result_iter1;
    ++ knots_iter1;
  }
  BOOST_CHECK_EQUAL(result.getAxis<2>().name(), name2);
  BOOST_CHECK_EQUAL(result.getAxis<2>().size(), knots2.size());
  auto result_iter2 = result.getAxis<2>().begin();
  auto knots_iter2 = knots2.begin();
  while (result_iter2 != result.getAxis<2>().end()) {
    BOOST_CHECK_EQUAL(result_iter2->value, knots_iter2->value);
    ++result_iter2;
    ++ knots_iter2;
  }
  BOOST_CHECK_EQUAL(result.size(), matrix.size());
  auto result_iter = result.begin();
  auto matrix_iter = matrix.begin();
  while (result_iter != result.end()) {
    BOOST_CHECK_EQUAL((*result_iter).value, (*matrix_iter).value);
    ++result_iter;
    ++matrix_iter;
  }
  
}

//-----------------------------------------------------------------------------
// Test serialization of non default constructible cell values
//-----------------------------------------------------------------------------
    
BOOST_AUTO_TEST_CASE(GridContainerSerializationNonDefaultConstructibleCells) {
  
  typedef DefaultConstructibleClass DCC;
  typedef NonDefaultConstructibleClass NDCC;
  typedef GridContainer::GridContainer<std::vector<NDCC>, double, DCC, NDCC> GridContainerType;
  
  // Given
  std::string name0 = "FundamentalAxis";
  std::vector<double> knots0 {0., 3.4, 12E-15};
  GridContainer::GridAxis<double> axis_info0 {name0, knots0};
  std::string name1 = "DefaultConstructibleAxis";
  std::vector<DCC> knots1 {DCC{}, DCC{}, DCC{}};
  knots1[0].value = 0.;
  knots1[1].value = 3.4;
  knots1[2].value = 12E-15;
  GridContainer::GridAxis<DCC> axis_info1 {name1, knots1};
  std::string name2 = "NonDefaultConstructibleAxis";
  std::vector<NDCC> knots2 {};
  knots2.push_back(NDCC{0.});
  knots2.push_back(NDCC{3.4});
  knots2.push_back(NDCC{12E-15});
  GridContainer::GridAxis<NDCC> axis_info2 {name2, knots2};
  std::unique_ptr<std::vector<NDCC>> data_manager {new std::vector<NDCC>{}};
  double value {0.};
  for (size_t i=0; i<knots0.size()*knots1.size()*knots2.size(); ++i) {
    data_manager->push_back({value});
    value += 0.1;
  }
  GridContainerType matrix {std::move(data_manager), axis_info0, axis_info1, axis_info2};
  
  // When
  std::stringstream stream {};
  GridContainer::binaryExport(stream, matrix);
  GridContainerType result = GridContainer::binaryImport<std::vector<NDCC>, double, DCC, NDCC>(stream);
  
  // Then
  BOOST_CHECK_EQUAL(result.axisNumber(), 3);
  BOOST_CHECK_EQUAL(result.getAxis<0>().name(), name0);
  BOOST_CHECK_EQUAL_COLLECTIONS(
      result.getAxis<0>().begin(), result.getAxis<0>().end(),
      knots0.begin(), knots0.end());
  BOOST_CHECK_EQUAL(result.getAxis<1>().name(), name1);
  BOOST_CHECK_EQUAL(result.getAxis<1>().size(), knots1.size());
  auto result_iter1 = result.getAxis<1>().begin();
  auto knots_iter1 = knots1.begin();
  while (result_iter1 != result.getAxis<1>().end()) {
    BOOST_CHECK_EQUAL(result_iter1->value, knots_iter1->value);
    ++result_iter1;
    ++ knots_iter1;
  }
  BOOST_CHECK_EQUAL(result.getAxis<2>().name(), name2);
  BOOST_CHECK_EQUAL(result.getAxis<2>().size(), knots2.size());
  auto result_iter2 = result.getAxis<2>().begin();
  auto knots_iter2 = knots2.begin();
  while (result_iter2 != result.getAxis<2>().end()) {
    BOOST_CHECK_EQUAL(result_iter2->value, knots_iter2->value);
    ++result_iter2;
    ++ knots_iter2;
  }
  BOOST_CHECK_EQUAL(result.size(), matrix.size());
  auto result_iter = result.begin();
  auto matrix_iter = matrix.begin();
  while (result_iter != result.end()) {
    BOOST_CHECK_EQUAL((*result_iter).value, (*matrix_iter).value);
    ++result_iter;
    ++matrix_iter;
  }
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
