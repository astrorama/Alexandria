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

/// Forward declaration
class Survey;

/**
 * Catalog contains a container of sources
 */
class Catalog {

public:

  /// Default constructor
  Catalog() = default;

  /// Constructor with member assignment
  Catalog(Survey & survey) :
      m_survey_ptr(&survey) {
  }

  /// Virtual default destructor
  virtual ~Catalog() {
  }

  /// Setter
  /// @param survey_ptr A pointer to the encompassing survey
  void setSurveyPtr(Survey * survey_ptr) {
    m_survey_ptr = survey_ptr;
  }

  /// Getter
  /// @return A back pointer to the encompassing survey
  Survey * getSurveyPtr() const {
    return m_survey_ptr;
  }

  /// Getter
  /// @return The container of sources
  std::map<int64_t, Source>& getSourceMap() {
    return m_source_map;
  }

  /// Get one source from the container of sources
  /// @return The source with the given sourceID
  Source & getSource(int64_t source_id);

  /// Add a source into the container of sources in this catalog
  /// @return Reference to the created source, added to the catalog container
  Source & addSource(const Source & source);

  /**
   * @brief printCatalog
   *   Prints the contents of the catalog object, all contained
   *   source objects and all contained photometry objects
   */
  void printCatalog();

private:

  /// The pointer to the encompassing survey
  Survey * m_survey_ptr { nullptr };

  /// The source map
  std::map<int64_t, Source> m_source_map { };

  //---------------------------------------------------------------------------

public:

  /**
   * Inner class SourceIterator which simplify the syntax for iterating
   * over all source elements.
   */
  class SourceIterator {

  public:

    /// Constructor
    SourceIterator(std::map<int64_t, Source>::iterator itr) {
      m_itr = itr;
    }
    /// Copy constructor
    SourceIterator(const SourceIterator& o) {
      m_itr = o.m_itr;
    }
    /// Destructor
    ~SourceIterator() {
    }
    /// Assignment operator
    SourceIterator& operator=(const SourceIterator& o) {
      if (&o != this)
        m_itr = o.m_itr;
      return *this;
    }
    /// Post increment, calls pre-increment on this
    SourceIterator operator++(int) {
      SourceIterator tmp(*this);
      this->operator++();
      return tmp;
    }
    /// Pre increment
    SourceIterator& operator++() {
      ++m_itr;
      return *this;
    }
    /// Indirection operator
    Source & operator*() {
      return m_itr->second;
    }
    /// Dereference operator
    Source * operator->() {
      return &(m_itr->second);
    }
    /// Equal to operator
    bool operator==(const SourceIterator& o) const {
      return m_itr == o.m_itr;
    }
    /// Not equal to operator
    bool operator!=(const SourceIterator& o) const {
      return m_itr != o.m_itr;
    }

  private:

    /// Iterator of the parent container
    std::map<int64_t, Source>::iterator m_itr;

  }; // Eof class SourceIterator

  /// Begin operator of the container
  SourceIterator begin() {
    return SourceIterator(m_source_map.begin());
  }
  /// End operator of the container
  SourceIterator end() {
    return SourceIterator(m_source_map.end());
  }
  /// Size of the container
  size_t size() {
    return m_source_map.size();
  }

};

} /* namespace ChDataModel */

#endif /* CATALOG_H_ */
