/**
 * @file Photometry.cpp
 *
 * @date Feb 5, 2014
 * @author admin
 */

#include "ChCatalog/SourceAttributes/Photometry.h"

using namespace std;

namespace ChCatalog {

Photometry::const_iterator::const_iterator(const std::vector<FilterName>::const_iterator& filters_iter,
                                           const std::vector<std::pair<double,double> >::const_iterator& values_iter)
                : m_filters_iter{filters_iter}, m_values_iter{values_iter} { }
                
auto Photometry::const_iterator::operator ++() -> const_iterator& {
  ++m_filters_iter;
  ++m_values_iter;
  return *this;
}

auto Photometry::const_iterator::operator *() -> reference {
  return *m_values_iter;
}

bool Photometry::const_iterator::operator ==(const const_iterator& other) const {
  return m_filters_iter == other.m_filters_iter;
}

bool Photometry::const_iterator::operator !=(const const_iterator& other) const {
  return m_filters_iter != other.m_filters_iter;
}

const FilterName& Photometry::const_iterator::filterName() const {
  return *m_filters_iter;
}

//-----------------------------------------------------------------------------
// find the value and error in the map for a specific filter name
// return a pair(value, error) otherwise null pointer

unique_ptr<pair<double, double>> Photometry::find(FilterName filter_name) const
{

  unique_ptr<pair<double, double>> flux_found_ptr {};
  auto filter_iter = m_filter_name_vector_ptr->begin();
  auto photometry_iter = m_photometry_vector.begin();
  while (filter_iter != m_filter_name_vector_ptr->end()) {
    if (*filter_iter == filter_name) {
      break;
    }
    ++filter_iter;
    ++photometry_iter;
  }
  if (filter_iter != m_filter_name_vector_ptr->end()) {
    flux_found_ptr = unique_ptr<pair<double, double>>{new pair<double, double>{*photometry_iter} };
  }

  return flux_found_ptr;
} // Eof Photometry::find


} // namespace ChCatalog
