/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
 *
 * This library is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free
 * Software Foundation; either version 3.0 of the License, or (at your option)
 * any later version.
 *
 * This library is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
 * details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this library; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 */

/**
 * @file tests/src/AsciiParser_test.cpp
 *
 * @date Apr 16, 2014
 * @author Nicolas Morisset
 */

#include <fstream>
#include <iostream>
#include <string>

#include <boost/filesystem.hpp>
#include <boost/test/unit_test.hpp>

#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Temporary.h"
#include "XYDataset/AsciiParser.h"
#include "XYDataset/XYDataset.h"

using namespace Euclid::XYDataset;

std::string makeDir(std::string name) {
  boost::filesystem::path d{name};
  boost::filesystem::create_directories(d);
  return name;
}
void removeDir(std::string base_dir) {
  boost::filesystem::path bd{base_dir};
  boost::filesystem::remove_all(bd);
}

struct AsciiParser_Fixture {

  // Do not forget the "/" at the end of the base directory
  std::string       no_file{"nofile.txt"};
  std::string       nolines_file{"nolines_file.txt"};
  std::string       empty_file{"empty_file.txt"};
  std::string       file{"Gext_ACSf435w.txt"};
  std::string       file_nodataset_name{"Nodataset_name_inside_file.txt"};
  std::string       not_a_dataset_file{"not_a_dataset_file.txt"};
  Elements::TempDir temp_dir;
  std::string       base_directory = makeDir(temp_dir.path().native() + "/euclid/filter/MER/");

  AsciiParser_Fixture() {
    // Create files
    std::ofstream offile(base_directory + file);
    // Fill up file
    offile << "\n";
    offile << "# Test_name\n";
    offile << "# TEST TEST_VALUE\n";
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

    std::ofstream ofnot_a_dataset_file(base_directory + not_a_dataset_file);
    // Fill up file
    ofnot_a_dataset_file << "\n";
    offile << "# Test_name\n";
    ofnot_a_dataset_file << "2222. 2222.2 test\n";
    ofnot_a_dataset_file.close();

    std::ofstream ofnolines_file(base_directory + nolines_file);
    // Fill up file
    ofnolines_file << "\n";
    ofnolines_file << "# Test_name\n";
    ofnolines_file.close();

    std::ofstream ofempty_file(base_directory + empty_file);
    ofempty_file.close();
  }
  ~AsciiParser_Fixture() {
    removeDir(base_directory);
  }
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(AsciiParser_test)

//-----------------------------------------------------------------------------
// Test the exception of the getParameter function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(exception_getParameter_function_test, AsciiParser_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the exception of getParameter function");
  BOOST_TEST_MESSAGE(" ");

  AsciiParser parser{};

  BOOST_CHECK_THROW(parser.getParameter(base_directory + no_file, "TEST"), Elements::Exception);
}

//-----------------------------------------------------------------------------
// Test of the getParameter function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getParameter_function_test, AsciiParser_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the  getParameter function");
  BOOST_TEST_MESSAGE(" ");

  // The dataset is the correct name, result: Keyword value
  AsciiParser parser{};

  BOOST_CHECK_EQUAL("TEST_VALUE", parser.getParameter(base_directory + file, "TEST"));

  BOOST_CHECK_EQUAL("", parser.getParameter(base_directory + file_nodataset_name, "TEST2"));

  BOOST_CHECK_EQUAL("", parser.getParameter(base_directory + file_nodataset_name, "TEST"));
}

//-----------------------------------------------------------------------------
// Test the exception of the getName function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(exception_getName_function_test, AsciiParser_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the exception of getName function");
  BOOST_TEST_MESSAGE(" ");

  AsciiParser parser{};

  BOOST_CHECK_THROW(parser.getName(base_directory + no_file), Elements::Exception);
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
  auto        xy_ptr = parser.getDataset(base_directory + file);
  BOOST_CHECK_EQUAL(xy_ptr->size(), 3);
}

//-----------------------------------------------------------------------------
// Test the isDatatsetFile function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(isDatatsetFile_function_test, AsciiParser_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the isDatatsetFile function");
  BOOST_TEST_MESSAGE(" ");

  AsciiParser parser{};
  BOOST_CHECK_EQUAL(parser.isDatasetFile(base_directory + file), true);
  // File with lines not following the dataset rule
  BOOST_CHECK_EQUAL(parser.isDatasetFile(base_directory + not_a_dataset_file), false);
  // File containing no data lines
  BOOST_CHECK_EQUAL(parser.isDatasetFile(base_directory + nolines_file), false);
  // File with no line at all
  BOOST_CHECK_EQUAL(parser.isDatasetFile(base_directory + empty_file), false);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
