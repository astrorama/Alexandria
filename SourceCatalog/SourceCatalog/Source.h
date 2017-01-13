/**
 * @file SourceCatalog/Source.h
 *
 * Created on: Jan 21, 2014
 *     Author: Pierre Dubath
 */
#ifndef SOURCE_H_
#define SOURCE_H_

#include <string>
#include <vector>
#include <memory>

#include "ElementsKernel/Exception.h"

#include "SourceCatalog/SourceAttributes/Photometry.h"
#include "SourceCatalog/SourceAttributes/SpectroscopicRedshift.h"
#include "SourceCatalog/SourceAttributes/Coordinates.h"
#include "SourceCatalog/Attribute.h"

namespace Euclid {
namespace SourceCatalog {

/**
 * @class Source
 * @brief
 * The Source class includes all information related to a sky source
 */
class Source {

public:
  /**
   * @brief Constructor
   * @param source_id
   *  Source identifier
   * @param  attibuteVector
   * Vector of shared pointers on Attribute objects
   */
  Source(int64_t source_id, std::vector<std::shared_ptr<Attribute>> attibuteVector)
        : m_source_id(source_id), m_attribute_vector( std::move(attibuteVector) ) {
  }

  /// Virtual default destructor
  virtual ~Source() { }

  /**
   * @brief Get the source ID
   * @return The source ID
   */
  int64_t getId() const {
    return m_source_id;
  }

  /**
   * @brief Get a pointer to source attribute of type T or a null pointer
   *    if the source do not contain an attribute of type T
   *
   * @details Typical usage is std::shared_ptr<Photometry>
   *  a_photometric_attribute = source.getAttribute<Photometry>(), where Photometry can be replaced
   *  by any other attributes
   * @return The pointer to the attribute or nullptr if the attribute is
   *  not found
   */
  template<typename T>
  std::shared_ptr<T> getAttribute() const;


 private:

  // Source identification
  int64_t m_source_id { };

  // Vector of shared pointers to attribute
  std::vector<std::shared_ptr<Attribute>> m_attribute_vector;

};
// Eof class Source

#define SOURCE_IMPL
#include "SourceCatalog/_impl/Source.icpp"
#undef SOURCE_IMPL

} /* namespace SourceCatalog */
} // end of namespace Euclid

#endif /* SOURCE_H_ */
