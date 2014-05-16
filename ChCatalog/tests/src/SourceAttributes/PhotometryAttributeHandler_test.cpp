/**
 * @file PhotometryAttributeHandler_test.cpp
 *
 * @date Apr 17, 2014
 * @author Pierre Dubath
 */

#include <boost/test/unit_test.hpp>
#include <memory>
#include <map>
#include "ChCatalog/SourceAttributes/PhotometryAttributeFromTable.h"
#include "ChCatalog/SourceAttributes/Photometry.h"
#include "ElementsKernel/ElementsException.h"
#include "ChCatalog/AttributeFromTable.h"
//#include "ChCatalog/Catalog.h"
#include "ChCatalog/FilterName.h"
#include "ChTable/ColumnInfo.h"

using namespace ChCatalog;
using namespace std;

//template<typename Derived, typename Base>
// unique_ptr<Derived>
// static_unique_ptr_cast( unique_ptr<Base>&& p )
// {
//     auto d = static_cast<Derived *>(p.release());
//     return unique_ptr<Derived>(d);
// }


struct PhotometryAttributeFromTableFix {

  double tolerance = 1e-12;

  // A test table with two flux columns and two rows
  const vector<ChTable::ColumnInfo::info_type> info_list {
      ChTable::ColumnInfo::info_type("Boolean", typeid(bool)),
      ChTable::ColumnInfo::info_type("Integer", typeid(int32_t)),
      ChTable::ColumnInfo::info_type("Long", typeid(int64_t)),
      ChTable::ColumnInfo::info_type("Float", typeid(float)),
      ChTable::ColumnInfo::info_type("Double_flux1", typeid(double)),
      ChTable::ColumnInfo::info_type("Double_flux2", typeid(double)),
      ChTable::ColumnInfo::info_type("Double_error1", typeid(double)),
      ChTable::ColumnInfo::info_type("Double_error2", typeid(double)),
      ChTable::ColumnInfo::info_type("String", typeid(string))
  };
  const shared_ptr<ChTable::ColumnInfo> column_info_ptr {new ChTable::ColumnInfo {info_list}};

  double flux1row1 = 1.12345e-12;
  double flux2row1 = 1.12345e-1;
  double error1row1 = 1.12345e-18;
  double error2row1 = 1.1e-2;

  const vector<ChTable::Row::cell_type> values0 {true, 1, int64_t{123}, 0.F, 0., 0., 0., 0., string{"first"}};
  const ChTable::Row row0 {values0, column_info_ptr};
  const vector<ChTable::Row::cell_type> values1 {false, 12345, int64_t{123456789}, 2.3e-2F, flux1row1, flux2row1, error1row1, error2row1, string{"second"}};
  const ChTable::Row row1 {values1, column_info_ptr};
  const vector<ChTable::Row> row_list {row0, row1};
  const ChTable::Table table {row_list};

  // Two filter names
  const ChCatalog::FilterName vFilterName {"TestGroup", "VtestName"};
  const ChCatalog::FilterName rFilterName {"TestGroup", "RtestName"};

  // the mapping variable
  map<FilterName, pair<string, string>> filter_name_mapping;


  PhotometryAttributeFromTableFix() {
    // This is how the mapping must be defined
     filter_name_mapping[vFilterName] = make_pair<string, string>("Double_flux1","Double_error1");
     filter_name_mapping[rFilterName] = make_pair<string, string>("Double_flux2","Double_error2");
  }
  ~PhotometryAttributeFromTableFix() {
    // teardown
  }
};

//-----------------------------------------------------------------------------
//

BOOST_AUTO_TEST_SUITE (PhotometryAttributeFromTable_test)

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( constructor_test, PhotometryAttributeFromTableFix ) {

  BOOST_TEST_MESSAGE("--> constructor test ");

  PhotometryAttributeFromTable pah {column_info_ptr, filter_name_mapping};

  map<ChCatalog::FilterName, pair<size_t, size_t>> map = pah.getFilterIndexMapping();
  BOOST_CHECK_EQUAL(map[vFilterName].first, 4);
  BOOST_CHECK_EQUAL(map[vFilterName].second, 6);
  BOOST_CHECK_EQUAL(map[rFilterName].first, 5);
  BOOST_CHECK_EQUAL(map[rFilterName].second, 7);
}

//-----------------------------------------------------------------------------

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE( createAttribute_test, PhotometryAttributeFromTableFix ) {

  BOOST_TEST_MESSAGE("--> createAttribute test ");

  PhotometryAttributeFromTable pah {column_info_ptr, filter_name_mapping};

  unique_ptr<ChCatalog::Attribute> attribute_ptr = pah.createAttribute(row1);

  BOOST_CHECK( typeid(*attribute_ptr) == typeid(ChCatalog::Photometry) );

  if(typeid(*attribute_ptr) == typeid(ChCatalog::Photometry)) {
      ChCatalog::Photometry& photometry = dynamic_cast<ChCatalog::Photometry&>( *attribute_ptr );
      BOOST_CHECK_CLOSE(photometry.find(vFilterName)->flux, flux1row1, tolerance);
      BOOST_CHECK_CLOSE(photometry.find(vFilterName)->error, error1row1, tolerance);
      BOOST_CHECK_CLOSE(photometry.find(rFilterName)->flux, flux2row1, tolerance);
      BOOST_CHECK_CLOSE(photometry.find(rFilterName)->error, error2row1, tolerance);
  }
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


