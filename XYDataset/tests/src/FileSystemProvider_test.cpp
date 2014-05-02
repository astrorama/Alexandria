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

namespace XYDataset {

struct FileSystemProvider_Fixture {

  std::string group { "filter/MER" };
  // Do not forget the "/" at the end of the base directory
  std::string base_directory { "/tmp/euclid/" };
  std::string directory_mer { base_directory + "filter/MER" };
  std::string directory_cosmos { base_directory + "filter/COSMOS" };
  std::unique_ptr<FileParser> fp {};

  FileSystemProvider<std::string> fsp {base_directory, std::move(fp)};

  FileSystemProvider_Fixture() {
    // Remove previous files
    boost::filesystem::path fsdir(base_directory);
    boost::filesystem::remove_all(fsdir);
    // Create directories in /tmp
    boost::filesystem::path fsdir_mer(directory_mer);
    boost::filesystem::create_directories(fsdir_mer);
    boost::filesystem::path fsdir_cosmos(directory_cosmos);
    boost::filesystem::create_directories(fsdir_cosmos);
    // Create files
    std::ofstream file1_mer(directory_mer+"/Gext_ACSf435w.txt");
    std::ofstream file2_mer(directory_mer+"/Hnir_WFC3f160w.txt");
    std::ofstream file_cosmos(directory_cosmos+"/cosmos_filter.txt");
  }

  ~FileSystemProvider_Fixture() {
    boost::filesystem::path fsdir(base_directory);
    boost::filesystem::remove_all(fsdir);
  }

};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (FileSystemProvider_test)

//-----------------------------------------------------------------------------
//            Test the exceptions of the listContents function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ListContent_exceptions_test, FileSystemProvider_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the exceptions");
  BOOST_TEST_MESSAGE(" ");

  // Group not valid
  group = "NO_VALID_DIRECTORY";
  BOOST_CHECK_THROW(fsp.listContents(group), ElementsException);

  // Group should not be a file
  group = "PhotZAuxData/Filter/MER/Gext_ACSf435w.txt";
  BOOST_CHECK_THROW(fsp.listContents(group), ElementsException);
}

//-----------------------------------------------------------------------------
//            Test the listContents function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ListContent_test, FileSystemProvider_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the list contents function");
  BOOST_TEST_MESSAGE(" ");

  std::vector<std::string> result_vector = fsp.listContents(group);

  BOOST_CHECK_EQUAL(2, result_vector.size());

}


//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()

} /* namespace XYDataset */


