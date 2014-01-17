/**
 * @file Source.h
 *
 * @author Pierre Dubath
 *
 * Created on: Jan 31, 2013
 */

#ifndef SOURCE_H_
#define SOURCE_H_

#include <string>
#include <map>

#include "ChDataModel/Photometry.h"

namespace ChDataModel {

/**
 * The Source class include all information related to a sky source
 */
class Source {

public:

  Source() {}
  /// Constructor with member assignment
  Source(int64_t source_id) : m_source_id(source_id) {
  }

  /// Virtual default destructor
  virtual ~Source() {
  }

  const int64_t getSourceId() const {
    return m_source_id;
  }

private:

  /// Source identification (attributed in the survey)
  const int64_t m_source_id {};

}; // Eof class Source

} /* namespace ChDataModel */
#endif /* SOURCE_H_ */
