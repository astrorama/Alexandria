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
 * @file FluxErrorPair.cpp
 * @date January 22, 2015
 * @author Nikolaos Apostolakos
 */

#include "SourceCatalog/SourceAttributes/Photometry.h"

namespace Euclid {
namespace SourceCatalog {

FluxErrorPair::FluxErrorPair(double input_flux, double input_error, bool no_data, bool upper_limit)
    : flux(input_flux), error(input_error), missing_photometry_flag(no_data), upper_limit_flag(upper_limit) {}

bool FluxErrorPair::operator==(const FluxErrorPair& other) const {
  return (this->missing_photometry_flag && other.missing_photometry_flag) ||
         (this->flux == other.flux && this->error == other.error && this->upper_limit_flag == other.upper_limit_flag);
}

bool FluxErrorPair::operator!=(const FluxErrorPair& other) const {
  return !(*this == other);
}

}  // end of namespace SourceCatalog
}  // end of namespace Euclid
