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
 * @file tests/src/SOM_serialization_test.cpp
 * @date 28/11/19
 * @author Alejandro Alvarez Ayllon
 */

#include <boost/archive/binary_iarchive.hpp>
#include <boost/archive/binary_oarchive.hpp>
#include <boost/archive/text_iarchive.hpp>
#include <boost/archive/text_oarchive.hpp>
#include <boost/mpl/list.hpp>
#include <boost/test/unit_test.hpp>
#include <sstream>

#include <ElementsKernel/Temporary.h>

#include "SOM/InitFunc.h"
#include "SOM/SOM.h"
#include "SOM/SOMTrainer.h"
#include "SOM/serialize.h"

using namespace Euclid::SOM;

// This should not be done, but it is the only way I found to get this test to compile in CentOS7
// BOOST_TEST_DONT_PRINT_LOG_VALUE didn't work there
namespace std {
std::ostream& operator<<(std::ostream& out, const std::array<double, 2>& array) {
  out << '[' << array[0] << ", " << array[1] << ']';
  return out;
}

std::ostream& operator<<(std::ostream& out, const std::pair<size_t, size_t>& pair) {
  out << '[' << pair.first << ", " << pair.second << ']';
  return out;
}
}  // namespace std

struct SerializationFixture {
  SOM<2> m_som{5, 5, InitFunc::uniformRandom(0, 1)};

  SerializationFixture() {
    m_som.findBMU({1, 2});
    m_som.findBMU({1, 2}, {0.1, 0.4});

    std::vector<std::pair<double, double>> trainset{{1, 1}, {0, 0}, {0, 1}, {1, 0}};

    SOMTrainer trainer{NeighborhoodFunc::linearUnitDisk(3), LearningRestraintFunc::linear()};
    auto       weight_func = [](const std::pair<double, double>& p) {
      std::array<double, 2> res;
      res[0] = p.first;
      res[1] = p.second;
      return res;
    };
    trainer.train(m_som, 5, trainset.begin(), trainset.end(), weight_func);
  }
};

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(SOM_test)

template <typename I, typename O>
struct archive {
  typedef I iarchive;
  typedef O oarchive;
};

typedef archive<boost::archive::binary_iarchive, boost::archive::binary_oarchive> binary_archive;
typedef archive<boost::archive::text_iarchive, boost::archive::text_oarchive>     text_archive;

typedef boost::mpl::list<binary_archive, text_archive> archive_types;

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE_TEMPLATE(serialize_som_test, T, archive_types, SerializationFixture) {
  std::stringstream stream;
  somExport<typename T::oarchive>(stream, m_som);

  auto result = somImport<typename T::iarchive, 2>(stream);

  BOOST_CHECK_EQUAL(m_som.getSize(), result.getSize());
  BOOST_CHECK_EQUAL_COLLECTIONS(m_som.begin(), m_som.end(), result.begin(), result.end());
}

//-----------------------------------------------------------------------------

BOOST_FIXTURE_TEST_CASE(serialize_som_fits_test, SerializationFixture) {
  Elements::TempPath fits_file;

  somFitsExport(fits_file.path().native(), m_som);
  auto result = somFitsImport<2>(fits_file.path().native());
  BOOST_CHECK_EQUAL(m_som.getSize(), result.getSize());
  BOOST_CHECK_EQUAL_COLLECTIONS(m_som.begin(), m_som.end(), result.begin(), result.end());
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
