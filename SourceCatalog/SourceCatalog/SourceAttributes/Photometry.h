/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
 *
 * This library is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free
 * Software Foundation; either version 3.0 of the License, or (at your option)
 * any later version.
 *
 * This library is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
 * details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this library; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 */

/**
 * @file SourceCatalog/SourceAttributes/Photometry.h
 *
 * Created on: Jan 17, 2014
 *     Author: Pierre Dubath
 */

#ifndef PHOTOMETRY_H_
#define PHOTOMETRY_H_

#include <iterator>
#include <memory>
#include <vector>

#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Export.h"

#include "SourceCatalog/Attribute.h"

namespace Euclid {
namespace SourceCatalog {

struct FluxErrorPair {
  double flux;
  double error;
  bool   missing_photometry_flag;
  bool   upper_limit_flag;
  FluxErrorPair(double flux, double error, bool missing_photometry_flag = false, bool upper_limit_flag = false);
  FluxErrorPair(const FluxErrorPair&) = default;
  bool operator==(const FluxErrorPair& other) const;
  bool operator!=(const FluxErrorPair& other) const;
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
class ELEMENTS_API Photometry : public Attribute {

public:
  /**
   * Iterator class, implemented as a template to avoid repetition for const and non const iterators
   * @tparam Const
   *    A boolean. If true, this will be a const iterator
   */
  template <bool Const>
  class PhotometryIterator : public std::iterator<std::forward_iterator_tag,
                                                  typename std::conditional<Const, const FluxErrorPair, FluxErrorPair>::type> {
  public:
    using value_t = typename std::conditional<Const, const FluxErrorPair, FluxErrorPair>::type;
    using typename std::iterator<std::forward_iterator_tag, value_t>::reference;
    using typename std::iterator<std::forward_iterator_tag, value_t>::pointer;

    using filters_iter_t =
        typename std::conditional<Const, std::vector<std::string>::const_iterator, std::vector<std::string>::iterator>::type;
    using values_iter_t =
        typename std::conditional<Const, std::vector<FluxErrorPair>::const_iterator, std::vector<FluxErrorPair>::iterator>::type;

    /**
     * Constructor from non-const iterator
     */
    PhotometryIterator(const PhotometryIterator<false>& other);

    /**
     * Increment the iterator
     */
    PhotometryIterator& operator++();

    /**
     * @return true if this iterator and other point to the same position
     */
    bool operator==(const PhotometryIterator& other) const;

    /**
     * @return true if this iterator and other do *not* point to the same position
     */
    bool operator!=(const PhotometryIterator& other) const;

    /**
     * @return A reference to the FluxErrorPair pointed by this iterator
     */
    reference operator*();

    /**
     * @return A pointer to the FluxErrorPair pointed by this iterator
     */
    pointer operator->();

    /**
     * @return The number of elements between this iterator and other
     */
    ssize_t operator-(const PhotometryIterator& other) const;

    /**
     * @return The filter name corresponding to this FluxErrorPair
     */
    const std::string& filterName() const;

  protected:
    /**
     * Constructor
     * @param filters_iter
     *  Filter name iterator
     * @param values_iter
     *  FluxErrorPair iterator
     */
    PhotometryIterator(const filters_iter_t& filters_iter, const values_iter_t& values_iter);

    friend class Photometry;

  private:
    filters_iter_t m_filters_iter;
    values_iter_t  m_values_iter;
  };

  typedef PhotometryIterator<true>  const_iterator;
  typedef PhotometryIterator<false> iterator;

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
  Photometry(std::shared_ptr<std::vector<std::string>> filter_name_vector_ptr, std::vector<FluxErrorPair> value_vector)
      : m_filter_name_vector_ptr(filter_name_vector_ptr), m_value_vector(std::move(value_vector)) {
    if (m_filter_name_vector_ptr == nullptr) {
      throw Elements::Exception() << "Photometry filter names vector pointer is null";
    }
    // Only check the size, but not the consistency
    if (m_filter_name_vector_ptr->size() != m_value_vector.size()) {
      throw Elements::Exception() << "Photometry filter names vector has different size than the values vector";
    }
  }

  /// default destructor
  virtual ~Photometry() = default;

  const_iterator cbegin() const {
    return const_iterator{m_filter_name_vector_ptr->cbegin(), m_value_vector.cbegin()};
  }

  const_iterator cend() const {
    return const_iterator{m_filter_name_vector_ptr->cend(), m_value_vector.cend()};
  }

  const_iterator begin() const {
    return const_iterator{m_filter_name_vector_ptr->cbegin(), m_value_vector.cbegin()};
  }

  const_iterator end() const {
    return const_iterator{m_filter_name_vector_ptr->cend(), m_value_vector.cend()};
  }

  iterator begin() {
    return iterator{m_filter_name_vector_ptr->begin(), m_value_vector.begin()};
  }

  iterator end() {
    return iterator{m_filter_name_vector_ptr->end(), m_value_vector.end()};
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
  std::unique_ptr<FluxErrorPair> find(const std::string& filter_name) const;

  const std::shared_ptr<std::vector<std::string>>& getFilterNames() const;

private:
  /// Shared pointer to the common list of filter names
  std::shared_ptr<std::vector<std::string>> m_filter_name_vector_ptr;

  /// The photometry map
  std::vector<FluxErrorPair> m_value_vector;
};
// Eof class Photometry

#define PHOTOMETRY_IMPL
#include "SourceCatalog/_impl/Photometry.icpp"
#undef PHOTOMETRY_IMPL

} /* namespace SourceCatalog */
}  // end of namespace Euclid

#endif /* PHOTOMETRY_H_ */
