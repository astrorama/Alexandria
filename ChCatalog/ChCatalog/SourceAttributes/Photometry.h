/**
 * @file Photometry.h
 *
 * Created on: Jan 17, 2014
 *     Author: Pierre Dubath
 */

#ifndef PHOTOMETRY_H_
#define PHOTOMETRY_H_

#include <memory>
#include <map>
#include <set>
#include "ElementsKernel/ElementsException.h"
#include "ChCatalog/Attribute.h"
#include "ChCatalog/FilterName.h"

namespace ChCatalog {

/**
 * The Photometry class is design to store a set of photometric flux measurements
 * obtained through different filters (filterName).
 */
class Photometry: public Attribute {

public:

  Photometry(std::map< FilterName, std::pair<double, double>> photometry_map)
            : m_photometry_map(photometry_map) { }

  /// default destructor
  virtual ~Photometry() { }

  /**
   * @brief
   * Return the size of the photometry map
   */
  std::size_t size() const { return m_photometry_map.size(); }

  /**
   * @brief
   * Return a photometry measurement through the specified filter
   * @param filter_name
   *  The filter name
   * @return
   *  A pair containing a value and the corresponding error
   */
  std::shared_ptr<std::pair<double, double>> find(FilterName filter_name) const;

  /**
   * @brief
   *  Get a const_iterator pointing to the first element in the map container
   * @return
   *  Returns a const_iterator pointing to the first element in the map container
   */
  std::map< FilterName, std::pair<double, double>>::const_iterator cbegin()
      { return m_photometry_map.cbegin() ; }

  /**
   * @brief
   *  Get an const_iterator pointing to the last element in the map container
   * @return
   *  Returns a const_iterator pointing to the past-the-end element in the
   *  map container
   */
  std::map< FilterName, std::pair<double, double>>::const_iterator cend()
      { return m_photometry_map.cend() ; }

private:

  /// The photometry map
  std::map< FilterName, std::pair<double, double>> m_photometry_map { };

}; // Eof class Photometry

} /* namespace ChCatalog */

#endif /* PHOTOMETRY_H_ */
