/**
 * @file Filter.h
 *
 * Created on: May 10, 2013
 *     Author: Pavel Binko
 */

#ifndef FILTER_H_
#define FILTER_H_

#include "ChDataModel/VectorPair.h"
#include "ChDataModel/Enumerations/FilterTypes.h"
#include "ChDataModel/Enumerations/FilterNames.h"

//#include <string>
//#include <vector>

namespace ChDataModel {

/**
 * Class Filter is using a VectorPair as the main field. It stores the total
 * filter efficiency, which is the total of efficiencies of the optics,
 * filter (itself) and CCD (Y axis) as a function of wave length (X axis).
 */
class Filter {

public:

  /**
   * @brief Constructor
   */
  Filter() = default;

  /**
   * @brief Constructor with assignment of all members,
   * i.e., the vectors, the filter type and the filter name
   */
  Filter(std::vector<double> & waveLengths, std::vector<double> & filterValues,
      FilterTypes filterType, FilterNames filterName,
      bool check_sort_unique = false);

  /**
   * @brief Constructor with assignment of all members,
   * i.e., the vector pair, the filter type and the filter name
   */
  Filter(ChDataModel::VectorPair vectorPair, FilterTypes filterType,
      FilterNames filterName);

  /**
   * @brief Default destructor
   */
  virtual ~Filter() {
  }

  //---------------------------------------------------------------------------

  /**
   * @brief getWaveLength
   * @param i
   *   Index on the X axis
   * @return
   *   The i-th value on the X axis
   */
  double getWaveLength(const int i) const {
    return m_filter_curve.getX(i);
  }

  /**
   * @brief getWaveLengths
   * @return
   *   The whole X axis
   */
  const std::vector<double> getWaveLengths() const {
    return m_filter_curve.getAxisX();
  }

  /**
   * @brief getEfficiencyValue
   * @param i
   *   Index on the Y axis
   * @return
   *   The i-th value on the Y axis
   */
  double getEfficiencyValue(const int i) const {
    return m_filter_curve.getY(i);
  }

  /**
   * @brief getEfficiencyValues
   * @return
   *   The whole Y axis
   */
  const std::vector<double> getEfficiencyValues() const {
    return m_filter_curve.getAxisY();
  }

  //---------------------------------------------------------------------------

  /**
   * @brief getFilterType
   * @return
   *   The filter type (as class enum FilterTypes)
   */
  const FilterTypes & getFilterType() const {
    return m_type;
  }

  /**
   * @brief getFilterName
   * @return
   *   The filter name (as class enum FilterNames)
   */
  const FilterNames & getFilterName() const {
    return m_name;
  }

  //---------------------------------------------------------------------------

  /**
   * @brief size
   * @return
   *   The size (the length, the number of elements) of the axis
   */
  size_t size() const {
    return m_filter_curve.size();
  }

  //---------------------------------------------------------------------------

  /**
   * @brief printFilter
   *   The print method prints the contents of the filter object
   */
  void printFilter();

  //---------------------------------------------------------------------------

private:

  /**
   * The vectorPair holding the two vectors
   */
  VectorPair m_filter_curve { };

  /**
   * Filter efficiency type (e.g. EUCLID, OPTICS, FILTER, CCD)
   *
   * EUCLID type stands for the total efficiency from the sky to the CCD
   */
  FilterTypes m_type { FilterTypes::None };

  /**
   * Filter name
   *
   * Coming either from an id provided within the corresponding file,
   * or if this is not available, the filename is used instead.
   */
  FilterNames m_name { FilterNames::None };

}; // Eof class Filter

} /* namespace ChDataModel */

#endif /* FILTER_H_ */
