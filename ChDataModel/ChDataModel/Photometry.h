/**
 * @file Photometry.h
 *
 * @author Pierre Dubath
 *
 * Created on: Jan 30, 2013
 */

#ifndef PHOTOMETRY_H_
#define PHOTOMETRY_H_

#include <string>

namespace ChDataModel {

/// Forward declaration
class Source;

/// Source pointer type
typedef Source* SourcePtr;

/**
 * The Photometry class is design to store a photometric measurement
 * obtained throw the specified filter (filterName).
 * The photometric "values" can be of different types:
 *
 *  - flux
 *  - AB magnitude
 *  - Vega magnitude
 *
 * as indicated by the "photometry type". All fields are constant and
 * should be provided to the constructor, except for the source "back" pointer,
 * that can be set. This allows to create "free floating" photometric objects,
 * that can be associated to a given source later.
 */
class Photometry {

public:

  /// constructor with members assignment
  Photometry(const std::string& filter_name, const double flux,
      const double flux_error) :
      m_filter_name(filter_name), m_flux(flux), m_flux_error(flux_error) {
  }
  /// default destructor
  virtual ~Photometry() {
  }

  const std::string& getFilterName() const {
    return m_filter_name;
  }

  const double getFlux() const {
    return m_flux;
  }

  const double getFluxError() const {
    return m_flux_error;
  }

private:

  /// The filter name
  const std::string m_filter_name;
  /// The flux value
  const double m_flux;
  /// The flux uncertainty value
  const double m_flux_error;

};
// Eof class Photometry

} /* namespace ChDataModel */

#endif /* PHOTOMETRY_H_ */
