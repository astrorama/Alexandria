/**
 * @file Keyword_test.cpp
 *
 * Created on: Oct 16, 2013
 *     Author: Pavel Binko
 */

#include <boost/test/unit_test.hpp>
#include "ChDataModel/Fits/Keyword.h"

#include <string>
#include <iostream>

using namespace ChDataModel::Fits;
using namespace std;

//------------------------------------------------------------------------------

struct KeywordFix {

  double precission = 1e-10;

  DoubleKeyword piKeyword = DoubleKeyword("PI", 3.14,
      "The PI keyword of the type double");

  string expectedPiKeywordName = "PI";
  double expectedPiKeywordValue = 3.14;
  KeywordTypes expectedPiKeywordType = KeywordTypes::Double;
  string expectedPiKeywordComment = "The PI keyword of the type double";

};

//------------------------------------------------------------------------------
//
// Begin of the Boost tests
//
//------------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Keyword_test)

//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( empty_constructors_test, KeywordFix ) {

  // An empty keyword
  Keyword<long> * emptyKeyword1 = new Keyword<long>();
  BOOST_CHECK(emptyKeyword1 != nullptr);
  delete emptyKeyword1;

  // The same empty keyword, with an other syntax
  LongKeyword emptyKeyword2;
  KeywordTypes emptyKeywordType = emptyKeyword2.getType();
  BOOST_CHECK(emptyKeywordType == KeywordTypes::Long);

} // Eof empty_constructors_test

//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( constructors_test, KeywordFix ) {

  string actualPiKeywordName = piKeyword.getName();
  BOOST_CHECK(actualPiKeywordName == expectedPiKeywordName);

  double actualPiKeywordValue = piKeyword.getValue();
  BOOST_CHECK_CLOSE(actualPiKeywordValue, expectedPiKeywordValue, precission);

  KeywordTypes actualPiKeywordType = piKeyword.getType();
  BOOST_CHECK(actualPiKeywordType == expectedPiKeywordType);

  string actualPiKeywordComment = piKeyword.getComment();
  BOOST_CHECK(actualPiKeywordComment == expectedPiKeywordComment);

} // Eof constructors_test

//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( copy_constructor_test, KeywordFix ) {

  DoubleKeyword keyword_copy(piKeyword);

  string actualKeywordCopyName = keyword_copy.getName();
  BOOST_CHECK(actualKeywordCopyName == expectedPiKeywordName);

  double actualKeywordCopyValue = keyword_copy.getValue();
  BOOST_CHECK_CLOSE(actualKeywordCopyValue, expectedPiKeywordValue, precission);

  KeywordTypes actualKeywordCopyType = keyword_copy.getType();
  BOOST_CHECK(actualKeywordCopyType == expectedPiKeywordType);

  string actualKeywordCopyComment = keyword_copy.getComment();
  BOOST_CHECK(actualKeywordCopyComment == expectedPiKeywordComment);

}  // Eof copy_constructor_test

//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( assignment_operator_test, KeywordFix ) {

  DoubleKeyword keyword_assigned = piKeyword;

  string actualKeywordAssignedName = keyword_assigned.getName();
  BOOST_CHECK(actualKeywordAssignedName == expectedPiKeywordName);

  double actualKeywordAssignedValue = keyword_assigned.getValue();
  BOOST_CHECK_CLOSE(actualKeywordAssignedValue, expectedPiKeywordValue,
      precission);

  KeywordTypes actualKeywordAssignedType = keyword_assigned.getType();
  BOOST_CHECK(actualKeywordAssignedType == expectedPiKeywordType);

  string actualKeywordAssignedComment = keyword_assigned.getComment();
  BOOST_CHECK(actualKeywordAssignedComment == expectedPiKeywordComment);

}  // Eof assignment_operator_test

//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( brief_assignment_operator_test, KeywordFix ) {

  DoubleKeyword twoPiKeyword = piKeyword;

  double expectedTwoPiKeywordValue = 6.28;
  twoPiKeyword = expectedTwoPiKeywordValue;

  string expectedTwoPiKeywordName = "TWO_PI";
  twoPiKeyword.setName(expectedTwoPiKeywordName);

  string actualTwoPiKeywordName = twoPiKeyword.getName();
  BOOST_CHECK(actualTwoPiKeywordName == expectedTwoPiKeywordName);

  double actualTwoPiKeywordValue = twoPiKeyword.getValue();
  BOOST_CHECK_CLOSE(actualTwoPiKeywordValue, expectedTwoPiKeywordValue,
      precission);

  // The other keyword attributes are unchanged
  KeywordTypes actualTwoPiKeywordType = twoPiKeyword.getType();
  BOOST_CHECK(actualTwoPiKeywordType == expectedPiKeywordType);

  string actualTwoPiKeywordComment = twoPiKeyword.getComment();
  BOOST_CHECK(actualTwoPiKeywordComment == expectedPiKeywordComment);

}  // Eof brief_assignment_operator_test

//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( equal_operator_test, KeywordFix ) {

  DoubleKeyword keyword_equal = piKeyword;

  BOOST_CHECK(keyword_equal == piKeyword);

}  // Eof equal_operator_test

//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( setters_test, KeywordFix ) {

  DoubleKeyword keyword("DBL_KEY2", 6.28, "New comment");

  DoubleKeyword keyword_set("DBL_KEY", 3.14, "A keyword of the type double");
  keyword_set.setName("DBL_KEY2");
  keyword_set.setValue(6.28);
  keyword_set.setComment("New comment");

  // Note: keyword_set.setType(an_other_type) is dangerous,
  //       therefore the method is protected in the class KeywordBase.

  BOOST_CHECK(keyword == keyword_set);

}  // Eof setters_test

//------------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( clone_test, KeywordFix ) {

  DoubleKeyword keyword("DBL_KEY", 3.14, "A keyword of the type double");
  KeywordBase * keyword_clone = keyword.keywordClone();

  BOOST_CHECK(keyword == *keyword_clone);

  string actualKeywordName = keyword.getName();
  string expectedKeywordName = keyword_clone->getName();
  BOOST_CHECK(actualKeywordName == expectedKeywordName);

  double actualKeywordValue = keyword.getValue();
  double expectedKeywordValue1 =
      dynamic_cast<DoubleKeyword *>(keyword_clone)->getValue();
  BOOST_CHECK_CLOSE(actualKeywordValue, expectedKeywordValue1, precission);
  double expectedKeywordValue2 =
      dynamic_cast<DoubleKeyword &>(*keyword_clone).getValue();
  BOOST_CHECK_CLOSE(actualKeywordValue, expectedKeywordValue2, precission);

  KeywordTypes actualKeywordType = keyword.getType();
  KeywordTypes expectedKeywordType = keyword_clone->getType();
  BOOST_CHECK(actualKeywordType == expectedKeywordType);

  string actualKeywordComment = keyword.getComment();
  string expectedKeywordComment = keyword_clone->getComment();
  BOOST_CHECK(actualKeywordComment == expectedKeywordComment);

}  // Eof clone_test

//------------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()

//------------------------------------------------------------------------------
//
// End of the Boost tests
//
//------------------------------------------------------------------------------
