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

/// Forward declaration
class Catalog;

/// Catalog pointer type
typedef Catalog* CatalogPtr;

/**
 * The Source class include all information related to a sky source
 */
class Source {

public:
  /// Default constructor
  Source() = default;

  /// Constructor with member assignment
  Source(int64_t source_id, double ra, double dec);

  /// Virtual default destructor
  virtual ~Source() {
  }

  // Default assignment operator would be needed because of clang
  // Source& operator=(const Source & s) { ... }

  /// Getter
  /// @return The source ID (defined independently in each survey)
  int64_t getSourceId() const {
    return m_source_id;
  }
  /// Getter
  /// @return The right ascension <0;360) in degrees
  double getRa() const {
    return m_ra;
  }
  /// Getter
  /// @return The declination <-90;90> in degree
  double getDec() const {
    return m_dec;
  }

  /// Getter
  /// @return Pointer to the catalog in which this source is identified
  CatalogPtr getCatalogPtr() const {
    return m_catalog_ptr;
  }

  /// Setter
  /// @param catalogPtr pointer to the catalog in which this source shall be identified
  void setCatalogPtr(const CatalogPtr catalogPtr) {
    m_catalog_ptr = catalogPtr;
  }

  /// Getter
  /// @return The whole photometry map
  std::map<FilterNames, Photometry>& getPhotometryMap() {
    return m_photometry_map;
  }

  /// Getter
  /// @return The whole photometric attribute map
  const std::map<std::string, double> & getPhotometricAttributeMap() const {
    return m_photometric_attribute_map;
  }

  /// Add a photometry to this source
  /// @param photometry photometry object to be added
  /// @return Reference to the photometry object inserted in the container
  Photometry & addPhotometry(const Photometry & photometry);

  /// Add a photometric attribute to this source
  /// @param photometric_attribute_name the photometric attribute name
  /// @param photometric_attribute_value the photometric attribute value
  void addPhotometricAttribute(const std::string & photometric_attribute_name,
      const double photometric_attribute_value);

  /// Get the photometric value for a given filter
  /// @param filter_name filter name
  /// @return The photometry object
  Photometry & getPhotometry(FilterNames filter_name);

  /// Get the photometric attribute of a given name
  /// @param photometric_attribute_name the photometric attribute name.
  /// @return The photometric attribute value.
  double getPhotometricAttribute(const std::string & photometric_attribute_name);

  /**
   * @brief printPhotometry
   *   Prints the contents of the source object and all contained
   *   photometry objects
   */
  void printSource();

  double getAgnFlag() const {
    return m_agn_flag;
  }

  void setAgnFlag(double agn_flag) {
    m_agn_flag = agn_flag;
  }

  double getSpecZ() const {
    return m_spec_z;
  }

  void setSpecZ(double spec_z) {
    m_spec_z = spec_z;
  }

  double getSuperId() const {
    return m_super_id;
  }

  void setSuperId(double super_id) {
    m_super_id = super_id;
  }

private:

  /// Pointer to the catalog in which this source is identified
  //CatalogPtr m_catalog_ptr {nullptr};
  /// Source identification (attributed in the survey)
  const int64_t m_source_id {0};
  /// Source right ascension
  const double m_ra {0};
  /// Source declination
  const double m_dec {0};
  /**
   * Source spectroscopic redshift
   */
   double m_spec_z;

   /**
    * Source AGN flag (MER data)
    */
  double m_agn_flag;

  /**
   * Source super ID (MER data)
   */
   double m_super_id;

  /// The photometry map
  std::map<FilterNames, Photometry> m_photometry_map;
  /// The photometric attribute map
  std::map<std::string, double> m_photometric_attribute_map;


public:

  /**
   * Inner class PhotometryIterator which simplify the syntaxe for iterating over all photometry elements.
   *
   */
  class PhotometryIterator {

  public:

    /// Constructor
    PhotometryIterator(std::map<FilterNames, Photometry>::iterator itr) {
      m_itr = itr;
    }
    /// Copy constructor
    PhotometryIterator(const PhotometryIterator& o) {
      m_itr = o.m_itr;
    }
    /// Destructor
    ~PhotometryIterator() {
    }
    /// Assignment operator
    PhotometryIterator& operator=(const PhotometryIterator& o) {
      if (&o != this)
        m_itr = o.m_itr;
      return *this;
    }
    /// Post increment, calls pre-increment on this
    PhotometryIterator operator++(int) {
      PhotometryIterator tmp(*this);
      this->operator++();
      return tmp;
    }
    /// Pre increment
    PhotometryIterator& operator++() {
      ++m_itr;
      return *this;
    }
    /// Indirection operator
    Photometry & operator*() {
      return m_itr->second;
    }
    /// Dereference operator
    Photometry * operator->() {
      return &(m_itr->second);
    }
    /// Equal to operator
    bool operator==(const PhotometryIterator& o) const {
      return m_itr == o.m_itr;
    }
    /// Not equal to operator
    bool operator!=(const PhotometryIterator& o) const {
      return m_itr != o.m_itr;
    }

  private:

    /// Iterator of the parent container
    std::map<FilterNames, Photometry>::iterator m_itr;

  }; // Eof class PhotometryIterator

  /// Begin operator of the container
  PhotometryIterator begin() {
    return PhotometryIterator(m_photometry_map.begin());
  }
  /// End operator of the container
  PhotometryIterator end() {
    return PhotometryIterator(m_photometry_map.end());
  }
  /// Size of the container
  size_t size() {
    return m_photometry_map.size();
  }

}; // Eof class Source

} /* namespace ChDataModel */
#endif /* SOURCE_H_ */
