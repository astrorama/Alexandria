/**
 * @file MakePCARing_test.cpp
 *
 *  Created on: December 2, 2013
 *      Author: Pavel Binko
 */

#include <boost/test/unit_test.hpp>
#include "PCA/MakePCARing.h"

using namespace PCA;
using namespace std;

//-----------------------------------------------------------------------------

struct MakePCARingFix {

  string fileName = "PCA/tests/...";

  MakePCARingFix() {
  }

  ~MakePCARingFix() {
  }

};

//-----------------------------------------------------------------------------
//
// Begin of the Boost tests
//
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (MakePCARing_test)

BOOST_FIXTURE_TEST_CASE( constructors_test, MakePCARingFix ) {

  MakePCARing * input = nullptr;
  BOOST_CHECK(nullptr == input);
  input = new MakePCARing();
  BOOST_CHECK(nullptr != input);
  delete input;

}


//-----------------------------------------------------------------------------
// End of the Boost tests
BOOST_AUTO_TEST_SUITE_END ()
