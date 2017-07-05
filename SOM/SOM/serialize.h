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
 * @file serialize.h
 * @author nikoapos
 */

#ifndef SOM_SERIALIZE_H
#define SOM_SERIALIZE_H

#include <iostream>
#include <boost/archive/binary_iarchive.hpp>
#include <boost/archive/binary_oarchive.hpp>
#include "SOM/Distance.h"
#include "SOM/serialization/SOM.h"

namespace Euclid {
namespace SOM {

template <std::size_t ND, typename DistFunc>
void somBinaryExport(std::ostream& out, const SOM<ND, DistFunc>& som) {
  // Do NOT delete this pointer!!! It  points to the actual som
  const SOM<ND, DistFunc>* ptr = &som;
  boost::archive::binary_oarchive boa {out};
  boa << ptr;
}

template <std::size_t ND, typename DistFunc=Distance::L2<ND>>
SOM<ND, DistFunc> somBinaryImport(std::istream& in) {
  boost::archive::binary_iarchive bia {in};
  // Do NOT delete manually this pointer. It is wrapped with a unique_ptr later.
  SOM<ND, DistFunc>* ptr;
  bia >> ptr;
  std::unique_ptr<SOM<ND, DistFunc>> smart_ptr {ptr};
  // We move out to the result the som pointed by the pointer. The unique_ptr
  // will delete the (now empty) pointed object
  return std::move(*smart_ptr);
}

}
}

#endif /* SOM_SERIALIZE_H */

