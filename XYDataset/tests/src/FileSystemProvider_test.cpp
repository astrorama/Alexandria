/**
 * @file FileSystemProvider_test.cpp
 *
 * @date Apr 16, 2014
 * @author Nicolas Morisset
 */

#include <iostream>
#include <fstream>
#include <string>

#include <boost/test/unit_test.hpp>
#include <boost/filesystem.hpp>

#include "ElementsKernel/ElementsException.h"
#include "XYDataset/FileSystemProvider.h"

using namespace XYDataset;

std::string makeDir(std::string name) {
  boost::filesystem::path d {name};
  boost::filesystem::create_directories(d);
  return name;
}
void removeDir(std::string base_dir) {
  boost::filesystem::path bd {base_dir};
  boost::filesystem::remove_all(bd);
}

struct FileSystemProvider_Fixture {

  std::string group { "filter/MER" };
  // Do not forget the "/" at the end of the base directory
  std::string base_directory   = makeDir("/tmp/euclid/");
  std::string directory_mer    = makeDir(base_directory + "filter/MER");
  std::string directory_cosmos = makeDir(base_directory + "filter/COSMOS");

  //std::unique_ptr<FileParser> fp {};
  //FileSystemProvider<std::string> fsp {base_directory, std::move(fp)};

  FileSystemProvider_Fixture() {
    // Create files
    std::ofstream file1_mer(directory_mer+"/Gext_ACSf435w.txt");
    std::ofstream file2_mer(directory_mer+"/Hnir_WFC3f160w.txt");
    std::ofstream file_cosmos(directory_cosmos+"/cosmos_filter.txt");
  }

  ~FileSystemProvider_Fixture() {
   // removeDir(base_directory);
  }


};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (FileSystemProvider_test)

//-----------------------------------------------------------------------------
//                            Test the exceptions
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(exceptions_test, FileSystemProvider_Fixture) {

//  BOOST_TEST_MESSAGE(" ");
//  BOOST_TEST_MESSAGE("--> Testing the exceptions");
//  BOOST_TEST_MESSAGE(" ");
//
//  // Group not valid
//  group = "NO_VALID_GROUP";
//  BOOST_CHECK_THROW(fsp.listContents(group), ElementsException);
//
//  // Group should not be a file
//  group = "PhotZAuxData/Filter/MER/Gext_ACSf435w.txt";
//  BOOST_CHECK_THROW(fsp.listContents(group), ElementsException);
}

//-----------------------------------------------------------------------------
//            Test the listContents function
//-----------------------------------------------------------------------------

//BOOST_FIXTURE_TEST_CASE(ListContent_test, FileSystemProvider_Fixture) {
//
//  BOOST_TEST_MESSAGE(" ");
//  BOOST_TEST_MESSAGE("--> Testing the list contents function");
//  BOOST_TEST_MESSAGE(" ");
//
//  std::vector<std::string> result_vector = fsp.listContents(group);
//
//  for (unsigned int i=0; i<= result_vector.size(); ++i )
//      std::cout<<result_vector[i]<<std::endl;

//  BOOST_CHECK_EQUAL(2, result_vector.size());

//}


//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
