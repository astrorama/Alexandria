/**
 * @file tests/src/AsciiParser_test.cpp
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
#include "ElementsKernel/Temporary.h"
#include "XYDataset/AsciiParser.h"
#include "XYDataset/XYDataset.h"

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

struct AsciiParser_Fixture {

  // Do not forget the "/" at the end of the base directory
  std::string no_file {"nofile.txt"};
  std::string file {"Gext_ACSf435w.txt"};
  std::string file_nodataset_name {"Nodataset_name_inside_file.txt"};
  TempDir temp_dir;
  std::string base_directory = makeDir(temp_dir.path().native()+"/euclid/filter/MER/");

  AsciiParser_Fixture() {
    // Create files
    std::ofstream offile(base_directory + file);
    // Fill up file
    offile << "\n";
    offile << "# Test_name\n";
    offile << "1234. 569.6\n";
    offile << "5678. 569.6\n";
    offile << "91011 569.6\n";
    offile.close();
    std::ofstream offile_nodataset_name(base_directory + file_nodataset_name);
    // Fill up file
    offile_nodataset_name << "\n";
    offile_nodataset_name << "2222. 2222.2\n";
    offile_nodataset_name << "1111. 1111.1\n";
    offile_nodataset_name.close();
  }
  ~AsciiParser_Fixture() {
    removeDir(base_directory);
  }


};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (AsciiParser_test)

//-----------------------------------------------------------------------------
// Test the exception of the getName function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(exception_getName_function_test, AsciiParser_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the exception of getName function");
  BOOST_TEST_MESSAGE(" ");

  AsciiParser parser{};

  BOOST_CHECK_THROW(parser.getName(base_directory + no_file), ElementsException);
}

//-----------------------------------------------------------------------------
// Test the getName function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getName_function_test, AsciiParser_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the getName function, dataset name inside file");
  BOOST_TEST_MESSAGE(" ");

  AsciiParser parser{};
  std::string dataset_name = parser.getName(base_directory + file);
  BOOST_CHECK_EQUAL("Test_name", dataset_name);

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the getName function, dataset is the filename");
  BOOST_TEST_MESSAGE(" ");

  dataset_name = parser.getName(base_directory + file_nodataset_name);
  BOOST_CHECK_EQUAL("Nodataset_name_inside_file", dataset_name);

}

//-----------------------------------------------------------------------------
// Test the getDataset function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getDataset_function_test, AsciiParser_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the getDataset function");
  BOOST_TEST_MESSAGE(" ");

  AsciiParser parser{};
  auto xy_ptr = parser.getDataset(base_directory + file);
  BOOST_CHECK_EQUAL(xy_ptr->size(), 3);

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
