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
 * @file ImplTools.h
 * @author nikoapos
 */


#include "SOM/ImplTools.h"
#include "GridContainer/GridAxis.h"

namespace Euclid {
namespace SOM {
namespace ImplTools {

GridContainer::GridAxis<std::size_t> indexAxis(const std::string& name, std::size_t size) {
  std::vector<std::size_t> indices{};
  for (std::size_t i = 0; i != size; ++i) {
    indices.push_back(i);
  }
  return GridContainer::GridAxis<std::size_t>{name, std::move(indices)};
}

}
}
}

