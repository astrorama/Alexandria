/*
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
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
 * @file SourceCatalog/Source.h
 *
 * Created on: Jan 21, 2014
 *     Author: Pierre Dubath
 */
#ifndef SOURCE_H_
#define SOURCE_H_

#include <boost/variant.hpp>
#include <memory>
#include <string>
#include <vector>

#include "ElementsKernel/Exception.h"

#include "SourceCatalog/Attribute.h"
#include "SourceCatalog/SourceAttributes/Coordinates.h"
#include "SourceCatalog/SourceAttributes/Photometry.h"
#include "SourceCatalog/SourceAttributes/SpectroscopicRedshift.h"

namespace Euclid {
namespace SourceCatalog {

/**
 * @class Source
 * @brief
 * The Source class includes all information related to a sky source
 */
class Source {

public:
  typedef boost::variant<int64_t, std::string> id_type;

  /**
   * @brief Constructor
   * @param source_id
   *  Source identifier
   * @param  attributeVector
   * Vector of shared pointers on Attribute objects
   */
  Source(id_type source_id, std::vector<std::shared_ptr<Attribute>> attributeVector)
      : m_source_id(source_id), m_attribute_vector(std::move(attributeVector)) {}

  /// Virtual default destructor
  virtual ~Source() = default;

  /**
   * @brief Get the source ID
   * @return The source ID
   */
  id_type getId() const {
    return m_source_id;
  }

  /**
   * @brief Get a pointer to source attribute of type T or a null pointer
   *    if the source do not contain an attribute of type T
   *
   * @details An example usage is
   *
   * std::shared_ptr<Photometry> a_photometric_attribute = source.getAttribute<Photometry>()
   *
   * where Photometry can be replaced by any other attributes.
   *
   * @return The pointer to the attribute or nullptr if the attribute is
   *  not found
   */
  template <typename T>
  std::shared_ptr<T> getAttribute() const;

private:
  // Source identification
  id_type m_source_id{};

  // Vector of shared pointers to attribute
  std::vector<std::shared_ptr<Attribute>> m_attribute_vector;
};
// Eof class Source

/**
 * @class CastSourceIdVisitor
 * @brief
 * This type can be used together with boost::apply_visitor to cast boost::variant
 * with an unknown underlying type, to a Source::id_type
 */
class CastSourceIdVisitor : public boost::static_visitor<Source::id_type> {
  template <typename From>
  static constexpr bool is_integer() {
    return std::is_integral<From>::value && !std::is_same<From, bool>::value;
  }

public:
  CastSourceIdVisitor() = default;

  Source::id_type operator()(const std::string& from) const {
    return from;
  }

  template <typename From>
  Source::id_type operator()(const From& from, typename std::enable_if<is_integer<From>()>::type* = 0) const {
    return Source::id_type(static_cast<int64_t>(from));
  }

  template <typename From>
  Source::id_type operator()(const From&, typename std::enable_if<!is_integer<From>()>::type* = 0) const {
    throw Elements::Exception() << "Only std::string and int64_t are supported types for a source ID, got "
                                << typeid(From).name() << " instead";
  }
};

#define SOURCE_IMPL
#include "SourceCatalog/_impl/Source.icpp"
#undef SOURCE_IMPL

} /* namespace SourceCatalog */
}  // end of namespace Euclid

#if BOOST_VERSION < 105800
namespace boost {

/**
 * @brief
 *  boost::variant specifies an equality operator (==), but, in older boost versions, *not* an inequality one
 *  CCfits expects != to be defined, so we do it here
 */
inline bool operator!=(const Euclid::SourceCatalog::Source::id_type& a,
                       const Euclid::SourceCatalog::Source::id_type& b) {
  return !(a == b);
}

}  // namespace boost
#endif

#endif /* SOURCE_H_ */
