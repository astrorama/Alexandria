/** 
 * @file src/lib/FitsReaderHelper.cpp
 * @date April 17, 2014
 * @author Nikolaos Apostolakos
 */

#include <CCfits/CCfits>
#include "ElementsKernel/Exception.h"
#include "FitsReaderHelper.h"

namespace Euclid {
namespace Table {

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
  throw Elements::Exception() << "FITS ASCII table format " << format << " is not "
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
  } else if (format.back() == 'B') {
    return typeid(std::vector<int32_t>);
  } else if (format.back() == 'I') {
    return typeid(std::vector<int32_t>);
  } else if (format.back() == 'J') {
    return typeid(std::vector<int32_t>);
  } else if (format.back() == 'K') {
    return typeid(std::vector<int64_t>);
  } else if (format.back() == 'E') {
    return typeid(std::vector<float>);
  } else if (format.back() == 'D') {
    return typeid(std::vector<double>);
  }
  throw Elements::Exception() << "FITS binary table format " << format << " is not "
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

std::vector<std::string> autoDetectColumnUnits(const CCfits::Table& table_hdu) {
  std::vector<std::string> units {};
  for (int i=1; i<=table_hdu.numCols(); ++i) {
    units.push_back(table_hdu.column(i).unit());
  }
  return units;
}

std::vector<std::string> autoDetectColumnDescriptions(const CCfits::Table& table_hdu) {
  std::vector<std::string> descriptions {};
  for (int i=1; i<=table_hdu.numCols(); ++i) {
    std::string desc;
    auto key = table_hdu.keyWord().find("TDESC" + std::to_string(i));
    if (key != table_hdu.keyWord().end()) {
      key->second->value(desc);
    }
    descriptions.push_back(desc);
  }
  return descriptions;
}

template<typename T>
std::vector<Row::cell_type> convertScalarColumn(CCfits::Column& column, long first, long last) {
  std::vector<T> data;
  column.read(data, first, last);
  std::vector<Row::cell_type> result;
  for (auto value : data) {
    result.push_back(value);
  }
  return result;
}

template<typename T>
std::vector<Row::cell_type> convertVectorColumn(CCfits::Column& column, long first, long last) {
  std::vector<std::valarray<T>> data;
  column.readArrays(data, first, last);
  std::vector<Row::cell_type> result;
  for (auto& valar : data) {
    result.push_back(std::vector<T>(std::begin(valar),std::end(valar)));
  }
  return result;
}

std::vector<Row::cell_type> translateColumn(CCfits::Column& column, std::type_index type) {
  return translateColumn(column, type, 1, column.rows());
}

std::vector<Row::cell_type> translateColumn(CCfits::Column& column, std::type_index type, long first, long last) {
  if (type == typeid(bool)) {
    return convertScalarColumn<bool>(column, first, last);
  } if (type == typeid(int32_t)) {
    return convertScalarColumn<int32_t>(column, first, last);
  } if (type == typeid(int64_t)) {
    return convertScalarColumn<int64_t>(column, first, last);
  } if (type == typeid(float)) {
    return convertScalarColumn<float>(column, first, last);
  } if (type == typeid(double)) {
    return convertScalarColumn<double>(column, first, last);
  } if (type == typeid(std::string)) {
    return convertScalarColumn<std::string>(column, first, last);
  } if (type == typeid(std::vector<int32_t>)) {
    return convertVectorColumn<int32_t>(column, first, last);
  } if (type == typeid(std::vector<int64_t>)) {
    return convertVectorColumn<int64_t>(column, first, last);
  } if (type == typeid(std::vector<float>)) {
    return convertVectorColumn<float>(column, first, last);
  } if (type == typeid(std::vector<double>)) {
    return convertVectorColumn<double>(column, first, last);
  }
  throw Elements::Exception() << "Unsupported column type " << type.name();
}

}
} // end of namespace Euclid