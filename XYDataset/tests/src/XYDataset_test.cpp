/**
 * @file tests/src/XYDataset_test.cpp
 *
 * @date Apr 9, 2014
 * @author Nicolas Morisset
 */

#include <iostream>
#include <boost/test/unit_test.hpp>

#include "ElementsKernel/ElementsException.h"
#include "XYDataset/XYDataset.h"

using namespace std;


namespace Euclid {
namespace XYDataset {

struct XYDataset_Fixture {
  std::vector<double> vector1 {1., 2., 3., 4., 5.};
  std::vector<double> vector2 {1.1, 2.2, 3.3, 4.4, 5.5};
  std::vector<double> vector3 {1.1, 2.2, 3.3};
  std::vector<std::pair<double,double>> vector_pair { {1,1}, {2,2}, {3,3} };
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (XYDataset_test)

//-----------------------------------------------------------------------------
// Test the factory function (the constructor)
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Constructor1_test, XYDataset_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the first constructor(with the vector pair)");
  BOOST_TEST_MESSAGE(" ");

  auto xy_ptr = Euclid::XYDataset::XYDataset::factory(vector_pair);
  // xy_ptr should not be null
  BOOST_CHECK(nullptr != xy_ptr);

}

//-----------------------------------------------------------------------------
// Test the factory function (second constructor)
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Constructor2_test, XYDataset_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the second constructor(with 2 vectors)");
  BOOST_TEST_MESSAGE(" ");

  auto xy_ptr = Euclid::XYDataset::XYDataset::factory(vector1, vector2);
  // xy_ptr should not be null
  BOOST_CHECK(nullptr != xy_ptr);

}

//-----------------------------------------------------------------------------
// Test the XYDataset size function (second constructor)
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(factory_test, XYDataset_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the size function");
  BOOST_TEST_MESSAGE(" ");

  auto xy_ptr = Euclid::XYDataset::XYDataset::factory(vector1, vector2);
  BOOST_CHECK(5 == xy_ptr->size());

}

//-----------------------------------------------------------------------------
// Test the ElementException
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(exception_test, XYDataset_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the constructor exception");
  BOOST_TEST_MESSAGE(" ");

  BOOST_CHECK_THROW(Euclid::XYDataset::XYDataset::factory(vector1, vector3), ElementsException);

}

//-----------------------------------------------------------------------------
//                      Test the iterators
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(const_iterator_test, XYDataset_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the begin, end functions");
  BOOST_TEST_MESSAGE(" ");

  auto xy_ptr = Euclid::XYDataset::XYDataset::factory(vector1, vector2);
  auto it = xy_ptr->begin();

  BOOST_CHECK(1   == it->first);
  BOOST_CHECK(1.1 == it->second);
  it = --xy_ptr->end();
  BOOST_CHECK(5   == it->first);
  BOOST_CHECK(5.5 == it->second);

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()

}
} // end of namespace Euclid
