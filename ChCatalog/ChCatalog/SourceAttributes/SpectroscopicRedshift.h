/**
 * @file SpectroscopicRedshift.h
 *
 * @date Jan 16, 2014
 * @author dubath
 */

#ifndef SPECTROSCOPICREDSHIFT_H_
#define SPECTROSCOPICREDSHIFT_H_

#include "ChCatalog/Attribute.h"

namespace ChCatalog {

/**
 * @class SpectroscopicRedshift
 *
 * @brief Store the spectroscopic redshift of a source
 *
 */
class SpectroscopicRedshift : public Attribute {
public:

  /**
 * @brief Constructor
 * @param value
 *  Value of the redshift
 * @param error
 *  Error value of the value parameter
 */
  SpectroscopicRedshift(double value, double error) : m_value(value), m_error(error) {}

  virtual ~SpectroscopicRedshift() {}

  double getValue() const { return m_value; }
  double getError() const { return m_error; }

private:

  double m_value {};
  double m_error {};
};

} // namespace ChCatalog

#endif // SPECTROSCOPICREDSHIFT_H_ 
