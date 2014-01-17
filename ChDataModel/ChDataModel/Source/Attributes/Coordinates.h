/**
 * @file Coordinates.h
 *
 * @date Jan 16, 2014
 * @author dubath
 */

#ifndef COORDINATES_H_
#define COORDINATES_H_

namespace ChDataModel {

class Coordinates : public Attribute {
public:
  Coordinates(double ra, double dec) : m_ra(ra), m_dec(dec) {}
  virtual ~Coordinates() {}

  const double getDec() const {
    return m_dec;
  }

  const double getRa() const {
    return m_ra;
  }

private:
  const double m_ra {};
  const double m_dec {};

};

} // namespace ChDataModel 

#endif // COORDINATES_H_ 
