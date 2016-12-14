/**
 * @file tests/src/FitsReader_test.cpp
 * @date April 17, 2014
 * @author Nikolaos Apostolakos
 */

#include <memory>
#include <boost/test/unit_test.hpp>
#include <CCfits/CCfits>
#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Temporary.h"
#include "Table/FitsReaderOld.h"

CCfits::Table* addTable(CCfits::FITS& fits) {

  std::vector<std::string> names {"Bool","Int","Long","String","Float","Double","IntVector","DoubleVector"};
  std::vector<std::string> types {"L","J","K","10A","E","D","2J","2D"};
  std::vector<std::string> units {"deg","mag","erg","ph","s","m","pc","count"};
  CCfits::Table* table_hdu = fits.addTable("Success", 2, names, types, units);
  std::vector<bool> bool_values {true, false};
  table_hdu->column(1).write(bool_values, 1);
  std::vector<int32_t> int_values {3, -2346};
  table_hdu->column(2).write(int_values, 1);
  std::vector<int64_t> long_values {123456789, -6};
  table_hdu->column(3).write(long_values, 1);
  std::vector<std::string> string_values {"Small", "1234567890"};
  table_hdu->column(4).write(string_values, 1);
  std::vector<float> float_values {3.4f, 2.1e-3f};
  table_hdu->column(5).write(float_values, 1);
  std::vector<double> double_values {3.4, 2.1e-13};
  table_hdu->column(6).write(double_values, 1);
  std::vector<std::valarray<int32_t>> int_vectors {{1,2}, {3,4}};
  table_hdu->column(7).writeArrays(int_vectors, 1);
  std::vector<std::valarray<double>> double_vectors {{1.1,1.2}, {2.1,2.2}};
  table_hdu->column(8).writeArrays(double_vectors, 1);
  for (int i=1; i<=8; i=i+2) {
    table_hdu->addKey("TDESC" + std::to_string(i), "Desc" + std::to_string(i), "");
  }
  return table_hdu;
}

struct FitsReader_Fixture {
  Elements::TempDir temp_dir;
  std::unique_ptr<CCfits::FITS> fits {new CCfits::FITS(
          (temp_dir.path()/"FitsReader_test.fits").native(), CCfits::RWmode::Write)};
  const CCfits::PHDU& primary_hdu = fits->pHDU();
  std::vector<long> image_size {2,2};
  CCfits::ExtHDU* image_hdu = fits->addImage("Image", FLOAT_IMG, image_size);
  CCfits::ExtHDU* table_hdu = addTable(*fits);
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (AsciiReader_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()
