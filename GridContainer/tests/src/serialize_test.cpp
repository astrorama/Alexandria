/** 
 * @file serialize_test.cpp
 * @date July 7, 2014
 * @author Nikolaos Apostolakos
 */

#include <sstream>
#include <boost/test/unit_test.hpp>
#include <boost/test/test_tools.hpp>
#include "ElementsKernel/Temporary.h"
#include "GridContainer/serialize.h"
#include "serialization/DefaultConstructibleClass.h"
#include "serialization/NonDefaultConstructibleClass.h"
#include "XYDataset/XYDataset.h"

namespace std {

std::ostream& operator<<(std::ostream& stream, const Euclid::XYDataset::QualifiedName& name) {
  stream << name.qualifiedName();
  return stream;
}

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (serialize_test)

//-----------------------------------------------------------------------------
// Test serialization of default constructible cell values
//-----------------------------------------------------------------------------
    
BOOST_AUTO_TEST_CASE(GridContainerSerializationDefaultConstructibleCells) {
  
  typedef DefaultConstructibleClass DCC;
  typedef NonDefaultConstructibleClass NDCC;
  typedef Euclid::GridContainer::GridContainer<std::vector<DCC>, double, DCC, NDCC> GridContainerType;
  
  // Given
  std::string name0 = "FundamentalAxis";
  std::vector<double> knots0 {0., 3.4, 12E-15};
  Euclid::GridContainer::GridAxis<double> axis0 {name0, knots0};
  std::string name1 = "DefaultConstructibleAxis";
  std::vector<DCC> knots1 {DCC{}, DCC{}, DCC{}};
  knots1[0].value = 0.;
  knots1[1].value = 3.4;
  knots1[2].value = 12E-15;
  Euclid::GridContainer::GridAxis<DCC> axis1 {name1, knots1};
  std::string name2 = "NonDefaultConstructibleAxis";
  std::vector<NDCC> knots2 {};
  knots2.push_back(NDCC{0.});
  knots2.push_back(NDCC{3.4});
  knots2.push_back(NDCC{12E-15});
  Euclid::GridContainer::GridAxis<NDCC> axis2 {name2, knots2};
  GridContainerType grid {axis0, axis1, axis2};
  double value {0.};
  for (auto& cell : grid) {
    cell.value = value;
    value += 0.1;
  }
  
  // When
  std::stringstream stream {};
  Euclid::GridContainer::gridBinaryExport(stream, grid);
  GridContainerType result = Euclid::GridContainer::gridBinaryImport<GridContainerType>(stream);
  
  // Then
  BOOST_CHECK_EQUAL(result.axisNumber(), 3u);
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
  BOOST_CHECK_EQUAL(result.size(), grid.size());
  auto result_iter = result.begin();
  auto grid_iter = grid.begin();
  while (result_iter != result.end()) {
    BOOST_CHECK_EQUAL((*result_iter).value, (*grid_iter).value);
    ++result_iter;
    ++grid_iter;
  }
  
}

//-----------------------------------------------------------------------------
// Test serialization of non default constructible cell values
//-----------------------------------------------------------------------------
    
BOOST_AUTO_TEST_CASE(GridContainerSerializationNonDefaultConstructibleCells) {
  
  typedef DefaultConstructibleClass DCC;
  typedef NonDefaultConstructibleClass NDCC;
  typedef Euclid::GridContainer::GridContainer<std::vector<NDCC>, double, DCC, NDCC> GridContainerType;
  
  // Given
  std::string name0 = "FundamentalAxis";
  std::vector<double> knots0 {0., 3.4, 12E-15};
  Euclid::GridContainer::GridAxis<double> axis0 {name0, knots0};
  std::string name1 = "DefaultConstructibleAxis";
  std::vector<DCC> knots1 {DCC{}, DCC{}, DCC{}};
  knots1[0].value = 0.;
  knots1[1].value = 3.4;
  knots1[2].value = 12E-15;
  Euclid::GridContainer::GridAxis<DCC> axis1 {name1, knots1};
  std::string name2 = "NonDefaultConstructibleAxis";
  std::vector<NDCC> knots2 {};
  knots2.push_back(NDCC{0.});
  knots2.push_back(NDCC{3.4});
  knots2.push_back(NDCC{12E-15});
  Euclid::GridContainer::GridAxis<NDCC> axis2 {name2, knots2};
  GridContainerType grid {axis0, axis1, axis2};
  double value {0.};
  for (auto& cell : grid) {
    cell = NDCC{value};
    value += 0.1;
  }
  
  // When
  std::stringstream stream {};
  Euclid::GridContainer::gridBinaryExport(stream, grid);
  GridContainerType result = Euclid::GridContainer::gridBinaryImport<GridContainerType>(stream);
  
  // Then
  BOOST_CHECK_EQUAL(result.axisNumber(), 3u);
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
  BOOST_CHECK_EQUAL(result.size(), grid.size());
  auto result_iter = result.begin();
  auto grid_iter = grid.begin();
  while (result_iter != result.end()) {
    BOOST_CHECK_EQUAL((*result_iter).value, (*grid_iter).value);
    ++result_iter;
    ++grid_iter;
  }
  
}

//-----------------------------------------------------------------------------
// Test FITS serialization
//-----------------------------------------------------------------------------
    
BOOST_AUTO_TEST_CASE(GridContainerSerializationFits) {
  
  using namespace Euclid::GridContainer;
  using namespace Euclid::XYDataset;
  typedef GridContainer<std::vector<int>, std::string> SmallGridContainerType;
  typedef GridContainer<std::vector<double>, int, double, QualifiedName> BigGridContainerType;
  
  // Given
  std::string name11 = "StringAxis";
  std::vector<std::string> knots11 {"one", "two", "three"};
  Euclid::GridContainer::GridAxis<std::string> axis11 {name11, knots11};
  SmallGridContainerType grid1 {axis11};
  int i = 0;
  for (auto& cell : grid1) {
    cell = i;
    ++i;
  }
  std::string name21 = "IntAxis";
  std::vector<int> knots21 {1, 2, 3};
  Euclid::GridContainer::GridAxis<int> axis21 {name21, knots21};
  std::string name22 = "DoubleAxis";
  std::vector<double> knots22 {0.1, 0.2, 0.3};
  Euclid::GridContainer::GridAxis<double> axis22 {name22, knots22};
  std::string name23 = "QualifiedNameAxis";
  std::vector<QualifiedName> knots23 {{"One"}, {"Two"}, {"Three"}};
  Euclid::GridContainer::GridAxis<QualifiedName> axis23 {name23, knots23};
  BigGridContainerType grid2 {axis21, axis22, axis23};
  double d = 0.;
  for (auto& cell : grid2) {
    cell = d;
    d += 0.1;
  }
  
  // When
  Elements::TempDir dir {};
  auto fits_file = dir.path() / "test.fits";
  gridFitsExport(fits_file, "first", grid1);
  gridFitsExport(fits_file, "second", grid2);
  auto result1 = gridFitsImport<SmallGridContainerType>(fits_file, 1);
  auto result2 = gridFitsImport<BigGridContainerType>(fits_file, 3);
  
  // Then
  BOOST_CHECK_EQUAL(result1.axisNumber(), grid1.axisNumber());
  BOOST_CHECK_EQUAL(result1.getAxis<0>().name(), name11);
  BOOST_CHECK_EQUAL_COLLECTIONS(
      result1.getAxis<0>().begin(), result1.getAxis<0>().end(),
      knots11.begin(), knots11.end());
  BOOST_CHECK_EQUAL_COLLECTIONS(
      result1.begin(), result1.end(),
      grid1.begin(), grid1.end());
  BOOST_CHECK_EQUAL(result2.axisNumber(), grid2.axisNumber());
  BOOST_CHECK_EQUAL(result2.getAxis<0>().name(), name21);
  BOOST_CHECK_EQUAL_COLLECTIONS(
      result2.getAxis<0>().begin(), result2.getAxis<0>().end(),
      knots21.begin(), knots21.end());
  BOOST_CHECK_EQUAL(result2.getAxis<1>().name(), name22);
  BOOST_CHECK_EQUAL_COLLECTIONS(
      result2.getAxis<1>().begin(), result2.getAxis<1>().end(),
      knots22.begin(), knots22.end());
  BOOST_CHECK_EQUAL(result2.getAxis<2>().name(), name23);
  BOOST_CHECK_EQUAL_COLLECTIONS(
      result2.getAxis<2>().begin(), result2.getAxis<2>().end(),
      knots23.begin(), knots23.end());
  BOOST_CHECK_EQUAL_COLLECTIONS(
      result2.begin(), result2.end(),
      grid2.begin(), grid2.end());
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
