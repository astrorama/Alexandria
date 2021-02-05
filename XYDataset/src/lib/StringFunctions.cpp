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
 * @file src/lib/StringFunctions.cpp
 *
 * @date May 22, 2014
 * @author Nicolas Morisset
 */

#include "StringFunctions.h"

namespace Euclid {
namespace XYDataset {

//
// Make sure the string does start with only one "/" character
//
std::string checkBeginSlashes(const std::string& input_str) {

  std::string output_str{};
  size_t      pos = input_str.find_first_not_of("/");
  if (pos != std::string::npos && pos != 0) {
    output_str = input_str.substr(pos);
    output_str = "/" + output_str;
  } else {
    // no slash at the beginning
    output_str = "/" + input_str;
  }

  return (output_str);
}

//
// Make sure the string does not start with a "/" character
//
std::string checkNoBeginSlashes(const std::string& input_str) {

  std::string output_str{};

  if (!input_str.empty()) {
    size_t pos = input_str.find_first_not_of("/");
    if (pos != 0) {
      output_str = input_str.substr(pos);
    } else {
      // no slash
      output_str = input_str;
    }
  }

  return (output_str);
}

//
// Make sure the string finishes with a "/" character and only one
//
std::string checkEndSlashes(const std::string& input_str) {

  std::string output_str{};

  size_t pos = input_str.find_last_not_of("/");
  if (pos != input_str.length() - 1) {
    // add one
    output_str = input_str.substr(0, pos + 1) + "/";
  } else {
    // No slash at the end
    output_str = input_str + "/";
  }

  return (output_str);
}

//
// Remove an extension, so any character after the last "." character
//
std::string removeExtension(const std::string& input_str) {

  std::string output_str{};

  if (!input_str.empty()) {
    // Remove any file extension
    size_t pos = input_str.find_last_of(".");
    if (pos != std::string::npos) {
      output_str = input_str.substr(0, pos);
    } else {
      output_str = input_str;
    }
  }

  return (output_str);
}

//
// Remove all characters before the last "/" character
//
std::string removeAllBeforeLastSlash(const std::string& input_str) {

  std::string output_str{};

  if (!input_str.empty()) {
    // Remove any file extension
    size_t pos = input_str.find_last_of("/");
    if (pos != std::string::npos) {
      output_str = input_str.substr(pos + 1);
    } else {
      output_str = input_str;
    }
  }

  return (output_str);
}

}  // namespace XYDataset
}  // end of namespace Euclid
