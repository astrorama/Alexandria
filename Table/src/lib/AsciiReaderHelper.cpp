/*
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
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
 * @file src/lib/AsciiReaderHelper.cpp
 * @date April 15, 2014
 * @author Nikolaos Apostolakos
 */

#include "AsciiReaderHelper.h"
#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Logging.h"
#include "NdArray/NdArray.h"
#include <boost/algorithm/string.hpp>
#include <boost/lexical_cast.hpp>
#include <boost/spirit/include/qi.hpp>
#include <boost/tokenizer.hpp>
#include <set>
#include <sstream>

namespace Euclid {
namespace Table {

using NdArray::NdArray;

static Elements::Logging logger = Elements::Logging::getLogger("AsciiReader");

size_t countColumns(std::istream& in, const std::string& comment) {
  StreamRewinder rewinder{in};
  size_t         count = 0;

  while (in) {
    std::string line;
    getline(in, line);
    // Remove any comments
    size_t comment_pos = line.find(comment);
    if (comment_pos != std::string::npos) {
      line = line.substr(0, comment_pos);
    }
    boost::trim(line);
    if (!line.empty()) {
      std::string       token;
      std::stringstream line_stream(line);
      line_stream >> boost::io::quoted(token);
      while (line_stream) {
        line_stream >> boost::io::quoted(token);
        ++count;
      }
      break;
    }
  }
  if (count == 0) {
    throw Elements::Exception() << "No data lines found";
  }
  return count;
}

/// Mapping between string representation of a type and the typeid
/// When doing the reverse lookup (from type id to string), the first one is the preferred one
extern const std::vector<std::pair<std::string, std::type_index>> KeywordTypeMap{
    // Boolean
    {"bool", typeid(bool)},
    {"boolean", typeid(bool)},
    // Integers
    {"int", typeid(int32_t)},
    {"long", typeid(int64_t)},
    {"int32", typeid(int32_t)},
    {"int64", typeid(int64_t)},
    // Floating point
    {"float", typeid(float)},
    {"double", typeid(double)},
    // Strings
    {"string", typeid(std::string)},
    // Arrays
    {"[bool]", typeid(std::vector<bool>)},
    {"[boolean]", typeid(std::vector<bool>)},
    {"[int]", typeid(std::vector<int32_t>)},
    {"[long]", typeid(std::vector<int64_t>)},
    {"[int32]", typeid(std::vector<int32_t>)},
    {"[int64]", typeid(std::vector<int64_t>)},
    {"[float]", typeid(std::vector<float>)},
    {"[double]", typeid(std::vector<double>)},
    // NdArrays
    {"[int+]", typeid(NdArray<int32_t>)},
    {"[long+]", typeid(NdArray<int64_t>)},
    {"[int32+]", typeid(NdArray<int32_t>)},
    {"[int64+]", typeid(NdArray<int64_t>)},
    {"[float+]", typeid(NdArray<float>)},
    {"[double+]", typeid(NdArray<double>)},
};

std::type_index keywordToType(const std::string& keyword) {
  for (auto p = KeywordTypeMap.begin(); p != KeywordTypeMap.end(); ++p) {
    if (p->first == keyword) {
      return p->second;
    }
  }
  throw Elements::Exception() << "Unknown column type keyword " << keyword;
}

std::map<std::string, ColumnDescription> autoDetectColumnDescriptions(std::istream& in, const std::string& comment) {
  StreamRewinder                           rewinder{in};
  std::map<std::string, ColumnDescription> descriptions;
  while (in) {
    std::string line;
    getline(in, line);
    boost::trim(line);
    if (line.empty()) {
      continue;  // We skip empty lines
    }
    if (boost::starts_with(line, comment)) {
      // If we have a comment we remove all comment characters and check if we have
      // a column description
      boost::replace_all(line, comment, "");
      boost::trim(line);
      if (boost::starts_with(line, "Column:")) {
        line.erase(0, 7);
        boost::trim(line);
        if (!line.empty()) {
          std::string       token;
          std::stringstream line_stream(line);
          std::string       name;
          line_stream >> boost::io::quoted(name);
          if (descriptions.count(name) != 0) {
            throw Elements::Exception() << "Duplicate column name " << name;
          }
          line_stream >> boost::io::quoted(token);
          std::type_index type = typeid(std::string);
          if (line_stream) {
            if (!boost::starts_with(token, "(") && token != "-") {
              type = keywordToType(token);
              line_stream >> boost::io::quoted(token);
            }
          }
          std::string unit = "";
          if (line_stream) {
            if (boost::starts_with(token, "(")) {
              unit = token;
              unit.erase(unit.begin());
              unit.erase(unit.end() - 1);
              line_stream >> boost::io::quoted(token);
            }
          }
          if (line_stream && token == "-") {
            line_stream >> boost::io::quoted(token);
          }
          std::stringstream desc;
          while (line_stream) {
            desc << token << ' ';
            line_stream >> boost::io::quoted(token);
          }
          std::string desc_str = desc.str();
          boost::trim(desc_str);
          descriptions.emplace(std::piecewise_construct, std::forward_as_tuple(name),
                               std::forward_as_tuple(name, type, unit, desc_str));
        }
      }
    } else {
      break;  // here we reached the first data line
    }
  }
  return descriptions;
}

std::vector<std::string> autoDetectColumnNames(std::istream& in, const std::string& comment, size_t columns_number) {
  StreamRewinder           rewinder{in};
  std::vector<std::string> names{};

  // Find the last comment line and at the same time read the names of the
  // column info description comments
  std::string              last_comment{};
  std::vector<std::string> desc_names{};
  while (in) {
    std::string line;
    getline(in, line);
    boost::trim(line);
    if (line.empty()) {
      continue;  // We skip empty lines
    }
    if (boost::starts_with(line, comment)) {
      // If we have a comment we remove all comment characters and check if we have
      // the correct number of tokens
      boost::replace_all(line, comment, "");
      boost::trim(line);
      if (!line.empty()) {
        last_comment = line;
      }
      if (boost::starts_with(line, "Column:")) {
        std::string temp = line;
        temp.erase(0, 7);
        boost::trim(temp);
        auto space_i = temp.find(' ');
        if (space_i > 0) {
          temp = temp.substr(0, space_i);
        }
        desc_names.emplace_back(std::move(temp));
      }
    } else {
      break;  // here we reached the first data line
    }
  }

  // Check if the last comment line contains the names of the columns
  if (!last_comment.empty()) {
    std::stringstream line_stream(last_comment);
    std::string       token;
    line_stream >> boost::io::quoted(token);
    while (line_stream) {
      names.push_back(token);
      line_stream >> boost::io::quoted(token);
    }
    if (names.size() != columns_number) {
      names.clear();
    }
  }

  // If the names are empty we fill them with the column descriprion ones
  if (names.empty()) {
    if (desc_names.size() != 0 && desc_names.size() != columns_number) {
      logger.warn() << "Number of column descriptions does not matches the number"
                    << " of the columns";
    }
    names = desc_names;
  }

  if (names.size() < columns_number) {
    for (size_t i = names.size() + 1; i <= columns_number; ++i) {
      names.push_back("col" + std::to_string(i));
    }
  }
  // Check for duplicate names
  std::set<std::string> set{};
  for (auto name : names) {
    if (!set.insert(name).second) {
      throw Elements::Exception() << "Duplicate column name " << name;
    }
  }
  return names;
}

namespace {

template <typename T>
std::vector<T> convertStringToVector(const std::string& str) {
  std::vector<T>                                result{};
  boost::char_separator<char>                   sep{","};
  boost::tokenizer<boost::char_separator<char>> tok{str, sep};
  for (auto& s : tok) {
    result.push_back(boost::get<T>(convertToCellType(s, typeid(T))));
  }
  return result;
}

template <typename T>
NdArray<T> convertStringToNdArray(const std::string& str) {
  if (str.empty()) {
    throw Elements::Exception() << "Cannot convert an empty string to a NdArray";
  } else if (str[0] != '<') {
    throw Elements::Exception() << "Unexpected initial character for a NdArray: " << str[0];
  }

  auto closing_char = str.find('>');
  if (closing_char == std::string::npos) {
    throw Elements::Exception() << "Could not find '>'";
  }

  auto shape_str = str.substr(1, closing_char - 1);
  auto shape_i   = convertStringToVector<int32_t>(shape_str);
  auto data      = convertStringToVector<T>(str.substr(closing_char + 1));

  std::vector<size_t> shape_u;
  std::copy(shape_i.begin(), shape_i.end(), std::back_inserter(shape_u));
  return NdArray<T>(shape_u, data);
}

}  // namespace

const std::map<std::type_index, std::function<Row::cell_type(const std::string&)>> sCellConverter{
    // Boolean
    {typeid(bool),
     [](const std::string& value) {
       if (value == "true" || value == "t" || value == "yes" || value == "y" || value == "1") {
         return true;
       } else if (value == "false" || value == "f" || value == "no" || value == "n" || value == "0") {
         return false;
       }
       throw Elements::Exception() << "Invalid boolean value " << value;
     }},
    // Integers
    {typeid(int32_t), boost::lexical_cast<int32_t, const std::string&>},
    {typeid(int64_t), boost::lexical_cast<int64_t, const std::string&>},
    // Floating point
    {typeid(float), boost::lexical_cast<float, const std::string&>},
    {typeid(double), boost::lexical_cast<double, const std::string&>},
    // String
    {typeid(std::string), boost::lexical_cast<std::string, const std::string&>},
    // Arrays
    {typeid(std::vector<bool>), convertStringToVector<bool>},
    {typeid(std::vector<int32_t>), convertStringToVector<int32_t>},
    {typeid(std::vector<int64_t>), convertStringToVector<int64_t>},
    {typeid(std::vector<float>), convertStringToVector<float>},
    {typeid(std::vector<double>), convertStringToVector<double>},
    // NdArray
    {typeid(NdArray<int32_t>), convertStringToNdArray<int32_t>},
    {typeid(NdArray<int64_t>), convertStringToNdArray<int64_t>},
    {typeid(NdArray<float>), convertStringToNdArray<float>},
    {typeid(NdArray<double>), convertStringToNdArray<double>},
};

Row::cell_type convertToCellType(const std::string& value, std::type_index type) {
  try {
    auto i = sCellConverter.find(type);
    if (i == sCellConverter.end()) {
      throw Elements::Exception() << "Unknown type name " << type.name();
    }
    return i->second(value);
  } catch (boost::bad_lexical_cast const&) {
    throw Elements::Exception() << "Cannot convert " << value << " to " << type.name();
  }
}

bool hasNextRow(std::istream& in, const std::string& comment) {
  StreamRewinder rewinder{in};
  while (in) {
    std::string line;
    getline(in, line);
    size_t comment_pos = line.find(comment);
    if (comment_pos != std::string::npos) {
      line = line.substr(0, comment_pos);
    }
    boost::trim(line);
    if (!line.empty()) {
      return true;
    }
  }
  return false;
}

std::size_t countRemainingRows(std::istream& in, const std::string& comment) {
  StreamRewinder rewinder{in};
  std::size_t    count = 0;
  while (in) {
    std::string line;
    getline(in, line);
    size_t comment_pos = line.find(comment);
    if (comment_pos != std::string::npos) {
      line = line.substr(0, comment_pos);
    }
    boost::trim(line);
    if (!line.empty()) {
      ++count;
    }
  }
  return count;
}

std::vector<std::string> splitLine(std::string line, const std::string& comment) {
  std::vector<std::string> cells;
  size_t                   comment_pos = line.find(comment);

  if (comment_pos != std::string::npos) {
    line = line.substr(0, comment_pos);
  }
  boost::trim(line);
  if (!line.empty()) {
    std::stringstream line_stream(line);
    size_t            count = 0;
    std::string       token;
    line_stream >> boost::io::quoted(token);
    while (line_stream) {
      cells.emplace_back(token);
      line_stream >> boost::io::quoted(token);
      ++count;
    }
  }
  return cells;
}

std::vector<std::string> firstDataLine(std::istream& in, const std::string& comment) {
  StreamRewinder rewinder{in};
  std::string    line(comment);
  while (in && boost::starts_with(line, comment)) {
    getline(in, line);
  }
  return splitLine(line, comment);
}

std::pair<std::type_index, std::size_t> guessColumnType(const std::string& token) {
  namespace qi = boost::spirit::qi;
  double d;
  long   l;

  auto it1 = token.begin(), it2 = it1;
  if (qi::parse(it1, token.end(), qi::long_, l) && it1 == token.end()) {
    return {typeid(long), 0};
  }
  if (qi::parse(it2, token.end(), qi::double_, d) && it2 == token.end()) {
    return {typeid(double), 0};
  }
  return {typeid(std::string), std::size_t(0)};
}

}  // namespace Table
}  // end of namespace Euclid
