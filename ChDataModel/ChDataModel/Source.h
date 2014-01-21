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
 * The Source class include all information related to a sky source
 */
class Source {

public:

  /// Constructor with member assignment
  Source(int64_t source_id) :
      m_source_id(source_id) {
  }

  /// Virtual default destructor
  virtual ~Source() {
  }

  int64_t getSourceId() const {
    return m_source_id;
  }

  template<typename T>
  T* getAttribute() {
    // loop over all source attribute
    for (Attribute* attribute_ptr : m_attribute_ptr_vector) {
      if (dynamic_cast<T*>(attribute_ptr) != nullptr) {
        return dynamic_cast<T*>(attribute_ptr);
      }
    }
    return nullptr;
  }

  template<typename T>
  bool hasAttribute() {
    bool hasAttribute = false;
    // loop over all source attribute
    for (Attribute* attribute_ptr : m_attribute_ptr_vector) {
      if (dynamic_cast<T*>(attribute_ptr) != nullptr) {
        hasAttribute = true;
        break;
      }
    }
    return hasAttribute;
  }

  template<typename T>
  bool addAttribute(Attribute* attribute_ptr) {
    bool did_it = true;
    if (!hasAttribute<T>()) {
      m_attribute_ptr_vector.push_back(attribute_ptr);
    } else {
      did_it = false;
    }
    return did_it;
  }

private:

  /// Source identification (attributed in the survey)
  const int64_t m_source_id { };

  std::vector<Attribute*> m_attribute_ptr_vector;

};
// Eof class Source

} /* namespace ChDataModel */
#endif /* SOURCE_H_ */
