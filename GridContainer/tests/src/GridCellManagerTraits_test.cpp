/** 
 * @file GridCellManagerTraits_test.cpp
 * @date July 4, 2014
 * @author Nikolaos Apostolakos
 */

#include <boost/test/unit_test.hpp>
#include "GridContainer/GridCellManagerTraits.h"

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (GridCellManagerTraits_test)

//-----------------------------------------------------------------------------
// Test the default operations of the GridCellManagerTraits
//-----------------------------------------------------------------------------
    
BOOST_AUTO_TEST_CASE(defaultOperations) {
  
  // Given
  class DefaultDataManager {
    int m_size;
  public:
    DefaultDataManager(int size) : m_size{size} {}
    typedef double data_type;
    struct iterator { int m_i {0}; };
    size_t size() const { return m_size; };
    iterator begin() { iterator i{}; i.m_i = 1; return i; };
    iterator end() { iterator i{}; i.m_i = 2; return i; };
  };
  
  // When
  typedef GridContainer::GridCellManagerTraits<DefaultDataManager> traits;
  auto result = traits::factory(5);
  
  // Then
  BOOST_CHECK(typeid(traits::data_type) == typeid(DefaultDataManager::data_type));
  BOOST_CHECK(typeid(traits::iterator) == typeid(DefaultDataManager::iterator));
  BOOST_CHECK(typeid(*result) == typeid(DefaultDataManager));
  BOOST_CHECK_EQUAL(traits::size(*result), 5);
  BOOST_CHECK_EQUAL(traits::begin(*result).m_i, 1);
  BOOST_CHECK_EQUAL(traits::end(*result).m_i, 2);
  BOOST_CHECK(!traits::enable_boost_serialize);
  
}

//-----------------------------------------------------------------------------
// Test the operations of the GridCellManagerTraits for a vector
//-----------------------------------------------------------------------------
    
BOOST_AUTO_TEST_CASE(vectorOperations) {
  
  // Given
  typedef std::vector<double> VectorDataManager;
  
  // When
  typedef GridContainer::GridCellManagerTraits<VectorDataManager> traits;
  auto result = traits::factory(5);
  
  // Then
  BOOST_CHECK(typeid(traits::data_type) == typeid(double));
  BOOST_CHECK(typeid(traits::iterator) == typeid(VectorDataManager::iterator));
  BOOST_CHECK(typeid(*result) == typeid(VectorDataManager));
  BOOST_CHECK_EQUAL(traits::size(*result), 5);
  BOOST_CHECK(traits::begin(*result) == result->begin());
  BOOST_CHECK(traits::end(*result) == result->end());
  BOOST_CHECK(traits::enable_boost_serialize);
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()