/**
 * @file Photometry.h
 *
 * Created on: Jan 17, 2014
 *     Author: Pierre Dubath
 */
#ifndef PHOTOMETRY_H_
#define PHOTOMETRY_H_

#include <string>

namespace ChDataModel {



/**
 * The Photometry class is design to store a photometric flux measurement
 * obtained through the specified filter (filterName).
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
