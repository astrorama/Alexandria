/**
 * @file Header_test.cpp
 *
 * Created on: Sep 19, 2013
 *     Author: Pavel Binko
 */

#include <boost/test/unit_test.hpp>
#include "ChDataModel/Fits/Header.h"
#include "ChDataModel/Fits/Keyword.h"

#include <string>
#include <iostream>

using namespace ChDataModel::Fits;
using namespace std;

//-----------------------------------------------------------------------------

struct HeaderFix {

  Header * header = new Header();

  BoolKeyword bool_keyword = BoolKeyword("BOOL_KEY", true, "A bool value");
  DoubleKeyword double_keyword = DoubleKeyword("DBL_KEY", 3.14,
      "A double value");
  LongKeyword long_keyword = LongKeyword("LONG_KEY", -999, "A long value");
  StringKeyword string_keyword = StringKeyword("STR_KEY", "MyValue1",
      "A string value");

  ~HeaderFix() {
    delete header;
  }

};

//-----------------------------------------------------------------------------
//
// Begin of the Boost tests
//
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (Header_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( constructors_test, HeaderFix ) {

  BOOST_CHECK(header != nullptr);

}  // Eof constructors_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( copy_constructor_test, HeaderFix ) {

  header->addKeyword(bool_keyword);
  header->addKeyword(double_keyword);
  header->addKeyword(long_keyword);
  header->addKeyword(string_keyword);

  // Copy constructor
  Header * headerComp = new Header(*header);

  BOOST_CHECK(*header == *headerComp);

}  // Eof copy_constructor_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( equal_operator_test, HeaderFix ) {

  header->addKeyword(bool_keyword);
  header->addKeyword(double_keyword);
  header->addKeyword(long_keyword);
  header->addKeyword(string_keyword);

  // These two headers are equal
  Header * headerComp = new Header();
  headerComp->addKeyword(bool_keyword);
  headerComp->addKeyword(double_keyword);
  headerComp->addKeyword(long_keyword);
  headerComp->addKeyword(string_keyword);

  BOOST_CHECK(*header == *headerComp);

  // Make the headers different

  // Assign a new different value to the long keyword "LONG_KEY"
  LongKeyword new_long_keyword = long_keyword;
  new_long_keyword = 12345;
  // Replacing the long keyword "LONG_KEY" makes the headers not equal
  headerComp->addKeyword(new_long_keyword);

  BOOST_CHECK(!(*header == *headerComp));

  // Putting back the original "LONG_KEY" makes the headers again equal
  headerComp->addKeyword(long_keyword);

  // Adding one more keyword makes the headers again not equal
  BoolKeyword * new_bool_keyword = new BoolKeyword("NEW_BOOL", false,
      "A new bool keyword");
  headerComp->addKeyword(*new_bool_keyword);

  BOOST_CHECK(!(*header == *headerComp));

} // Eof equal_operator_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( assignment_operator_test, HeaderFix ) {

  header->addKeyword(bool_keyword);
  header->addKeyword(double_keyword);
  header->addKeyword(long_keyword);
  header->addKeyword(string_keyword);

  Header * headerComp = new Header();

  // Assignment operator
  *headerComp = *header;

  BOOST_CHECK(*header == *headerComp);

} // Eof assignment_operator_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( addKeyword_test, HeaderFix ) {

  header->addKeyword(bool_keyword);
  header->addKeyword(long_keyword);

  int actualNofKeywords = header->getNofKeywords();
  int expectedNofKeywords = 2;

  BOOST_CHECK_EQUAL(actualNofKeywords, expectedNofKeywords);

} // Eof addKeyword_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( deleteKeyword_test, HeaderFix ) {

  header->addKeyword(bool_keyword);
  header->addKeyword(double_keyword);
  header->addKeyword(long_keyword);
  header->addKeyword(string_keyword);

  header->deleteKeyword("DBL_KEY");

  size_t actualNofKeywords = header->getKeywords().size();
  size_t expectedNofKeywords = 3;

  BOOST_CHECK_EQUAL(actualNofKeywords, expectedNofKeywords);

} // Eof deleteKeyword_test

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( getKeyword_test, HeaderFix ) {

  header->addKeyword(bool_keyword);
  header->addKeyword(double_keyword);
  header->addKeyword(long_keyword);
  header->addKeyword(string_keyword);

  // To get the name, such a more compact one line code can be used,
  // because the function getName() is a function of the class KeywordBase.
  // (The same is valid for getName(), getUnit() and getComment().)
  string actualKeywordName = header->getKeyword("LONG_KEY").getName();
  string expectedKeywordName = "LONG_KEY";
  BOOST_CHECK_EQUAL(actualKeywordName, expectedKeywordName);

  // Retrieve the comment using the same style
  string actualKeywordComment = header->getKeyword("LONG_KEY").getComment();
  string expectedKeywordComment = "A long value";
  BOOST_CHECK(actualKeywordComment == expectedKeywordComment);

  // To get the value, the code must be expanded into two lines,
  // because the function getValue() is a function of the class Keyword.
  // Note: In the first line, the cast is performed automatically.
  LongKeyword & longKeyword = header->getKeyword("LONG_KEY");
  long actualKeywordValue = longKeyword.getValue();
  long expectedKeywordValue = -999;
  BOOST_CHECK_EQUAL(actualKeywordValue, expectedKeywordValue);

  // An other possibility is using the dynamic cast explicitly
  // Note: In case the "operator IntKeyword & ()" (and similarly for the other
  //       types) would not be implemented, such a cast would be mandatory.
  LongKeyword & longKeyword2 = dynamic_cast<LongKeyword &>(header->getKeyword(
      "LONG_KEY"));

  int actualKeywordValue2 = longKeyword2.getValue();
  int expectedKeywordValue2 = -999;

  BOOST_CHECK_EQUAL(actualKeywordValue2, expectedKeywordValue2);

  // Try to retrieve a non-existent keyword
  bool exception = false;

  try {
    header->getKeyword("NONEXIST");
  }
  catch (const std::out_of_range & e) {
    // This keyword does not exist, this exception should be thrown
    exception = true;
  }
  BOOST_CHECK(exception);

} // Eof getKeyword_test

//-----------------------------------------------------------------------------
BOOST_AUTO_TEST_SUITE_END ()

//-----------------------------------------------------------------------------
//
// End of the Boost tests
//
//-----------------------------------------------------------------------------
