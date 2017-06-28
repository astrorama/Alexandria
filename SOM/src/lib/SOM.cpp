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
 * @file src/lib/SOM.cpp
 * @date 06/21/17
 * @author nikoapos
 */

#include "SOM/SOM.h"

namespace Euclid {
namespace SOM {

namespace {

GridContainer::GridAxis<int> indexAxis(const std::string& name, std::size_t size) {
  std::vector<int> indices{};
  for (std::size_t i = 0; i != size; ++i) {
    indices.push_back(i);
  }
  return GridContainer::GridAxis<int>{name, std::move(indices)};
}

}

SOM::SOM(std::size_t nd, std::size_t x, std::size_t y, InitFunc::Signature init_func)
        : m_cells{indexAxis("X", x), indexAxis("Y", y)} {

  // Initialize all the grid cells using the given function
  for (auto& v : m_cells) {
    for (std::size_t i = 0; i != nd; ++i) {
      v.push_back(init_func());
    }
  }

}

} // SOM namespace
} // Euclid namespace



