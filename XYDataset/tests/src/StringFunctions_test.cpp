/**
 * @file StringFunctions_test.cpp
 *
 * @date May 26, 2014
 * @author Nicolas Morisset
 */

#include <iostream>
#include <fstream>
#include <string>
#include <memory>

#include <boost/test/unit_test.hpp>
#include <boost/filesystem.hpp>

#include "../../XYDataset/src/lib/StringFunctions.h"

using namespace XYDataset;



struct Stringfunctions_Fixture {


  Stringfunctions_Fixture() {
 }
  ~Stringfunctions_Fixture() {

  }

};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (FitsParser_test)

//-----------------------------------------------------------------------------
// Test the checkBeginSlashes function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(checkBeginSlashes_test, Stringfunctions_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the checkBeginSlashes function");
  BOOST_TEST_MESSAGE(" ");

  BOOST_CHECK_EQUAL("/", checkBeginSlashes("") );
  BOOST_CHECK_EQUAL("/string/test", checkBeginSlashes("string/test") );
  BOOST_CHECK_EQUAL("/string/test", checkBeginSlashes("//string/test") );
}

//-----------------------------------------------------------------------------
// Test the checkNoBeginSlashes function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(checkNoBeginSlashes_test, Stringfunctions_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the checkNoBeginSlashes function");
  BOOST_TEST_MESSAGE(" ");

  BOOST_CHECK_EQUAL("", checkNoBeginSlashes("") );
  BOOST_CHECK_EQUAL("string/test", checkNoBeginSlashes("string/test") );
  BOOST_CHECK_EQUAL("string/test", checkNoBeginSlashes("/string/test") );
  BOOST_CHECK_EQUAL("string/test", checkNoBeginSlashes("//string/test") );
}

//-----------------------------------------------------------------------------
// Test the checkEndSlashesfunction
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(checkEndSlashes_test, Stringfunctions_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the checkEndSlashes function");
  BOOST_TEST_MESSAGE(" ");

  BOOST_CHECK_EQUAL("/", checkEndSlashes("") );
  BOOST_CHECK_EQUAL("string/test/", checkEndSlashes("string/test") );
  BOOST_CHECK_EQUAL("string/test/", checkEndSlashes("string/test/") );
  BOOST_CHECK_EQUAL("string/test/", checkEndSlashes("string/test//") );
}

//-----------------------------------------------------------------------------
// Test the removeExtension
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(removeExtension_test, Stringfunctions_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the removeExtension function");
  BOOST_TEST_MESSAGE(" ");

  BOOST_CHECK_EQUAL("", removeExtension("") );
  BOOST_CHECK_EQUAL("extension", removeExtension("extension.txt") );
  BOOST_CHECK_EQUAL("extension", removeExtension("extension") );
}

//-----------------------------------------------------------------------------
// Test the removeAllBeforeLastSlash
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(removeAllBeforeLastSlash_test, Stringfunctions_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the removeExtension function");
  BOOST_TEST_MESSAGE(" ");

  BOOST_CHECK_EQUAL("", removeAllBeforeLastSlash("") );
  BOOST_CHECK_EQUAL("file.txt", removeAllBeforeLastSlash("file.txt") );
  BOOST_CHECK_EQUAL("file.txt", removeAllBeforeLastSlash("/test/test1/file.txt") );
  BOOST_CHECK_EQUAL("file.txt", removeAllBeforeLastSlash("/test/test1//file.txt") );
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()




