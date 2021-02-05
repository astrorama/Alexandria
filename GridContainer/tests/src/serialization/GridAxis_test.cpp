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
 * @file tests/src/serialization/GridAxis_test.cpp
 * @date June 27, 2014
 * @author Nikolaos Apostolakos
 */

#include "DefaultConstructibleClass.h"
#include "GridContainer/GridAxis.h"
#include "GridContainer/serialization/GridAxis.h"
#include "NonDefaultConstructibleClass.h"
#include <boost/archive/binary_iarchive.hpp>
#include <boost/archive/binary_oarchive.hpp>
#include <boost/archive/text_iarchive.hpp>
#include <boost/archive/text_oarchive.hpp>
#include <boost/mpl/list.hpp>
#include <boost/test/test_tools.hpp>
#include <boost/test/unit_test.hpp>
#include <sstream>

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(GridAxis_serialization_test)

template <typename I, typename O>
struct archive {
  typedef I iarchive;
  typedef O oarchive;
};

typedef archive<boost::archive::binary_iarchive, boost::archive::binary_oarchive> binary_archive;
typedef archive<boost::archive::text_iarchive, boost::archive::text_oarchive>     text_archive;

typedef boost::mpl::list<binary_archive, text_archive> archive_types;

//-----------------------------------------------------------------------------
// Test serialization of GridAxis with fundamental knot values
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE_TEMPLATE(fundamentalKnotValues, T, archive_types) {

  // Given
  std::string                             name = "AxisName";
  std::vector<double>                     knots{0., 3.4, 12E-15};
  Euclid::GridContainer::GridAxis<double> axis{name, knots};

  // When
  std::stringstream stream{};

  // We write to the stream a pointer to enable the non-default constructor
  // functionality of boost serialization
  Euclid::GridContainer::GridAxis<double>* axis_ptr = &axis;
  {
    // XML serializer requires to be destroyed to flush the closing tag
    typename T::oarchive boa{stream};
    boa << axis_ptr;
  }
  Euclid::GridContainer::GridAxis<double>* result;
  {
    typename T::iarchive bia{stream};
    bia >> result;
  }
  // We use a unique_ptr for the memory management
  std::unique_ptr<Euclid::GridContainer::GridAxis<double>> result_ptr{result};

  // Then
  BOOST_CHECK_EQUAL(result_ptr->name(), name);
  BOOST_CHECK_EQUAL_COLLECTIONS(result_ptr->begin(), result_ptr->end(), knots.begin(), knots.end());
}

//-----------------------------------------------------------------------------
// Test serialization of GridAxis with default constructible knot values
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE_TEMPLATE(defaultConstructibleKnotValues, T, archive_types) {

  // Given
  std::string                            name = "AxisName";
  std::vector<DefaultConstructibleClass> knots{};
  knots.push_back(DefaultConstructibleClass{});
  knots.back().value = 0.;
  knots.push_back(DefaultConstructibleClass{});
  knots.back().value = 3.4;
  knots.push_back(DefaultConstructibleClass{});
  knots.back().value = 12E-15;
  Euclid::GridContainer::GridAxis<DefaultConstructibleClass> axis{name, knots};

  // When
  std::stringstream stream{};
  {
    typename T::oarchive boa{stream};
    // We write to the stream a pointer to enable the non-default constructor
    // functionality of boost serialization
    Euclid::GridContainer::GridAxis<DefaultConstructibleClass>* axis_ptr = &axis;
    boa << axis_ptr;
  }
  Euclid::GridContainer::GridAxis<DefaultConstructibleClass>* result;
  {
    typename T::iarchive bia{stream};
    bia >> result;
  }
  // We use a unique_ptr for the memory management
  std::unique_ptr<Euclid::GridContainer::GridAxis<DefaultConstructibleClass>> result_ptr{result};

  // Then
  BOOST_CHECK_EQUAL(result_ptr->name(), name);
  BOOST_CHECK_EQUAL(result_ptr->size(), knots.size());
  auto result_iter = result_ptr->begin();
  auto knots_iter  = knots.begin();
  while (result_iter != result_ptr->end()) {
    BOOST_CHECK_EQUAL(result_iter->value, knots_iter->value);
    ++result_iter;
    ++knots_iter;
  }
}

//-----------------------------------------------------------------------------
// Test serialization of GridAxis with non default constructible knot values
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE_TEMPLATE(nonDefaultConstructibleKnotValues, T, archive_types) {

  // Given
  std::string                               name = "AxisName";
  std::vector<NonDefaultConstructibleClass> knots{};
  knots.push_back(NonDefaultConstructibleClass{0.});
  knots.push_back(NonDefaultConstructibleClass{3.4});
  knots.push_back(NonDefaultConstructibleClass{12E-15});
  Euclid::GridContainer::GridAxis<NonDefaultConstructibleClass> axis{name, knots};

  // When
  std::stringstream stream{};
  {
    typename T::oarchive boa{stream};
    // We write to the stream a pointer to enable the non-default constructor
    // functionality of boost serialization
    Euclid::GridContainer::GridAxis<NonDefaultConstructibleClass>* axis_ptr = &axis;
    boa << axis_ptr;
  }
  Euclid::GridContainer::GridAxis<NonDefaultConstructibleClass>* result;
  {
    typename T::iarchive bia{stream};
    bia >> result;
  }
  // We use a unique_ptr for the memory management
  std::unique_ptr<Euclid::GridContainer::GridAxis<NonDefaultConstructibleClass>> result_ptr{result};

  // Then
  BOOST_CHECK_EQUAL(result_ptr->name(), name);
  BOOST_CHECK_EQUAL(result_ptr->size(), knots.size());
  auto result_iter = result_ptr->begin();
  auto knots_iter  = knots.begin();
  while (result_iter != result_ptr->end()) {
    BOOST_CHECK_EQUAL(result_iter->value, knots_iter->value);
    ++result_iter;
    ++knots_iter;
  }
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
