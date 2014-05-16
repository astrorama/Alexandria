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
 * obtained through different filters (filterName). The flux and value and the
 * associated error are stored in a vector of ValuePair, while the list of filter
 * names is kept in a vector that is common to all objects (which only keep a shared_ptr
 * to it). In this way, their is no waste of memory to keep the filter information in
 * each Photometry object and the consistency of the relationship between filter and
 * the corresponding values (flux and error) is ensure through the code.
 *
 * The user must however provide a ValuePair vector which matches the vector of
 * FilterName. This is why the Photometry constructor should never be called directly.
 * Always use the PhotometryAttributeHandler to build Photometry objects.
 *
 */
class Photometry: public Attribute {

public:

  struct ValuePair {
    double flux;
    double error;
    ValuePair(double flux, double error) :
        flux(flux), error(error) {
    }
  };

  /**
   * Iterator for the photometry flux and error values. See the Photometry_test to see
   * how this can be used to iterate through the flux and error the different filters.
   */
  class const_iterator: public std::iterator<std::forward_iterator_tag,
      const ValuePair> {
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


  /**
   * @brief Constructor which should never be called directly. Use the
   * PhotometryAttributeHandler to build Photometry objects
   *
   * @param filter_name_vector_ptr
   *  a shared pointer to the vector of filter names
   * @param photometry_vector
   *  the vector of ValuePair, i..e, the flux values with their errors
   *
   */
  Photometry(std::shared_ptr<std::vector<FilterName>> filter_name_vector_ptr,
      std::vector<ValuePair> photometry_vector) :
      m_filter_name_vector_ptr(filter_name_vector_ptr), m_photometry_vector(
          std::move(photometry_vector)) {
    // Only check the size, but not the consistency
    if (m_filter_name_vector_ptr->size() != m_photometry_vector.size()) {
      throw ElementsException()
          << "The FilterName and the flux vectors have different size";
    }
  }

  /// default destructor
  virtual ~Photometry() {
  }

  const_iterator begin() const {
    return const_iterator { m_filter_name_vector_ptr->cbegin(),
        m_photometry_vector.cbegin() };
  }

  const_iterator end() const {
    return const_iterator { m_filter_name_vector_ptr->cend(),
        m_photometry_vector.cend() };
  }

  /**
   * @brief
   * Return the size of the photometry map
   */
  std::size_t size() const {
    return m_filter_name_vector_ptr->size();
  }

  /**
   * @brief Return a photometry measurement through the specified filter.
   *  The current implementation of this method is relatively slow as it
   *  is not expected to be used very intensively.
   * @param filter_name
   *  The filter name
   * @return
   *  A pair containing a value and the corresponding error
   */
  std::unique_ptr<ValuePair> find(FilterName filter_name) const;

private:

  /// Shared pointer to the common list of filter names
  std::shared_ptr<std::vector<FilterName>> m_filter_name_vector_ptr;

  /// The photometry map
  std::vector<ValuePair> m_photometry_vector;

};
// Eof class Photometry

} /* namespace ChCatalog */

#endif /* PHOTOMETRY_H_ */
