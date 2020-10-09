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

#include <iterator>
#include <list>
#include <random>
#include <utility>

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

    std::random_device              rd;
    std::mt19937                    gen(rd());
    std::uniform_int_distribution<> dis(0, std::distance(begin, end) - 1);
    auto                            random_index = dis(gen);

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

template <typename IterType>
class Jackknife : public Interface<IterType> {

public:
  explicit Jackknife(std::size_t sample_size) : m_sample_size(sample_size), m_current(sample_size) {
    m_iter_list.reserve(sample_size);
  }

  IterType start(IterType begin, IterType end) const override {

    m_end = end;

    // Clear the iterators list, for the case it has already something inside
    m_iter_list.clear();
    m_iter_list.reserve(m_sample_size);

    // Put all the possible iterators in a temporary linked list
    std::list<IterType> all_iter_list{};
    for (auto it = begin; it != end; ++it) {
      all_iter_list.push_back(it);
    }

    // Create the random device to use
    std::random_device rd;
    std::mt19937       gen(rd());

    // Pick up m_sample_size random iterators from the temporary list
    int all_max_index = all_iter_list.size() - 1;
    for (std::size_t i = 0; i < m_sample_size && all_max_index >= 0; ++i, --all_max_index) {
      std::uniform_int_distribution<> dis(0, all_max_index);
      auto                            it = all_iter_list.begin();
      std::advance(it, dis(gen));
      m_iter_list.push_back(*it);
      all_iter_list.erase(it);
    }

    // Set the current iterator at the beginning of the vector and return it
    m_current        = 0;
    m_iter_list_size = m_iter_list.size();
    return m_iter_list[m_current];
  }

  IterType next(IterType) const override {
    ++m_current;
    if (m_current >= m_iter_list_size) {
      return m_end;
    }
    return m_iter_list[m_current];
  }

private:
  std::size_t                   m_sample_size;
  mutable std::vector<IterType> m_iter_list;
  mutable std::size_t           m_iter_list_size;
  mutable IterType              m_end;
  mutable std::size_t           m_current;
};

template <typename IterType>
Jackknife<IterType> jackknifeFactory(IterType, std::size_t sample_size) {
  return Jackknife<IterType>{sample_size};
}

}  // namespace SamplingPolicy
}  // namespace SOM
}  // namespace Euclid

#endif /* SOM_SAMPLINGPOLICY_H */
