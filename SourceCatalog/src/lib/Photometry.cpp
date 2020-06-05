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
 * @file src/lib/Photometry.cpp
 *
 * @date Feb 5, 2014
 * @author Pierre Dubath
 */

#include "SourceCatalog/SourceAttributes/Photometry.h"

using namespace std;

namespace Euclid {
namespace SourceCatalog {

Photometry::PhotometryConstIterator::PhotometryConstIterator(
                        const std::vector<string>::const_iterator& filters_iter,
                        const std::vector<FluxErrorPair>::const_iterator& values_iter)
                : m_filters_iter{filters_iter}, m_values_iter{values_iter} { }

auto Photometry::PhotometryConstIterator::operator ++() -> const_iterator& {
  ++m_filters_iter;
  ++m_values_iter;
  return *this;
}

auto Photometry::PhotometryConstIterator::operator *() -> reference {
  return *m_values_iter;
}

bool Photometry::PhotometryConstIterator::operator ==(const const_iterator& other) const {
  return m_filters_iter == other.m_filters_iter;
}

bool Photometry::PhotometryConstIterator::operator !=(const const_iterator& other) const {
  return m_filters_iter != other.m_filters_iter;
}

ssize_t Photometry::PhotometryConstIterator::operator-(const PhotometryConstIterator& other) const {
  return m_values_iter - other.m_values_iter;
}

const string& Photometry::PhotometryConstIterator::filterName() const {
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
    flux_found_ptr = unique_ptr<FluxErrorPair>{new FluxErrorPair{*photometry_iter} };
  }

  return flux_found_ptr;
} // Eof Photometry::find


} // namespace SourceCatalog
} // end of namespace Euclid
