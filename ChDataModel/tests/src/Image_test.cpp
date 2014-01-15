/**
 * @file Image_test.cpp
 *
 * Created on: Oct 17, 2013
 *     Author: Pavel Binko
 */

#include <boost/test/unit_test.hpp>
#include "ChDataModel/Fits/Image.h"
#include "ChDataModel/Fits/Header.h"
#include "ChDataModel/Fits/Keyword.h"

#include <iostream>

#include <string>
#include <Eigen/Core>

using namespace ChDataModel::Fits;
using namespace std;
using namespace Eigen;

//-----------------------------------------------------------------------------

struct ImageFix {

  double precission = 1e-10;

  Image image = Image();

  Header * header = new Header();

  BoolKeyword bool_keyword = BoolKeyword("BOOL_KEY", true, "A bool value");
  DoubleKeyword double_keyword = DoubleKeyword("DBL_KEY", 3.14,
      "A double value");
  LongKeyword long_keyword = LongKeyword("LONG_KEY", -999, "A long value");
  StringKeyword string_keyword = StringKeyword("STR_KEY", "MyValue1",
      "A string value");

  LongKeyword sizeX = LongKeyword("NAXIS1", 2, "The size of the axis X");
  LongKeyword sizeY = LongKeyword("NAXIS2", 2, "The size of the axis Y");

  MatrixXd testData;

  ImageFix() {

    // It is irrelevant, if the header is attached to the image object here
    // or after the keywords will be added.
    image.setHeader(header);

    header->addKeyword(bool_keyword);
    header->addKeyword(double_keyword);
    header->addKeyword(long_keyword);
    header->addKeyword(string_keyword);

    header->addKeyword(sizeX);
    header->addKeyword(sizeY);

    // Create a matrix of 2 * 2 elements
    testData.resize(2,2);
    testData << 1.1, 2.2,
                3.3, 4.4;

    image.setData(testData);

  }

};

//-----------------------------------------------------------------------------
//
// Begin of the Boost tests
//
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Image_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( constructors_test, ImageFix ) {

  Image * empty_image = new Image();
  BOOST_CHECK(empty_image != nullptr);
  delete empty_image;

}  // Eof constructors_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( copy_constructor_and_equal_operator_test, ImageFix ) {

  Image image_copy = Image(image);
  BOOST_CHECK(image_copy == image);

}  // Eof copy_constructor_and_equal_operator_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( assign_operator_test, ImageFix ) {

  Image image_assigned = image;
  BOOST_CHECK(image_assigned == image);

}  // Eof assign_operator_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( get_header_test, ImageFix ) {

  Header * header = image.getHeader();
  long actualNofKeywords = header->getNofKeywords();
//  cout << actualNofKeywords << endl;
  long expectedNofKeywords = 6;
//  cout << expectedNofKeywords << endl;
  BOOST_CHECK_EQUAL(actualNofKeywords, expectedNofKeywords);

}  // Eof get_header_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( getters_test, ImageFix ) {

  Eigen::MatrixXd testData = image.getData();
  double actualElement0 = testData(0);
  double expectedElement0 = 1.1;
  BOOST_CHECK_CLOSE(actualElement0, expectedElement0, precission);

  // Access to non-existent element in the data - NO CHECK DONE HERE

}  // Eof getters_test

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()

//-----------------------------------------------------------------------------
//
// End of the Boost tests
//
//-----------------------------------------------------------------------------
