/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
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
 * @file SourceCatalog/PhotometryParsingException.h
 *
 * Created on: Jan 20, 2017
 *     Author: Florian Dubath
 */
#ifndef PHOTOMETRYPARSINGEXCEPTION_H_
#define PHOTOMETRYPARSINGEXCEPTION_H_

#include "ElementsKernel/Exception.h"
#include <string>

namespace Euclid {
namespace SourceCatalog {

class PhotometryParsingException : public Elements::Exception {
public:
  explicit PhotometryParsingException(const char* message, const char *context, double flux, double error)
      : Elements::Exception(message), m_flux(flux), m_error(error) {
    *this << context << " ( Flux=" << flux << ", Error=" << error << ")";
  }

  virtual ~PhotometryParsingException() noexcept {}

  const double& GetFlux() const {
    return m_flux;
  }
  const double& GetError() const {
    return m_error;
  }

private:
  double m_flux;
  double m_error;
};

}  // namespace SourceCatalog
}  // end of namespace Euclid

#endif  // PHOTOMETRYPARSINGEXCEPTION_H_
