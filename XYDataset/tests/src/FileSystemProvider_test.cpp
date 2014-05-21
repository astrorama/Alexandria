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
#include "XYDataset/AsciiParser.h"
#include "XYDataset/QualifiedName.h"

using namespace XYDataset;

// Create a directory on disk
void makeDirectory(const std::string name) {
  boost::filesystem::path d {name};
  boost::filesystem::create_directories(d);
}

// Remove a directory on disk
void removeDir(const std::string base_dir) {
  boost::filesystem::path bd {base_dir};
  boost::filesystem::remove_all(bd);
}

struct FileSystemProvider_Fixture {

  std::string group { "filter/MER" };
  // Do not forget the "/" at the end of the base directory
  std::string base_directory { "/tmp/euclid/" };
  std::string mer_directory    = base_directory + "filter/MER";
  std::string cosmos_directory = base_directory + "filter/COSMOS";


  FileSystemProvider_Fixture() {
    makeDirectory(base_directory);
    makeDirectory(mer_directory);
    makeDirectory(cosmos_directory);
    // Create files
    std::ofstream file1_mer(mer_directory + "/file1.txt");
    std::ofstream file2_mer(mer_directory + "/file2.txt");
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
  }

  ~FileSystemProvider_Fixture() {
   removeDir(base_directory);
  }

  std::unique_ptr<FileParser> fp { new AsciiParser{} };

};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (FileSystemProvider_test)


//-----------------------------------------------------------------------------
//                            Test the exceptions
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(exceptions_test, FileSystemProvider_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the exceptions");
  BOOST_TEST_MESSAGE(" ");

  // Path is not valid
  base_directory = "/tmp/PATH_DOES_NOT_EXIST";
  BOOST_CHECK_THROW( FileSystemProvider fsp (base_directory, std::move(fp)),
                     ElementsException);

  // Path as a file is not valid
  base_directory = base_directory + "filter/MER/Gext_ACSf435w.txt";
  BOOST_CHECK_THROW( FileSystemProvider fsp (base_directory, std::move(fp)),
                     ElementsException);

  // Fill up a new file with dataset name already existing
  // We must have only unique qualify name
  std::ofstream file3_mer("/tmp/euclid/filter/MER/file3.txt");
  file3_mer << "\n";
  file3_mer << "# Dataset_name_for_file1\n";
  file3_mer << "0.1111 1.0000 \n";
  file3_mer.close();

  BOOST_CHECK_THROW( FileSystemProvider fsp (base_directory, std::move(fp)),
                     ElementsException);

  // Remove file3 to avoid exception in the next test
  removeDir("/tmp/euclid/filter/MER/file3.txt");
}

//-----------------------------------------------------------------------------
//            Test the listContents function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(listContent_test, FileSystemProvider_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the listContents function");
  BOOST_TEST_MESSAGE(" ");

  FileSystemProvider fsp {"/tmp/euclid/", std::move(fp)};

  // Even with two slashes in the group it must work
  group = { "filter/MER//" };
  std::vector<QualifiedName> result_vector = fsp.listContents(group);
  BOOST_CHECK_EQUAL(2, result_vector.size());
  BOOST_CHECK(std::find(result_vector.begin(), result_vector.end(), QualifiedName{{"filter","MER"},"Dataset_name_for_file1"})!=result_vector.end());
  BOOST_CHECK(std::find(result_vector.begin(), result_vector.end(), QualifiedName{{"filter","MER"},"file2"})!=result_vector.end());

  // With this group the vector must be empty
  group = { "MER" };
  std::vector<QualifiedName> result_vector2 = fsp.listContents(group);
  BOOST_CHECK_EQUAL(0, result_vector2.size());

}

//-----------------------------------------------------------------------------
//            Test the listContents function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getDataset_test, FileSystemProvider_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the getDataset function");
  BOOST_TEST_MESSAGE(" ");

  FileSystemProvider fsp {"/tmp/euclid/", std::move(fp)};

  // Check a no null pointer must be return
  QualifiedName identifier {{"filter","MER"},"Dataset_name_for_file1"};
  std::unique_ptr<XYDataset::XYDataset> dataset_ptr = fsp.getDataset(identifier);

  BOOST_CHECK(dataset_ptr);

  // Check a nullptr must be returned
  identifier = QualifiedName{{"filter"},"DOES_NOT_EXIST"};
  dataset_ptr = fsp.getDataset(identifier);

  BOOST_CHECK(!dataset_ptr);

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
