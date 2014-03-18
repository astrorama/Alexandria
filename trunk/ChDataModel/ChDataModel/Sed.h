/**
 * @file Sed.h
 *
 * Created on: May 16, 2013
 *     Author: Pavel Binko
 */

#ifndef SED_H_
#define SED_H_

#include "ChDataModel/VectorPair.h"
#include "ChDataModel/Enumerations/SedNames.h"

namespace ChDataModel {

/**
 * Class Sed (for Spectral Energy Distribution) is using a VectorPair
 * as the main field. It stores the Intensity (X axis) as a function
 * of wave length (Y axis).
 */
class Sed {

public:

  /**
   * @brief Constructor
   */
  Sed() = default;

  /**
   * @brief Constructor with assignment of all members,
   * i.e., the vectors and the sed name
   */
  Sed(std::vector<double> & waveLengths, std::vector<double> & intensities,
      SedNames sedName, bool check_sort_unique = false);

  /**
   * @brief Constructor with assignment of all members,
   * i.e., the vector pair and the sed name
   */
  Sed(ChDataModel::VectorPair vectorPair, SedNames sedName);

  /**
   * @brief Default destructor
   */
  virtual ~Sed() {
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
    return m_sed_curve.getX(i);
  }

  /**
   * @brief getWaveLengths
   * @return
   *   The whole X axis
   */
  const std::vector<double> getWaveLengths() const {
    return m_sed_curve.getAxisX();
  }

  /**
   * @brief getIntensity
   * @param i
   *   Index on the Y axis
   * @return
   *   The i-th value on the Y axis
   */
  double getIntensity(const int i) const {
    return m_sed_curve.getY(i);
  }

  /**
   * @brief getIntensities
   * @return
   *   The i-th value on the Y axis
   */
  const std::vector<double> getIntensities() const {
    return m_sed_curve.getAxisY();
  }

  //---------------------------------------------------------------------------

  /**
   * @brief getSedName
   * @return
   *   The sed name (as class enum SedNames)
   */
  const SedNames & getSedName() const {
    return m_name;
  }

  //---------------------------------------------------------------------------

  /**
   * @brief size
   * @return
   *   The size (the length, the number of elements) of the axis
   */
  size_t size() const {
    return m_sed_curve.size();
  }

  //---------------------------------------------------------------------------

  /**
   * @brief printSed
   *   The print method prints the contents of the filter object
   */
  void printSed();

  //---------------------------------------------------------------------------

  void setSedName(const SedNames & sedName) {
    m_name = sedName;
  }
  void setSedCurve(const VectorPair & sedCurve) {
    m_sed_curve = sedCurve;
  }

  //---------------------------------------------------------------------------

private:

  /**
   * The vectorPair holding the two vectors
   */
  VectorPair m_sed_curve { };

  /**
   * Name of the Sed
   */
  SedNames m_name { SedNames::None };

}; // Eof class Sed

} /* namespace ChDataModel */

#endif /* SED_H_ */
