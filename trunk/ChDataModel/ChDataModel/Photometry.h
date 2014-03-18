/**
 * @file Photometry.h
 *
 * @author Pierre Dubath
 *
 * Created on: Jan 30, 2013
 */

#ifndef PHOTOMETRY_H_
#define PHOTOMETRY_H_

#include "ChDataModel/Enumerations/FilterNames.h"
#include "ChDataModel/Enumerations/PhotometryTypes.h"

namespace ChDataModel {

/// Forward declaration
class Source;

/// Source pointer type
typedef Source* SourcePtr;

/**
 * The Photometry class is design to store a photometric measurement
 * obtained throw the specified filter (filterName).
 * The photometric "values" can be of different types:
 *
 *  - flux
 *  - AB magnitude
 *  - Vega magnitude
 *
 * as indicated by the "photometry type". All fields are constant and
 * should be provided to the constructor, except for the source "back" pointer,
 * that can be set. This allows to create "free floating" photometric objects,
 * that can be associated to a given source later.
 */
class Photometry {

public:

  /// default constructor
  Photometry();
  /// constructor with members assignment
  Photometry(SourcePtr source_ptr, const FilterNames filter_name,
      const PhotometryTypes photometry_type, const double value,
      const double value_error);
  /// constructor with members assignment, but without source back pointer
  Photometry(const FilterNames filter_name,
      const PhotometryTypes photometry_type, const double value,
      const double valueError);
  /// default destructor
  virtual ~Photometry() {
  }

  /**
   * @brief setSourcePtr
   * @param source_ptr
   *   The pointer to the parent source
   */
  void setSourcePtr(const SourcePtr source_ptr) {
    m_source_ptr = source_ptr;
  }

  /**
   * @brief getSourcePtr
   * @return
   *   The pointer to the parent source
   */
  SourcePtr getSourcePtr() const {
    return m_source_ptr;
  }

  /**
   * @brief getFilterName
   * @return
   *   The filter name
   */
  FilterNames getFilterName() const {
    return m_filter_name;
  }

  /**
   * @brief getPhotometryType
   * @return
   *   The photometry type
   */
  PhotometryTypes getPhotometryType() const {
    return m_photometry_type;
  }

  /**
   * @brief getValue
   * @return
   *   The photometry value
   */
  double getValue() const {
    return m_value;
  }

  /**
   * @brief getValueError
   * @return
   *   The photometry value error
   */
  double getValueError() const {
    return m_value_error;
  }

  /**
   * @brief getAbMagnitude
   *   Return the AB magnitude, either directly from the stored values
   *   if photometryType == AB_Magnitude
   *   or calling conversion tools if it is not the case.
   * @return
   *   The AB magnitude
   */
  double getAbMagnitude() const;

  /**
   * @brief printPhotometry
   *   Prints the contents of the photometry object
   */
  void printPhotometry();

private:
  /// The pointer to the parent source
  SourcePtr m_source_ptr;
  /// The filter name
  const FilterNames m_filter_name;
  /// The photometry types (flux, AB or Vega Magnitude)
  const PhotometryTypes m_photometry_type;
  /// The flux value
  const double m_value;
  /// The flux uncertainty value
  const double m_value_error;

}; // Eof class Photometry

} /* namespace ChDataModel */

#endif /* PHOTOMETRY_H_ */
