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
  
  struct ValuePair {
    double flux;
    double error;
    ValuePair(double flux, double error) : flux(flux), error(error) {}
  };

  class const_iterator : public std::iterator<std::forward_iterator_tag, const ValuePair> {
  public:
    const_iterator(const std::vector<FilterName>::const_iterator& filters_iter,
                   const std::vector<ValuePair>::const_iterator& values_iter);
    const_iterator& operator++();
    reference operator*();
    bool operator==(const const_iterator& other) const;
    bool operator!=(const const_iterator& other) const;
    const FilterName& filterName() const;
  private:
    std::vector<FilterName>::const_iterator m_filters_iter;
    std::vector<ValuePair>::const_iterator m_values_iter;
  };

  Photometry(std::shared_ptr<std::vector<FilterName>> filter_name_vector_ptr,
        std::vector<ValuePair> photometry_vector)
            : m_filter_name_vector_ptr(filter_name_vector_ptr), m_photometry_vector( std::move(photometry_vector) ) {

    if( m_filter_name_vector_ptr->size() != m_photometry_vector.size() ) {
      throw ElementsException() << "The FilterName and the flux vectors have different size";
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
  std::unique_ptr<ValuePair> find(FilterName filter_name) const;

private:

  std::shared_ptr<std::vector<FilterName>> m_filter_name_vector_ptr;

  /// The photometry map
  std::vector<ValuePair> m_photometry_vector;

}; // Eof class Photometry

} /* namespace ChCatalog */

#endif /* PHOTOMETRY_H_ */
