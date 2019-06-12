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
 * @file src/lib/StringFunctions.h
 *
 * @date May 21, 2014
 * @author Nicolas Morisset
 */

#ifndef STRINGFUNCTIONS_H_
#define STRINGFUNCTIONS_H_

#include <string>
#include <iostream>

#include "ElementsKernel/Export.h"

namespace Euclid {
namespace XYDataset {

//
// Make sure the string does not start with a "/" character
//
std::string checkNoBeginSlashes(const std::string& input_str);

//
// Make sure the string does start with only one "/" character
//
std::string checkBeginSlashes(const std::string& input_str);

//
// Make sure the string finishes with a "/" character and only one
//
std::string checkEndSlashes(const std::string& input_str);

//
// Make sure the string does not start with a "/" character
//
std::string removeExtension(const std::string& input_str);


//
// Remove all characters before the last "/" character
//
std::string removeAllBeforeLastSlash(const std::string& input_str);

} // XYDataset namespace
} // end of namespace Euclid

#endif // STRINGFUNCTIONS_H_
