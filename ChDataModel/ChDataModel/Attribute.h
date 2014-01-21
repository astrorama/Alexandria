/**
 * @file Attribute.h
 *
 * Created on: Jan 20, 2014
 *     Author: Pierre Dubath
 */
#ifndef ATTRIBUTE_H_
#define ATTRIBUTE_H_

#include "AttributeName.h"

namespace ChDataModel {

class Attribute {
public:
  Attribute() {
  }
  virtual ~Attribute() {
  }

  //  Attribute(AttributeName attribute_name) : m_attribute_name(attribute_name) {}
//  virtual ~Attribute() {}
//
//  AttributeName getAttributeName() const {
//    return m_attribute_name;
//  }
//
//private:
//  const AttributeName m_attribute_name;
};

} // namespace ChDataModel 

#endif // ATTRIBUTE_H_ 
