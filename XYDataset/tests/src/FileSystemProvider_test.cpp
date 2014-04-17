/**
 * @file FileSystemProvider_test.cpp
 *
 * @date Apr 16, 2014
 * @author Nicolas Morisset
 */

#include <iostream>
#include <boost/test/unit_test.hpp>
#include "ElementsKernel/ElementsException.h"
#include "XYDataset/FileSystemProvider.h"

using namespace std;

namespace XYDataset {

struct FileSystemProvider_Fixture {
  string group = "PhotZAuxData/Filter";
  unique_ptr<FileParser> fp {};
  FileSystemProvider<string> fsp {"/Users/admin/Eclipse/Alexandria/", std::move(fp)};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (FileSystemProvider_test)
//
////-----------------------------------------------------------------------------
////            Test the listContents function
////-----------------------------------------------------------------------------
//
//BOOST_FIXTURE_TEST_CASE(ListContent_test, FileSystemProvider_Fixture) {
//
//  BOOST_TEST_MESSAGE(" ");
//  BOOST_TEST_MESSAGE("--> Testing the list contents");
//  BOOST_TEST_MESSAGE(" ");
//
//  //vector<string> result_vector = fsp.listContents(group);
//
//  // BOOST_CHECK(nullptr != xy_ptr);
//
//}
//
//
////-----------------------------------------------------------------------------
//
BOOST_AUTO_TEST_SUITE_END ()

}


