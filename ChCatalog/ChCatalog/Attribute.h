/**
 * @file ChCatalog/Attribute.h
 *
 * Created on: Jan 20, 2014
 *     Author: Pierre Dubath
 */
#ifndef ATTRIBUTE_H_
#define ATTRIBUTE_H_

namespace ChCatalog {

/**
 * @class Attribute
 * @brief
 * Attribute interface extended by all source attributes
 *
 * @details
 * This interface that must be extended by all kind of source attributes, such
 * as coordinates or photometry. A Source includes a vector of attributes of
 * arbitrary type.
 */
class Attribute {
public:
  virtual ~Attribute() { }

};

} // namespace ChDataModel 

#endif // ATTRIBUTE_H_ 
