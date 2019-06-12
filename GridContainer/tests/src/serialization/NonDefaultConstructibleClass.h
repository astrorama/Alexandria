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
 * @file tests/src/serialization/NonDefaultConstructibleClass.h
 * @date June 27, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef GRIDCONTAINER_NONDEFAULTCONSTRUCTIBLECLASS_H
#define	GRIDCONTAINER_NONDEFAULTCONSTRUCTIBLECLASS_H

#include "GridContainer/GridCellManagerTraits.h"

class NonDefaultConstructibleClass {
public:
  NonDefaultConstructibleClass(double v) : value{v} {}
  double value;
};

namespace boost {
namespace serialization {

template<typename Archive>
void serialize(Archive&, NonDefaultConstructibleClass&, const unsigned int) { }

template<typename Archive>
void save_construct_data(Archive &ar, const NonDefaultConstructibleClass* p, const unsigned int) {
  double v = p->value;
  ar << v;
}

template<typename Archive>
void load_construct_data(Archive &ar, NonDefaultConstructibleClass* p, const unsigned int) {
  double v;
  ar >> v;
  ::new(p) NonDefaultConstructibleClass(v);
}

}
}

namespace Euclid {
namespace GridContainer {

template<>
struct GridCellManagerTraits<std::vector<NonDefaultConstructibleClass>> {
  typedef NonDefaultConstructibleClass data_type;
  typedef typename std::vector<NonDefaultConstructibleClass>::iterator iterator;
  static std::unique_ptr<std::vector<NonDefaultConstructibleClass>> factory(size_t size) {
    return std::unique_ptr<std::vector<NonDefaultConstructibleClass>> {new std::vector<NonDefaultConstructibleClass>(size, NonDefaultConstructibleClass{0})};
  }
  static size_t size(const std::vector<NonDefaultConstructibleClass>& vector){
    return vector.size();
  }
  static iterator begin(std::vector<NonDefaultConstructibleClass>& vector) {
    return vector.begin();
  }
  static iterator end(std::vector<NonDefaultConstructibleClass>& vector) {
    return vector.end();
  }
  static const bool enable_boost_serialize = true;
  
};

}
} // end of namespace Euclid

#endif	/* GRIDCONTAINER_NONDEFAULTCONSTRUCTIBLECLASS_H */

