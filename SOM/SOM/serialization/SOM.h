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

/* 
 * @file SOM.h
 * @author nikoapos
 */

#ifndef SOM_SERIALIZATION_SOM_H
#define SOM_SERIALIZATION_SOM_H

#include <typeinfo>
#include <boost/serialization/array.hpp>
#include <boost/serialization/string.hpp>
#include <boost/serialization/split_free.hpp>
#include "ElementsKernel/Exception.h"
#include "SOM/SOM.h"

namespace boost {
namespace serialization {

template <class Archive, std::size_t ND, typename DistFunc>
void save(Archive& ar, const Euclid::SOM::SOM<ND, DistFunc>& som, const unsigned int) {
  for (auto& cell : som) {
    ar << cell;
  }
}

template <class Archive, std::size_t ND, typename DistFunc>
void load(Archive& ar, Euclid::SOM::SOM<ND, DistFunc>& som, const unsigned int) {
  for (auto& cell : som) {
    ar >> cell;
  }
}

template <class Archive, std::size_t ND, typename DistFunc>
void serialize(Archive& ar, Euclid::SOM::SOM<ND, DistFunc>& som, const unsigned int version) {
  split_free(ar, som, version);
}

template <class Archive, std::size_t ND, typename DistFunc>
void save_construct_data(Archive& ar, const Euclid::SOM::SOM<ND, DistFunc>* t, const unsigned int) {
  std::string dist_func_type = typeid(DistFunc).name();
  ar << dist_func_type;
  auto size = t->getSize();
  ar << size.first;
  ar << size.second;
}

template <class Archive, std::size_t ND, typename DistFunc>
void load_construct_data(Archive& ar, Euclid::SOM::SOM<ND, DistFunc>* t, const unsigned int) {
  std::string dist_func_type;
  ar >> dist_func_type;
  if (dist_func_type != typeid(DistFunc).name()) {
    throw Elements::Exception() << "Incompatible DistFunc parameter. File contains SOM with "
            << dist_func_type << " and is read as " << typeid(DistFunc).name();
  }
  std::size_t x;
  ar >> x;
  std::size_t y;
  ar >> y;
  ::new(t) Euclid::SOM::SOM<ND, DistFunc>(x,  y);
}

}
}

#endif /* SOM_SERIALIZATION_SOM_H */

