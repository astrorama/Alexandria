/** 
 * @file src/lib/FitsReaderHelper.cpp
 * @date April 17, 2014
 * @author Nikolaos Apostolakos
 */

#include <CCfits/CCfits>
#include "ElementsKernel/ElementsException.h"
#include "FitsReaderHelper.h"

namespace Euclid {
namespace ChTable {

std::vector<std::string> autoDetectColumnNames(const CCfits::Table& table_hdu) {
  std::vector<std::string> names {};
  for (int i=1; i<=table_hdu.numCols(); ++i) {
    std::string name = table_hdu.column(i).name();
    if (name.empty()) {
      name = "Col" + std::to_string(i);
    }
    names.push_back(std::move(name));
  }
  return names;
}

std::type_index asciiFormatToType(const std::string& format) {
  if (format[0] == 'A') {
    return typeid(std::string);
  } else if (format[0] == 'I') {
    return typeid(int64_t);
  } else if (format[0] == 'F') {
    return typeid(double);
  } else if (format[0] == 'E') {
    return typeid(double);
  } else if (format[0] == 'D') {
    return typeid(double);
  }
  throw ElementsException() << "FITS ASCII table format " << format << " is not "
                            << "yet supported";
}

std::type_index binaryFormatToType(const std::string& format) {
  if (format[0] == 'L') {
    return typeid(bool);
  } else if (format[0] == 'B') {
    return typeid(int32_t);
  } else if (format[0] == 'I') {
    return typeid(int32_t);
  } else if (format[0] == 'J') {
    return typeid(int32_t);
  } else if (format[0] == 'K') {
    return typeid(int64_t);
  } else if (format.back() == 'A') {
    return typeid(std::string);
  } else if (format[0] == 'E') {
    return typeid(float);
  } else if (format[0] == 'D') {
    return typeid(double);
  }
  throw ElementsException() << "FITS binary table format " << format << " is not "
                            << "yet supported";
}

std::vector<std::type_index> autoDetectColumnTypes(const CCfits::Table& table_hdu) {
  std::vector<std::type_index> types {};
  for (int i=1; i<=table_hdu.numCols(); i++) {
    if (typeid(table_hdu) == typeid(CCfits::BinTable)) {
      types.push_back(binaryFormatToType(table_hdu.column(i).format()));
    } else {
      types.push_back(asciiFormatToType(table_hdu.column(i).format()));
    }
  }
  return types;
}

template<typename T>
std::vector<Row::cell_type> convertScalarColumn(CCfits::Column& column) {
  std::vector<T> data;
  column.read(data, 1, column.rows());
  std::vector<Row::cell_type> result;
  for (auto value : data) {
    result.push_back(value);
  }
  return result;
}

std::vector<Row::cell_type> translateColumn(CCfits::Column& column, std::type_index type) {
  if (type == typeid(bool)) {
    return convertScalarColumn<bool>(column);
  } if (type == typeid(int32_t)) {
    return convertScalarColumn<int32_t>(column);
  } if (type == typeid(int64_t)) {
    return convertScalarColumn<int64_t>(column);
  } if (type == typeid(float)) {
    return convertScalarColumn<float>(column);
  } if (type == typeid(double)) {
    return convertScalarColumn<double>(column);
  } if (type == typeid(std::string)) {
    return convertScalarColumn<std::string>(column);
  }
  throw ElementsException() << "Unsupported column type " << type.name();
}

}
} // end of namespace Euclid