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

#ifndef _ALEXANDRIAKERNEL_REGEX_HELPER_H
#define _ALEXANDRIAKERNEL_REGEX_HELPER_H

// The std regex library is not fully implemented in GCC 4.8.
#if !defined(__llvm__) && !defined(__INTEL_COMPILER) && defined(__GNUC__) && __GNUC__ == 4 && __GNUC_MINOR__ <= 8
#include <boost/regex.hpp>

namespace Euclid {
namespace regex {
using boost::match_results;
using boost::regex;
using boost::regex_match;
using boost::regex_search;
}  // namespace regex
}  // namespace Euclid
#else
#include <regex>

namespace Euclid {
namespace regex {
using std::match_results;
using std::regex;
using std::regex_match;
using std::regex_search;
}  // namespace regex
}  // namespace Euclid
#endif

#endif  // _ALEXANDRIAKERNEL_REGEX_HELPER_H
