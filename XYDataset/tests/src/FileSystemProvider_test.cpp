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
 * @file tests/src/FileSystemProvider_test.cpp
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
#include "XYDataset/FileSystemProvider.h"
#include "XYDataset/QualifiedName.h"

using namespace Euclid::XYDataset;

// Create a directory on disk
void makeDirectory(const std::string& name) {
  boost::filesystem::path d{name};
  boost::filesystem::create_directories(d);
}

// Remove a directory on disk
void removeDir(const std::string& base_dir) {
  boost::filesystem::path bd{base_dir};
  boost::filesystem::remove_all(bd);
}

struct FileSystemProvider_Fixture {

  std::string group{"filter/MER"};
  // Do not forget the "/" at the end of the base directory
  Elements::TempDir temp_dir;
  std::string       base_directory{temp_dir.path().native() + "/euclid/"};
  std::string       mer_directory    = base_directory + "filter/MER";
  std::string       cosmos_directory = base_directory + "filter/COSMOS";

  FileSystemProvider_Fixture() {

    makeDirectory(base_directory);
    makeDirectory(mer_directory);
    makeDirectory(cosmos_directory);
    // Create files
    std::ofstream file1_mer(mer_directory + "/file1.txt");
    std::ofstream file2_mer(mer_directory + "/file2.txt");
    std::ofstream dotfile_mer(mer_directory + "/.DS_Store");
    // Fill up file
    file1_mer << "\n";
    file1_mer << "# Dataset_name_for_file1\n";
    file1_mer << "1234. 569.6\n";
    file1_mer.close();
    // Fill up 2nd file
    file2_mer << "\n";
    file2_mer << "111.1 111.1\n";
    file2_mer << "222.2 222.2\n";
    file2_mer.close();
    // Fill up 3rd file
    dotfile_mer << "\n";
    dotfile_mer << ".......\n";
    dotfile_mer << ".......\n";
    dotfile_mer.close();
  }

  ~FileSystemProvider_Fixture() {
    removeDir(base_directory);
  }

  std::unique_ptr<FileParser> fp{new AsciiParser{}};
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(FileSystemProvider_test)

//-----------------------------------------------------------------------------
// Test the empty name
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(empty_datasetname_test, FileSystemProvider_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the empty dataset name, .DS_Store file must be ignored");
  BOOST_TEST_MESSAGE(" ");

  FileSystemProvider fsp{temp_dir.path().native() + "/euclid/", std::move(fp)};

  // Even with two slashes in the group it must work
  group                                    = "filter/MER/";
  std::vector<QualifiedName> result_vector = fsp.listContents(group);
  BOOST_CHECK_EQUAL(2, result_vector.size());
  BOOST_CHECK(std::find(result_vector.begin(), result_vector.end(),
                        QualifiedName{{"filter", "MER"}, "Dataset_name_for_file1"}) != result_vector.end());
  BOOST_CHECK(std::find(result_vector.begin(), result_vector.end(), QualifiedName{{"filter", "MER"}, "file2"}) !=
              result_vector.end());
}

//-----------------------------------------------------------------------------
// Test the exceptions
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(exceptions_test, FileSystemProvider_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the exceptions");
  BOOST_TEST_MESSAGE(" ");

  // Path is not valid
  base_directory = temp_dir.path().native() + "/PATH_DOES_NOT_EXIST";
  BOOST_CHECK_THROW(FileSystemProvider fsp(base_directory, std::move(fp)), Elements::Exception);

  // Path to a file which is not valid
  base_directory = base_directory + "filter/MER/Gext_ACSf435w.txt";
  BOOST_CHECK_THROW(FileSystemProvider fsp(base_directory, std::move(fp)), Elements::Exception);

  // Fill up a new file with dataset name already existing
  // We must have only unique qualify name
  std::ofstream file3_mer(temp_dir.path().native() + "/euclid/filter/MER/file3.txt");
  file3_mer << "\n";
  file3_mer << "# Dataset_name_for_file1\n";
  file3_mer << "0.1111 1.0000 \n";
  file3_mer.close();

  BOOST_CHECK_THROW(FileSystemProvider fsp(base_directory, std::move(fp)), Elements::Exception);

  // Remove file3 to avoid exception in the next test
  removeDir(temp_dir.path().native() + "/euclid/filter/MER/file3.txt");
}

//-----------------------------------------------------------------------------
// Test the listContents function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(listContent_test, FileSystemProvider_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the listContents function");
  BOOST_TEST_MESSAGE(" ");

  FileSystemProvider fsp{temp_dir.path().native() + "/euclid/", std::move(fp)};

  // Even with two slashes in the group it must work
  group                                    = "filter/MER//";
  std::vector<QualifiedName> result_vector = fsp.listContents(group);
  BOOST_CHECK_EQUAL(2, result_vector.size());
  BOOST_CHECK(std::find(result_vector.begin(), result_vector.end(),
                        QualifiedName{{"filter", "MER"}, "Dataset_name_for_file1"}) != result_vector.end());
  BOOST_CHECK(std::find(result_vector.begin(), result_vector.end(), QualifiedName{{"filter", "MER"}, "file2"}) !=
              result_vector.end());

  // With this group the vector must be empty
  group                                     = "MER";
  std::vector<QualifiedName> result_vector2 = fsp.listContents(group);
  BOOST_CHECK_EQUAL(0, result_vector2.size());
}

//-----------------------------------------------------------------------------
// Test the getDataset function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getDataset_test, FileSystemProvider_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the getDataset function");
  BOOST_TEST_MESSAGE(" ");

  FileSystemProvider fsp{temp_dir.path().native() + "/euclid/", std::move(fp)};

  // Check that a pointer must be returned (and not the nullptr)
  QualifiedName                                 identifier{{"filter", "MER"}, "Dataset_name_for_file1"};
  std::unique_ptr<Euclid::XYDataset::XYDataset> dataset_ptr = fsp.getDataset(identifier);

  BOOST_CHECK(dataset_ptr);

  // Check a nullptr must be returned
  identifier  = QualifiedName{{"filter"}, "DOES_NOT_EXIST"};
  dataset_ptr = fsp.getDataset(identifier);

  BOOST_CHECK(!dataset_ptr);
}

//-----------------------------------------------------------------------------
// Test when using an empty order.txt file
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(empty_order_file_listContents_test, FileSystemProvider_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the listContents function when using an empty order.txt file");
  BOOST_TEST_MESSAGE(" ");

  std::ofstream order_mer(mer_directory + "/order.txt");
  // Empty order.txt file
  order_mer.close();

  FileSystemProvider fsp{temp_dir.path().native() + "/euclid/", std::move(fp)};

  // Even with two slashes in the group it must work
  group                                    = "filter/MER//";
  std::vector<QualifiedName> result_vector = fsp.listContents(group);
  for (auto& elt : result_vector) {
    std::cout << elt.datasetName() << std::endl;
  }
  BOOST_CHECK_EQUAL(2, result_vector.size());
  BOOST_CHECK_EQUAL(result_vector[0].datasetName(), "Dataset_name_for_file1");
  BOOST_CHECK_EQUAL(result_vector[1].datasetName(), "file2");
}

//-----------------------------------------------------------------------------
// Test when using the order.txt file
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(ordering_listContents_test, FileSystemProvider_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the listContents function when using the order.txt file");
  BOOST_TEST_MESSAGE(" ");

  std::ofstream order_mer(mer_directory + "/order.txt");
  // Empty order.txt file
  order_mer << "file2.txt\n";
  order_mer << "file1.txt\n";
  order_mer << "file3.txt\n";  // This file should have no effect to the result
  order_mer.close();

  FileSystemProvider fsp{temp_dir.path().native() + "/euclid/", std::move(fp)};

  // Even with two slashes in the group it must work
  group                                    = "filter/MER//";
  std::vector<QualifiedName> result_vector = fsp.listContents(group);
  for (auto& elt : result_vector) {
    std::cout << elt.datasetName() << std::endl;
  }
  BOOST_CHECK_EQUAL(2, result_vector.size());
  BOOST_CHECK_EQUAL(result_vector[0].datasetName(), "file2");
  BOOST_CHECK_EQUAL(result_vector[1].datasetName(), "Dataset_name_for_file1");
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
