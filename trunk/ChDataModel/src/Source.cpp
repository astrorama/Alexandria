/*
 * PhotSource.cpp
 *
 *  Created on: Jan 14, 2013
 *      Author: dubath
 */

#include <sstream>
#include <iostream>
#include <iomanip>

#include "boost/format.hpp"

#include "ChDataModel/Photometry.h"
#include "ChDataModel/Enumerations/FilterNames.h"
#include "ChDataModel/Source.h"

#include "ElementsKernel/ElementsException.h"

using namespace std;
/// using boost::io::group;

namespace ChDataModel {

//-----------------------------------------------------------------------------
/// Constructor with member assignment

Source::Source(int64_t source_id, double ra, double dec) :
    m_catalog_ptr(nullptr), m_source_id(source_id), m_ra(ra), m_dec(dec) {
}

//-----------------------------------------------------------------------------

Photometry & Source::addPhotometry(const Photometry & photometry) {

  const pair<map<FilterNames, Photometry>::iterator, bool> & p =
      m_photometry_map.insert(
          pair<FilterNames, Photometry>(photometry.getFilterName(),
              photometry));

  // Throw an exception, if that photometry was already included in the source
  if (p.second == false) {
    stringstream errorBuffer;
    errorBuffer << "Source::addPhotometry : Photometry "
        << photometry.getFilterName() << " is already in this source" << endl;
    throw ElementsException(errorBuffer.str());
  }

  // In the photometry, set the back pointer to this source
  p.first->second.setSourcePtr(this);

  // Return the photometry object, copied while inserting into the container
  return p.first->second;

} // Eof Source::addPhotometry

//-----------------------------------------------------------------------------

void Source::addPhotometricAttribute(const string & photometric_attribute_name,
    const double photometric_attribute_value) {

  // Check if an attribute with this name is already included in the map
  map<string, double>::iterator it = m_photometric_attribute_map.find(
      photometric_attribute_name);

  if (it == m_photometric_attribute_map.end()) {
    /// attribute not yet included, add it to the photmetric map
    m_photometric_attribute_map.insert(
        pair<string, double>(photometric_attribute_name,
            photometric_attribute_value));
  }
  else {
    // Attribute already included, throw an exception
    std::stringstream errorBuffer;
    errorBuffer << "Source::addPhotometricAttribute : a "
        << photometric_attribute_name
        << " photometric attribute is already in source : "
        << this->getSourceId() << endl;
    throw ElementsException(errorBuffer.str());
  }

} // Eof Source::addPhotometricAttribute

//-----------------------------------------------------------------------------

Photometry & Source::getPhotometry(const FilterNames filter_name) {

  map<FilterNames, Photometry>::iterator it = m_photometry_map.find(
      filter_name);

  if (it == m_photometry_map.end()) {
    /// throw an exception as this "filter_name" photometry is not available
    std::stringstream errorBuffer;
    errorBuffer
        << "Source::getPhotometry : a filter_band photometry is not available in source : "
        << this->getSourceId() << endl;
    /// When a enum solution has been found, the following message should be implemented
    /// a photometry.getFilterName() photometry is already in source: this->getSourceId()
    throw ElementsException(errorBuffer.str());
  }

  return m_photometry_map[filter_name];

} // Eof Source::getPhotometry

//-----------------------------------------------------------------------------

double Source::getPhotometricAttribute(
    const string & photometric_attribute_name) {

  map<string, double>::iterator it = m_photometric_attribute_map.find(
      photometric_attribute_name);

  if (it == m_photometric_attribute_map.end()) {
    /// throw an exception as this photometric attribute is not available
    std::stringstream errorBuffer;
    errorBuffer << "Source::getPhotometricAttribute : a "
        << photometric_attribute_name
        << "photometric attribute is not available in source : "
        << this->getSourceId() << endl;
    throw ElementsException(errorBuffer.str());
  }

  return m_photometric_attribute_map[photometric_attribute_name];

} // Eof Source::getPhotometricAttribute

//-----------------------------------------------------------------------------

void Source::printSource() {

  cout << "In Source : Source ID    = " << m_source_id << endl;
  cout << "In Source : RA           = " << m_ra << endl;
  cout << "In Source : DEC          = " << m_dec << endl;

  int photNr = 0;
  for (PhotometryIterator it3 = begin(); it3 != end(); ++it3) {
    cout << "----- Photometry no. " << ++photNr << " ---------\n";
    it3->printPhotometry();
  }

} // Eof Source::printSource

//-----------------------------------------------------------------------------

} /* namespace ChDataModel */
