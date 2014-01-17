/*
 * Catalog.cpp
 *
 *  Created on: Jan 14, 2013
 *      Author: dubath
 */

#include <sstream>
#include <iostream>
#include <iomanip>

#include "ChDataModel/Catalog.h"
#include "ChDataModel/Source.h"

#include "ElementsKernel/ElementsException.h"

using namespace std;

namespace ChDataModel {

//-----------------------------------------------------------------------------
// Add a source to the catalog

void Catalog::addSource(const Source & source) {

  // Insert the source into the container
  const pair<map<int64_t, Source>::iterator, bool> & p = m_source_map.insert(
      pair<int64_t, Source>(source.getSourceId(), source));

  // Throw an exception, if that source was already included in the catalog
  if (p.second == false) {
    stringstream errorBuffer;
    errorBuffer << "Catalog::addSource : source " << source.getSourceId()
        << " is already in this catalog" << endl;
    throw ElementsException(errorBuffer.str());
  }

} // Eof Catalog::createSource

//-----------------------------------------------------------------------------
// Get one source from the container of sources

Source & Catalog::getSource(int64_t source_id) {

  // Try to find it in the container
  map<int64_t, Source>::iterator it = m_source_map.find(source_id);

  // Throw exception, if that source is not included in the catalog
  if (it == m_source_map.end()) {
    stringstream errorBuffer;
    errorBuffer << "Catalog::getSource : source " << source_id
        << " is not available in this catalog" << endl;
    throw ElementsException(errorBuffer.str());
  }

  // Return the source, if found in the container
  return it->second;

} // Eof Catalog::getSource

//-----------------------------------------------------------------------------

} /* namespace ChDataModel */
