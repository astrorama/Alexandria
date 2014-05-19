/**
 * @file TableFixture.h
 *
 * @date May 16, 2014
 * @author Pierre Dubath
 */

#ifndef TABLEFIXTURE_H_
#define TABLEFIXTURE_H_

#include <memory>
#include <vector>
#include <utility>
//#include "ChCatalog/Source.h"
//#include "ChCatalog/SourceAttributes/Photometry.h"
//#include "ChCatalog/SourceAttributes/Coordinates.h"
//#include "ChCatalog/SourceAttributes/SpectroscopicRedshift.h"
#include "ChCatalog/FilterName.h"
#include "ChTable/Row.h"
#include "ChTable/Table.h"
#include "ChTable/ColumnInfo.h"


using namespace ChCatalog;
using namespace std;

struct TableFixture {

  double tolerance = 1e-12;

  string source_id_name = "Test_source_id";

  // A test table with two flux columns and two rows
  const vector<ChTable::ColumnInfo::info_type> info_list {
      ChTable::ColumnInfo::info_type(source_id_name, typeid(int64_t)),
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

  int64_t source_id_1 {756330785};
  int64_t source_id_2 {127548910};

  double flux1_row1 = 1.12345e-12;
  double flux2_row1 = 1.12345e-1;
  double error1_row1 = 1.12345e-18;
  double error2_row1 = 1.1e-2;

  const vector<ChTable::Row::cell_type> values0 {source_id_1, true, 1, int64_t{123}, 0.F, 0., 0., 0., 0., string{"first"}};
  const ChTable::Row row0 {values0, column_info_ptr};
  const vector<ChTable::Row::cell_type> values1 {source_id_2, false, 12345, int64_t{123456789}, 2.3e-2F, flux1_row1, flux2_row1, error1_row1, error2_row1, string{"second"}};
  const ChTable::Row row1 {values1, column_info_ptr};
  const vector<ChTable::Row> row_list {row0, row1};
  const ChTable::Table table {row_list};

  // Two filter names
  const ChCatalog::FilterName v_filter_name {"TestGroup", "VtestName"};
  const ChCatalog::FilterName r_filter_name {"TestGroup", "RtestName"};

  // the mapping variable
  map<FilterName, pair<string, string>> filter_name_mapping;


  TableFixture() {
    // This is how the mapping must be defined
     filter_name_mapping[v_filter_name] = make_pair<string, string>("Double_flux1","Double_error1");
     filter_name_mapping[r_filter_name] = make_pair<string, string>("Double_flux2","Double_error2");
  }
  ~TableFixture() {
    // teardown
  }

};

#endif // TABLEFIXTURE_H_ 
