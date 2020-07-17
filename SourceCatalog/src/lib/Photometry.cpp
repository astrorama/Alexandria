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


namespace Euclid {
namespace SourceCatalog {

//-----------------------------------------------------------------------------
// find the value and error in the map for a specific filter name
// return a ptr to a ValuePair(value, error) and null pointer otherwise
std::unique_ptr<FluxErrorPair> Photometry::find(const std::string& filter_name) const
{
  std::unique_ptr<FluxErrorPair> flux_found_ptr {};
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
    flux_found_ptr = std::unique_ptr<FluxErrorPair>{new FluxErrorPair{*photometry_iter} };
  }

  return flux_found_ptr;
} // Eof Photometry::find

const std::shared_ptr<std::vector<std::string>>& Photometry::getFilterNames() const {
  return m_filter_name_vector_ptr;
}

} // namespace SourceCatalog
} // end of namespace Euclid
