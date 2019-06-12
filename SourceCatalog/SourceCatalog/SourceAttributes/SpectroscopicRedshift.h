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
 * @file SourceCatalog/SourceAttributes/SpectroscopicRedshift.h
 *
 * @date Jan 16, 2014
 * @author Pierre Dubath
 */

#ifndef SPECTROSCOPICREDSHIFT_H_
#define SPECTROSCOPICREDSHIFT_H_

#include "SourceCatalog/Attribute.h"

namespace Euclid {
namespace SourceCatalog {

/**
 * @class SpectroscopicRedshift
 *
 * @brief Store the spectroscopic redshift of a source
 *
 */
class SpectroscopicRedshift : public Attribute {
public:

  /**
 * @brief Constructor
 * @param value
 *  Value of the redshift
 * @param error
 *  Error value of the value parameter
 */
  SpectroscopicRedshift(double value, double error) : m_value(value), m_error(error) {}

  virtual ~SpectroscopicRedshift() {}

  double getValue() const { return m_value; }
  double getError() const { return m_error; }

private:

  double m_value {};
  double m_error {};
};

} // namespace SourceCatalog
} // end of namespace Euclid

#endif // SPECTROSCOPICREDSHIFT_H_ 
