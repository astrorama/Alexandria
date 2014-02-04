/**
 * Catalog.cpp
 *
 *  Created on : Feb 4, 2014
 *      Author : Nicolas Morisset
 */


#include "ChDataModel/Catalog.h"
#include "ChDataModel/Source.h"

#include "ElementsKernel/ElementsException.h"

using namespace std;

namespace ChDataModel {

//-----------------------------------------------------------------------------
// Constructor
Catalog::Catalog(vector<Source> source_vector): m_sourceVector(source_vector)
{
  // Set the m_indeces_map map
  for (size_t index=0; index < m_sourceVector.size(); ++index) {
     auto it = m_indeces_map.emplace(m_sourceVector[index].getId(), index);
     // Make sure the element does not already exist
     if (!it.second)
     {
       throw ElementsException("Catalog::Catalog: Source object already exist "
             "in the map for source ID : %d, index: %d\n",
             m_sourceVector[index].getId(), index);
     }
  }
} // Eof Catalog::Catalog


//-----------------------------------------------------------------------------
// find source in the map
// return source otherwise null pointer

shared_ptr<Source> Catalog::find(const uint64_t source_id)
{
  shared_ptr<Source> ptr(nullptr);
  auto it = m_indeces_map.find(source_id);
  if (it != m_indeces_map.end()) {
    ptr = make_shared<Source>(m_sourceVector[it->second]);
  }

  return (ptr);

} // Eof Catalog::find

//-----------------------------------------------------------------------------

} /* namespace ChDataModel */
