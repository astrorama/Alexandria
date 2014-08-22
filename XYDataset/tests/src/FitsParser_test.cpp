/**
 * @file tests/src/FitsParser_test.cpp
 *
 * @date May 19, 2014
 * @author Nicolas Morisset
 */

#include <iostream>
#include <fstream>
#include <string>
#include <memory>

#include <boost/test/unit_test.hpp>
#include <boost/filesystem.hpp>

#include "ElementsKernel/ElementsException.h"
#include "ElementsKernel/Temporary.h"
#include <CCfits/CCfits>
#include "ChTable/FitsReader.h"
#include "XYDataset/FitsParser.h"
#include "XYDataset/XYDataset.h"

using namespace Euclid::XYDataset;


CCfits::Table* addTable(CCfits::FITS& fits) {
  std::vector<std::string> names {"X","Y"};
  std::vector<std::string> types {"D","D"};
  CCfits::Table* table_hdu = fits.addTable("extension", 2, names, types);
  std::vector<double> x_values {3.4f, 2.1e-3f};
  table_hdu->column(1).write(x_values, 1);
  std::vector<double> y_values {3.4, 2.1e-13};
  table_hdu->column(2).write(y_values, 1);
  table_hdu->addKey("dataset", "TEST_NAME","Dataset name");
  return table_hdu;
}

struct FitsParser_Fixture {
  TempDir temp_dir;
  std::string fits_file        = temp_dir.path().native()+"/FitsParser_test.fits";
  std::string fits_nodata_file = temp_dir.path().native()+"/FitsParser_nodata_test.fits";


  FitsParser_Fixture() {
    std::unique_ptr<CCfits::FITS> fits { new CCfits::FITS("!"+fits_file, CCfits::RWmode::Write) };
    addTable(*fits);
    std::unique_ptr<CCfits::FITS> fits_nodata { new CCfits::FITS("!"+fits_nodata_file, CCfits::RWmode::Write) };
 }
  ~FitsParser_Fixture() {

  }

};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (FitsParser_test)

//-----------------------------------------------------------------------------
// Test the exception of the getName function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(exception_getName_function_test, FitsParser_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the exception of getName function");
  BOOST_TEST_MESSAGE(" ");

  FitsParser parser{};

  BOOST_CHECK_THROW(parser.getName("File_does_not_exist.fits"), ElementsException);
}

//-----------------------------------------------------------------------------
// Test of the getName function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getName_function_test, FitsParser_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the exception of getName function");
  BOOST_TEST_MESSAGE(" ");

  // The dataset is the correct name, result: Keyword value
  FitsParser fits_parser {"DATASET"};

  BOOST_CHECK_EQUAL("TEST_NAME", fits_parser.getName(fits_file));

  // The dataset name does not exist, result: file name
  fits_parser = FitsParser{"DATASET_NOT_EXISTING"};

  BOOST_CHECK_EQUAL("FitsParser_test", fits_parser.getName(fits_file));
}

//-----------------------------------------------------------------------------
// Test the getDataset function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getDataset_function_test, FitsParser_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the getDataset function");
  BOOST_TEST_MESSAGE(" ");

  FitsParser fits_parser {"TEST_NAME"};
  auto xy_ptr = fits_parser.getDataset(fits_file);
  BOOST_CHECK_EQUAL(xy_ptr->size(), 2);

  // Catch exception if FITS file incorrect
  FitsParser fits_parser_nodata { };

  BOOST_CHECK_THROW(fits_parser_nodata.getDataset(fits_nodata_file), ElementsException);

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


