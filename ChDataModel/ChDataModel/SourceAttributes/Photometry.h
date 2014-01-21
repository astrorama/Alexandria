/**
 * @file Photometry.h
 *
 * Created on: Jan 17, 2014
 *     Author: Pierre Dubath
 */
#ifndef PHOTOMETRY_H_
#define PHOTOMETRY_H_

#include <string>
#include <utility>
#include <sstream>
#include <map>
#include "ElementsKernel/ElementsException.h"
#include "ChDataModel/FilterName.h"

namespace ChDataModel {

/**
 * The Photometry class is design to store a photometric flux measurement
 * obtained through the specified filter (filterName).
 */
class Photometry {

public:

  Photometry() {
  }
  /// constructor with members assignment
  Photometry(
      std::map<const FilterName, std::pair<double, double>> photometry_map) :
      m_photometry_map(photometry_map) {
  }
  /// default destructor
  virtual ~Photometry() {
  }

  void addFlux(const FilterName filterName, const double flux,
      const double fluxError) {
    auto isUniq = m_photometry_map.emplace(filterName,
        std::pair<double, double> { flux, fluxError });

    if (!isUniq.second) {
      std::stringstream errorBuffer;
      errorBuffer << "Photometry::addFlux: A photometric value of type "
          << filterName.qualifiedName()
          << " is already included in the photometric map " << std::endl;
      throw ElementsException(errorBuffer.str());
    }
  }

  void clear() {
    m_photometry_map.clear();
  }

  std::size_t size() {
    return m_photometry_map.size();
  }

  double getFlux(FilterName filterName) const {
    /// here it is not clear if we should use "at()" or "[]", i.e., do we need range checking or not?
    return m_photometry_map.at(filterName).first;
  }

  double getFluxError(FilterName filterName) const {
    /// here it is not clear if we should use "at()" or "[]", i.e., do we need range checking or not?
    return m_photometry_map.at(filterName).second;
  }

private:

  /// The photometry map
  std::map<const FilterName, std::pair<double, double>> m_photometry_map { };

};
// Eof class Photometry

} /* namespace ChDataModel */

#endif /* PHOTOMETRY_H_ */
