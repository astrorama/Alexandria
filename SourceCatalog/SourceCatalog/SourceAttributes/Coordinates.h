/**
 * @file SourceCatalog/SourceAttributes/Coordinates.h
 *
 * Created on: Jan 22, 2014
 *     Author: Pierre Dubath
 */
#ifndef COORDINATES_H_
#define COORDINATES_H_

#include "SourceCatalog/Attribute.h"

namespace Euclid {
namespace SourceCatalog {

/**
 * @class Coordinates
 * @brief Store the Right Ascension (Ra) and Delination (Dec) of a source in
 * decimal degrees, i.e.,
 *    0.0 < Ra  < 360.00
 *  -90.0 < Dec <  90.0
 *
 */
class Coordinates : public Attribute {
public:
  Coordinates(double ra, double dec) : m_ra(ra), m_dec(dec) {}
  virtual ~Coordinates() {}

  double getDec() const { return m_dec; }

  double getRa() const { return m_ra; }

private:
  double m_ra {};
  double m_dec {};

};

} // namespace SourceCatalog
} // end of namespace Euclid

#endif // COORDINATES_H_ 
