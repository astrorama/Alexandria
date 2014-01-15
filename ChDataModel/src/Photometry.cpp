/**
 * @file Photometry.cpp
 *
 * @author Pierre Dubath
 *
 * Created on: Jan 30, 2013
 */

#include <iostream>

#include "ChDataModel/Photometry.h"

using namespace std;

namespace ChDataModel {

Photometry::Photometry() :
    m_source_ptr(nullptr), m_filter_name(FilterNames::None), m_photometry_type(
        PhotometryTypes::None), m_value(0.0), m_value_error(0.0) {
}

/// constructor with members assignment, but without source back pointer
Photometry::Photometry(const FilterNames filter_name,
    const PhotometryTypes photometry_type, const double value,
    const double value_error) :
    m_filter_name(filter_name), m_photometry_type(photometry_type), m_value(
        value), m_value_error(value_error) {
  m_source_ptr = nullptr;
}

/// constructor with members assignment
Photometry::Photometry(const SourcePtr source_ptr,
    const FilterNames filter_name, const PhotometryTypes photometry_type,
    const double value, const double value_error) :
    m_source_ptr(source_ptr), m_filter_name(filter_name), m_photometry_type(
        photometry_type), m_value(value), m_value_error(value_error) {
}

/**
 * Return the AB magnitude, either directly from the stored values if photometryType == AB_Magnitude or calling
 * conversion tools if it is not the case.
 */
double Photometry::getAbMagnitude() const {
  double magnitude = 0.0;
  if (this->m_photometry_type == PhotometryTypes::AB_MAGNITUDE) {
    magnitude = this->m_value;
  }
  else {
    /// TODO call a conversion tool
  }
  return magnitude;
}

//-----------------------------------------------------------------------------

void Photometry::printPhotometry() {

  cout << "In Photometry : FilterName  = " << m_filter_name << endl;
  cout << "In Photometry : Value       = " << m_value << endl;
  cout << "In Photometry : Value error = " << m_value_error << endl;

} // Eof Photometry::printPhotometry

//-----------------------------------------------------------------------------

} /* namespace ChDataModel */
