/*  
 * Copyright (C) 2012-2020 Euclid Science Ground Segment    
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

#include <boost/test/unit_test.hpp>

#include "Table/Row.h"
#include "Table/CastVisitor.h"

using namespace Euclid::Table;

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (CastVisitor_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(castToString) {

  // Given
  Row::cell_type string_cell = std::string{"text"};
  Row::cell_type double_cell = 12.345;
  Row::cell_type float_cell = 12.34F;
  Row::cell_type long_cell = std::int64_t{12345};
  Row::cell_type int_cell = std::int32_t{1234};
  Row::cell_type bool_cell = true;
  
  // When
  CastVisitor<std::string> cast {};
  auto string_res = boost::apply_visitor(cast, string_cell);
  auto double_res = boost::apply_visitor(cast, double_cell);
  auto float_res = boost::apply_visitor(cast, float_cell);
  auto long_res = boost::apply_visitor(cast, long_cell);
  auto int_res = boost::apply_visitor(cast, int_cell);
  auto bool_res = boost::apply_visitor(cast, bool_cell);
  
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

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(castToDouble) {

  // Given
  Row::cell_type string_cell = std::string{"12.345"};
  Row::cell_type double_cell = 12.345;
  Row::cell_type float_cell = 12.34F;
  Row::cell_type long_cell = std::int64_t{12345};
  Row::cell_type int_cell = std::int32_t{1234};
  Row::cell_type bool_cell = true;
  
  // When
  CastVisitor<double> cast {};
  auto string_res = boost::apply_visitor(cast, string_cell);
  auto double_res = boost::apply_visitor(cast, double_cell);
  auto float_res = boost::apply_visitor(cast, float_cell);
  auto long_res = boost::apply_visitor(cast, long_cell);
  auto int_res = boost::apply_visitor(cast, int_cell);
  auto bool_res = boost::apply_visitor(cast, bool_cell);
//  
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

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(castToFloat) {

  // Given
  Row::cell_type string_cell = std::string{"12.345"};
  Row::cell_type double_cell = 12.345;
  Row::cell_type float_cell = 12.34F;
  Row::cell_type long_cell = std::int64_t{12345};
  Row::cell_type int_cell = std::int32_t{1234};
  Row::cell_type bool_cell = true;
  
  // When
  CastVisitor<float> cast {};
  auto string_res = boost::apply_visitor(cast, string_cell);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, double_cell), Elements::Exception);
  auto float_res = boost::apply_visitor(cast, float_cell);
  auto long_res = boost::apply_visitor(cast, long_cell);
  auto int_res = boost::apply_visitor(cast, int_cell);
  auto bool_res = boost::apply_visitor(cast, bool_cell);

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
  Row::cell_type string_cell = std::string{"12345"};
  Row::cell_type double_cell = 12.345;
  Row::cell_type float_cell = 12.34F;
  Row::cell_type long_cell = std::int64_t{12345};
  Row::cell_type int_cell = std::int32_t{1234};
  Row::cell_type bool_cell = true;
  
  // When
  CastVisitor<int64_t> cast {};
  auto string_res = boost::apply_visitor(cast, string_cell);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, double_cell), Elements::Exception);
  BOOST_CHECK_THROW( boost::apply_visitor(cast, float_cell), Elements::Exception);
  auto long_res = boost::apply_visitor(cast, long_cell);
  auto int_res = boost::apply_visitor(cast, int_cell);
  auto bool_res = boost::apply_visitor(cast, bool_cell);

  // Then
  BOOST_CHECK_EQUAL(typeid(string_res).name(), typeid(int64_t).name());
  BOOST_CHECK_EQUAL(string_res, 12345);
  BOOST_CHECK_EQUAL(typeid(long_res).name(), typeid(int64_t).name());
  BOOST_CHECK_EQUAL(long_res, 12345);
  BOOST_CHECK_EQUAL(typeid(int_res).name(), typeid(int64_t).name());
  BOOST_CHECK_EQUAL(int_res, 1234);
  BOOST_CHECK_EQUAL(typeid(bool_res).name(), typeid(int64_t).name());
  BOOST_CHECK_EQUAL(bool_res, 1);

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(castToInt32) {

  // Given
  Row::cell_type string_cell = std::string{"12345"};
  Row::cell_type double_cell = 12.345;
  Row::cell_type float_cell = 12.34F;
  Row::cell_type long_cell = std::int64_t{12345};
  Row::cell_type int_cell = std::int32_t{1234};
  Row::cell_type bool_cell = true;
  
  // When
  CastVisitor<int32_t> cast {};
  auto string_res = boost::apply_visitor(cast, string_cell);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, double_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, float_cell), Elements::Exception);
  BOOST_CHECK_THROW(boost::apply_visitor(cast, long_cell), Elements::Exception);
  auto int_res = boost::apply_visitor(cast, int_cell);
  auto bool_res = boost::apply_visitor(cast, bool_cell);

  // Then
  BOOST_CHECK_EQUAL(typeid(string_res).name(), typeid(int32_t).name());
  BOOST_CHECK_EQUAL(string_res, 12345);
  BOOST_CHECK_EQUAL(typeid(int_res).name(), typeid(int32_t).name());
  BOOST_CHECK_EQUAL(int_res, 1234);
  BOOST_CHECK_EQUAL(typeid(bool_res).name(), typeid(int32_t).name());
  BOOST_CHECK_EQUAL(bool_res, 1);

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


