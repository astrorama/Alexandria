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
#include "ChDataModel/Attribute.h"
#include "ChDataModel/FilterName.h"

namespace ChDataModel {

/**
 * The Photometry class is design to store a set of photometric flux measurements
 * obtained through different filters (filterName).
 */
class Photometry: public Attribute {

public:

  Photometry() {
  }
  /// default destructor
  virtual ~Photometry() {
  }

  /**
   * @brief Add a particular flux measurement to the photometry map
   * @details
   * @param filterName
   *
   * @through An exception in there is already a flux measurement
   *    for this filter in the photometry map
   */
  void addFlux(const FilterName filterName, const double flux,
      const double fluxError) {
    auto filterUnicity = m_photometry_map.emplace(filterName,
        std::pair<double, double> { flux, fluxError });

    if (!(filterUnicity.second)) {
      std::stringstream errorBuffer;
      errorBuffer << "Photometry::addFlux: A photometric flux if filter: "
          << filterName.qualifiedName()
          << " is already included in the photometry map " << std::endl;
      throw ElementsException(errorBuffer.str());
    }
  }

  /**
   * @brief Erase all elements in the photometry map
   */
  void clear() {
    m_photometry_map.clear();
  }

  /**
   * @brief Return teh size of the photometry map
   */
  std::size_t size() {
    return m_photometry_map.size();
  }

  /**
   * @brief Return a photometry measurement through the specified filter
   *
   * @param filterName
   *    The filter name
   * @return A pair with the Flux and the FluxError
   */
  std::pair<double, double> getFluxAndError(FilterName filterName) {
    /// here it is not clear if we should use "at()" or "[]", i.e., do we need range checking or not?
    return m_photometry_map.at(filterName);
  }

  /**
   * @brief Return a photometry measurement through the specified filter
   *
   * @param filterName
   *    The filter name
   * @return The Flux
   */
  double getFlux(FilterName filterName) const {
    /// here it is not clear if we should use "at()" or "[]", i.e., do we need range checking or not?
    return m_photometry_map.at(filterName).first;
  }

  /**
   * @brief Return a photometry measurement through the specified filter
   *
   * @param filterName
   *    The filter name
   * @return The Flux Error
   */
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
