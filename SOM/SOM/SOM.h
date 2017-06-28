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
 * @file SOM/SOM.h
 * @date 06/21/17
 * @author nikoapos
 */

#ifndef _SOM_SOM_H
#define _SOM_SOM_H

#include <vector>
#include "GridContainer/GridContainer.h"
#include "SOM/InitFunc.h"

namespace Euclid {
namespace SOM {

/**
 * @class SOM
 * @brief
 *
 */
class SOM {

public:
  
  SOM(std::size_t nd, std::size_t x, std::size_t y, InitFunc::Signature init_func=InitFunc::zero);

  /**
   * @brief Destructor
   */
  virtual ~SOM() = default;
  
  
  GridContainer::GridContainer<std::vector<std::vector<double>>, int, int>& getCells() {
    return m_cells;
  }


private:
  
  GridContainer::GridContainer<std::vector<std::vector<double>>, int, int> m_cells;

}; /* End of SOM class */

} /* namespace SOM */
} /* namespace Euclid */


#endif
