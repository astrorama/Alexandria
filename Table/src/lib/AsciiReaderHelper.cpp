/** 
 * @file src/lib/AsciiReaderHelper.cpp
 * @date April 15, 2014
 * @author Nikolaos Apostolakos
 */

#include <set>
#include <boost/regex.hpp>
using boost::regex;
using boost::regex_match;
#include <boost/algorithm/string.hpp>
#include <boost/lexical_cast.hpp>
#include "ElementsKernel/Exception.h"
#include "AsciiReaderHelper.h"

namespace Euclid {
namespace ChTable {

size_t countColumns(std::istream& in, const std::string& comment) {
  StreamRewinder rewinder {in};
  size_t count = 0;
  regex column_separator {"\\s+"};
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
      boost::sregex_token_iterator i (line.begin(), line.end(), column_separator, -1);
      boost::sregex_token_iterator j;
      while (i != j) {
        ++i;
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

std::vector<std::string> autoDetectColumnNames(std::istream& in,
                                               const std::string& comment,
                                               size_t columns_number) {
  StreamRewinder rewinder {in};
  std::vector<std::string> names {};
  regex column_separator {"\\s+"};
  while (in) {
    std::string line;
    getline(in, line);
    boost::trim(line);
    if (line.empty()) {
      continue; // We skip empty lines
    }
    if (boost::starts_with(line, comment)) {
      // If we have a comment we remove all comment characters and check if we have
      // the correct number of tokens
      boost::replace_all(line, comment, "");
      boost::trim(line);
      if (!line.empty()) {
        boost::sregex_token_iterator i (line.begin(), line.end(), column_separator, -1);
        boost::sregex_token_iterator j;
        while (i != j) {
          names.push_back(*i);
          ++i;
        }
        if (names.size() == columns_number) {
          break;
        } else {
          names.clear();
        }
      }
    } else {
      break; // here we reached the first data line
    }
  }
  if (names.empty()) {
    for (size_t i=1; i<=columns_number; ++i) {
      names.push_back("col" + std::to_string(i));
    }
  } else {
    // Check for duplicate names
    std::set<std::string> set {};
    for (auto name : names) {
      if (!set.insert(name).second) {
        throw Elements::Exception() << "Duplicate column name " << name;
      }
    }
  }
  return names;
}

std::type_index keywordToType(const std::string& keyword) {
  if (keyword == "bool" || keyword == "boolean") {
    return typeid(bool);
  } else if (keyword == "int" || keyword == "int32") {
    return typeid(int32_t);
  } else if (keyword == "long" || keyword == "int64") {
    return typeid(int64_t);
  } else if (keyword == "float") {
    return typeid(float);
  } else if (keyword == "double") {
    return typeid(double);
  } else if (keyword == "string") {
    return typeid(std::string);
  }
  throw Elements::Exception() << "Unknown column type keyword " << keyword;
}

std::vector<std::type_index> autoDetectColumnTypes(std::istream& in,
                                                   const std::string& comment,
                                                   size_t columns_number) {
  StreamRewinder rewinder {in};
  bool names_found {false};
  std::vector<std::type_index> types {};
  regex column_separator {"\\s+"};
  while (in) {
    std::string line;
    getline(in, line);
    boost::trim(line);
    if (line.empty()) {
      continue; // We skip empty lines
    }
    if (boost::starts_with(line, comment)) {
      // If we have a comment we remove all comment characters and check if we have
      // the correct number of tokens
      boost::replace_all(line, comment, "");
      boost::trim(line);
      std::vector<std::string> keywords {};
      if (!line.empty()) {
        boost::sregex_token_iterator i (line.begin(), line.end(), column_separator, -1);
        boost::sregex_token_iterator j;
        while (i != j) {
          keywords.push_back(*i);
          ++i;
        }
        if (keywords.size() == columns_number) {
          // The first comment having correct number of columns is the names and
          // we skip it
          if (names_found) {
            for (auto keyword : keywords) {
              types.push_back(keywordToType(keyword));
            }
            break;
          } else {
            names_found = true;
          }
        }
      }
    } else {
      break; // here we reached the first data line
    }
  }
  if (types.empty()) {
    for (size_t i=1; i<=columns_number; ++i) {
      types.push_back(typeid(std::string));
    }
  }
  return types;
}

Row::cell_type convertToCellType(const std::string& value, std::type_index type) {
  try {
    if (type == typeid(bool)) {
      if (value == "true" || value == "t" || value == "yes" || value == "y" || value == "1") {
        return Row::cell_type {true};
      }
      if (value == "false" || value == "f" || value == "no" || value == "n" || value == "0") {
        return Row::cell_type {false};
      }
    } else if (type == typeid(int32_t)) {
      return Row::cell_type {boost::lexical_cast<int32_t>(value)};
    } else if (type == typeid(int64_t)) {
      return Row::cell_type {boost::lexical_cast<int64_t>(value)};
    } else if (type == typeid(float)) {
      return Row::cell_type {boost::lexical_cast<float>(value)};
    } else if (type == typeid(double)) {
      return Row::cell_type {boost::lexical_cast<double>(value)};
    } else if (type == typeid(std::string)) {
      return Row::cell_type {boost::lexical_cast<std::string>(value)};
    }
  } catch( boost::bad_lexical_cast const& ) {
    throw Elements::Exception() << "Cannot convert " << value << " to " << type.name();
  }
  throw Elements::Exception() << "Unknown type name " << type.name();
}

}
} // end of namespace Euclid