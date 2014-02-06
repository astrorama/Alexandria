/**
 * @file Source.h
 *
 * Created on: Jan 21, 2014
 *     Author: Pierre Dubath
 */
#ifndef SOURCE_H_
#define SOURCE_H_

#include <string>
#include <vector>
#include <memory>

#include "ElementsKernel/ElementsException.h"

#include "ChDataModel/SourceAttributes/Photometry.h"
#include "ChDataModel/SourceAttributes/SpectroscopicRedshift.h"
#include "ChDataModel/SourceAttributes/Coordinates.h"
#include "ChDataModel/Attribute.h"

namespace ChDataModel {

/**
* @class Source
 * @brief The Source class include all information related to a sky source
 */
class Source {

public:
  /**
   * @brief Constructor
   * @param source_id
   *  Source identification
   * @param  vector<std::shared_ptr<Attribute>>
   * Vector of shared pointer on Attribute objects
   */
  Source(uint64_t source_id, std::vector<std::shared_ptr<Attribute>> attibuteVector)
        : m_source_id(source_id), m_attribute_vector(attibuteVector) {
  }

  /// Virtual default destructor
  virtual ~Source() { }

  /**
   * @brief Get the source ID
   * @return The source ID
   */
  uint64_t getId() const {
    return m_source_id;
  }

  /**
   * @brief Get a pointer to source attribute of type T or a null pointer
   *    if the source do not contain
   *    an attribute of type T
   * @return The pointer to the attribute or nullptr if
   *    the attribute is not found
   */
  template<typename T>
  std::shared_ptr<T> getAttribute();


 private:

  /// Source identification
  uint64_t m_source_id { };

  /// Vector of shared pointers to attribute
  std::vector<std::shared_ptr<Attribute>> m_attribute_vector;

};
// Eof class Source

#define SOURCE_IMPL
#include "ChDataModel/_impl/Source.icpp"
#undef SOURCE_IMPL

} /* namespace ChDataModel */

#endif /* SOURCE_H_ */
