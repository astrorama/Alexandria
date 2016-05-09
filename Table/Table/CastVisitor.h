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
 * @file Table/CastVisitor.h
 * @date 05/09/16
 * @author nikoapos
 */

#ifndef _TABLE_CASTVISITOR_H
#define _TABLE_CASTVISITOR_H

#include <sstream>
#include "ElementsKernel/Exception.h"

namespace Euclid {
namespace Table {

template <typename To>
class CastVisitor : public boost::static_visitor<To> {
  
public:
  
  template <typename From>
  To operator() (const From&) const {
    throw Elements::Exception() << "CastVisitor cannot convert "
            << typeid(From).name() << " type to " << typeid(To).name();
  }
  
};

template <>
class CastVisitor<std::string> : public boost::static_visitor<std::string> {
  
public:
  
  template <typename From>
  std::string operator() (const From& from) const {
    std::stringstream result {};
    result << from;
    return result.str();
  }

};

template <>
class CastVisitor<double> : public boost::static_visitor<double> {
  
public:
  
  template <typename From>
  double operator() (const From& from) const {
    return from;
  }
  
  double operator() (const std::string& from) const {
    return std::atof(from.c_str());
  }

};

template <>
class CastVisitor<float> : public boost::static_visitor<float> {
  
public:
  
  template <typename From>
  float operator() (const From& from) const {
    return from;
  }
  
  float operator() (const double&) const {
    throw Elements::Exception() << "CastVisitor cannot convert "
            << typeid(double).name() << " type to " << typeid(float).name();
  }
  
  float operator() (const std::string& from) const {
    return std::atof(from.c_str());
  }

};

template <>
class CastVisitor<int64_t> : public boost::static_visitor<int64_t> {
  
public:
  
  template <typename From>
  int64_t operator() (const From& from) const {
    return from;
  }
  
  int64_t operator() (const double&) const {
    throw Elements::Exception() << "CastVisitor cannot convert "
            << typeid(double).name() << " type to " << typeid(float).name();
  }
  
  int64_t operator() (const float&) const {
    throw Elements::Exception() << "CastVisitor cannot convert "
            << typeid(float).name() << " type to " << typeid(float).name();
  }
  
  int64_t operator() (const std::string& from) const {
    return std::atoi(from.c_str());
  }

};

template <>
class CastVisitor<int32_t> : public boost::static_visitor<int32_t> {
  
public:
  
  template <typename From>
  int32_t operator() (const From& from) const {
    return from;
  }
  
  int32_t operator() (const double&) const {
    throw Elements::Exception() << "CastVisitor cannot convert "
            << typeid(double).name() << " type to " << typeid(float).name();
  }
  
  int32_t operator() (const float&) const {
    throw Elements::Exception() << "CastVisitor cannot convert "
            << typeid(float).name() << " type to " << typeid(float).name();
  }
  
  int32_t operator() (const int64_t&) const {
    throw Elements::Exception() << "CastVisitor cannot convert "
            << typeid(int64_t).name() << " type to " << typeid(float).name();
  }
  
  int32_t operator() (const std::string& from) const {
    return std::atoi(from.c_str());
  }

};

} /* namespace Table */
} /* namespace Euclid */


#endif
