/**
 * @file Source.h
 *
 * Created on: Jan 21, 2014
 *     Author: Pierre Dubath
 */
#ifndef SOURCE_H_
#define SOURCE_H_

#include <string>
#include <map>
#include "ElementsKernel/ElementsException.h"

#include "ChDataModel/SourceAttributes/Photometry.h"
#include "ChDataModel/SourceAttributes/SpectroscopicRedshift.h"
#include "ChDataModel/SourceAttributes/Coordinates.h"
#include "ChDataModel/AttributeName.h"
#include "ChDataModel/Attribute.h"

namespace ChDataModel {

/**
* @class Source
 * @brief The Source class include all information related to a sky source
 */
class Source {

public:
  /// Constructor with source ID assignment
  Source(int64_t source_id) :
      m_source_id(source_id) {
  }
  /// Virtual default destructor
  virtual ~Source() { }

  /**
   * @brief Get the source ID
   *
   * @return The source ID
   */
  int64_t getSourceId() const {
    return m_source_id;
  }

  /**
   * @brief Get a pointer to source attribute of type T or a
   *    null pointer if the source do not contain
   *    an attribute of type T
   *
   * @return The pointer to the attribute or nullptr if
   *    the attribute is not found
   */
  template<typename T>
  T* getAttribute();

  /**
   * @brief Check whether a source has an attribute of type T
   *
   * @return true/false if the source has/has not an attribute of type T
   */
  template<typename T>
  bool hasAttribute();

  /**
   * @brief Add a pointer to an attribute of type T to the source
   *    if pointer to an attribute of type T is not already included
   *    in teh source
   *
   * @return true/false depending whether the adding was successful or not
   *
   */
  template<typename T>
  bool addAttribute(Attribute* attribute_ptr);

private:

  /// Source identification
  const int64_t m_source_id { };

  /// Vector of pointers to attribute (base class)
  std::vector<Attribute*> m_attribute_ptr_vector;

};
// Eof class Source

#define SOURCE_IMPL
#include "ChDataModel/_impl/Source.icpp"
#undef SOURCE_IMPL

} /* namespace ChDataModel */

#endif /* SOURCE_H_ */
