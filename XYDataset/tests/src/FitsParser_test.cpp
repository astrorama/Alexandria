/**
 * @file FitsParser_test.cpp
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
#include <CCfits/CCfits>
#include "ChTable/FitsReader.h"
#include "XYDataset/FitsParser.h"
#include "XYDataset/XYDataset.h"

using namespace XYDataset;


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
  std::string fits_file = "/tmp/FitsParser_test.fits";
  std::unique_ptr<CCfits::FITS> fits { new CCfits::FITS("!"+fits_file, CCfits::RWmode::Write) };
  CCfits::ExtHDU* table_hdu = addTable(*fits);


  FitsParser_Fixture() {
  }
  ~FitsParser_Fixture() {

  }


};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (FitsParser_test)

//-----------------------------------------------------------------------------
// Test of the getName function
//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(getName_function_test, FitsParser_Fixture) {

  BOOST_TEST_MESSAGE(" ");
  BOOST_TEST_MESSAGE("--> Testing the exception of getName function");
  BOOST_TEST_MESSAGE(" ");

  FitsParser fits_parser {"TEST_NAME"};
std::cout<<"fits_file "<< fits_file<<" getname_result "<<fits_parser.getName(fits_file)<<std::endl;

// BOOST_CHECK_EQUAL("TEST_NAME", fits_parser.getName(fits_file));
}

//-----------------------------------------------------------------------------
// Test the getDataset function
//-----------------------------------------------------------------------------

//BOOST_FIXTURE_TEST_CASE(getDataset_function_test, FitsParser_Fixture) {
//
//  BOOST_TEST_MESSAGE(" ");
//  BOOST_TEST_MESSAGE("--> Testing the getDataset function");
//  BOOST_TEST_MESSAGE(" ");
//
//  FitsParser fits_parser {"TEST_NAME"};
//  auto xy_ptr = fits_parser.getDataset(fits_file);
//  BOOST_CHECK_EQUAL(xy_ptr->size(), 2);
//
//}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


