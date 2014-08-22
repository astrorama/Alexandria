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
ELEMENTS_API std::string checkNoBeginSlashes(const std::string& input_str);

//
// Make sure the string does start with only one "/" character
//
ELEMENTS_API std::string checkBeginSlashes(const std::string& input_str);

//
// Make sure the string finishes with a "/" character and only one
//
ELEMENTS_API std::string checkEndSlashes(const std::string& input_str);

//
// Make sure the string does not start with a "/" character
//
ELEMENTS_API std::string removeExtension(const std::string& input_str);


//
// Remove all characters before the last "/" character
//
ELEMENTS_API std::string removeAllBeforeLastSlash(const std::string& input_str);

} // XYDataset namespace
} // end of namespace Euclid

#endif // STRINGFUNCTIONS_H_
