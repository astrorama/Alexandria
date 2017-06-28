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
        : m_cells{indexAxis("X", x), indexAxis("Y", y)}, m_size{x, y} {

  // Initialize all the grid cells using the given function
  for (auto& v : m_cells) {
    for (std::size_t i = 0; i != nd; ++i) {
      v.push_back(init_func());
    }
  }

}

const std::pair<std::size_t, std::size_t>& SOM::getSize() const {
  return m_size;
}

std::vector<double>& SOM::operator()(std::size_t x, std::size_t y) {
  return m_cells(x, y);
}

const std::vector<double>& SOM::operator()(std::size_t x, std::size_t y) const {
  return m_cells(x, y);
}

SOM::iterator SOM::begin() {
  return m_cells.begin();
}

SOM::iterator SOM::end() {
  return m_cells.end();
}

SOM::const_iterator SOM::begin() const {
  return m_cells.begin();
}

SOM::const_iterator SOM::end() const {
  return m_cells.end();
}

SOM::const_iterator SOM::cbegin() {
  return m_cells.cbegin();
}

SOM::const_iterator SOM::cend() {
  return m_cells.cend();
}

} // SOM namespace
} // Euclid namespace



