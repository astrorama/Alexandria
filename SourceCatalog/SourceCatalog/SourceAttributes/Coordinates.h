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
 * @file SourceCatalog/SourceAttributes/Coordinates.h
 *
 * Created on: Jan 22, 2014
 *     Author: Pierre Dubath
 */
#ifndef COORDINATES_H_
#define COORDINATES_H_

#include "SourceCatalog/Attribute.h"

namespace Euclid {
namespace SourceCatalog {

/**
 * @class Coordinates
 * @brief Store the Right Ascension (Ra) and Delination (Dec) of a source in
 * decimal degrees, i.e.,
 *    0.0 < Ra  < 360.00
 *  -90.0 < Dec <  90.0
 *
 */
class Coordinates : public Attribute {
public:
  Coordinates(double ra, double dec) : m_ra(ra), m_dec(dec) {}
  virtual ~Coordinates() {}

  double getDec() const {
    return m_dec;
  }

  double getRa() const {
    return m_ra;
  }

private:
  double m_ra{};
  double m_dec{};
};

}  // namespace SourceCatalog
}  // end of namespace Euclid

#endif  // COORDINATES_H_
