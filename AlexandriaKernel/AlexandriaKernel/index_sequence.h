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

#ifndef _ALEXANDRIAKERNEL_SEQUENCE_H
#define _ALEXANDRIAKERNEL_SEQUENCE_H

#if __cplusplus > 201103L
#include <utility>
#endif
#include <cstddef>

namespace Euclid {

#if __cplusplus > 201103L
template <typename T, T... Idx>
using _integer_sequence = std::integer_sequence<T, Idx...>;

template <std::size_t... Idx>
using _index_sequence = std::index_sequence<Idx...>;

template <std::size_t N>
using _make_index_sequence = std::make_index_sequence<N>;
#else
#warning "Index sequences not available, using a custom implementation"

template <typename T, T... Idx>
struct _integer_sequence {
  typedef T                    value_type;
  static constexpr std::size_t size() noexcept {
    return sizeof...(Idx);
  }
};

template <std::size_t... Idx>
using _index_sequence = _integer_sequence<std::size_t, Idx...>;

template <std::size_t N, std::size_t... Rest>
struct _index_sequence_helper : public _index_sequence_helper<N - 1, N - 1, Rest...> {};

template <std::size_t... Rest>
struct _index_sequence_helper<0, Rest...> {
  using type = _index_sequence<Rest...>;
};

template <std::size_t N>
using _make_index_sequence = typename _index_sequence_helper<N>::type;
#endif

}  // namespace Euclid

#endif  // _ALEXANDRIAKERNEL_SEQUENCE_H
