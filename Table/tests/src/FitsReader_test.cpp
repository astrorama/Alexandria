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
 * @file tests/src/FitsReader_test.cpp
 * @date 12/05/16
 * @author nikoapos
 */

#include <boost/test/unit_test.hpp>

#include "Table/FitsReader.h"


#include "Table/AsciiWriter.h"

using namespace Euclid::Table;

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (FitsReader_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE( example_test ) {

  FitsReader reader {"/home/nikoapos/Phosphoros/Catalogs/Example/test-cat.fits"};
  auto info = reader.getInfo();
  std::cout << info.size() << '\n';
  for (size_t i=0 ; i<info.size(); ++i ) {
    std::cout << info.getDescription(i).name << '\n';
  }
  
  reader.skip(710);
  AsciiWriter{std::cout}.addData(reader.read(2));
  AsciiWriter{std::cout}.addData(reader.read());

}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


