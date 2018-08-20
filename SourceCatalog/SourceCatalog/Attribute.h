/*
 * Copyright (C) 2012-2020 Euclid Science Ground Segment    
 *  
 * This library is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free 
 * Software Foundation; either version 3.0 of the License, or (at your option)  
 * any later version.  
 *  
 * This library is distributed in the hope that it will be useful, but WITHOUT 
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more  
 * details.  
 *  
 * You should have received a copy of the GNU Lesser General Public License 
 * along with this library; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA  
 */
 
 /**
 * @file SourceCatalog/Attribute.h
 *
 * Created on: Jan 20, 2014
 *     Author: Pierre Dubath
 */
#ifndef ATTRIBUTE_H_
#define ATTRIBUTE_H_

namespace Euclid {
namespace SourceCatalog {

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
} // end of namespace Euclid

#endif // ATTRIBUTE_H_ 
