/**
 * @file StringFunctions.h
 *
 * @date May 21, 2014
 * @author Nicolas Morisset
 */

#ifndef STRINGFUNCTIONS_H_
#define STRINGFUNCTIONS_H_

#include <string>
#include <iostream>

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

#endif // STRINGFUNCTIONS_H_
