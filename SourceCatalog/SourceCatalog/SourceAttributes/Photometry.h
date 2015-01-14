/**
 * @file SourceCatalog/SourceAttributes/Photometry.h
 *
 * Created on: Jan 17, 2014
 *     Author: Pierre Dubath
 */

#ifndef PHOTOMETRY_H_
#define PHOTOMETRY_H_

#include <memory>
#include <vector>
#include <iterator>

#include "ElementsKernel/Export.h"
#include "ElementsKernel/Exception.h"

#include "SourceCatalog/Attribute.h"

namespace Euclid {
namespace SourceCatalog {

struct FluxErrorPair {
  double flux;
  double error;
  FluxErrorPair(double flux, double error) :
      flux(flux), error(error) {
  }
  bool operator==(const FluxErrorPair& other) const {
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wfloat-equal"
	  return this->flux == other.flux && this->error == other.error;
#pragma GCC diagnostic pop
  }
  bool operator!=(const FluxErrorPair& other) const {
	  return !(*this == other);
  }
};

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
class ELEMENTS_API Photometry: public Attribute {

public:

  /**
   * Iterator for the photometry flux and error values. See the Photometry_test to see
   * how this can be used to iterate through the flux and error the different filters.
   */
  class PhotometryConstIterator : public std::iterator<std::forward_iterator_tag,
      const FluxErrorPair> {
  public:
    PhotometryConstIterator(const std::vector<std::string>::const_iterator& filters_iter,
                            const std::vector<FluxErrorPair>::const_iterator& values_iter);
    PhotometryConstIterator& operator++();
    reference operator*();
    bool operator==(const PhotometryConstIterator& other) const;
    bool operator!=(const PhotometryConstIterator& other) const;
    const std::string& filterName() const;
  private:
    std::vector<std::string>::const_iterator m_filters_iter;
    std::vector<FluxErrorPair>::const_iterator m_values_iter;
  };
  typedef PhotometryConstIterator const_iterator;


  /**
   * @brief Constructor which should never be called directly. Use the
   * PhotometryAttributeHandler to build Photometry objects
   *
   * @param filter_name_vector_ptr
   *  a shared pointer to the vector of filter names
   * @param value_vector
   *  the vector of ValuePair, i..e, the flux values with their errors
   *
   */
  Photometry(std::shared_ptr<std::vector<std::string>> filter_name_vector_ptr,
      std::vector<FluxErrorPair> value_vector) :
      m_filter_name_vector_ptr(filter_name_vector_ptr), m_value_vector(
          std::move(value_vector)) {
    // Only check the size, but not the consistency
    if (m_filter_name_vector_ptr->size() != m_value_vector.size()) {
      throw Elements::Exception()
          << "The std::string and the flux vectors have different size";
    }
  }

  /// default destructor
  virtual ~Photometry() {
  }

  const_iterator begin() const {
    return const_iterator { m_filter_name_vector_ptr->cbegin(),
        m_value_vector.cbegin() };
  }

  const_iterator end() const {
    return const_iterator { m_filter_name_vector_ptr->cend(),
        m_value_vector.cend() };
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
  std::unique_ptr<FluxErrorPair> find(std::string filter_name) const;

private:

  /// Shared pointer to the common list of filter names
  std::shared_ptr<std::vector<std::string>> m_filter_name_vector_ptr;

  /// The photometry map
  std::vector<FluxErrorPair> m_value_vector;

};
// Eof class Photometry

} /* namespace SourceCatalog */
} // end of namespace Euclid

#endif /* PHOTOMETRY_H_ */
