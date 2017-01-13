/**
 * @file SourceCatalog/SourceAttributes/SpectroscopicRedshift.h
 *
 * @date Jan 16, 2014
 * @author Pierre Dubath
 */

#ifndef SPECTROSCOPICREDSHIFT_H_
#define SPECTROSCOPICREDSHIFT_H_

#include "SourceCatalog/Attribute.h"

namespace Euclid {
namespace SourceCatalog {

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

} // namespace SourceCatalog
} // end of namespace Euclid

#endif // SPECTROSCOPICREDSHIFT_H_ 
