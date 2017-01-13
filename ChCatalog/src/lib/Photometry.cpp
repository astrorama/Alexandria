/**
 * @file Photometry.cpp
 *
 * @date Feb 5, 2014
 * @author Pierre Dubath
 */

#include "ChCatalog/SourceAttributes/Photometry.h"

using namespace std;

namespace ChCatalog {

Photometry::const_iterator::const_iterator(const std::vector<string>::const_iterator& filters_iter,
                                           const std::vector<FluxErrorPair>::const_iterator& values_iter)
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

const string& Photometry::const_iterator::filterName() const {
  return *m_filters_iter;
}

//-----------------------------------------------------------------------------
// find the value and error in the map for a specific filter name
// return a ptr to a ValuePair(value, error) and null pointer otherwise
unique_ptr<FluxErrorPair> Photometry::find(string filter_name) const
{

  unique_ptr<FluxErrorPair> flux_found_ptr {};
  auto filter_iter = m_filter_name_vector_ptr->begin();
  auto photometry_iter = m_value_vector.begin();
  while (filter_iter != m_filter_name_vector_ptr->end()) {
    if (*filter_iter == filter_name) {
      break;
    }
    ++filter_iter;
    ++photometry_iter;
  }
  if (filter_iter != m_filter_name_vector_ptr->end()) {
    flux_found_ptr = unique_ptr<FluxErrorPair>{new FluxErrorPair{(*photometry_iter).flux, (*photometry_iter).error} };
  }

  return move(flux_found_ptr);
} // Eof Photometry::find


} // namespace ChCatalog
