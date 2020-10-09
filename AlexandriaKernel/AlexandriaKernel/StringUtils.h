/**
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

#ifndef _ALEXANDRIAKERNEL_STRINGUTILS_H
#define _ALEXANDRIAKERNEL_STRINGUTILS_H

#include <boost/algorithm/string/classification.hpp>
#include <boost/algorithm/string/split.hpp>
#include <boost/algorithm/string/trim.hpp>
#include <boost/lexical_cast.hpp>
#include <vector>

#include <ElementsKernel/Exception.h>

namespace Euclid {

/**
 * Convert a string into a vector of any given type.
 * @tparam T
 *  The destination type. boost::lexical_cast<T> will be used internally.
 * @param str
 *  The original string.
 * @param separators
 *  List of characters to be used as separator. Defaults to the space and the comma.
 * @return
 *  A vector of type T.
 */
template <typename T>
std::vector<T> stringToVector(std::string str, const std::string& separators = std::string(", ")) {
  std::vector<std::string> parts;
  boost::trim(str);
  boost::split(parts, str, boost::is_any_of(separators), boost::token_compress_on);
  std::vector<T> result(parts.size());
  try {
    std::transform(parts.begin(), parts.end(), result.begin(), boost::lexical_cast<T, const std::string&>);
  } catch (const boost::bad_lexical_cast& e) {
    throw Elements::Exception(e.what());
  }
  return result;
}

} /* namespace Euclid */

#endif /* _ALEXANDRIAKERNEL_STRINGUTILS_H */
