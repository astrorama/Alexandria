/**
 * Catalog.cpp
 *
 *  Created on : Feb 4, 2014
 *      Author : Nicolas Morisset
 */


#include "SourceCatalog/Catalog.h"
#include "SourceCatalog/Source.h"

#include "ElementsKernel/Exception.h"

using namespace std;

namespace Euclid {
namespace SourceCatalog {

//-----------------------------------------------------------------------------
// Constructor
Catalog::Catalog(vector<Source> source_vector): m_source_vector(source_vector)
{
  // Set the m_indices_map map
  for (size_t index=0; index < m_source_vector.size(); ++index) {
     auto it = m_source_index_map.emplace(m_source_vector[index].getId(), index);
     // Make sure the element does not already exist
     if (!it.second)
     {
       throw Elements::Exception("Euclid::SourceCatalog::Catalog: Source object already exist "
             "in the map for source ID : %d, index: %d\n",
             m_source_vector[index].getId(), index);
     }
  }
} // Eof Euclid::SourceCatalog::Catalog


//-----------------------------------------------------------------------------
// find source in the map
// return source otherwise null pointer
shared_ptr<Source> Catalog::find(const int64_t source_id) const
{
  shared_ptr<Source> ptr(nullptr);
  auto it = m_source_index_map.find(source_id);
  if (it != m_source_index_map.end()) {
    ptr = make_shared<Source>(m_source_vector[it->second]);
  }

  return (ptr);

} // Eof Catalog::find

//-----------------------------------------------------------------------------

} /* namespace SourceCatalog */
} // end of namespace Euclid
