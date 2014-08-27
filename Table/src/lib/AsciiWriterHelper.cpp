/** 
 * @file src/lib/AsciiWriterHelper.cpp
 * @date April 16, 2014
 * @author Nikolaos Apostolakos
 */

#include <algorithm>
#include <boost/lexical_cast.hpp>
#include "ElementsKernel/Exception.h"
#include "AsciiWriterHelper.h"

namespace Euclid {
namespace ChTable {

std::string typeToKeyword(std::type_index type) {
  if (type == typeid(bool)) {
    return "bool";
  } if (type == typeid(int32_t)) {
    return "int";
  } if (type == typeid(int64_t)) {
    return "long";
  } if (type == typeid(float)) {
    return "float";
  } if (type == typeid(double)) {
    return "double";
  } if (type == typeid(std::string)) {
    return "string";
  }
  throw Elements::Exception() << "Conversion to string for type " << type.name()
                            << " is not supported";
}

std::vector<size_t> calculateColumnLengths(const Table& table) {
  std::vector<size_t> sizes {};
  // We initialize the values to the required size for the column name and type
  auto column_info = table.getColumnInfo();
  for (size_t i=0; i<column_info->size(); ++i) {
    sizes.push_back(std::max(column_info->getName(i).size(),
                             typeToKeyword(column_info->getType(i)).size()));
  }
  for (auto row : table) {
    for (size_t i=0; i<sizes.size(); ++i) {
      sizes[i] = std::max(sizes[i], boost::lexical_cast<std::string>(row[i]).size());
    }
  }
  for (auto& s : sizes) {
    s += 1;
  }
  return sizes;
}

}
} // end of namespace Euclid