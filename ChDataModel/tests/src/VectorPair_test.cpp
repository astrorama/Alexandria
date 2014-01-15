/**
 * @file VectorPair_test.cpp
 *
 * Created on: May 29, 2013
 *
 * @author dubath
 *
 * @section LICENSE
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 2 of
 * the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * General Public License for more details at
 * http://www.gnu.org/copyleft/gpl.html
 *
 * @section DESCRIPTION
 *
 * This class represents ...
 */
#include <boost/test/unit_test.hpp>
#include <iostream>
#include <vector>
#include "ChDataModel/VectorPair.h"

#include "ElementsKernel/ElementsException.h"

#include <exception>

using namespace ChDataModel;
using namespace std;

//------------------------------------------------------------------------------

struct VectorPairFixture_Base {
  std::vector<double> x;
  std::vector<double> y;
  double tolerence = 1e-6;
};

struct VectorPairFixture : public VectorPairFixture_Base {
  VectorPairFixture() {
    x = {1.0, 2.0, 3.0, 4.0};
    y = {1.1, 2.1, 3.1, 4.1};
  }
};

struct VectorPairFixture_DifferentSize  : public VectorPairFixture_Base {
  VectorPairFixture_DifferentSize() {
    x = {1.0, 2.0};
    y = {1.1, 2.1, 3.1};
  }
};

struct VectorPairFixture_NotUnique  : public VectorPairFixture_Base {
  VectorPairFixture_NotUnique() {
    x = {1.0, 2.0, 2.0, 4.0};
    y = {1.1, 2.1, 3.1, 4.1};
  }
};

struct VectorPairFixture_NotSorted  : public VectorPairFixture_Base {
  VectorPairFixture_NotSorted() {
    x = {1.0, 3.0, 2.0, 4.0};
    y = {1.1, 2.1, 3.1, 4.1};
  }
};

//------------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (VectorPairFixture_test)

//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( constructors_test_OK, VectorPairFixture ) {

  VectorPair * vectorPair = nullptr;

  try {
    vectorPair = new VectorPair(x, y);
  } catch (const ElementsException & e) {
    // Constructor failed
    cout << "Exception raised : " << e.what() << endl;
    BOOST_CHECK(false);
  }
  BOOST_CHECK(true);

  delete vectorPair;

} // Eof constructors_test_OK

//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( constructors_test_DifferentSize, VectorPairFixture_DifferentSize ) {

  VectorPair * vectorPair = nullptr;

  bool exception = false;

  try {
    vectorPair = new VectorPair(x, y);
  } catch (const ElementsException & e) {
    // Constructor failed
    cout << "Exception raised : " << e.what() << endl;
    string exception_str = e.what();
    exception =
        (exception_str.find(
            "DataModel::VectorPair : The vectors provided in the constructor do not have the same length.")
            != string::npos);
    if (true == exception) {
      cout << "Result OK - this exception should have been thrown" << endl;
    }
    else {
      cout << "Result NOT OK - an other exception should have been thrown" << endl;
    }
  }

  BOOST_CHECK(exception);

  delete vectorPair;

} // Eof constructors_test_DifferentSize

//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( constructors_test_NotSorted, VectorPairFixture_NotSorted ) {

  VectorPair * vectorPair = nullptr;
  bool check_sort_unique = true;

  bool exception = false;

  try {
    vectorPair = new VectorPair(x, y, check_sort_unique);
    vectorPair->printVectorPair();
  } catch (const ElementsException & e) {
    // Constructor failed
    cout << "Exception raised : " << e.what() << endl;
    string exception_str = e.what();
    exception =
        (exception_str.find(
            "DataModel::VectorPair : The values of the vector X are not sorted.")
            != string::npos);
    if (true == exception) {
      cout << "Result OK - this exception should have been thrown" << endl;
    }
    else {
      cout << "Result NOT OK - an other exception should have been thrown" << endl;
    }
  }

  BOOST_CHECK(exception);

  delete vectorPair;

} // Eof constructors_test_NotSorted
//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( constructors_test_NotUnique, VectorPairFixture_NotUnique ) {

  VectorPair * vectorPair = nullptr;
  bool check_sort_unique = true;

  bool exception = false;

  try {
    vectorPair = new VectorPair(x, y, check_sort_unique);
    vectorPair->printVectorPair();
  } catch (const ElementsException & e) {
    // Constructor failed
    cout << "Exception raised : " << e.what() << endl;
    string exception_str = e.what();
    exception =
        (exception_str.find(
            "DataModel::VectorPair : The values of the vector X are not unique.")
            != string::npos);
    if (true == exception) {
      cout << "Result OK - this exception should have been thrown" << endl;
    }
    else {
      cout << "Result NOT OK - an other exception should have been thrown" << endl;
    }
  }

  BOOST_CHECK(exception);

  delete vectorPair;

} // Eof constructors_test_NotUnique

//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( getter_test, VectorPairFixture ) {

  // This getter_test is not using pointers to the vector pairs

  bool exception = true;

  try {

    VectorPair vectorPairA(x, y);
    VectorPair vectorPairB = VectorPair(x, y);

    // Getters of individual vector elements
    for (size_t i = 0; i < x.size(); i++) {
      BOOST_CHECK_CLOSE(y.at(i), vectorPairA.getY(i), tolerence);
      BOOST_CHECK_CLOSE(x.at(i), vectorPairB.getX(i), tolerence);
    }

    // Getters of the whole vectors
    vector<double> axisX = vectorPairA.getAxisX();
    vector<double> axisY = vectorPairB.getAxisY();

    for (size_t i = 0; i < axisX.size(); i++) {
      BOOST_CHECK_CLOSE(x.at(i), axisX.at(i), tolerence);
      BOOST_CHECK_CLOSE(y.at(i), axisY.at(i), tolerence);
    }

  } catch (const ElementsException & e) {
    // Constructor failed
    cout << "Exception raised : " << e.what() << endl;
    exception = false;
  }

  BOOST_CHECK(exception);

} // Eof getter_test

//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( getter_out_of_range, VectorPairFixture ) {

  VectorPair * vectorPair = new VectorPair(x, y);

  // On the axis X
  bool exception = false;

  try {
    vectorPair->getX(4);
  } catch (const ElementsException & e) {
    //exception = true;
    string exception_str = e.what();
    exception = (exception_str.find(
        "DataModel::VectorPair::getX : Index is out of range") != string::npos);
  }
  BOOST_CHECK(exception);

  // On the axis Y
  exception = false;

  try {
    vectorPair->getY(4);
  } catch (const ElementsException & e) {
    string exception_str = e.what();
    exception = (exception_str.find(
        "DataModel::VectorPair::getY : Index is out of range") != string::npos);
  }
  BOOST_CHECK(exception);

} // Eof getter_out_of_range

//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( getter_out_of_range_vector, VectorPairFixture ) {

  VectorPair * vectorPair = new VectorPair(x, y);

  /**
   * Beware that with vectorPair->getX()[6] no exception or error messages are produced!
   */

  // On the axis X
  bool exception = false;

  try {
    vectorPair->getAxisX().at(6);
  } catch (const std::exception & e) {
    // This index does not exist on the X axis, this exception should be thrown
    exception = true;
  }
  BOOST_CHECK(exception);

  // On the axis Y
  exception = false;

  try {
    vectorPair->getAxisY().at(7);
  } catch (const std::exception & e) {
    // This index does not exist on the Y axis, this exception should be thrown
    exception = true;
  }
  BOOST_CHECK(exception);

}

//------------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()

