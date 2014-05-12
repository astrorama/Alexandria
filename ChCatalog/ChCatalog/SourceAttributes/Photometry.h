/**
 * @file Photometry.h
 *
 * Created on: Jan 17, 2014
 *     Author: Pierre Dubath
 */

#ifndef PHOTOMETRY_H_
#define PHOTOMETRY_H_

#include <memory>
#include <vector>
#include <iterator>
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
  
  class const_iterator : public std::iterator<std::forward_iterator_tag, const std::pair<double, double>> {
  public:
    const_iterator(const std::vector<FilterName>::const_iterator& filters_iter,
                   const std::vector<std::pair<double, double>>::const_iterator& values_iter);
    const_iterator& operator++();
    reference operator*();
    bool operator==(const const_iterator& other) const;
    bool operator!=(const const_iterator& other) const;
    const FilterName& filterName() const;
  private:
    std::vector<FilterName>::const_iterator m_filters_iter;
    std::vector<std::pair<double, double>>::const_iterator m_values_iter;
  };

  Photometry(std::shared_ptr<std::vector<FilterName>> filter_name_vector_ptr,
        std::vector<std::pair<double, double>> photometry_vector)
            : m_filter_name_vector_ptr(filter_name_vector_ptr), m_photometry_vector( std::move(photometry_vector) ) {
    if( m_filter_name_vector_ptr->size() != m_photometry_vector.size() ) {
      throw ElementsException() << "The sizes of the FilterName and the flux vectors are not identical";
    }
  }

  /// default destructor
  virtual ~Photometry() { }
  
  const_iterator begin() const {
    return const_iterator {m_filter_name_vector_ptr->cbegin(), m_photometry_vector.cbegin()};
  }
  
  const_iterator end() const {
    return const_iterator {m_filter_name_vector_ptr->cend(), m_photometry_vector.cend()};
  }

  /**
   * @brief
   * Return the size of the photometry map
   */
  std::size_t size() const { return m_filter_name_vector_ptr->size(); }

  /**
   * @brief
   * Return a photometry measurement through the specified filter
   * @param filter_name
   *  The filter name
   * @return
   *  A pair containing a value and the corresponding error
   */
  std::unique_ptr<std::pair<double, double>> find(FilterName filter_name) const;

  /**
//   * @brief
//   *  Get a const_iterator pointing to the first element in the map container
//   * @return
//   *  Returns a const_iterator pointing to the first element in the map container
//   */
//  std::map< FilterName, std::pair<double, double>>::const_iterator begin()
//      { return m_photometry_vector.begin() ; }
//
//  /**
//   * @brief
//   *  Get an const_iterator pointing to the last element in the map container
//   * @return
//   *  Returns a const_iterator pointing to the past-the-end element in the
//   *  map container
//   */
//  std::map< FilterName, std::pair<double, double>>::const_iterator end()
//      { return m_photometry_vector.end() ; }

private:

  std::shared_ptr<std::vector<FilterName>> m_filter_name_vector_ptr;

  /// The photometry map
  std::vector<std::pair<double, double>> m_photometry_vector;

}; // Eof class Photometry

} /* namespace ChCatalog */

#endif /* PHOTOMETRY_H_ */
