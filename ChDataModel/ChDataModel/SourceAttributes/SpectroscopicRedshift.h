/**
 * @file SpectroscopicRedshift.h
 *
 * @date Jan 16, 2014
 * @author dubath
 */

#ifndef SPECTROSCOPICREDSHIFT_H_
#define SPECTROSCOPICREDSHIFT_H_

namespace ChDataModel {

class SpectroscopicRedshift : public Attribute {
public:
  SpectroscopicRedshift(double value, double error) : m_value(value), m_error(error) {}
  virtual ~SpectroscopicRedshift();

  const double getError() const {
    return m_error;
  }

  const double getValue() const {
    return m_value;
  }

private:

  const double m_value {};

  const double m_error {};
};

} // namespace ChDataModel 

#endif // SPECTROSCOPICREDSHIFT_H_ 
