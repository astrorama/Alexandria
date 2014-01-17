/**
 * @file Attribute.h
 *
 * @date Jan 16, 2014
 * @author dubath
 */

#ifndef ATTRIBUTE_H_
#define ATTRIBUTE_H_

#include "AttributeName.h"

namespace ChDataModel {

class Attribute {
public:
  Attribute(AttributeName attribute_name) : m_attribute_name(attribute_name) {}
  virtual ~Attribute() {}

  const AttributeName getAttributeName() const {
    return m_attribute_name;
  }

private:
  const AttributeName m_attribute_name;
};

} // namespace ChDataModel 

#endif // ATTRIBUTE_H_ 
