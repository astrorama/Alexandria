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
 * Catalog.cpp
 *
 *  Created on : Feb 4, 2014
 *      Author : Nicolas Morisset
 */

#include "SourceCatalog/Catalog.h"
#include "SourceCatalog/Source.h"

#include "ElementsKernel/Exception.h"

namespace Euclid {
namespace SourceCatalog {

//-----------------------------------------------------------------------------
// Constructor
Catalog::Catalog(std::vector<Source> source_vector) : m_source_vector(source_vector) {
  // Set the m_indices_map map
  for (size_t index = 0; index < m_source_vector.size(); ++index) {
    auto it = m_source_index_map.emplace(m_source_vector[index].getId(), index);
    // Make sure the element does not already exist
    if (!it.second) {
      throw Elements::Exception() << "Euclid::SourceCatalog::Catalog: Source object already exist "
                                  << "in the map for source ID : " << m_source_vector[index].getId() << ", index: " << index;
    }
  }
}  // Eof Euclid::SourceCatalog::Catalog

//-----------------------------------------------------------------------------
// find source in the map
// return source otherwise null pointer
std::shared_ptr<Source> Catalog::find(const Source::id_type& source_id) const {
  std::shared_ptr<Source> ptr(nullptr);
  auto                    it = m_source_index_map.find(source_id);
  if (it != m_source_index_map.end()) {
    ptr = std::make_shared<Source>(m_source_vector[it->second]);
  }

  return ptr;

}  // Eof Catalog::find

//-----------------------------------------------------------------------------

} /* namespace SourceCatalog */
}  // end of namespace Euclid
