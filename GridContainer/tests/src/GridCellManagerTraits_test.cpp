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
 * @file GridCellManagerTraits_test.cpp
 * @date July 4, 2014
 * @author Nikolaos Apostolakos
 */

#include "GridContainer/GridCellManagerTraits.h"
#include <boost/test/unit_test.hpp>

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE(GridCellManagerTraits_test)

//-----------------------------------------------------------------------------
// Test the default operations of the GridCellManagerTraits
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(defaultOperations) {

  // Given
  class DefaultCellManager {
    int m_size;

  public:
    explicit DefaultCellManager(int size_) : m_size{size_} {}
    typedef double data_type;
    struct iterator {
      int m_i{0};
    };
    size_t size() const {
      return m_size;
    };
    iterator begin() {
      iterator i{};
      i.m_i = 1;
      return i;
    };
    iterator end() {
      iterator i{};
      i.m_i = 2;
      return i;
    };
  };

  // When
  using traits = Euclid::GridContainer::GridCellManagerTraits<DefaultCellManager>;
  auto result  = traits::factory(5);

  // Then
  BOOST_CHECK(typeid(traits::data_type) == typeid(DefaultCellManager::data_type));
  BOOST_CHECK(typeid(traits::iterator) == typeid(DefaultCellManager::iterator));
  BOOST_CHECK(typeid(*result) == typeid(DefaultCellManager));
  BOOST_CHECK_EQUAL(traits::size(*result), 5u);
  BOOST_CHECK_EQUAL(traits::begin(*result).m_i, 1);
  BOOST_CHECK_EQUAL(traits::end(*result).m_i, 2);
  BOOST_CHECK(!traits::enable_boost_serialize);
}

//-----------------------------------------------------------------------------
// Test the operations of the GridCellManagerTraits for a vector
//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE(vectorOperations) {

  // Given
  typedef std::vector<double> VectorCellManager;

  // When
  typedef Euclid::GridContainer::GridCellManagerTraits<VectorCellManager> traits;
  auto                                                                    result = traits::factory(5);

  // Then
  BOOST_CHECK(typeid(traits::data_type) == typeid(double));
  BOOST_CHECK(typeid(traits::iterator) == typeid(VectorCellManager::iterator));
  BOOST_CHECK(typeid(*result) == typeid(VectorCellManager));
  BOOST_CHECK_EQUAL(traits::size(*result), 5u);
  BOOST_CHECK(traits::begin(*result) == result->begin());
  BOOST_CHECK(traits::end(*result) == result->end());
  BOOST_CHECK(traits::enable_boost_serialize);
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END()
