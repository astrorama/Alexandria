/*
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
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
 * @file tests/src/TableFixture.h
 *
 * @date May 16, 2014
 * @author Pierre Dubath
 */

#ifndef TABLEFIXTURE_H_
#define TABLEFIXTURE_H_

#include "Table/ColumnInfo.h"
#include "Table/Row.h"
#include "Table/Table.h"
#include <cfloat>
#include <cmath>
#include <memory>
#include <utility>
#include <vector>

namespace Euclid {
namespace SourceCatalog {

struct TableFixture {
  double tolerance = 1e-12;

  std::string source_id_name      = "Test_source_id";
  std::string source_id_str_name  = "Test_source_id_str";
  std::string spec_z_val_col_name = "SpecZval";
  std::string spec_z_err_col_name = "SpecZerr";

  // A test table with two flux columns and two rows
  const std::vector<Euclid::Table::ColumnInfo::info_type> info_list{
      Euclid::Table::ColumnInfo::info_type(source_id_name, typeid(int64_t)),
      Euclid::Table::ColumnInfo::info_type(source_id_str_name, typeid(std::string), 3),
      Euclid::Table::ColumnInfo::info_type("Boolean", typeid(bool)),
      Euclid::Table::ColumnInfo::info_type("Integer", typeid(int32_t)),
      Euclid::Table::ColumnInfo::info_type("Long", typeid(int64_t)),
      Euclid::Table::ColumnInfo::info_type("Float", typeid(float)),
      Euclid::Table::ColumnInfo::info_type("Double_flux1", typeid(double)),
      Euclid::Table::ColumnInfo::info_type("Double_flux2", typeid(double)),
      Euclid::Table::ColumnInfo::info_type("Double_error1", typeid(double)),
      Euclid::Table::ColumnInfo::info_type("Double_error2", typeid(double)),
      Euclid::Table::ColumnInfo::info_type("String", typeid(std::string)),
      Euclid::Table::ColumnInfo::info_type(spec_z_val_col_name, typeid(double)),
      Euclid::Table::ColumnInfo::info_type(spec_z_err_col_name, typeid(double))};
  const std::shared_ptr<Euclid::Table::ColumnInfo> column_info_ptr{new Euclid::Table::ColumnInfo{info_list}};

  int64_t source_id_1{756330785};
  int64_t source_id_2{127548910};

  std::string source_str_id_1{"ID0"};
  std::string source_str_id_2{"ID1"};

  double flux1_row1  = 1.12345e-12;
  double flux2_row1  = 1.12345e-1;
  double error1_row1 = 1.12345e-18;
  double error2_row1 = 1.1e-2;

  double spec_z_val_row0 = 0.234657;
  double spec_z_err_row0 = 0.089757;
  double spec_z_val_row1 = 0.1296457;
  double spec_z_err_row1 = 0.003647;

  const std::vector<Euclid::Table::Row::cell_type> values0{
      source_id_1,          source_str_id_1, true,           1, int64_t{123}, 0.F, 0.1, 0.2, 0.3, 0.4,
      std::string{"first"}, spec_z_val_row0, spec_z_err_row0};
  const Euclid::Table::Row row0{values0, column_info_ptr};

  const std::vector<Euclid::Table::Row::cell_type> values1{
      source_id_2,    source_str_id_2, false,       12345,       int64_t{123456789},    2.3e-2F,
      flux1_row1,     flux2_row1,      error1_row1, error2_row1, std::string{"second"}, spec_z_val_row1,
      spec_z_err_row1};
  const Euclid::Table::Row row1{values1, column_info_ptr};

  const std::vector<Euclid::Table::Row> row_list{row0, row1};
  const Euclid::Table::Table            table{row_list};

  const std::vector<Euclid::Table::Row::cell_type> values2{
      int64_t(999),         std::string{"ID2"}, true,           1, int64_t{123}, 0.F, -1., 3., 0.5, 0.3,
      std::string{"first"}, spec_z_val_row0,    spec_z_err_row0};
  const Euclid::Table::Row row_neg_flux{values2, column_info_ptr};

  const std::vector<Euclid::Table::Row::cell_type> values3{
      int64_t(1000),        std::string{"ID3"}, true,           1, int64_t{123}, 0.F, 0., 3., 0.5, 0.3,
      std::string{"first"}, spec_z_val_row0,    spec_z_err_row0};
  const Euclid::Table::Row row_zero_flux{values3, column_info_ptr};

  const std::vector<Euclid::Table::Row::cell_type> values4{
      int64_t(1001),        std::string{"ID4"}, true,           1, int64_t{123}, 0.F, 1., 3., 0.5, 0.3,
      std::string{"first"}, spec_z_val_row0,    spec_z_err_row0};
  const Euclid::Table::Row row_nominal_case{values4, column_info_ptr};

  const std::vector<Euclid::Table::Row::cell_type> values5{
      int64_t(1002),        std::string{"ID5"}, true,           1, int64_t{123}, 0.F, -99., 3., 0.5, 0.3,
      std::string{"first"}, spec_z_val_row0,    spec_z_err_row0};
  const Euclid::Table::Row row_flag_flux{values5, column_info_ptr};

  const std::vector<Euclid::Table::Row::cell_type> values6{
      int64_t(1005),        std::string{"ID6"}, true,           1, int64_t{123}, 0.F, 1., 3., -0.5, 0.3,
      std::string{"first"}, spec_z_val_row0,    spec_z_err_row0};
  const Euclid::Table::Row row_neg_error{values6, column_info_ptr};

  const std::vector<Euclid::Table::Row::cell_type> values7{
      int64_t(1006),        std::string{"ID7"}, true,           1, int64_t{123}, 0.F, 1., 3., 0., 0.3,
      std::string{"first"}, spec_z_val_row0,    spec_z_err_row0};
  const Euclid::Table::Row row_zero_error{values7, column_info_ptr};

  const std::vector<Euclid::Table::Row::cell_type> values8{
      int64_t(1007),        std::string{"ID8"}, true,           1, int64_t{123}, 0.F, -99., 3., -0.5, 0.3,
      std::string{"first"}, spec_z_val_row0,    spec_z_err_row0};
  const Euclid::Table::Row row_flag_flux_neg_error{values8, column_info_ptr};

  const std::vector<Euclid::Table::Row::cell_type> values9{
      int64_t(1008),        std::string{"ID9"}, true,           1, int64_t{123}, 0.F, -99., 3., 0., 0.3,
      std::string{"first"}, spec_z_val_row0,    spec_z_err_row0};
  const Euclid::Table::Row row_flag_flux_zero_error{values9, column_info_ptr};

  const std::vector<Euclid::Table::Row::cell_type> values10{
      int64_t(1009),        std::string{"ID10"}, true,           1, int64_t{123}, 0.F, 0., 3., -0.5, 0.3,
      std::string{"first"}, spec_z_val_row0,     spec_z_err_row0};
  const Euclid::Table::Row row_zero_flux_neg_error{values10, column_info_ptr};

  const std::vector<Euclid::Table::Row::cell_type> values10b{
      int64_t(1009),        std::string{"ID10b"}, true,           1, int64_t{123}, 0.F, 1., 3., -0.5, 0.3,
      std::string{"first"}, spec_z_val_row0,      spec_z_err_row0};
  const Euclid::Table::Row row_1_flux_neg_error{values10b, column_info_ptr};

  const std::vector<Euclid::Table::Row::cell_type> values11{
      int64_t(1010),        std::string{"ID11"}, true,           1, int64_t{123}, 0.F, -1., 3., -0.5, 0.3,
      std::string{"first"}, spec_z_val_row0,     spec_z_err_row0};
  const Euclid::Table::Row row_neg_flux_neg_error{values11, column_info_ptr};

  const std::vector<Euclid::Table::Row::cell_type> values12{
      int64_t(1011),        std::string{"ID12"}, true,           1, int64_t{123}, 0.F, 1., 3., -99., -99.,
      std::string{"first"}, spec_z_val_row0,     spec_z_err_row0};
  const Euclid::Table::Row row_neg_error_flag{values12, column_info_ptr};

  const std::vector<Euclid::Table::Row::cell_type> values13{int64_t(1012),
                                                            std::string{"ID13"},
                                                            true,
                                                            1,
                                                            int64_t{123},
                                                            0.F,
                                                            std::numeric_limits<double>::quiet_NaN(),
                                                            3.,
                                                            0.5,
                                                            0.3,
                                                            std::string{"first"},
                                                            spec_z_val_row0,
                                                            spec_z_err_row0};
  const Euclid::Table::Row                         row_nan_flux{values13, column_info_ptr};

  // Two filter names
  const std::string v_filter_name{"TestGroup/VtestName"};
  const std::string r_filter_name{"TestGroup/RtestName"};

  // the mapping variable
  std::vector<std::pair<std::string, std::pair<std::string, std::string>>> filter_name_mapping;
  std::vector<std::pair<std::string, float>>                               threshold_mapping;

  TableFixture() {
    // This is how the mapping must be defined
    filter_name_mapping.push_back(make_pair(v_filter_name, std::make_pair("Double_flux1", "Double_error1")));
    filter_name_mapping.push_back(make_pair(r_filter_name, std::make_pair("Double_flux2", "Double_error2")));

    threshold_mapping.push_back(std::make_pair(v_filter_name, 3.0));
    threshold_mapping.push_back(std::make_pair(r_filter_name, 5.0));
  }

  ~TableFixture() = default;
};

}  // end of namespace SourceCatalog
}  // end of namespace Euclid

#endif  // TABLEFIXTURE_H_
