/**
 * @file Photometry.cpp
 *
 * @date Feb 5, 2014
 * @author admin
 */

#include "ChCatalog/SourceAttributes/Photometry.h"

using namespace std;

namespace ChCatalog {


//-----------------------------------------------------------------------------
// find the value and error in the map for a specific filter name
// return a pair(value, error) otherwise null pointer

shared_ptr<pair<double, double>> Photometry::find(FilterName filter_name) const
{
  shared_ptr<pair<double, double>> ptr(nullptr);
  auto it = m_photometry_map.find(filter_name);
  if (it != m_photometry_map.end()) {
    ptr = make_shared<pair<double, double>>(it->second);
  }

  return (ptr);
} // Eof Photometry::find


} // namespace ChCatalog
