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
#include <typeinfo>
#include <vector>
#include <type_traits>
#include <boost/variant/static_visitor.hpp>
#include <boost/tokenizer.hpp>
#include <cmath>
#include "ElementsKernel/Exception.h"

namespace Euclid {
namespace Table {

template <typename To>
class CastVisitor : public boost::static_visitor<To> {

public:

  template <typename From>
  To operator() (const From& from, typename std::enable_if<std::is_same<From, To>::value>::type* = 0) const {
    return from;
  }

  template <typename From>
  To operator() (const From&, typename std::enable_if<!std::is_same<From, To>::value>::type* = 0) const {
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

  template <typename From>
  static constexpr bool generic() {
    return std::is_arithmetic<From>::value;
  }

public:

  template <typename From>
  double operator() (const From& , typename std::enable_if<!generic<From>()>::type* = 0) const {
    throw Elements::Exception() << "CastVisitor cannot convert "
            << typeid(From).name() << " type to " << typeid(double).name();
  }

  template <typename From>
  double operator() (const From& from, typename std::enable_if<generic<From>()>::type* = 0) const {
    return from;
  }

  double operator() (const std::string& from) const {
    char *endptr = nullptr;
    double value = std::strtod(from.c_str(), &endptr);
    if (endptr == from.c_str()) {
      throw Elements::Exception() << "CastVisitor cannot convert the string '"
                                  << from << "' to " << typeid(double).name();
    }
    if (value == HUGE_VAL || value == -HUGE_VAL) {
      throw Elements::Exception() << "CastVisitor overflows converting the string '"
                                  << from << "' to " << typeid(double).name();
    }
    return value;
  }

};

template <>
class CastVisitor<float> : public boost::static_visitor<float> {

  template <typename From>
  static constexpr bool generic() {
    return std::is_arithmetic<From>::value &&
           !std::is_same<From, double>::value;
  }

public:

  template <typename From>
  double operator() (const From& , typename std::enable_if<!generic<From>()>::type* = 0) const {
    throw Elements::Exception() << "CastVisitor cannot convert "
            << typeid(From).name() << " type to " << typeid(float).name();
  }

  template <typename From>
  float operator() (const From& from, typename std::enable_if<generic<From>()>::type* = 0) const {
    return from;
  }

  float operator() (const std::string& from) const {
    char *endptr = nullptr;
    float value = std::strtof(from.c_str(), &endptr);
    if (endptr == from.c_str()) {
      throw Elements::Exception() << "CastVisitor cannot convert the string '"
                                  << from << "' to " << typeid(float).name();
    }
    if (value == HUGE_VALF || value == -HUGE_VALF) {
      throw Elements::Exception() << "CastVisitor overflows converting the string '"
                                  << from << "' to " << typeid(float).name();
    }
    return value;
  }

};

template <>
class CastVisitor<int64_t> : public boost::static_visitor<int64_t> {

  template <typename From>
  static constexpr bool generic() {
    return std::is_integral<From>::value;
  }

public:

  template <typename From>
  double operator() (const From& , typename std::enable_if<!generic<From>()>::type* = 0) const {
    throw Elements::Exception() << "CastVisitor cannot convert "
            << typeid(From).name() << " type to " << typeid(int64_t).name();
  }

  template <typename From>
  int64_t operator() (const From& from, typename std::enable_if<generic<From>()>::type* = 0) const {
    return from;
  }

  int64_t operator() (const std::string& from) const {
    char *endptr = nullptr;
    int64_t value = std::strtoll(from.c_str(), &endptr, 10);
    if (endptr == from.c_str()) {
      throw Elements::Exception() << "CastVisitor cannot convert the string '"
            << from << "' to " << typeid(int64_t).name();
    }
    return value;
  }

};

template <>
class CastVisitor<int32_t> : public boost::static_visitor<int32_t> {

  template <typename From>
  static constexpr bool generic() {
    return std::is_integral<From>::value &&
            !std::is_same<From, int64_t>::value;
  }

public:

  template <typename From>
  double operator() (const From& , typename std::enable_if<!generic<From>()>::type* = 0) const {
    throw Elements::Exception() << "CastVisitor cannot convert "
            << typeid(From).name() << " type to " << typeid(int32_t).name();
  }

  template <typename From>
  int32_t operator() (const From& from, typename std::enable_if<generic<From>()>::type* = 0) const {
    return from;
  }

  int32_t operator() (const std::string& from) const {
    char *endptr = nullptr;
    int64_t value = std::strtoll(from.c_str(), &endptr, 10);
    if (endptr == from.c_str()) {
      throw Elements::Exception() << "CastVisitor cannot convert the string '"
                                  << from << "' to " << typeid(int32_t).name();
    }
    if (value > INT32_MAX || value < INT32_MIN) {
      throw Elements::Exception() << "CastVisitor overflows converting the string '"
                                  << from << "' to " << typeid(int32_t).name();
    }
    return static_cast<int32_t>(value);
  }

};

template <typename VectorType>
class CastVisitor<std::vector<VectorType>> : public boost::static_visitor<std::vector<VectorType>> {

public:

  template <typename From>
  std::vector<VectorType> operator() (const From& from) const {
    std::vector<VectorType> result {};
    result.push_back(CastVisitor<VectorType>{}(from));
    return result;
  }

  template <typename From>
  std::vector<VectorType> operator() (const std::vector<From>& from) const {
    std::vector<VectorType> result {};
    for (auto v : from) {
      result.push_back(CastVisitor<VectorType>{}(v));
    }
    return result;
  }

  std::vector<VectorType> operator() (const std::string& from) const {
    std::vector<VectorType> result {};
    boost::char_separator<char> sep {","};
    boost::tokenizer< boost::char_separator<char> > tok {from, sep};
    for (auto& s : tok) {
      result.push_back(CastVisitor<VectorType>{}(s));
    }
    return result;
  }

  // If the types match exactly we avoid an expensive copying
  const std::vector<VectorType>& operator() (const std::vector<VectorType>& from) const {
    return from;
  }

};

} /* namespace Table */
} /* namespace Euclid */


#endif
