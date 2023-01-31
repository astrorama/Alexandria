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
 * @file tests/src/CastVisitor_test.cpp
 * @date 05/09/16
 * @author nikoapos
 */

#include <cstdint>
#include <boost/test/unit_test.hpp>

#include "Table/CastVisitor.h"
#include "Table/Row.h"

using namespace Euclid::Table;

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(CastVisitor_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(castToString) {

  // Given
  Row::cell_type string_cell        = std::string{"text"};
  Row::cell_type double_cell        = 12.345;
  Row::cell_type float_cell         = 12.34F;
  Row::cell_type long_cell          = std::int64_t{12345};
  Row::cell_type int_cell           = std::int32_t{1234};
  Row::cell_type bool_cell          = true;
  Row::cell_type vector_double_cell = std::vector<double>{1.23, 4.56, 7.89};
  Row::cell_type vector_float_cell  = std::vector<float>{1.2, 3.4, 5.6, 7.8};
  Row::cell_type vector_long_cell   = std::vector<std::int64_t>{123, 456, 789};
  Row::cell_type vector_int_cell    = std::vector<std::int32_t>{12, 34, 56, 78};
  Row::cell_type vector_bool_cell   = std::vector<bool>{true, false, true};

  // When
  CastVisitor<std::string> cast{};
  auto                     string_res        = boost::apply_visitor(cast, string_cell);
  auto                     double_res        = boost::apply_visitor(cast, double_cell);
  auto                     float_res         = boost::apply_visitor(cast, float_cell);
  auto                     long_res          = boost::apply_visitor(cast, long_cell);
  auto                     int_res           = boost::apply_visitor(cast, int_cell);
  auto                     bool_res          = boost::apply_visitor(cast, bool_cell);
  auto                     vector_double_res = boost::apply_visitor(cast, vector_double_cell);
  auto                     vector_float_res  = boost::apply_visitor(cast, vector_float_cell);
  auto                     vector_long_res   = boost::apply_visitor(cast, vector_long_cell);
  auto                     vector_int_res    = boost::apply_visitor(cast, vector_int_cell);
  auto                     vector_bool_res   = boost::apply_visitor(cast, vector_bool_cell);

  // Then
  BOOST_CHECK_EQUAL(typeid(string_res).name(), typeid(std::string).name());
  BOOST_CHECK_EQUAL(string_res, "text");
  BOOST_CHECK_EQUAL(typeid(double_res).name(), typeid(std::string).name());
  BOOST_CHECK_EQUAL(double_res, "12.345");
  BOOST_CHECK_EQUAL(typeid(float_res).name(), typeid(std::string).name());
  BOOST_CHECK_EQUAL(float_res, "12.34");
  BOOST_CHECK_EQUAL(typeid(long_res).name(), typeid(std::string).name());
  BOOST_CHECK_EQUAL(long_res, "12345");
  BOOST_CHECK_EQUAL(typeid(int_res).name(), typeid(std::string).name());
  BOOST_CHECK_EQUAL(int_res, "1234");
  BOOST_CHECK_EQUAL(typeid(bool_res).name(), typeid(std::string).name());
  BOOST_CHECK_EQUAL(bool_res, "1");
  BOOST_CHECK_EQUAL(typeid(vector_double_res).name(), typeid(std::string).name());
  BOOST_CHECK_EQUAL(vector_double_res, "1.23,4.56,7.89");
  BOOST_CHECK_EQUAL(typeid(vector_float_res).name(), typeid(std::string).name());
  BOOST_CHECK_EQUAL(vector_float_res, "1.2,3.4,5.6,7.8");
  BOOST_CHECK_EQUAL(typeid(vector_long_res).name(), typeid(std::string).name());
  BOOST_CHECK_EQUAL(vector_long_res, "123,456,789");
  BOOST_CHECK_EQUAL(typeid(vector_int_res).name(), typeid(std::string).name());
  BOOST_CHECK_EQUAL(vector_int_res, "12,34,56,78");
  BOOST_CHECK_EQUAL(typeid(vector_bool_res).name(), typeid(std::string).name());
  BOOST_CHECK_EQUAL(vector_bool_res, "1,0,1");
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(castToDouble) {

  // Given
  Row::cell_type string_cell          = std::string{"12.345"};
  Row::cell_type double_cell          = 12.345;
  Row::cell_type float_cell           = 12.34F;
  Row::cell_type long_cell            = std::int64_t{12345};
  Row::cell_type int_cell             = std::int32_t{1234};
  Row::cell_type bool_cell            = true;
  Row::cell_type vector_double_cell   = std::vector<double>{1.23, 4.56, 7.89};
  Row::cell_type vector_float_cell    = std::vector<float>{1.2, 3.4, 5.6, 7.8};
  Row::cell_type vector_long_cell     = std::vector<std::int64_t>{123, 456, 789};
  Row::cell_type vector_int_cell      = std::vector<std::int32_t>{12, 34, 56, 78};
  Row::cell_type vector_bool_cell     = std::vector<bool>{true, false, true};
  Row::cell_type bad_string_cell      = std::string{"str12.345"};
  Row::cell_type overflow_string_cell = std::string{"1.79e+400"};
  Row::cell_type big_string_cell      = std::string{"3.40282e+40"};

  // When
  CastVisitor<double> cast{};
  auto                string_res = boost::apply_visitor(cast, string_cell);
  auto                double_res = boost::apply_visitor(cast, double_cell);
  auto                float_res  = boost::apply_visitor(cast, float_cell);
  auto                long_res   = boost::apply_visitor(cast, long_cell);
  auto                int_res    = boost::apply_visitor(cast, int_cell);
  auto                bool_res   = boost::apply_visitor(cast, bool_cell);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_double_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_float_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_long_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_int_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_bool_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, bad_string_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, overflow_string_cell), Elements::Exception);
  auto big_string_res = boost::apply_visitor(cast, big_string_cell);

  // Then
  BOOST_CHECK_EQUAL(typeid(string_res).name(), typeid(double).name());
  BOOST_CHECK_EQUAL(string_res, 12.345);
  BOOST_CHECK_EQUAL(typeid(double_res).name(), typeid(double).name());
  BOOST_CHECK_EQUAL(double_res, 12.345);
  BOOST_CHECK_EQUAL(typeid(float_res).name(), typeid(double).name());
  BOOST_CHECK_EQUAL(float_res, 12.34F);
  BOOST_CHECK_EQUAL(typeid(long_res).name(), typeid(double).name());
  BOOST_CHECK_EQUAL(long_res, 12345);
  BOOST_CHECK_EQUAL(typeid(int_res).name(), typeid(double).name());
  BOOST_CHECK_EQUAL(int_res, 1234);
  BOOST_CHECK_EQUAL(typeid(bool_res).name(), typeid(double).name());
  BOOST_CHECK_EQUAL(bool_res, 1);
  BOOST_CHECK_EQUAL(typeid(big_string_res).name(), typeid(double).name());
  BOOST_CHECK_EQUAL(big_string_res, 3.40282e+40);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(castToFloat) {

  // Given
  Row::cell_type string_cell          = std::string{"12.345"};
  Row::cell_type double_cell          = 12.345;
  Row::cell_type float_cell           = 12.34F;
  Row::cell_type long_cell            = std::int64_t{12345};
  Row::cell_type int_cell             = std::int32_t{1234};
  Row::cell_type bool_cell            = true;
  Row::cell_type vector_double_cell   = std::vector<double>{1.23, 4.56, 7.89};
  Row::cell_type vector_float_cell    = std::vector<float>{1.2, 3.4, 5.6, 7.8};
  Row::cell_type vector_long_cell     = std::vector<std::int64_t>{123, 456, 789};
  Row::cell_type vector_int_cell      = std::vector<std::int32_t>{12, 34, 56, 78};
  Row::cell_type vector_bool_cell     = std::vector<bool>{true, false, true};
  Row::cell_type bad_string_cell      = std::string{"str12.345"};
  Row::cell_type overflow_string_cell = std::string{"3.40282e+40"};

  // When
  CastVisitor<float> cast{};
  auto               string_res = boost::apply_visitor(cast, string_cell);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, double_cell), Elements::Exception);
  auto float_res = boost::apply_visitor(cast, float_cell);
  auto long_res  = boost::apply_visitor(cast, long_cell);
  auto int_res   = boost::apply_visitor(cast, int_cell);
  auto bool_res  = boost::apply_visitor(cast, bool_cell);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_double_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_float_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_long_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_int_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_bool_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, bad_string_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, overflow_string_cell), Elements::Exception);

  // Then
  BOOST_CHECK_EQUAL(typeid(string_res).name(), typeid(float).name());
  BOOST_CHECK_EQUAL(string_res, 12.345F);
  BOOST_CHECK_EQUAL(typeid(float_res).name(), typeid(float).name());
  BOOST_CHECK_EQUAL(float_res, 12.34F);
  BOOST_CHECK_EQUAL(typeid(long_res).name(), typeid(float).name());
  BOOST_CHECK_EQUAL(long_res, 12345);
  BOOST_CHECK_EQUAL(typeid(int_res).name(), typeid(float).name());
  BOOST_CHECK_EQUAL(int_res, 1234);
  BOOST_CHECK_EQUAL(typeid(bool_res).name(), typeid(float).name());
  BOOST_CHECK_EQUAL(bool_res, 1);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(castToInt64) {

  // Given
  Row::cell_type string_cell        = std::string{"12345"};
  Row::cell_type double_cell        = 12.345;
  Row::cell_type float_cell         = 12.34F;
  Row::cell_type long_cell          = std::int64_t{12345};
  Row::cell_type int_cell           = std::int32_t{1234};
  Row::cell_type bool_cell          = true;
  Row::cell_type vector_double_cell = std::vector<double>{1.23, 4.56, 7.89};
  Row::cell_type vector_float_cell  = std::vector<float>{1.2, 3.4, 5.6, 7.8};
  Row::cell_type vector_long_cell   = std::vector<std::int64_t>{123, 456, 789};
  Row::cell_type vector_int_cell    = std::vector<std::int32_t>{12, 34, 56, 78};
  Row::cell_type vector_bool_cell   = std::vector<bool>{true, false, true};
  Row::cell_type bad_string_cell    = std::string{"str12345"};
  Row::cell_type long_string_cell   = std::string{"8589934592"};
  Row::cell_type long2_string_cell  = std::string{"-2147483650"};

  // When
  CastVisitor<int64_t> cast{};
  auto                 string_res = boost::apply_visitor(cast, string_cell);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, double_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, float_cell), Elements::Exception);
  auto long_res = boost::apply_visitor(cast, long_cell);
  auto int_res  = boost::apply_visitor(cast, int_cell);
  auto bool_res = boost::apply_visitor(cast, bool_cell);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_double_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_float_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_long_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_int_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_bool_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, bad_string_cell), Elements::Exception);
  auto long_string_res  = boost::apply_visitor(cast, long_string_cell);
  auto long2_string_res = boost::apply_visitor(cast, long2_string_cell);

  // Then
  BOOST_CHECK_EQUAL(typeid(string_res).name(), typeid(int64_t).name());
  BOOST_CHECK_EQUAL(string_res, 12345);
  BOOST_CHECK_EQUAL(typeid(long_res).name(), typeid(int64_t).name());
  BOOST_CHECK_EQUAL(long_res, 12345);
  BOOST_CHECK_EQUAL(typeid(int_res).name(), typeid(int64_t).name());
  BOOST_CHECK_EQUAL(int_res, 1234);
  BOOST_CHECK_EQUAL(typeid(bool_res).name(), typeid(int64_t).name());
  BOOST_CHECK_EQUAL(bool_res, 1);
  BOOST_CHECK_EQUAL(typeid(long_string_res).name(), typeid(int64_t).name());
  BOOST_CHECK_EQUAL(long_string_res, 8589934592);
  BOOST_CHECK_EQUAL(typeid(long2_string_res).name(), typeid(int64_t).name());
  BOOST_CHECK_EQUAL(long2_string_res, -2147483650);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(castToInt32) {

  // Given
  Row::cell_type string_cell           = std::string{"12345"};
  Row::cell_type double_cell           = 12.345;
  Row::cell_type float_cell            = 12.34F;
  Row::cell_type long_cell             = std::int64_t{12345};
  Row::cell_type int_cell              = std::int32_t{1234};
  Row::cell_type bool_cell             = true;
  Row::cell_type vector_double_cell    = std::vector<double>{1.23, 4.56, 7.89};
  Row::cell_type vector_float_cell     = std::vector<float>{1.2, 3.4, 5.6, 7.8};
  Row::cell_type vector_long_cell      = std::vector<std::int64_t>{123, 456, 789};
  Row::cell_type vector_int_cell       = std::vector<std::int32_t>{12, 34, 56, 78};
  Row::cell_type vector_bool_cell      = std::vector<bool>{true, false, true};
  Row::cell_type bad_string_cell       = std::string{"str12345"};
  Row::cell_type overflow_string_cell  = std::string{"8589934592"};
  Row::cell_type overflow2_string_cell = std::string{"-2147483650"};

  // When
  CastVisitor<int32_t> cast{};
  auto                 string_res = boost::apply_visitor(cast, string_cell);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, double_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, float_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, long_cell), Elements::Exception);
  auto int_res  = boost::apply_visitor(cast, int_cell);
  auto bool_res = boost::apply_visitor(cast, bool_cell);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_double_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_float_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_long_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_int_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_bool_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, overflow_string_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, overflow2_string_cell), Elements::Exception);

  // Then
  BOOST_CHECK_EQUAL(typeid(string_res).name(), typeid(int32_t).name());
  BOOST_CHECK_EQUAL(string_res, 12345);
  BOOST_CHECK_EQUAL(typeid(int_res).name(), typeid(int32_t).name());
  BOOST_CHECK_EQUAL(int_res, 1234);
  BOOST_CHECK_EQUAL(typeid(bool_res).name(), typeid(int32_t).name());
  BOOST_CHECK_EQUAL(bool_res, 1);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(castToDoubleVector) {

  // Given
  Row::cell_type string_cell        = std::string{"1.23,4.56,7.89"};
  Row::cell_type double_cell        = 12.345;
  Row::cell_type float_cell         = 12.34F;
  Row::cell_type long_cell          = std::int64_t{12345};
  Row::cell_type int_cell           = std::int32_t{1234};
  Row::cell_type bool_cell          = true;
  Row::cell_type vector_double_cell = std::vector<double>{1.23, 4.56, 7.89};
  Row::cell_type vector_float_cell  = std::vector<float>{1.2, 3.4, 5.6, 7.8};
  Row::cell_type vector_long_cell   = std::vector<std::int64_t>{123, 456, 789};
  Row::cell_type vector_int_cell    = std::vector<std::int32_t>{12, 34, 56, 78};
  Row::cell_type vector_bool_cell   = std::vector<bool>{true, false, true};

  // When
  CastVisitor<std::vector<double>> cast{};
  auto                             string_res        = boost::apply_visitor(cast, string_cell);
  auto                             double_res        = boost::apply_visitor(cast, double_cell);
  auto                             float_res         = boost::apply_visitor(cast, float_cell);
  auto                             long_res          = boost::apply_visitor(cast, long_cell);
  auto                             int_res           = boost::apply_visitor(cast, int_cell);
  auto                             bool_res          = boost::apply_visitor(cast, bool_cell);
  auto                             vector_double_res = boost::apply_visitor(cast, vector_double_cell);
  auto                             vector_float_res  = boost::apply_visitor(cast, vector_float_cell);
  auto                             vector_long_res   = boost::apply_visitor(cast, vector_long_cell);
  auto                             vector_int_res    = boost::apply_visitor(cast, vector_int_cell);
  auto                             vector_bool_res   = boost::apply_visitor(cast, vector_bool_cell);

  // Then
  BOOST_CHECK_EQUAL(typeid(string_res).name(), typeid(std::vector<double>).name());
  BOOST_CHECK_EQUAL(string_res.size(), 3);
  BOOST_CHECK_EQUAL(string_res[0], 1.23);
  BOOST_CHECK_EQUAL(string_res[1], 4.56);
  BOOST_CHECK_EQUAL(string_res[2], 7.89);
  BOOST_CHECK_EQUAL(typeid(double_res).name(), typeid(std::vector<double>).name());
  BOOST_CHECK_EQUAL(double_res.size(), 1);
  BOOST_CHECK_EQUAL(double_res[0], 12.345);
  BOOST_CHECK_EQUAL(typeid(float_res).name(), typeid(std::vector<double>).name());
  BOOST_CHECK_EQUAL(float_res.size(), 1);
  BOOST_CHECK_EQUAL(float_res[0], 12.34F);
  BOOST_CHECK_EQUAL(typeid(long_res).name(), typeid(std::vector<double>).name());
  BOOST_CHECK_EQUAL(long_res.size(), 1);
  BOOST_CHECK_EQUAL(long_res[0], 12345);
  BOOST_CHECK_EQUAL(typeid(int_res).name(), typeid(std::vector<double>).name());
  BOOST_CHECK_EQUAL(int_res.size(), 1);
  BOOST_CHECK_EQUAL(int_res[0], 1234);
  BOOST_CHECK_EQUAL(typeid(bool_res).name(), typeid(std::vector<double>).name());
  BOOST_CHECK_EQUAL(bool_res.size(), 1);
  BOOST_CHECK_EQUAL(bool_res[0], 1);
  BOOST_CHECK_EQUAL(typeid(vector_double_res).name(), typeid(std::vector<double>).name());
  BOOST_CHECK_EQUAL(vector_double_res.size(), 3);
  BOOST_CHECK_EQUAL(vector_double_res[0], 1.23);
  BOOST_CHECK_EQUAL(vector_double_res[1], 4.56);
  BOOST_CHECK_EQUAL(vector_double_res[2], 7.89);
  BOOST_CHECK_EQUAL(typeid(vector_float_res).name(), typeid(std::vector<double>).name());
  BOOST_CHECK_EQUAL(vector_float_res.size(), 4);
  BOOST_CHECK_EQUAL(vector_float_res[0], 1.2F);
  BOOST_CHECK_EQUAL(vector_float_res[1], 3.4F);
  BOOST_CHECK_EQUAL(vector_float_res[2], 5.6F);
  BOOST_CHECK_EQUAL(vector_float_res[3], 7.8F);
  BOOST_CHECK_EQUAL(typeid(vector_long_res).name(), typeid(std::vector<double>).name());
  BOOST_CHECK_EQUAL(vector_long_res.size(), 3);
  BOOST_CHECK_EQUAL(vector_long_res[0], 123);
  BOOST_CHECK_EQUAL(vector_long_res[1], 456);
  BOOST_CHECK_EQUAL(vector_long_res[2], 789);
  BOOST_CHECK_EQUAL(typeid(vector_int_res).name(), typeid(std::vector<double>).name());
  BOOST_CHECK_EQUAL(vector_int_res.size(), 4);
  BOOST_CHECK_EQUAL(vector_int_res[0], 12);
  BOOST_CHECK_EQUAL(vector_int_res[1], 34);
  BOOST_CHECK_EQUAL(vector_int_res[2], 56);
  BOOST_CHECK_EQUAL(vector_int_res[3], 78);
  BOOST_CHECK_EQUAL(typeid(vector_bool_res).name(), typeid(std::vector<double>).name());
  BOOST_CHECK_EQUAL(vector_bool_res.size(), 3);
  BOOST_CHECK_EQUAL(vector_bool_res[0], 1);
  BOOST_CHECK_EQUAL(vector_bool_res[1], 0);
  BOOST_CHECK_EQUAL(vector_bool_res[2], 1);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(castToFloatVector) {

  // Given
  Row::cell_type string_cell        = std::string{"1.23,4.56,7.89"};
  Row::cell_type double_cell        = 12.345;
  Row::cell_type float_cell         = 12.34F;
  Row::cell_type long_cell          = std::int64_t{12345};
  Row::cell_type int_cell           = std::int32_t{1234};
  Row::cell_type bool_cell          = true;
  Row::cell_type vector_double_cell = std::vector<double>{1.23, 4.56, 7.89};
  Row::cell_type vector_float_cell  = std::vector<float>{1.2, 3.4, 5.6, 7.8};
  Row::cell_type vector_long_cell   = std::vector<std::int64_t>{123, 456, 789};
  Row::cell_type vector_int_cell    = std::vector<std::int32_t>{12, 34, 56, 78};
  Row::cell_type vector_bool_cell   = std::vector<bool>{true, false, true};

  // When
  CastVisitor<std::vector<float>> cast{};
  auto                            string_res = boost::apply_visitor(cast, string_cell);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, double_cell), Elements::Exception);
  auto float_res = boost::apply_visitor(cast, float_cell);
  auto long_res  = boost::apply_visitor(cast, long_cell);
  auto int_res   = boost::apply_visitor(cast, int_cell);
  auto bool_res  = boost::apply_visitor(cast, bool_cell);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_double_cell), Elements::Exception);
  auto vector_float_res = boost::apply_visitor(cast, vector_float_cell);
  auto vector_long_res  = boost::apply_visitor(cast, vector_long_cell);
  auto vector_int_res   = boost::apply_visitor(cast, vector_int_cell);
  auto vector_bool_res  = boost::apply_visitor(cast, vector_bool_cell);

  // Then
  BOOST_CHECK_EQUAL(typeid(string_res).name(), typeid(std::vector<float>).name());
  BOOST_CHECK_EQUAL(string_res.size(), 3);
  BOOST_CHECK_EQUAL(string_res[0], 1.23F);
  BOOST_CHECK_EQUAL(string_res[1], 4.56F);
  BOOST_CHECK_EQUAL(string_res[2], 7.89F);
  BOOST_CHECK_EQUAL(typeid(float_res).name(), typeid(std::vector<float>).name());
  BOOST_CHECK_EQUAL(float_res.size(), 1);
  BOOST_CHECK_EQUAL(float_res[0], 12.34F);
  BOOST_CHECK_EQUAL(typeid(long_res).name(), typeid(std::vector<float>).name());
  BOOST_CHECK_EQUAL(long_res.size(), 1);
  BOOST_CHECK_EQUAL(long_res[0], 12345);
  BOOST_CHECK_EQUAL(typeid(int_res).name(), typeid(std::vector<float>).name());
  BOOST_CHECK_EQUAL(int_res.size(), 1);
  BOOST_CHECK_EQUAL(int_res[0], 1234);
  BOOST_CHECK_EQUAL(typeid(bool_res).name(), typeid(std::vector<float>).name());
  BOOST_CHECK_EQUAL(bool_res.size(), 1);
  BOOST_CHECK_EQUAL(bool_res[0], 1);
  BOOST_CHECK_EQUAL(typeid(vector_float_res).name(), typeid(std::vector<float>).name());
  BOOST_CHECK_EQUAL(vector_float_res.size(), 4);
  BOOST_CHECK_EQUAL(vector_float_res[0], 1.2F);
  BOOST_CHECK_EQUAL(vector_float_res[1], 3.4F);
  BOOST_CHECK_EQUAL(vector_float_res[2], 5.6F);
  BOOST_CHECK_EQUAL(vector_float_res[3], 7.8F);
  BOOST_CHECK_EQUAL(typeid(vector_long_res).name(), typeid(std::vector<float>).name());
  BOOST_CHECK_EQUAL(vector_long_res.size(), 3);
  BOOST_CHECK_EQUAL(vector_long_res[0], 123);
  BOOST_CHECK_EQUAL(vector_long_res[1], 456);
  BOOST_CHECK_EQUAL(vector_long_res[2], 789);
  BOOST_CHECK_EQUAL(typeid(vector_int_res).name(), typeid(std::vector<float>).name());
  BOOST_CHECK_EQUAL(vector_int_res.size(), 4);
  BOOST_CHECK_EQUAL(vector_int_res[0], 12);
  BOOST_CHECK_EQUAL(vector_int_res[1], 34);
  BOOST_CHECK_EQUAL(vector_int_res[2], 56);
  BOOST_CHECK_EQUAL(vector_int_res[3], 78);
  BOOST_CHECK_EQUAL(typeid(vector_bool_res).name(), typeid(std::vector<float>).name());
  BOOST_CHECK_EQUAL(vector_bool_res.size(), 3);
  BOOST_CHECK_EQUAL(vector_bool_res[0], 1);
  BOOST_CHECK_EQUAL(vector_bool_res[1], 0);
  BOOST_CHECK_EQUAL(vector_bool_res[2], 1);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(castToLongVector) {

  // Given
  Row::cell_type string_cell        = std::string{"123,456,789"};
  Row::cell_type double_cell        = 12.345;
  Row::cell_type float_cell         = 12.34F;
  Row::cell_type long_cell          = std::int64_t{12345};
  Row::cell_type int_cell           = std::int32_t{1234};
  Row::cell_type bool_cell          = true;
  Row::cell_type vector_double_cell = std::vector<double>{1.23, 4.56, 7.89};
  Row::cell_type vector_float_cell  = std::vector<float>{1.2, 3.4, 5.6, 7.8};
  Row::cell_type vector_long_cell   = std::vector<std::int64_t>{123, 456, 789};
  Row::cell_type vector_int_cell    = std::vector<std::int32_t>{12, 34, 56, 78};
  Row::cell_type vector_bool_cell   = std::vector<bool>{true, false, true};

  // When
  CastVisitor<std::vector<std::int64_t>> cast{};
  auto                                   string_res = boost::apply_visitor(cast, string_cell);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, double_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, float_cell), Elements::Exception);
  auto long_res = boost::apply_visitor(cast, long_cell);
  auto int_res  = boost::apply_visitor(cast, int_cell);
  auto bool_res = boost::apply_visitor(cast, bool_cell);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_double_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_float_cell), Elements::Exception);
  auto vector_long_res = boost::apply_visitor(cast, vector_long_cell);
  auto vector_int_res  = boost::apply_visitor(cast, vector_int_cell);
  auto vector_bool_res = boost::apply_visitor(cast, vector_bool_cell);

  // Then
  BOOST_CHECK_EQUAL(typeid(string_res).name(), typeid(std::vector<std::int64_t>).name());
  BOOST_CHECK_EQUAL(string_res.size(), 3);
  BOOST_CHECK_EQUAL(string_res[0], 123);
  BOOST_CHECK_EQUAL(string_res[1], 456);
  BOOST_CHECK_EQUAL(string_res[2], 789);
  BOOST_CHECK_EQUAL(typeid(long_res).name(), typeid(std::vector<std::int64_t>).name());
  BOOST_CHECK_EQUAL(long_res.size(), 1);
  BOOST_CHECK_EQUAL(long_res[0], 12345);
  BOOST_CHECK_EQUAL(typeid(int_res).name(), typeid(std::vector<std::int64_t>).name());
  BOOST_CHECK_EQUAL(int_res.size(), 1);
  BOOST_CHECK_EQUAL(int_res[0], 1234);
  BOOST_CHECK_EQUAL(typeid(bool_res).name(), typeid(std::vector<std::int64_t>).name());
  BOOST_CHECK_EQUAL(bool_res.size(), 1);
  BOOST_CHECK_EQUAL(bool_res[0], 1);
  BOOST_CHECK_EQUAL(typeid(vector_long_res).name(), typeid(std::vector<std::int64_t>).name());
  BOOST_CHECK_EQUAL(vector_long_res.size(), 3);
  BOOST_CHECK_EQUAL(vector_long_res[0], 123);
  BOOST_CHECK_EQUAL(vector_long_res[1], 456);
  BOOST_CHECK_EQUAL(vector_long_res[2], 789);
  BOOST_CHECK_EQUAL(typeid(vector_int_res).name(), typeid(std::vector<std::int64_t>).name());
  BOOST_CHECK_EQUAL(vector_int_res.size(), 4);
  BOOST_CHECK_EQUAL(vector_int_res[0], 12);
  BOOST_CHECK_EQUAL(vector_int_res[1], 34);
  BOOST_CHECK_EQUAL(vector_int_res[2], 56);
  BOOST_CHECK_EQUAL(vector_int_res[3], 78);
  BOOST_CHECK_EQUAL(typeid(vector_bool_res).name(), typeid(std::vector<std::int64_t>).name());
  BOOST_CHECK_EQUAL(vector_bool_res.size(), 3);
  BOOST_CHECK_EQUAL(vector_bool_res[0], 1);
  BOOST_CHECK_EQUAL(vector_bool_res[1], 0);
  BOOST_CHECK_EQUAL(vector_bool_res[2], 1);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(castToIntVector) {

  // Given
  Row::cell_type string_cell        = std::string{"123,456,789"};
  Row::cell_type double_cell        = 12.345;
  Row::cell_type float_cell         = 12.34F;
  Row::cell_type long_cell          = std::int64_t{12345};
  Row::cell_type int_cell           = std::int32_t{1234};
  Row::cell_type bool_cell          = true;
  Row::cell_type vector_double_cell = std::vector<double>{1.23, 4.56, 7.89};
  Row::cell_type vector_float_cell  = std::vector<float>{1.2, 3.4, 5.6, 7.8};
  Row::cell_type vector_long_cell   = std::vector<std::int64_t>{123, 456, 789};
  Row::cell_type vector_int_cell    = std::vector<std::int32_t>{12, 34, 56, 78};
  Row::cell_type vector_bool_cell   = std::vector<bool>{true, false, true};

  // When
  CastVisitor<std::vector<std::int32_t>> cast{};
  auto                                   string_res = boost::apply_visitor(cast, string_cell);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, double_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, float_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, long_cell), Elements::Exception);
  auto int_res  = boost::apply_visitor(cast, int_cell);
  auto bool_res = boost::apply_visitor(cast, bool_cell);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_double_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_float_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, vector_long_cell), Elements::Exception);
  auto vector_int_res  = boost::apply_visitor(cast, vector_int_cell);
  auto vector_bool_res = boost::apply_visitor(cast, vector_bool_cell);

  // Then
  BOOST_CHECK_EQUAL(typeid(string_res).name(), typeid(std::vector<std::int32_t>).name());
  BOOST_CHECK_EQUAL(string_res.size(), 3);
  BOOST_CHECK_EQUAL(string_res[0], 123);
  BOOST_CHECK_EQUAL(string_res[1], 456);
  BOOST_CHECK_EQUAL(string_res[2], 789);
  BOOST_CHECK_EQUAL(typeid(int_res).name(), typeid(std::vector<std::int32_t>).name());
  BOOST_CHECK_EQUAL(int_res.size(), 1);
  BOOST_CHECK_EQUAL(int_res[0], 1234);
  BOOST_CHECK_EQUAL(typeid(bool_res).name(), typeid(std::vector<std::int32_t>).name());
  BOOST_CHECK_EQUAL(bool_res.size(), 1);
  BOOST_CHECK_EQUAL(bool_res[0], 1);
  BOOST_CHECK_EQUAL(typeid(vector_int_res).name(), typeid(std::vector<std::int32_t>).name());
  BOOST_CHECK_EQUAL(vector_int_res.size(), 4);
  BOOST_CHECK_EQUAL(vector_int_res[0], 12);
  BOOST_CHECK_EQUAL(vector_int_res[1], 34);
  BOOST_CHECK_EQUAL(vector_int_res[2], 56);
  BOOST_CHECK_EQUAL(vector_int_res[3], 78);
  BOOST_CHECK_EQUAL(typeid(vector_bool_res).name(), typeid(std::vector<std::int32_t>).name());
  BOOST_CHECK_EQUAL(vector_bool_res.size(), 3);
  BOOST_CHECK_EQUAL(vector_bool_res[0], 1);
  BOOST_CHECK_EQUAL(vector_bool_res[1], 0);
  BOOST_CHECK_EQUAL(vector_bool_res[2], 1);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
