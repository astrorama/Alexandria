/**
 * @file tests/src/XYDataset_test.cpp
 *
 * @date Apr 9, 2014
 * @author Nicolas Morisset
 */

#include <iostream>
#include <boost/test/unit_test.hpp>

#include "ElementsKernel/Real.h"
#include "ElementsKernel/Exception.h"
#include "XYDataset/XYDataset.h"

using namespace std;
using Elements::isEqual;

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
// Test the move constructor
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(MoveConstructor_test, XYDataset_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the move constructor");
  BOOST_TEST_MESSAGE(" ");

  auto xydataset = Euclid::XYDataset::XYDataset::factory(vector_pair);
  auto xy_move(std::move(xydataset));

  BOOST_CHECK(3 == xy_move.size());

}

//-----------------------------------------------------------------------------
// Test the factory function (the constructor)
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Constructor1_test, XYDataset_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the first constructor (with the vector pair)");
  BOOST_TEST_MESSAGE(" ");

  auto xydataset = Euclid::XYDataset::XYDataset::factory(vector_pair);

  BOOST_CHECK(3 == xydataset.size());

}

//-----------------------------------------------------------------------------
// Test the factory function (second constructor)
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(Constructor2_test, XYDataset_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the second constructor (with 2 vectors)");
  BOOST_TEST_MESSAGE(" ");

  auto xydataset = Euclid::XYDataset::XYDataset::factory(vector1, vector2);

  BOOST_CHECK(5 == xydataset.size());

}

//-----------------------------------------------------------------------------
// Test the XYDataset size function (second constructor)
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(factory_test, XYDataset_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the size function");
  BOOST_TEST_MESSAGE(" ");

  auto xydataset = Euclid::XYDataset::XYDataset::factory(vector1, vector2);
  BOOST_CHECK(5 == xydataset.size());

}

//-----------------------------------------------------------------------------
// Test the ElementException
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(exception_test, XYDataset_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the constructor exception");
  BOOST_TEST_MESSAGE(" ");

  BOOST_CHECK_THROW(Euclid::XYDataset::XYDataset::factory(vector1, vector3), Elements::Exception);

}

//-----------------------------------------------------------------------------
//                      Test the iterators
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(const_iterator_test, XYDataset_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the begin, end functions");
  BOOST_TEST_MESSAGE(" ");

  auto xydataset = Euclid::XYDataset::XYDataset::factory(vector1, vector2);
  auto it = xydataset.begin();

// The XYDataset specification guarantees that the iterator will iterate over
// the exact same double representations in the memory (which is a stricter
// guarantee than just the same real number representation). To allow testing
// the float-equal warning must be dissabled.
// WARNING: In the following lines the double literals are NOT representing the
// real values (1, 1.1, etc) but the double representation of these values as
// converted by the compiler. The test guarantees that the XYDataset does not
// perform any arithmetics with them.
  BOOST_CHECK(1   == it->first);
  BOOST_CHECK(1.1 == it->second);
  ++it;
  BOOST_CHECK(2   == it->first);
  BOOST_CHECK(2.2 == it->second);
  it = --xydataset.end();
  BOOST_CHECK(5   == it->first);
  BOOST_CHECK(5.5 == it->second);

}

//-----------------------------------------------------------------------------
//                      Test the front and back
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(front_back_test, XYDataset_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the front, back functions");
  BOOST_TEST_MESSAGE(" ");

  auto xydataset = Euclid::XYDataset::XYDataset::factory(vector1, vector2);
  auto& front = xydataset.front();
  auto& back = xydataset.back();

// The XYDataset specification guarantees that the iterator will iterate over
// the exact same double representations in the memory (which is a stricter
// guarantee than just the same real number representation). To allow testing
// the float-equal warning must be dissabled.
// WARNING: In the following lines the double literals are NOT representing the
// real values (1, 1.1, etc) but the double representation of these values as
// converted by the compiler. The test guarantees that the XYDataset does not
// perform any arithmetics with them.
  BOOST_CHECK(1   == front.first);
  BOOST_CHECK(1.1 == front.second);
  BOOST_CHECK(5   == back.first);
  BOOST_CHECK(5.5 == back.second);

}


BOOST_AUTO_TEST_SUITE_END ()

}
} // end of namespace Euclid
