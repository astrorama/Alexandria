/**
 * @file Catalog.h
 *
 * @author Pierre Dubath
 *
 * Created on: Feb 1, 2013
 */

#ifndef CATALOG_H_
#define CATALOG_H_

#include <map>
#include "ChDataModel/Source.h"

namespace ChDataModel {

/**
 * Catalog contains a container of sources
 */
class Catalog {

public:

  /// Default constructor
  Catalog() = default;

  /// Constructor with member assignment
  Catalog(std::map<int64_t, Source> source_map) :
      m_source_map(source_map) {
  }

  /// Virtual default destructor
  virtual ~Catalog() {
  }

  const std::map<int64_t, Source>& getSourceMap() const {
    return m_source_map;
  }

  /// Get one source from the container of sources
  /// @return The source with the given sourceID
  Source & getSource(int64_t source_id);

  /// Add a source into the container of sources in this catalog
  /// @return Reference to the created source, added to the catalog container
  void addSource(const Source & source);

private:

  /// The source map
  std::map<int64_t, Source> m_source_map { };

};

} /* namespace ChDataModel */

#endif /* CATALOG_H_ */
