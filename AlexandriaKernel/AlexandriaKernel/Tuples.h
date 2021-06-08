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

#ifndef _ALEXANDRIAKERNEL_TUPLES_H
#define _ALEXANDRIAKERNEL_TUPLES_H

#include "AlexandriaKernel/index_sequence.h"
#include <tuple>
#include <vector>

namespace Euclid {
namespace Tuple {

template <typename Seq>
struct TupleTailImpl {};

template <std::size_t... Is>
struct TupleTailImpl<_index_sequence<Is...>> {
  template <typename T0, typename... Tn>
  static std::tuple<Tn...> extract(std::tuple<T0, Tn...>&& knots) {
    return std::tuple<Tn...>{std::move(std::get<1 + Is>(knots))...};
  }

  template <typename T0, typename... Tn>
  static std::tuple<Tn...> get(const std::tuple<T0, Tn...>& knots) {
    return std::tuple<Tn...>{std::get<1 + Is>(knots)...};
  }
};

/**
 * Use this to extract the tail of a tuple
 * \details
 * For instance:
 *
 * \code {.cpp}
 * std::tuple<double, int, char> x;
 * auto x = TupleTail::get(x);
 * \endcode
 *
 * The type of x will be std::tuple<int, char>, and the content will be moved
 */
template <typename T0, typename... Tn>
static std::tuple<Tn...> Tail(std::tuple<T0, Tn...>&& tuple) {
  return TupleTailImpl<_make_index_sequence<sizeof...(Tn)>>::extract(std::move(tuple));
}

/**
 * Use this to extract the tail of a tuple
 * \details
 * For instance:
 *
 * \code {.cpp}
 * std::tuple<double, int, char> x;
 * auto x = TupleTail::get(x);
 * \endcode
 *
 * The type of x will be std::tuple<int, char>, and the content will be copied
 */
template <typename T0, typename... Tn>
static std::tuple<Tn...> Tail(const std::tuple<T0, Tn...>& tuple) {
  return TupleTailImpl<_make_index_sequence<sizeof...(Tn)>>::get(tuple);
}

}  // namespace Tuple
}  // namespace Euclid

#endif  // _ALEXANDRIAKERNEL_TUPLES_H
