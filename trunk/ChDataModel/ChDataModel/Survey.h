/**
 * @file Survey.h
 *
 * @author Pierre Dubath
 *
 * Created on: Feb. 6, 2013
 */

#ifndef SURVEY_H_
#define SURVEY_H_

#include <string>
#include <vector>
#include <map>
#include "ChDataModel/Enumerations/SurveyNames.h"
#include "ChDataModel/Catalog.h"
#include "ChDataModel/Filter.h"
#include "ChDataModel/Sed.h"

namespace ChDataModel {

/*
 * @class Survey contains a container of catalogs
 */
class Survey {

public:

  /**
   * @brief Constructor with member assignment (as enum class SurveyNames)
   */
  Survey(const SurveyNames surveyName) :
      m_survey_name(surveyName) {
  }

  /**
   * @brief Constructor with member assignment (as string)
   */
  Survey(const std::string & surveyName) :
      m_survey_name(string2surveyNames(surveyName)) {
  }

  /**
   * @brief Virtual destructor
   */
  virtual ~Survey() {
  }

  /**
   * @brief getSurveyName
   * @return
   *   The survey name
   */
  SurveyNames getSurveyName() const {
    return m_survey_name;
  }

  /**
   * @brief getCatalogMap
   * @return
   *   The whole catalog map
   */
  std::map<int, Catalog>& getCatalogMap() {
    return m_catalog_map;
  }

  /**
   * @brief getFilterMap
   * @return
   *   The whole filter map
   */
  const std::map<FilterNames, Filter>& getFilterMap() const {
    return m_filter_map;
  }

  /**
   * @brief setFilterMap
   * @param filterMap
   *   Sets the data member filter map
   */
  void setFilterMap(const std::map<FilterNames, Filter>& filterMap) {
    m_filter_map = filterMap;
  }

  /**
   * @brief getSedMap
   * @return
   *   The whole sed map
   */
  const std::map<SedNames, Sed>& getSedMap() const {
    return m_sed_map;
  }

  /**
   * @brief setSedMap
   * @param sedMap
   *   Sets the data member sed map
   */
  void setSedMap(const std::map<SedNames, Sed>& sedMap) {
    m_sed_map = sedMap;
  }

  /**
   * @brief getFirstCatalog
   * @return
   *   The reference to the first catalog from the map of catalogs
   */
  Catalog & getFirstCatalog();

  /**
   * @brief createCatalog
   *   Create a catalog and add it into the map of catalogs in this survey
   * @return
   *   The reference to the created catalog
   */
  Catalog & createCatalog();

  /**
   * @brief printCatalogsInSurvey
   *   Prints all catalog objects contained in the survey, and consecutively
   *   all contained source objects and all contained photometry objects
   */
  void printCatalogsInSurvey();

  /**
   * @brief printFiltersInSurvey
   *   Prints all filter objects contained in the survey
   */
  void printFiltersInSurvey();

  /**
   * @brief printSedsInSurvey
   *   Prints all SED objects contained in the survey
   */
  void printSedsInSurvey();

  /**
   * @brief printSurvey
   *   Prints all catalogs, filters and SEDs contained in the survey
   */
  void printSurvey();

private:

  /// Unique name of the survey
  const SurveyNames m_survey_name = SurveyNames::None;

  /// Map of catalogs
  std::map<int, Catalog> m_catalog_map { };

  /// Map of filters
  std::map<FilterNames, Filter> m_filter_map { };

  /// Map of sed's
  std::map<SedNames, Sed> m_sed_map { };

  //---------------------------------------------------------------------------

public:

   /**
   * Inner class Iterator which simplify the syntax for iterating
   * over all catalog, filter and SED objects
   */

  template<class T1, class T2>
  class Iterator {

  public:

    /// Constructor
    Iterator(typename std::map<T1, T2>::iterator itr) {
      m_itr = itr;
    }
    /// Copy constructor
    Iterator(const Iterator& o) {
      m_itr = o.m_itr;
    }
    /// Destructor
    ~Iterator() {
    }
    /// Assignment operator
    Iterator& operator=(const Iterator& o) {
      if (&o != this)
        m_itr = o.m_itr;
      return *this;
    }
    /// Post increment, calls pre-increment on this
    Iterator operator++(int) {
      Iterator tmp(*this);
      this->operator++();
      return tmp;
    }
    /// Pre increment
    Iterator& operator++() {
      ++m_itr;
      return *this;
    }
    /// Indirection operator
    T2 & operator*() {
      return m_itr->second;
    }
    /// Dereference operator
    T2 * operator->() {
      return &(m_itr->second);
    }
    /// Equal to operator
    bool operator==(const Iterator& o) const {
      return m_itr == o.m_itr;
    }
    /// Not equal to operator
    bool operator!=(const Iterator& o) const {
      return m_itr != o.m_itr;
    }

  private:

    /// Iterator of the parent container
    typename std::map<T1, T2>::iterator m_itr;

  }; // Eof class Iterator

  typedef Iterator<int, Catalog> CatalogIterator;
  typedef Iterator<FilterNames, Filter> FilterIterator;
  typedef Iterator<SedNames, Sed> SedIterator;

  /// Begin operator of the catalog container
  CatalogIterator catalogBegin() {
    return CatalogIterator(m_catalog_map.begin());
  }
  /// End operator of the catalog container
  CatalogIterator catalogEnd() {
    return CatalogIterator(m_catalog_map.end());
  }
  /// Size of the catalog container
  size_t catalogSize() {
    return m_catalog_map.size();
  }

  /// Begin operator of the filter container
  FilterIterator filterBegin() {
    return FilterIterator(m_filter_map.begin());
  }
  /// End operator of the filter container
  FilterIterator filterEnd() {
    return FilterIterator(m_filter_map.end());
  }
  /// Size of the filter container
  size_t filterSize() {
    return m_filter_map.size();
  }

  /// Begin operator of the SED container
  SedIterator sedBegin() {
    return SedIterator(m_sed_map.begin());
  }
  /// End operator of the SED container
  SedIterator sedEnd() {
    return SedIterator(m_sed_map.end());
  }
  /// Size of the SED container
  size_t sedSize() {
    return m_sed_map.size();
  }

};
// Eof class Survey

} /* namespace ChDataModel */

#endif /* SURVEY_H_ */
