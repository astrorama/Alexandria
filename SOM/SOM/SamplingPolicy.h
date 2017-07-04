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
 * @file SamplingPolicy.h
 * @author nikoapos
 */

#ifndef SOM_SAMPLINGPOLICY_H
#define SOM_SAMPLINGPOLICY_H

#include <utility>
#include <random>
#include <iterator>

namespace Euclid {
namespace SOM {
namespace SamplingPolicy {

template <typename IterType>
class Interface {
  
public:
  
  virtual IterType start(IterType begin, IterType end) const = 0;
  
  virtual IterType next(IterType iter) const = 0;
  
};

template <typename IterType>
class FullSet : public Interface<IterType> {
  
public:
  
  IterType start(IterType begin, IterType) const override {
    return begin;
  }
  
  IterType next(IterType iter) const override {
    return ++iter;
  }
  
};

template <typename IterType>
class Bootstrap : public Interface<IterType> {
  
  public:
  
  IterType start(IterType begin, IterType end) const override {
    
    m_end = end;
    
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, std::distance(begin, end) - 1);
    auto random_index = dis(gen);
    
    auto result = begin;
    std::advance(result, random_index);

    return result;
  }
  
  IterType next(IterType) const override {
    return m_end;
  }
  
private:
  
  mutable IterType m_end;
  
};

template <typename IterType>
Bootstrap<IterType> bootstrapFactory(IterType) {
  return Bootstrap<IterType>{};
}

}
}
}

#endif /* SOM_SAMPLINGPOLICY_H */

