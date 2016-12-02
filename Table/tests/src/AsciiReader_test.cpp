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
 * @file tests/src/AsciiReader_test.cpp
 * @date 12/02/16
 * @author nikoapos
 */

#include <boost/test/unit_test.hpp>

#include "Table/AsciiReader.h"
#include "Table/TableWriter.h"


#include <iostream>
#include "Table/AsciiWriter.h"

using namespace Euclid::Table;

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (AsciiReader_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE( example_test ) {

  AsciiReader reader {"/home/nikoapos/temp/test.cat"};
  
  AsciiWriter(std::cout).addData(reader.read(2));
  AsciiWriter(std::cout).addData(reader.read(2));
  AsciiWriter(std::cout).addData(reader.read(2));

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


